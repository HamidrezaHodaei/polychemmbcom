from flask import Flask, app, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import config
from utils.database import Database
from routes.admin_routes import admin_bp
from routes.client_routes import client_bp
from routes.pricing_admin_routes import pricing_admin_bp
from routes.pricing_client_routes import pricing_client_bp
import os

def create_app(config_name='development'):
    """ایجاد اپلیکیشن Flask"""
    
    app = Flask(__name__)
    
    # بارگذاری تنظیمات
    app.config.from_object(config[config_name])
    
    # ✅ FIX: فعال‌سازی CORS با تنظیمات کامل
    CORS(app, 
         resources={r"/api/*": {"origins": "*"}},
         allow_headers=["Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
         methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
         supports_credentials=True,
         expose_headers=["Content-Type", "Authorization"],
         max_age=3600
    )
    
    # راه‌اندازی JWT
    jwt = JWTManager(app)
    
    # ثبت Blueprint‌ها
    app.register_blueprint(admin_bp)
    app.register_blueprint(client_bp)
    # ثبت Blueprint‌های قیمت‌گذاری داینامیک
    app.register_blueprint(pricing_admin_bp)
    app.register_blueprint(pricing_client_bp)
    # روت اصلی
    @app.route('/')
    def index():
        return jsonify({
            'message': 'PolyChem API Server',
            'version': '1.0.0',
            'status': 'running',
            'endpoints': {
                'admin': '/api/admin',
                'client': '/api/client'
            }
        }), 200
    
    # روت سلامتی (Health Check)
    @app.route('/health')
    def health():
        try:
            # بررسی اتصال به دیتابیس
            Database.get_connection().close()
            db_status = 'connected'
        except Exception as e:
            db_status = f'error: {str(e)}'
        
        return jsonify({
            'status': 'healthy',
            'database': db_status
        }), 200
    
    # ✅ FIX: Handle OPTIONS requests explicitly
    @app.before_request
    def handle_preflight():
        from flask import request
        if request.method == "OPTIONS":
            response = app.make_default_options_response()
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
            response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
            response.headers['Access-Control-Max-Age'] = '3600'
            return response
    
    # مدیریت خطای 404
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'message': 'Endpoint not found'
        }), 404
    
    # مدیریت خطای 500
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            'success': False,
            'message': 'Internal server error'
        }), 500
    
    # مدیریت خطای JWT
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
    """راه‌اندازی اولیه دیتابیس"""
    print("🔧 Initializing database...")
    try:
        Database.init_database()
        print("✅ Database initialized successfully!")
        
        # ایجاد ادمین پیش‌فرض اگر وجود ندارد
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
            print("✅ Default admin created (username: admin, password: admin123)")
        
        # ایجاد کلاینت نمونه
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
            print("✅ Test client created (username: test_client, password: test123)")
        
        # ایجاد چند قیمت نمونه
        from models.pricing import Pricing
        sample_products = [
            {
                'product_name': 'PVC Resin',
                'product_code': 'PVC-001',
                'category': 'Resins',
                'base_price': 1250.00,
                'currency': 'USD',
                'unit': 'ton',
                'description': 'High quality PVC resin for industrial use'
            },
            {
                'product_name': 'Polyethylene',
                'product_code': 'PE-002',
                'category': 'Polymers',
                'base_price': 980.00,
                'currency': 'USD',
                'unit': 'ton',
                'description': 'Low density polyethylene'
            },
            {
                'product_name': 'Polypropylene',
                'product_code': 'PP-003',
                'category': 'Polymers',
                'base_price': 1100.00,
                'currency': 'USD',
                'unit': 'ton',
                'description': 'Homopolymer polypropylene'
            }
        ]
        
        existing_products = Pricing.get_all()
        if len(existing_products) == 0:
            for product in sample_products:
                Pricing.create(**product)
            print(f"✅ {len(sample_products)} sample products created")
        
    except Exception as e:
        print(f"❌ Error initializing database: {e}")
        raise


if __name__ == '__main__':
    # راه‌اندازی دیتابیس
    init_database()
    
    # ایجاد و اجرای برنامه
    app = create_app(os.getenv('FLASK_ENV', 'development'))
    
    print("\n" + "="*50)
    print("🚀 PolyChem Flask Server Starting...")
    print("="*50)
    print(f"📍 Server: http://{app.config['HOST']}:{app.config['PORT']}")
    print(f"📍 Admin Panel API: http://{app.config['HOST']}:{app.config['PORT']}/api/admin")
    print(f"📍 Client Panel API: http://{app.config['HOST']}:{app.config['PORT']}/api/client")
    print(f"🌐 CORS: Enabled for all origins (*)")
    print("="*50 + "\n")
    
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )