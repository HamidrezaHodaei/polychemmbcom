from flask import Blueprint, request, jsonify
from middleware.auth import admin_required
from models.dynamic_pricing import (
    Category, Product, WeightBracket, 
    PackagingType, PaymentTerm, DeliverySettings,
    PriceCalculator
)

pricing_admin_bp = Blueprint('pricing_admin', __name__, url_prefix='/admin/pricing-management')


# ===== Categories =====

@pricing_admin_bp.route('/categories', methods=['GET'])
@admin_required
def get_categories():
    """Get complete category tree"""
    try:
        tree = Category.get_category_tree()
        return jsonify({
            'success': True,
            'categories': tree
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500


@pricing_admin_bp.route('/categories', methods=['POST'])
@admin_required
def create_category():
    """Create new category"""
    data = request.get_json()
    
    name = data.get('name')
    parent_id = data.get('parent_id')
    display_order = data.get('display_order', 0)
    
    if not name:
        return jsonify({
            'success': False,
            'message': 'Name is required'
        }), 400
    
    cat_id = Category.create(name, parent_id, display_order)
    
    if cat_id:
        return jsonify({
            'success': True,
            'message': 'Category created successfully',
            'category_id': cat_id
        }), 201
    else:
        return jsonify({
            'success': False,
            'message': 'Failed to create category'
        }), 500


# ===== Products =====

@pricing_admin_bp.route('/products', methods=['GET'])
@admin_required
def get_products():
    """Get all products"""
    try:
        products = Product.get_all()
        
        # Add weight brackets to each product
        for product in products:
            product['weight_brackets'] = WeightBracket.get_by_product(product['id'])
        
        return jsonify({
            'success': True,
            'products': products
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500


@pricing_admin_bp.route('/products/<int:product_id>', methods=['GET'])
@admin_required
def get_product(product_id):
    """Get product with details"""
    try:
        product = Product.get_by_id(product_id)
        
        if not product:
            return jsonify({
                'success': False,
                'message': 'Product not found'
            }), 404
        
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


@pricing_admin_bp.route('/products', methods=['POST'])
@admin_required
def create_product():
    """Create new product with weight brackets"""
    data = request.get_json()
    
    name = data.get('name')
    category_id = data.get('category_id')
    
    if not name or not category_id:
        return jsonify({
            'success': False,
            'message': 'Name and category_id are required'
        }), 400
    
    try:
        # Create product
        product_id = Product.create(
            name=name,
            category_id=category_id,
            product_code=data.get('product_code'),
            subcategory_id=data.get('subcategory_id'),
            free_shipping_threshold=data.get('free_shipping_threshold', 30000),
            description=data.get('description')
        )
        
        if not product_id:
            raise Exception("Failed to create product")
        
        # Add weight brackets
        weight_brackets = data.get('weight_brackets', [])
        if weight_brackets:
            for bracket in weight_brackets:
                WeightBracket.create(
                    product_id,
                    bracket['min_weight'],
                    bracket['price_per_kg']
                )
        
        return jsonify({
            'success': True,
            'message': 'Product created successfully',
            'product_id': product_id
        }), 201
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500


@pricing_admin_bp.route('/products/<int:product_id>', methods=['PUT'])
@admin_required
def update_product(product_id):
    """Update product and weight brackets"""
    data = request.get_json()
    
    try:
        # Update main product information
        product_data = {k: v for k, v in data.items() if k != 'weight_brackets'}
        if product_data:
            Product.update(product_id, **product_data)
        
        # Update weight brackets
        if 'weight_brackets' in data:
            WeightBracket.bulk_upsert(product_id, data['weight_brackets'])
        
        return jsonify({
            'success': True,
            'message': 'Product updated successfully'
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500


@pricing_admin_bp.route('/products/<int:product_id>', methods=['DELETE'])
@admin_required
def delete_product(product_id):
    """Delete product"""
    success = Product.delete(product_id)
    
    if success:
        return jsonify({
            'success': True,
            'message': 'Product deleted successfully'
        }), 200
    else:
        return jsonify({
            'success': False,
            'message': 'Failed to delete product'
        }), 500


# ===== Packaging =====

@pricing_admin_bp.route('/packaging', methods=['GET'])
@admin_required
def get_packaging_types():
    """Get all packaging types"""
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


@pricing_admin_bp.route('/packaging', methods=['POST'])
@admin_required
def create_packaging():
    """Create new packaging type"""
    data = request.get_json()
    
    name = data.get('name')
    extra_cost = data.get('extra_cost', 0)
    cost_type = data.get('cost_type', 'fixed')
    
    if not name:
        return jsonify({
            'success': False,
            'message': 'Name is required'
        }), 400
    
    pkg_id = PackagingType.create(name, extra_cost, cost_type)
    
    if pkg_id:
        return jsonify({
            'success': True,
            'message': 'Packaging type created successfully',
            'packaging_id': pkg_id
        }), 201
    else:
        return jsonify({
            'success': False,
            'message': 'Failed to create packaging type'
        }), 500


@pricing_admin_bp.route('/packaging/<int:packaging_id>', methods=['PUT'])
@admin_required
def update_packaging(packaging_id):
    """Update packaging type"""
    data = request.get_json()
    
    success = PackagingType.update(packaging_id, **data)
    
    if success:
        return jsonify({
            'success': True,
            'message': 'Packaging type updated successfully'
        }), 200
    else:
        return jsonify({
            'success': False,
            'message': 'Failed to update packaging type'
        }), 500


@pricing_admin_bp.route('/packaging/<int:packaging_id>', methods=['DELETE'])
@admin_required
def delete_packaging(packaging_id):
    """Delete packaging type"""
    success = PackagingType.delete(packaging_id)
    
    if success:
        return jsonify({
            'success': True,
            'message': 'Packaging type deleted successfully'
        }), 200
    else:
        return jsonify({
            'success': False,
            'message': 'Failed to delete packaging type'
        }), 500


# ===== Payment Terms =====

@pricing_admin_bp.route('/payment-terms', methods=['GET'])
@admin_required
def get_payment_terms():
    """Get all payment terms"""
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


@pricing_admin_bp.route('/payment-terms', methods=['POST'])
@admin_required
def create_payment_term():
    """Create new payment term"""
    data = request.get_json()
    
    name = data.get('name')
    adjustment = data.get('adjustment', 0)
    adjustment_type = data.get('adjustment_type', 'percent')
    
    if not name:
        return jsonify({
            'success': False,
            'message': 'Name is required'
        }), 400
    
    term_id = PaymentTerm.create(name, adjustment, adjustment_type)
    
    if term_id:
        return jsonify({
            'success': True,
            'message': 'Payment term created successfully',
            'term_id': term_id
        }), 201
    else:
        return jsonify({
            'success': False,
            'message': 'Failed to create payment term'
        }), 500


@pricing_admin_bp.route('/payment-terms/<int:term_id>', methods=['PUT'])
@admin_required
def update_payment_term(term_id):
    """Update payment term"""
    data = request.get_json()
    
    success = PaymentTerm.update(term_id, **data)
    
    if success:
        return jsonify({
            'success': True,
            'message': 'Payment term updated successfully'
        }), 200
    else:
        return jsonify({
            'success': False,
            'message': 'Failed to update payment term'
        }), 500


@pricing_admin_bp.route('/payment-terms/<int:term_id>', methods=['DELETE'])
@admin_required
def delete_payment_term(term_id):
    """Delete payment term"""
    success = PaymentTerm.delete(term_id)
    
    if success:
        return jsonify({
            'success': True,
            'message': 'Payment term deleted successfully'
        }), 200
    else:
        return jsonify({
            'success': False,
            'message': 'Failed to delete payment term'
        }), 500


# ===== Delivery Settings =====

@pricing_admin_bp.route('/delivery-settings', methods=['GET'])
@admin_required
def get_delivery_settings():
    """Get delivery settings"""
    try:
        settings = DeliverySettings.get_all()
        
        # Convert to dictionary
        settings_dict = {s['setting_key']: s['setting_value'] for s in settings}
        
        return jsonify({
            'success': True,
            'settings': settings_dict
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500


@pricing_admin_bp.route('/delivery-settings', methods=['POST'])
@admin_required
def update_delivery_settings():
    """Update delivery settings"""
    data = request.get_json()
    
    try:
        for key, value in data.items():
            DeliverySettings.set(key, str(value))
        
        return jsonify({
            'success': True,
            'message': 'Delivery settings updated successfully'
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500


# ===== Price Calculation =====

@pricing_admin_bp.route('/calculate-price', methods=['POST'])
@admin_required
def calculate_price():
    """Calculate price for preview"""
    data = request.get_json()
    
    product_id = data.get('product_id')
    weight_kg = data.get('weight_kg')
    packaging_id = data.get('packaging_id')
    payment_term_id = data.get('payment_term_id')
    delivery_method = data.get('delivery_method', 'factory')
    
    if not all([product_id, weight_kg, packaging_id, payment_term_id]):
        return jsonify({
            'success': False,
            'message': 'Missing required parameters'
        }), 400
    
    try:
        result = PriceCalculator.calculate(
            product_id,
            weight_kg,
            packaging_id,
            payment_term_id,
            delivery_method
        )
        
        return jsonify({
            'success': True,
            'price': result
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500