# routes/pricing_client_routes.py
"""
API Routes برای نمایش قیمت‌ها و محصولات در پنل کلاینت
این فایل باید به client_routes.py اضافه شود
"""

from flask import Blueprint, request, jsonify
from middleware.auth import client_required
from flask_jwt_extended import get_jwt_identity
from models.dynamic_pricing import (
    Category, Product, WeightBracket, 
    PackagingType, PaymentTerm, DeliverySettings,
    PriceCalculator
)

pricing_client_bp = Blueprint('pricing_client', __name__, url_prefix='/api/client/pricing')


# ========== دریافت داده‌های عمومی برای UI ==========

@pricing_client_bp.route('/categories-tree', methods=['GET'])
@client_required
def get_categories_tree():
    """
    دریافت درخت کامل دسته‌بندی‌ها و محصولات
    برای پر کردن dropdown‌های Select Grade
    """
    try:
        tree = Category.get_category_tree()
        
        # اضافه کردن محصولات به هر دسته
        for category in tree:
            # محصولات دسته اصلی (بدون زیردسته)
            category['products'] = Product.get_by_category(category['id'])
            
            # محصولات زیردسته‌ها
            for subcategory in category.get('subcategories', []):
                subcategory['products'] = Product.get_by_category(
                    category['id'], 
                    subcategory['id']
                )
        
        return jsonify({
            'success': True,
            'categories': tree
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500


@pricing_client_bp.route('/packaging-options', methods=['GET'])
@client_required
def get_packaging_options():
    """دریافت گزینه‌های بسته‌بندی"""
    try:
        packaging = PackagingType.get_all()
        return jsonify({
            'success': True,
            'packaging': packaging
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500


@pricing_client_bp.route('/payment-options', methods=['GET'])
@client_required
def get_payment_options():
    """دریافت گزینه‌های پرداخت"""
    try:
        terms = PaymentTerm.get_all()
        return jsonify({
            'success': True,
            'payment_terms': terms
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500


@pricing_client_bp.route('/delivery-options', methods=['GET'])
@client_required
def get_delivery_options():
    """دریافت گزینه‌های ارسال"""
    try:
        delivery_method = DeliverySettings.get('delivery_method')
        delivery_cost_customer = DeliverySettings.get('delivery_cost_customer')
        
        return jsonify({
            'success': True,
            'options': {
                'methods': [
                    {
                        'id': 'factory',
                        'name': 'Ex-Factory Delivery',
                        'cost': 0
                    },
                    {
                        'id': 'customer',
                        'name': 'Delivery to Customer',
                        'cost': float(delivery_cost_customer) if delivery_cost_customer else 150
                    }
                ],
                'default_method': delivery_method or 'factory'
            }
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500


# ========== دریافت جزئیات محصول ==========

@pricing_client_bp.route('/products/<int:product_id>', methods=['GET'])
@client_required
def get_product_details(product_id):
    """
    دریافت جزئیات کامل یک محصول شامل براکت‌های وزنی
    """
    try:
        product = Product.get_by_id(product_id)
        
        if not product:
            return jsonify({
                'success': False,
                'message': 'Product not found'
            }), 404
        
        # دریافت براکت‌های وزنی
        product['weight_brackets'] = WeightBracket.get_by_product(product_id)
        
        return jsonify({
            'success': True,
            'product': product
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500


@pricing_client_bp.route('/products/<int:product_id>/weight-options', methods=['GET'])
@client_required
def get_product_weight_options(product_id):
    """
    دریافت گزینه‌های وزنی موجود برای یک محصول
    برای پر کردن dropdown "Pick Your Amount"
    """
    try:
        brackets = WeightBracket.get_by_product(product_id)
        
        # استخراج وزن‌های موجود
        weight_options = [b['min_weight'] for b in brackets]
        weight_options.sort()
        
        return jsonify({
            'success': True,
            'weight_options': weight_options,
            'brackets': brackets
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500


# ========== محاسبه قیمت ==========

@pricing_client_bp.route('/calculate', methods=['POST'])
@client_required
def calculate_price():
    """
    محاسبه قیمت نهایی بر اساس انتخاب‌های کاربر
    """
    data = request.get_json()
    
    product_id = data.get('product_id')
    weight_kg = data.get('weight_kg')
    packaging_id = data.get('packaging_id')
    payment_term_id = data.get('payment_term_id')
    delivery_method = data.get('delivery_method', 'factory')
    
    # اعتبارسنجی
    if not all([product_id, weight_kg, packaging_id, payment_term_id]):
        return jsonify({
            'success': False,
            'message': 'Missing required parameters: product_id, weight_kg, packaging_id, payment_term_id'
        }), 400
    
    try:
        # محاسبه قیمت
        result = PriceCalculator.calculate(
            product_id,
            int(weight_kg),
            packaging_id,
            payment_term_id,
            delivery_method
        )
        
        return jsonify({
            'success': True,
            'price': result
        }), 200
    except ValueError as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 400
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error calculating price: {str(e)}'
        }), 500


# ========== ذخیره سفارش موقت (برای Start Order) ==========

@pricing_client_bp.route('/save-quote', methods=['POST'])
@client_required
def save_quote():
    """
    ذخیره یک پیش‌فاکتور موقت
    این می‌تواند بعداً به سفارش واقعی تبدیل شود
    """
    client_id = int(get_jwt_identity())
    data = request.get_json()
    
    try:
        # محاسبه قیمت
        price_result = PriceCalculator.calculate(
            data['product_id'],
            data['weight_kg'],
            data['packaging_id'],
            data['payment_term_id'],
            data.get('delivery_method', 'factory')
        )
        
        # اینجا می‌توانید پیش‌فاکتور را در دیتابیس ذخیره کنید
        # یا آن را به صورت JSON برگردانید
        
        return jsonify({
            'success': True,
            'message': 'Quote saved successfully',
            'quote': {
                'client_id': client_id,
                'product_id': data['product_id'],
                'weight_kg': data['weight_kg'],
                'packaging_id': data['packaging_id'],
                'payment_term_id': data['payment_term_id'],
                'delivery_method': data.get('delivery_method', 'factory'),
                'price_breakdown': price_result
            }
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500


# ========== جستجو در محصولات ==========

@pricing_client_bp.route('/search', methods=['GET'])
@client_required
def search_products():
    """جستجو در محصولات"""
    keyword = request.args.get('q', '')
    category_id = request.args.get('category_id', type=int)
    subcategory_id = request.args.get('subcategory_id', type=int)
    
    try:
        if category_id:
            products = Product.get_by_category(category_id, subcategory_id)
        else:
            # جستجو در تمام محصولات
            all_products = Product.get_all()
            
            if keyword:
                products = [
                    p for p in all_products
                    if keyword.lower() in p.get('name', '').lower()
                    or keyword.lower() in (p.get('product_code', '') or '').lower()
                ]
            else:
                products = all_products
        
        return jsonify({
            'success': True,
            'products': products
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500