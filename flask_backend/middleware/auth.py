from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity, get_jwt
from models.admin import Admin
from models.client import Client
from utils.database import Database

def admin_required(fn):
    """
    Decorator to protect admin routes
    Only authenticated admins can access these routes
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
            claims = get_jwt()
            
            if claims.get('user_type') != 'admin':
                return jsonify({
                    'success': False,
                    'message': 'Access denied. Admin only.'
                }), 403
            
            return fn(*args, **kwargs)
            
        except Exception as e:
            print(f"Admin auth error: {e}")
            return jsonify({
                'success': False,
                'message': 'Invalid or expired token',
                'error': str(e)
            }), 401
    
    return wrapper


def client_required(fn):
    """
    Decorator to protect client routes
    Only authenticated clients can access these routes
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            # Check for Authorization header
            auth_header = request.headers.get('Authorization', None)
            if not auth_header:
                return jsonify({
                    'success': False,
                    'message': 'Authorization header is missing'
                }), 401
            
            # Check Bearer format
            if not auth_header.startswith('Bearer '):
                return jsonify({
                    'success': False,
                    'message': 'Invalid authorization header format. Use: Bearer <token>'
                }), 401
            
            # Verify JWT
            verify_jwt_in_request()
            
            # Get claims
            claims = get_jwt()
            user_type = claims.get('user_type')
            
            # Check user type
            if user_type != 'client':
                return jsonify({
                    'success': False,
                    'message': 'Access denied. Client only.'
                }), 403
            
            # Check if user is active
            user_id_str = get_jwt_identity()
            
            # Convert from string to int
            try:
                user_id = int(user_id_str)
            except (ValueError, TypeError):
                return jsonify({
                    'success': False,
                    'message': 'Invalid user ID in token'
                }), 401
            
            client = Client.find_by_id(user_id)
            
            if not client:
                return jsonify({
                    'success': False,
                    'message': 'Client not found or inactive'
                }), 401
            
            if not client.get('is_active', True):
                return jsonify({
                    'success': False,
                    'message': 'Account is inactive'
                }), 403
            
            return fn(*args, **kwargs)
            
        except Exception as e:
            error_msg = str(e)
            print(f"Client auth error: {error_msg}")
            
            # Handle different JWT errors
            if 'expired' in error_msg.lower():
                return jsonify({
                    'success': False,
                    'message': 'Token has expired'
                }), 401
            elif 'signature' in error_msg.lower():
                return jsonify({
                    'success': False,
                    'message': 'Invalid token signature'
                }), 401
            elif 'decode' in error_msg.lower():
                return jsonify({
                    'success': False,
                    'message': 'Token decode error'
                }), 401
            else:
                return jsonify({
                    'success': False,
                    'message': 'Invalid or expired token',
                    'error': error_msg
                }), 401
    
    return wrapper


def get_current_user():
    """Get current user information from JWT"""
    try:
        verify_jwt_in_request()
        user_id_str = get_jwt_identity()
        claims = get_jwt()
        user_type = claims.get('user_type')
        
        # Convert from string to int
        try:
            user_id = int(user_id_str)
        except (ValueError, TypeError):
            return None
        
        if user_type == 'admin':
            user = Admin.find_by_id(user_id)
        elif user_type == 'client':
            user = Client.find_by_id(user_id)
        else:
            return None
        
        return user
        
    except Exception as e:
        print(f"Get current user error: {e}")
        return None


def log_login_attempt(user_type, user_id, username, ip_address, location, success):
    """Log login attempt to database"""
    query = """
    INSERT INTO login_logs (user_type, user_id, username, ip_address, location, success)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    try:
        Database.execute_query(
            query,
            (user_type, user_id, username, ip_address, location, success),
            commit=True
        )
        print(f"Login log recorded: {username} - {success}")
    except Exception as e:
        print(f"Error logging login attempt: {e}")


def get_client_ip():
    """Get client IP address"""
    # Check proxy headers
    if request.headers.get('X-Forwarded-For'):
        ip = request.headers.get('X-Forwarded-For').split(',')[0].strip()
    elif request.headers.get('X-Real-IP'):
        ip = request.headers.get('X-Real-IP')
    elif request.environ.get('HTTP_X_FORWARDED_FOR'):
        ip = request.environ['HTTP_X_FORWARDED_FOR'].split(',')[0].strip()
    else:
        ip = request.environ.get('REMOTE_ADDR', 'Unknown')
    
    return ip


def get_login_logs(user_type, user_id, limit=10):
    """Get login logs for a user"""
    query = """
    SELECT id, user_type, username, ip_address, location, success, login_time
    FROM login_logs
    WHERE user_type = %s AND user_id = %s
    ORDER BY login_time DESC
    LIMIT %s
    """
    try:
        logs = Database.execute_query(query, (user_type, user_id, limit), fetch_all=True)
        return logs or []
    except Exception as e:
        print(f"Error getting login logs: {e}")
        return []


def optional_auth(fn):
    """
    Decorator for routes that can work with or without token
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request(optional=True)
        except Exception:
            pass
        
        return fn(*args, **kwargs)
    
    return wrapper