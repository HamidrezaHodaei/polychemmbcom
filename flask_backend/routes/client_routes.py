#/client_routes.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required
from models.client import Client
from models.pricing import ClientPricing
from middleware.auth import client_required, log_login_attempt, get_client_ip, get_login_logs
from datetime import datetime, timedelta

client_bp = Blueprint('client', __name__, url_prefix='/client')


@client_bp.route('/login', methods=['POST'])
def login():
    """Client login"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'message': 'Request body is required'
            }), 400
        
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({
                'success': False,
                'message': 'Username and password are required'
            }), 400
        
        print(f"Login attempt for username: {username}")
        
        # Authentication
        client = Client.authenticate(username, password)
        
        if not client:
            # Log failed attempt
            log_login_attempt('client', 0, username, get_client_ip(), 'Unknown', False)
            
            return jsonify({
                'success': False,
                'message': 'Invalid username or password'
            }), 401
        
        # Check if account is active
        if not client.get('is_active', True):
            log_login_attempt('client', client['id'], username, get_client_ip(), 'Unknown', False)
            return jsonify({
                'success': False,
                'message': 'Account is inactive'
            }), 403
        
        # Create tokens with proper expiration
        access_token = create_access_token(
            identity=str(client['id']),
            additional_claims={'user_type': 'client'},
            expires_delta=timedelta(hours=24)
        )
        
        refresh_token = create_refresh_token(
            identity=str(client['id']),
            additional_claims={'user_type': 'client'},
            expires_delta=timedelta(days=30)
        )
        
        # Log successful login
        log_login_attempt('client', client['id'], username, get_client_ip(), 'Tehran, Iran', True)
        
        print(f"Login successful for: {username}")
        
        return jsonify({
            'success': True,
            'message': 'Login successful',
            'access_token': access_token,
            'refresh_token': refresh_token,
            'user': {
                'id': client['id'],
                'username': client['username'],
                'email': client['email'],
                'company_name': client['company_name'],
                'first_name': client['first_name'],
                'last_name': client['last_name'],
                'phone': client['phone'],
                'profile_image': client.get('profile_image')
            }
        }), 200
        
    except Exception as e:
        print(f"Login error: {e}")
        return jsonify({
            'success': False,
            'message': 'Login failed',
            'error': str(e)
        }), 500


@client_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    """Refresh access token using refresh token"""
    try:
        current_user_id = get_jwt_identity()
        
        # Create new access token
        new_access_token = create_access_token(
            identity=str(current_user_id),
            additional_claims={'user_type': 'client'},
            expires_delta=timedelta(hours=24)
        )
        
        return jsonify({
            'success': True,
            'access_token': new_access_token
        }), 200
        
    except Exception as e:
        print(f"Token refresh error: {e}")
        return jsonify({
            'success': False,
            'message': 'Failed to refresh token'
        }), 401


@client_bp.route('/profile', methods=['GET'])
@client_required
def get_profile():
    """Get client profile"""
    try:
        client_id = get_jwt_identity()
        client_id = int(client_id)
        
        print(f"Getting profile for client ID: {client_id}")
        
        client = Client.find_by_id(client_id)
        
        if not client:
            return jsonify({
                'success': False,
                'message': 'Client not found'
            }), 404
        
        # Remove sensitive fields
        client.pop('password_hash', None)
        
        return jsonify(client), 200
        
    except Exception as e:
        print(f"Get profile error: {e}")
        return jsonify({
            'success': False,
            'message': 'Failed to get profile',
            'error': str(e)
        }), 500


@client_bp.route('/profile', methods=['PUT'])
@client_required
def update_profile():
    """Update client profile"""
    try:
        client_id = get_jwt_identity()
        client_id = int(client_id)
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'message': 'Request body is required'
            }), 400
        
        # Remove sensitive fields
        data.pop('password', None)
        data.pop('password_hash', None)
        data.pop('id', None)
        data.pop('username', None)
        data.pop('is_active', None)
        
        success = Client.update(client_id, **data)
        
        if success:
            return jsonify({
                'success': True,
                'message': 'Profile updated successfully'
            }), 200
        else:
            return jsonify({
                'success': False,
                'message': 'Failed to update profile'
            }), 500
            
    except Exception as e:
        print(f"Update profile error: {e}")
        return jsonify({
            'success': False,
            'message': 'Failed to update profile',
            'error': str(e)
        }), 500


@client_bp.route('/change-password', methods=['POST'])
@client_required
def change_password():
    """Change password"""
    try:
        client_id = get_jwt_identity()
        client_id = int(client_id)
        data = request.get_json()
        
        current_password = data.get('current_password')
        new_password = data.get('new_password')
        
        if not current_password or not new_password:
            return jsonify({
                'success': False,
                'message': 'Current password and new password are required'
            }), 400
        
        # Verify current password
        client = Client.find_by_id(client_id)
        if not client:
            return jsonify({
                'success': False,
                'message': 'Client not found'
            }), 404
        
        # Get password_hash for verification
        full_client = Client.find_by_username(client['username'])
        if not Client.verify_password(current_password, full_client['password_hash']):
            return jsonify({
                'success': False,
                'message': 'Current password is incorrect'
            }), 400
        
        # Change password
        success = Client.update_password(client_id, new_password)
        
        if success:
            return jsonify({
                'success': True,
                'message': 'Password changed successfully'
            }), 200
        else:
            return jsonify({
                'success': False,
                'message': 'Failed to change password'
            }), 500
            
    except Exception as e:
        print(f"Change password error: {e}")
        return jsonify({
            'success': False,
            'message': 'Failed to change password',
            'error': str(e)
        }), 500


@client_bp.route('/logout', methods=['POST'])
@client_required
def logout():
    """Client logout"""
    try:
        client_id = get_jwt_identity()
        client_id = int(client_id)
        print(f"Logout for client ID: {client_id}")
        
        # In future can add token to blacklist
        
        return jsonify({
            'success': True,
            'message': 'Logged out successfully'
        }), 200
        
    except Exception as e:
        print(f"Logout error: {e}")
        return jsonify({
            'success': False,
            'message': 'Logout failed'
        }), 500


@client_bp.route('/activity-logs', methods=['GET'])
@client_required
def get_activity_logs():
    """Get client activity logs"""
    try:
        client_id = get_jwt_identity()
        client_id = int(client_id)
        limit = request.args.get('limit', 10, type=int)
        
        print(f"Getting activity logs for client ID: {client_id}, limit: {limit}")
        
        logs = get_login_logs('client', client_id, limit)
        
        # Format logs for UI display
        formatted_logs = []
        for log in logs:
            try:
                # Calculate time ago
                login_time = log.get('login_time')
                if login_time:
                    if isinstance(login_time, str):
                        login_time = datetime.strptime(login_time, '%Y-%m-%d %H:%M:%S')
                    
                    time_diff = datetime.now() - login_time
                    
                    if time_diff.days > 0:
                        time_ago = f"{time_diff.days} days ago"
                    elif time_diff.seconds >= 3600:
                        hours = time_diff.seconds // 3600
                        time_ago = f"{hours} hours ago"
                    elif time_diff.seconds >= 60:
                        minutes = time_diff.seconds // 60
                        time_ago = f"{minutes} mins ago"
                    else:
                        time_ago = "Just now"
                else:
                    time_ago = "Unknown"
                
                formatted_logs.append({
                    'id': log.get('id'),
                    'action': 'Login Successful' if log.get('success') else 'Login Failed',
                    'time': time_ago,
                    'status': 'Success' if log.get('success') else 'Failed',
                    'success': bool(log.get('success')),
                    'location': log.get('location') or 'Unknown',
                    'ip': log.get('ip_address') or 'Unknown'
                })
            except Exception as e:
                print(f"Error formatting log: {e}")
                continue
        
        return jsonify({
            'success': True,
            'logs': formatted_logs
        }), 200
        
    except Exception as e:
        print(f"Get activity logs error: {e}")
        return jsonify({
            'success': False,
            'message': 'Failed to get activity logs',
            'error': str(e)
        }), 500


@client_bp.route('/pricing', methods=['GET'])
@client_required
def get_pricing():
    """Get pricing list (with custom prices)"""
    try:
        client_id = get_jwt_identity()
        client_id = int(client_id)
        
        pricing_list = ClientPricing.get_client_prices(client_id)
        
        return jsonify({
            'success': True,
            'pricing': pricing_list
        }), 200
        
    except Exception as e:
        print(f"Get pricing error: {e}")
        return jsonify({
            'success': False,
            'message': 'Failed to get pricing',
            'error': str(e)
        }), 500


@client_bp.route('/pricing/<int:pricing_id>', methods=['GET'])
@client_required
def get_specific_pricing(pricing_id):
    """Get specific product pricing"""
    try:
        client_id = get_jwt_identity()
        client_id = int(client_id)
        
        pricing = ClientPricing.get_specific_price(client_id, pricing_id)
        
        if not pricing:
            return jsonify({
                'success': False,
                'message': 'Pricing not found'
            }), 404
        
        return jsonify({
            'success': True,
            'pricing': pricing
        }), 200
        
    except Exception as e:
        print(f"Get specific pricing error: {e}")
        return jsonify({
            'success': False,
            'message': 'Failed to get pricing',
            'error': str(e)
        }), 500


@client_bp.route('/pricing/search', methods=['GET'])
@client_required
def search_pricing():
    """Search pricing"""
    try:
        client_id = get_jwt_identity()
        client_id = int(client_id)
        keyword = request.args.get('q', '')
        
        if not keyword:
            return jsonify({
                'success': False,
                'message': 'Search keyword is required'
            }), 400
        
        # Get all client pricing
        all_pricing = ClientPricing.get_client_prices(client_id)
        
        # Filter by keyword
        filtered_pricing = [
            p for p in all_pricing
            if keyword.lower() in (p.get('product_name', '') or '').lower()
            or keyword.lower() in (p.get('product_code', '') or '').lower()
            or keyword.lower() in (p.get('category', '') or '').lower()
        ]
        
        return jsonify({
            'success': True,
            'pricing': filtered_pricing
        }), 200
        
    except Exception as e:
        print(f"Search pricing error: {e}")
        return jsonify({
            'success': False,
            'message': 'Failed to search pricing',
            'error': str(e)
        }), 500