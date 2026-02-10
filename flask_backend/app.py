# app.py - Production Ready Version for cPanel (NO UNICODE/EMOJI)
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import get_config
from utils.database import Database
import os

def create_app(config_name=None):
    """Create Flask application"""
    
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'production')
    
    app = Flask(__name__)
    
    # Load configuration
    config_class = get_config(config_name)
    app.config.from_object(config_class)
    
    # CORS Configuration
    CORS(app, 
         resources={r"/api/*": {"origins": "*"}},
         allow_headers=["Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
         methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
         supports_credentials=True,
         expose_headers=["Content-Type", "Authorization"],
         max_age=3600
    )
    
    # Initialize JWT
    jwt = JWTManager(app)
    
    # Import and register blueprints
    try:
        # Old blueprints
        from routes.admin_routes import admin_bp
        from routes.client_routes import client_bp
        
        app.register_blueprint(admin_bp)
        app.register_blueprint(client_bp)
        print("Old blueprints registered: admin_bp, client_bp")
        
    except ImportError as e:
        print("Warning importing old routes: " + str(e))
    
    try:
        # New blueprints (Dynamic Pricing)
        from routes.pricing_admin_routes import pricing_admin_bp
        from routes.pricing_client_routes import pricing_client_bp
        
        app.register_blueprint(pricing_admin_bp)
        app.register_blueprint(pricing_client_bp)
        print("New blueprints registered: pricing_admin_bp, pricing_client_bp")
        
    except ImportError as e:
        print("Warning importing pricing routes: " + str(e))
        print("Pricing routes will not be available")
    
    # Root endpoint
    @app.route('/')
    def index():
        return jsonify({
            'message': 'PolyChem API Server',
            'version': '1.0.0',
            'status': 'running',
            'endpoints': {
                'admin': '/api/admin',
                'client': '/api/client',
                'pricing_admin': '/api/admin/pricing-management',
                'pricing_client': '/api/client/pricing'
            }
        }), 200
    
    # API Info endpoint
    @app.route('/api')
    def api_info():
        return jsonify({
            'message': 'PolyChem API Server',
            'version': '1.0.0',
            'status': 'running',
            'endpoints': {
                'admin': '/api/admin',
                'client': '/api/client',
                'pricing_admin': '/api/admin/pricing-management',
                'pricing_client': '/api/client/pricing'
            }
        }), 200
    
    # Health Check endpoint
    @app.route('/health')
    def health():
        try:
            # Check database connection
            conn = Database.get_connection()
            conn.close()
            db_status = 'connected'
        except Exception as e:
            db_status = 'error: ' + str(e)
        
        return jsonify({
            'status': 'healthy',
            'database': db_status,
            'environment': config_name
        }), 200
    
    # List all routes (for debugging)
    @app.route('/api/routes')
    def list_routes():
        """Show all available routes"""
        routes = []
        for rule in app.url_map.iter_rules():
            routes.append({
                'endpoint': rule.endpoint,
                'methods': list(rule.methods),
                'path': str(rule)
            })
        return jsonify({'routes': routes}), 200
    
    # Handle OPTIONS requests (CORS Preflight)
    @app.before_request
    def handle_preflight():
        if request.method == "OPTIONS":
            response = app.make_default_options_response()
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
            response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
            response.headers['Access-Control-Max-Age'] = '3600'
            return response
    
    # Error handler 404
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'message': 'Endpoint not found',
            'path': request.path,
            'method': request.method
        }), 404
    
    # Error handler 500
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            'success': False,
            'message': 'Internal server error',
            'error': str(error)
        }), 500
    
    # JWT error handlers
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({
            'success': False,
            'message': 'Token has expired'
        }), 401
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({
            'success': False,
            'message': 'Invalid token'
        }), 401
    
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify({
            'success': False,
            'message': 'Authorization token is missing'
        }), 401
    
    return app


def init_database():
    """Initialize database"""
    print("Initializing database...")
    try:
        Database.init_database()
        print("Database initialized successfully")
        
        # Create default admin
        try:
            from models.admin import Admin
            admin = Admin.find_by_username('admin')
            if not admin:
                Admin.create(
                    username='admin',
                    password='admin123',
                    email='admin@polychemmb.com',
                    first_name='Admin',
                    last_name='User'
                )
                print("Default admin created (username: admin, password: admin123)")
        except ImportError as e:
            print("Could not create admin: " + str(e))
        
        # Create test client
        try:
            from models.client import Client
            client = Client.find_by_username('test_client')
            if not client:
                Client.create(
                    username='test_client',
                    password='test123',
                    email='test@example.com',
                    company_name='Test Company',
                    first_name='Test',
                    last_name='Client'
                )
                print("Test client created (username: test_client, password: test123)")
        except ImportError as e:
            print("Could not create test client: " + str(e))
        
    except Exception as e:
        print("Error initializing database: " + str(e))
        # Don't raise - let app continue even if DB init fails


if __name__ == '__main__':
    # Initialize database
    init_database()
    
    # Create and run application
    app = create_app(os.getenv('FLASK_ENV', 'development'))
    
    print("\n" + "="*50)
    print("PolyChem Flask Server Starting...")
    print("="*50)
    print("Server: http://" + str(app.config.get('HOST', '0.0.0.0')) + ":" + str(app.config.get('PORT', 8080)))
    print("Environment: " + str(os.getenv('FLASK_ENV', 'development')))
    print("="*50 + "\n")
    
    app.run(
        host=app.config.get('HOST', '0.0.0.0'),
        port=app.config.get('PORT', 8080),
        debug=app.config.get('DEBUG', False)
    )