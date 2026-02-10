# models/dynamic_pricing.py
"""
New models for dynamic pricing system
This file replaces the old pricing.py
"""

from utils.database import Database


class Category:
    """Category and subcategory management"""
    
    @staticmethod
    def create(name, parent_id=None, display_order=0):
        """Create new category"""
        query = """
        INSERT INTO categories (name, parent_id, display_order)
        VALUES (%s, %s, %s)
        """
        try:
            return Database.execute_query(query, (name, parent_id, display_order), commit=True)
        except Exception as e:
            print(f"Error creating category: {e}")
            return None
    
    @staticmethod
    def get_all(include_inactive=False):
        """Get all categories"""
        where_clause = "" if include_inactive else "WHERE is_active = TRUE"
        query = f"""
        SELECT id, name, parent_id, display_order, is_active
        FROM categories
        {where_clause}
        ORDER BY display_order ASC, name ASC
        """
        return Database.execute_query(query, fetch_all=True)
    
    @staticmethod
    def get_main_categories():
        """Get main categories (without parent)"""
        query = """
        SELECT id, name, display_order
        FROM categories
        WHERE parent_id IS NULL AND is_active = TRUE
        ORDER BY display_order ASC
        """
        return Database.execute_query(query, fetch_all=True)
    
    @staticmethod
    def get_subcategories(parent_id):
        """Get subcategories of a category"""
        query = """
        SELECT id, name, display_order
        FROM categories
        WHERE parent_id = %s AND is_active = TRUE
        ORDER BY display_order ASC
        """
        return Database.execute_query(query, (parent_id,), fetch_all=True)
    
    @staticmethod
    def get_category_tree():
        """Get complete category tree"""
        main_cats = Category.get_main_categories()
        tree = []
        
        for cat in main_cats:
            cat_dict = dict(cat)
            cat_dict['subcategories'] = Category.get_subcategories(cat['id'])
            tree.append(cat_dict)
        
        return tree


class Product:
    """Product management"""
    
    @staticmethod
    def create(name, category_id, product_code=None, subcategory_id=None, 
               free_shipping_threshold=30000, description=None):
        """Create new product"""
        query = """
        INSERT INTO products 
        (name, product_code, category_id, subcategory_id, free_shipping_threshold, description)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        try:
            return Database.execute_query(
                query,
                (name, product_code, category_id, subcategory_id, free_shipping_threshold, description),
                commit=True
            )
        except Exception as e:
            print(f"Error creating product: {e}")
            return None
    
    @staticmethod
    def get_all():
        """Get all products with category information"""
        query = """
        SELECT 
            p.id,
            p.name,
            p.product_code,
            p.category_id,
            c1.name AS category_name,
            p.subcategory_id,
            c2.name AS subcategory_name,
            p.free_shipping_threshold,
            p.description,
            p.is_active,
            p.created_at,
            p.updated_at
        FROM products p
        LEFT JOIN categories c1 ON p.category_id = c1.id
        LEFT JOIN categories c2 ON p.subcategory_id = c2.id
        WHERE p.is_active = TRUE
        ORDER BY c1.name, c2.name, p.name
        """
        return Database.execute_query(query, fetch_all=True)
    
    @staticmethod
    def get_by_id(product_id):
        """Get product with details"""
        query = """
        SELECT 
            p.id,
            p.name,
            p.product_code,
            p.category_id,
            c1.name AS category_name,
            p.subcategory_id,
            c2.name AS subcategory_name,
            p.free_shipping_threshold,
            p.description,
            p.is_active
        FROM products p
        LEFT JOIN categories c1 ON p.category_id = c1.id
        LEFT JOIN categories c2 ON p.subcategory_id = c2.id
        WHERE p.id = %s
        """
        return Database.execute_query(query, (product_id,), fetch_one=True)
    
    @staticmethod
    def get_by_category(category_id, subcategory_id=None):
        """Get products of a category"""
        if subcategory_id:
            query = """
            SELECT id, name, product_code, free_shipping_threshold, description
            FROM products
            WHERE category_id = %s AND subcategory_id = %s AND is_active = TRUE
            ORDER BY name
            """
            return Database.execute_query(query, (category_id, subcategory_id), fetch_all=True)
        else:
            query = """
            SELECT id, name, product_code, free_shipping_threshold, description
            FROM products
            WHERE category_id = %s AND is_active = TRUE
            ORDER BY name
            """
            return Database.execute_query(query, (category_id,), fetch_all=True)
    
    @staticmethod
    def update(product_id, **kwargs):
        """Update product"""
        allowed_fields = ['name', 'product_code', 'category_id', 'subcategory_id',
                         'free_shipping_threshold', 'description', 'is_active']
        
        updates = []
        params = []
        
        for field, value in kwargs.items():
            if field in allowed_fields:
                updates.append(f"{field} = %s")
                params.append(value)
        
        if not updates:
            return False
        
        params.append(product_id)
        query = f"UPDATE products SET {', '.join(updates)} WHERE id = %s"
        
        try:
            Database.execute_query(query, tuple(params), commit=True)
            return True
        except Exception as e:
            print(f"Error updating product: {e}")
            return False
    
    @staticmethod
    def delete(product_id):
        """Delete product (deactivate)"""
        query = "UPDATE products SET is_active = FALSE WHERE id = %s"
        try:
            Database.execute_query(query, (product_id,), commit=True)
            return True
        except Exception as e:
            print(f"Error deleting product: {e}")
            return False


class WeightBracket:
    """Product weight bracket management"""
    
    @staticmethod
    def create(product_id, min_weight, price_per_kg):
        """Create new weight bracket"""
        query = """
        INSERT INTO weight_brackets (product_id, min_weight, price_per_kg)
        VALUES (%s, %s, %s)
        """
        try:
            return Database.execute_query(query, (product_id, min_weight, price_per_kg), commit=True)
        except Exception as e:
            print(f"Error creating weight bracket: {e}")
            return None
    
    @staticmethod
    def get_by_product(product_id):
        """Get all brackets of a product"""
        query = """
        SELECT id, min_weight, price_per_kg
        FROM weight_brackets
        WHERE product_id = %s AND is_active = TRUE
        ORDER BY min_weight ASC
        """
        return Database.execute_query(query, (product_id,), fetch_all=True)
    
    @staticmethod
    def update(bracket_id, **kwargs):
        """Update bracket"""
        allowed_fields = ['min_weight', 'price_per_kg', 'is_active']
        
        updates = []
        params = []
        
        for field, value in kwargs.items():
            if field in allowed_fields:
                updates.append(f"{field} = %s")
                params.append(value)
        
        if not updates:
            return False
        
        params.append(bracket_id)
        query = f"UPDATE weight_brackets SET {', '.join(updates)} WHERE id = %s"
        
        try:
            Database.execute_query(query, tuple(params), commit=True)
            return True
        except Exception as e:
            print(f"Error updating weight bracket: {e}")
            return False
    
    @staticmethod
    def delete(bracket_id):
        """Delete bracket"""
        query = "DELETE FROM weight_brackets WHERE id = %s"
        try:
            Database.execute_query(query, (bracket_id,), commit=True)
            return True
        except Exception as e:
            print(f"Error deleting weight bracket: {e}")
            return False
    
    @staticmethod
    def bulk_upsert(product_id, brackets):
        """
        Bulk update brackets
        brackets: [{'min_weight': 100, 'price_per_kg': 1.2}, ...]
        """
        try:
            # Delete old brackets
            Database.execute_query(
                "DELETE FROM weight_brackets WHERE product_id = %s",
                (product_id,),
                commit=True
            )
            
            # Add new brackets
            for bracket in brackets:
                WeightBracket.create(
                    product_id,
                    bracket['min_weight'],
                    bracket['price_per_kg']
                )
            
            return True
        except Exception as e:
            print(f"Error in bulk upsert: {e}")
            return False


class PackagingType:
    """Packaging type management"""
    
    @staticmethod
    def create(name, extra_cost=0, cost_type='fixed'):
        """Create new packaging type"""
        query = """
        INSERT INTO packaging_types (name, extra_cost, cost_type)
        VALUES (%s, %s, %s)
        """
        try:
            return Database.execute_query(query, (name, extra_cost, cost_type), commit=True)
        except Exception as e:
            print(f"Error creating packaging type: {e}")
            return None
    
    @staticmethod
    def get_all():
        """Get all packaging types"""
        query = """
        SELECT id, name, extra_cost, cost_type, is_active
        FROM packaging_types
        WHERE is_active = TRUE
        ORDER BY name
        """
        return Database.execute_query(query, fetch_all=True)
    
    @staticmethod
    def update(packaging_id, **kwargs):
        """Update packaging"""
        allowed_fields = ['name', 'extra_cost', 'cost_type', 'is_active']
        
        updates = []
        params = []
        
        for field, value in kwargs.items():
            if field in allowed_fields:
                updates.append(f"{field} = %s")
                params.append(value)
        
        if not updates:
            return False
        
        params.append(packaging_id)
        query = f"UPDATE packaging_types SET {', '.join(updates)} WHERE id = %s"
        
        try:
            Database.execute_query(query, tuple(params), commit=True)
            return True
        except Exception as e:
            print(f"Error updating packaging type: {e}")
            return False
    
    @staticmethod
    def delete(packaging_id):
        """Delete packaging"""
        query = "UPDATE packaging_types SET is_active = FALSE WHERE id = %s"
        try:
            Database.execute_query(query, (packaging_id,), commit=True)
            return True
        except Exception as e:
            print(f"Error deleting packaging type: {e}")
            return False


class PaymentTerm:
    """Payment terms management"""
    
    @staticmethod
    def create(name, adjustment=0, adjustment_type='percent'):
        """Create new payment term"""
        query = """
        INSERT INTO payment_terms (name, adjustment, adjustment_type)
        VALUES (%s, %s, %s)
        """
        try:
            return Database.execute_query(query, (name, adjustment, adjustment_type), commit=True)
        except Exception as e:
            print(f"Error creating payment term: {e}")
            return None
    
    @staticmethod
    def get_all():
        """Get all payment terms"""
        query = """
        SELECT id, name, adjustment, adjustment_type, is_active
        FROM payment_terms
        WHERE is_active = TRUE
        ORDER BY adjustment ASC
        """
        return Database.execute_query(query, fetch_all=True)
    
    @staticmethod
    def update(term_id, **kwargs):
        """Update payment term"""
        allowed_fields = ['name', 'adjustment', 'adjustment_type', 'is_active']
        
        updates = []
        params = []
        
        for field, value in kwargs.items():
            if field in allowed_fields:
                updates.append(f"{field} = %s")
                params.append(value)
        
        if not updates:
            return False
        
        params.append(term_id)
        query = f"UPDATE payment_terms SET {', '.join(updates)} WHERE id = %s"
        
        try:
            Database.execute_query(query, tuple(params), commit=True)
            return True
        except Exception as e:
            print(f"Error updating payment term: {e}")
            return False
    
    @staticmethod
    def delete(term_id):
        """Delete payment term"""
        query = "UPDATE payment_terms SET is_active = FALSE WHERE id = %s"
        try:
            Database.execute_query(query, (term_id,), commit=True)
            return True
        except Exception as e:
            print(f"Error deleting payment term: {e}")
            return False


class DeliverySettings:
    """Delivery settings management"""
    
    @staticmethod
    def get(setting_key):
        """Get a setting"""
        query = "SELECT setting_value FROM delivery_settings WHERE setting_key = %s"
        result = Database.execute_query(query, (setting_key,), fetch_one=True)
        return result['setting_value'] if result else None
    
    @staticmethod
    def set(setting_key, setting_value, description=None):
        """Set a value"""
        query = """
        INSERT INTO delivery_settings (setting_key, setting_value, description)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE setting_value = VALUES(setting_value), description = VALUES(description)
        """
        try:
            Database.execute_query(query, (setting_key, setting_value, description), commit=True)
            return True
        except Exception as e:
            print(f"Error setting delivery setting: {e}")
            return False
    
    @staticmethod
    def get_all():
        """Get all settings"""
        query = "SELECT setting_key, setting_value, description FROM delivery_settings"
        return Database.execute_query(query, fetch_all=True)


class PriceCalculator:
    """Final price calculator"""
    
    @staticmethod
    def calculate(product_id, weight_kg, packaging_id, payment_term_id, delivery_method='factory'):
        """
        Calculate final price
        
        Returns:
            dict: {
                'base_price': float,
                'packaging_cost': float,
                'delivery_cost': float,
                'payment_adjustment': float,
                'total_price': float,
                'breakdown': {}
            }
        """
        try:
            # 1. Get product info
            product = Product.get_by_id(product_id)
            if not product:
                raise ValueError("Product not found")
            
            # 2. Find appropriate bracket
            brackets = WeightBracket.get_by_product(product_id)
            if not brackets:
                raise ValueError("No price brackets defined for this product")
            
            # Sort brackets from high to low
            sorted_brackets = sorted(brackets, key=lambda x: x['min_weight'], reverse=True)
            
            # Find first bracket where weight is greater than minimum
            applicable_bracket = None
            for bracket in sorted_brackets:
                if weight_kg >= bracket['min_weight']:
                    applicable_bracket = bracket
                    break
            
            if not applicable_bracket:
                applicable_bracket = sorted_brackets[-1]  # Lowest bracket
            
            # Calculate base price
            base_price = float(applicable_bracket['price_per_kg']) * weight_kg
            
            # 3. Calculate packaging cost
            packaging_query = "SELECT extra_cost, cost_type FROM packaging_types WHERE id = %s"
            packaging = Database.execute_query(packaging_query, (packaging_id,), fetch_one=True)
            
            if packaging['cost_type'] == 'percent':
                packaging_cost = base_price * (float(packaging['extra_cost']) / 100)
            else:
                packaging_cost = float(packaging['extra_cost'])
            
            # 4. Calculate delivery cost
            delivery_cost = 0
            if delivery_method == 'customer':
                # Check free shipping threshold
                if weight_kg < product['free_shipping_threshold']:
                    delivery_cost_setting = DeliverySettings.get('delivery_cost_customer')
                    delivery_cost = float(delivery_cost_setting) if delivery_cost_setting else 150
            
            # 5. Calculate payment adjustment
            payment_query = "SELECT adjustment, adjustment_type FROM payment_terms WHERE id = %s"
            payment = Database.execute_query(payment_query, (payment_term_id,), fetch_one=True)
            
            subtotal = base_price + packaging_cost + delivery_cost
            
            if payment['adjustment_type'] == 'percent':
                payment_adjustment = subtotal * (float(payment['adjustment']) / 100)
            else:
                payment_adjustment = float(payment['adjustment'])
            
            # 6. Calculate final price
            total_price = subtotal + payment_adjustment
            
            return {
                'base_price': round(base_price, 2),
                'packaging_cost': round(packaging_cost, 2),
                'delivery_cost': round(delivery_cost, 2),
                'payment_adjustment': round(payment_adjustment, 2),
                'total_price': round(total_price, 2),
                'breakdown': {
                    'product_name': product['name'],
                    'weight_kg': weight_kg,
                    'price_per_kg': float(applicable_bracket['price_per_kg']),
                    'free_shipping': delivery_method == 'customer' and weight_kg >= product['free_shipping_threshold']
                }
            }
            
        except Exception as e:
            print(f"Error calculating price: {e}")
            raise