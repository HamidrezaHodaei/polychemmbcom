#/admin_routes.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity
from models.admin import Admin
from models.client import Client
from models.pricing import Pricing, ClientPricing
from middleware.auth import admin_required, log_login_attempt, get_client_ip, get_login_logs

admin_bp = Blueprint('admin', __name__, url_prefix='/api/admin')


@admin_bp.route('/login', methods=['POST'])
def login():
    """ورود ادمین به سیستم"""
    data = request.get_json()
    
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({
            'success': False,
            'message': 'Username and password are required'
        }), 400
    
    # احراز هویت
    admin = Admin.authenticate(username, password)
    
    if not admin:
        # ثبت تلاش ناموفق
        log_login_attempt('admin', 0, username, get_client_ip(), 'Unknown', False)
        
        return jsonify({
            'success': False,
            'message': 'Invalid username or password'
        }), 401
    
    # ✅ تبدیل admin['id'] به string
    admin_id_str = str(admin['id'])
    
    # ایجاد توکن
    access_token = create_access_token(
        identity=admin_id_str,  # ✅ باید string باشد
        additional_claims={'user_type': 'admin'}
    )
    refresh_token = create_refresh_token(
        identity=admin_id_str,  # ✅ باید string باشد
        additional_claims={'user_type': 'admin'}
    )
    
    # ثبت ورود موفق
    log_login_attempt('admin', admin['id'], username, get_client_ip(), 'Tehran, Iran', True)
    
    return jsonify({
        'success': True,
        'message': 'Login successful',
        'token': access_token,
        'refresh_token': refresh_token,
        'user': {
            'id': admin['id'],
            'username': admin['username'],
            'email': admin['email'],
            'first_name': admin['first_name'],
            'last_name': admin['last_name']
        }
    }), 200


@admin_bp.route('/profile', methods=['GET'])
@admin_required
def get_profile():
    """دریافت پروفایل ادمین"""
    admin_id_str = get_jwt_identity()
    
    # ✅ تبدیل از string به int
    try:
        admin_id = int(admin_id_str)
    except (ValueError, TypeError):
        return jsonify({
            'success': False,
            'message': 'Invalid user ID'
        }), 401
    
    admin = Admin.find_by_id(admin_id)
    
    if not admin:
        return jsonify({
            'success': False,
            'message': 'Admin not found'
        }), 404
    
    return jsonify(admin), 200


@admin_bp.route('/logout', methods=['POST'])
@admin_required
def logout():
    """خروج ادمین از سیستم"""
    return jsonify({
        'success': True,
        'message': 'Logged out successfully'
    }), 200


# ========== مدیریت کاربران (Clients) ==========

@admin_bp.route('/clients', methods=['GET'])
@admin_required
def get_all_clients():
    """دریافت لیست تمام کلاینت‌ها"""
    clients = Client.get_all()
    return jsonify({
        'success': True,
        'clients': clients
    }), 200


@admin_bp.route('/clients/<int:client_id>', methods=['GET'])
@admin_required
def get_client(client_id):
    """دریافت اطلاعات یک کلاینت"""
    client = Client.find_by_id(client_id)
    
    if not client:
        return jsonify({
            'success': False,
            'message': 'Client not found'
        }), 404
    
    return jsonify({
        'success': True,
        'client': client
    }), 200


@admin_bp.route('/clients', methods=['POST'])
@admin_required
def create_client():
    """ایجاد کلاینت جدید"""
    data = request.get_json()
    
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    company_name = data.get('company_name')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    phone = data.get('phone')
    address = data.get('address')
    
    if not username or not password:
        return jsonify({
            'success': False,
            'message': 'Username and password are required'
        }), 400
    
    # بررسی تکراری نبودن username
    existing_client = Client.find_by_username(username)
    if existing_client:
        return jsonify({
            'success': False,
            'message': 'Username already exists'
        }), 400
    
    client_id = Client.create(
        username=username,
        password=password,
        email=email,
        company_name=company_name,
        first_name=first_name,
        last_name=last_name,
        phone=phone,
        address=address
    )
    
    if client_id:
        return jsonify({
            'success': True,
            'message': 'Client created successfully',
            'client_id': client_id
        }), 201
    else:
        return jsonify({
            'success': False,
            'message': 'Failed to create client'
        }), 500


@admin_bp.route('/clients/<int:client_id>', methods=['PUT'])
@admin_required
def update_client(client_id):
    """به‌روزرسانی اطلاعات کلاینت"""
    data = request.get_json()
    
    # حذف فیلدهای حساس
    data.pop('password', None)
    data.pop('password_hash', None)
    data.pop('id', None)
    
    success = Client.update(client_id, **data)
    
    if success:
        return jsonify({
            'success': True,
            'message': 'Client updated successfully'
        }), 200
    else:
        return jsonify({
            'success': False,
            'message': 'Failed to update client'
        }), 500


@admin_bp.route('/clients/<int:client_id>', methods=['DELETE'])
@admin_required
def delete_client(client_id):
    """حذف (غیرفعال کردن) کلاینت"""
    success = Client.delete(client_id)
    
    if success:
        return jsonify({
            'success': True,
            'message': 'Client deleted successfully'
        }), 200
    else:
        return jsonify({
            'success': False,
            'message': 'Failed to delete client'
        }), 500


@admin_bp.route('/clients/search', methods=['GET'])
@admin_required
def search_clients():
    """جستجو در کلاینت‌ها"""
    keyword = request.args.get('q', '')
    
    if not keyword:
        return jsonify({
            'success': False,
            'message': 'Search keyword is required'
        }), 400
    
    clients = Client.search(keyword)
    
    return jsonify({
        'success': True,
        'clients': clients
    }), 200


# ========== مدیریت قیمت‌گذاری ==========

@admin_bp.route('/pricing', methods=['GET'])
@admin_required
def get_all_pricing():
    """دریافت لیست تمام قیمت‌ها"""
    pricing_list = Pricing.get_all()
    return jsonify({
        'success': True,
        'pricing': pricing_list
    }), 200


@admin_bp.route('/pricing/<int:pricing_id>', methods=['GET'])
@admin_required
def get_pricing(pricing_id):
    """دریافت یک قیمت"""
    pricing = Pricing.get_by_id(pricing_id)
    
    if not pricing:
        return jsonify({
            'success': False,
            'message': 'Pricing not found'
        }), 404
    
    return jsonify({
        'success': True,
        'pricing': pricing
    }), 200


@admin_bp.route('/pricing', methods=['POST'])
@admin_required
def create_pricing():
    """ایجاد قیمت جدید"""
    data = request.get_json()
    
    product_name = data.get('product_name')
    base_price = data.get('base_price')
    
    if not product_name or not base_price:
        return jsonify({
            'success': False,
            'message': 'Product name and base price are required'
        }), 400
    
    pricing_id = Pricing.create(
        product_name=product_name,
        base_price=base_price,
        product_code=data.get('product_code'),
        category=data.get('category'),
        currency=data.get('currency', 'USD'),
        unit=data.get('unit', 'kg'),
        description=data.get('description')
    )
    
    if pricing_id:
        return jsonify({
            'success': True,
            'message': 'Pricing created successfully',
            'pricing_id': pricing_id
        }), 201
    else:
        return jsonify({
            'success': False,
            'message': 'Failed to create pricing'
        }), 500


@admin_bp.route('/pricing/<int:pricing_id>', methods=['PUT'])
@admin_required
def update_pricing(pricing_id):
    """به‌روزرسانی قیمت"""
    data = request.get_json()
    
    success = Pricing.update(pricing_id, **data)
    
    if success:
        return jsonify({
            'success': True,
            'message': 'Pricing updated successfully'
        }), 200
    else:
        return jsonify({
            'success': False,
            'message': 'Failed to update pricing'
        }), 500


@admin_bp.route('/pricing/<int:pricing_id>', methods=['DELETE'])
@admin_required
def delete_pricing(pricing_id):
    """حذف قیمت"""
    success = Pricing.delete(pricing_id)
    
    if success:
        return jsonify({
            'success': True,
            'message': 'Pricing deleted successfully'
        }), 200
    else:
        return jsonify({
            'success': False,
            'message': 'Failed to delete pricing'
        }), 500


# ========== مدیریت قیمت‌گذاری اختصاصی مشتریان ==========

@admin_bp.route('/clients/<int:client_id>/pricing', methods=['GET'])
@admin_required
def get_client_pricing(client_id):
    """دریافت قیمت‌های اختصاصی یک مشتری"""
    pricing_list = ClientPricing.get_client_prices(client_id)
    
    return jsonify({
        'success': True,
        'pricing': pricing_list
    }), 200


@admin_bp.route('/clients/<int:client_id>/pricing', methods=['POST'])
@admin_required
def set_client_pricing(client_id):
    """تنظیم قیمت اختصاصی برای مشتری"""
    data = request.get_json()
    
    pricing_id = data.get('pricing_id')
    custom_price = data.get('custom_price')
    discount_percentage = data.get('discount_percentage', 0)
    
    if not pricing_id:
        return jsonify({
            'success': False,
            'message': 'Pricing ID is required'
        }), 400
    
    success = ClientPricing.create(client_id, pricing_id, custom_price, discount_percentage)
    
    if success:
        return jsonify({
            'success': True,
            'message': 'Client pricing set successfully'
        }), 200
    else:
        return jsonify({
            'success': False,
            'message': 'Failed to set client pricing'
        }), 500


@admin_bp.route('/clients/<int:client_id>/pricing/bulk', methods=['POST'])
@admin_required
def bulk_update_client_pricing(client_id):
    """به‌روزرسانی دسته‌ای قیمت‌های اختصاصی"""
    data = request.get_json()
    pricing_list = data.get('pricing_list', [])
    
    if not pricing_list:
        return jsonify({
            'success': False,
            'message': 'Pricing list is required'
        }), 400
    
    success = ClientPricing.bulk_update(client_id, pricing_list)
    
    if success:
        return jsonify({
            'success': True,
            'message': 'Client pricing updated successfully'
        }), 200
    else:
        return jsonify({
            'success': False,
            'message': 'Failed to update client pricing'
        }), 500


@admin_bp.route('/activity-logs', methods=['GET'])
@admin_required
def get_activity_logs():
    """دریافت لاگ‌های فعالیت"""
    admin_id_str = get_jwt_identity()
    
    # ✅ تبدیل از string به int
    try:
        admin_id = int(admin_id_str)
    except (ValueError, TypeError):
        return jsonify({
            'success': False,
            'message': 'Invalid user ID'
        }), 401
    
    limit = request.args.get('limit', 10, type=int)
    
    logs = get_login_logs('admin', admin_id, limit)
    
    return jsonify({
        'success': True,
        'logs': logs
    }), 200