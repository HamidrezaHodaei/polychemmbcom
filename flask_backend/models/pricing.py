#/pricing.py
from utils.database import Database

class Pricing:
    """مدل قیمت‌گذاری برای مدیریت قیمت محصولات"""
    
    @staticmethod
    def create(product_name, base_price, product_code=None, category=None, 
               currency='USD', unit='kg', description=None):
        """ایجاد قیمت جدید برای محصول"""
        query = """
        INSERT INTO pricing (product_name, product_code, category, base_price, 
                           currency, unit, description)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        try:
            pricing_id = Database.execute_query(
                query,
                (product_name, product_code, category, base_price, currency, unit, description),
                commit=True
            )
            return pricing_id
        except Exception as e:
            print(f"خطا در ایجاد قیمت: {e}")
            return None
    
    @staticmethod
    def get_all():
        """دریافت لیست تمام قیمت‌ها"""
        query = """
        SELECT id, product_name, product_code, category, base_price, 
               currency, unit, description, is_active, created_at, updated_at
        FROM pricing
        WHERE is_active = TRUE
        ORDER BY product_name ASC
        """
        return Database.execute_query(query, fetch_all=True)
    
    @staticmethod
    def get_by_id(pricing_id):
        """دریافت قیمت با ID"""
        query = """
        SELECT id, product_name, product_code, category, base_price, 
               currency, unit, description, is_active
        FROM pricing
        WHERE id = %s
        """
        return Database.execute_query(query, (pricing_id,), fetch_one=True)
    
    @staticmethod
    def get_by_category(category):
        """دریافت قیمت‌ها بر اساس دسته‌بندی"""
        query = """
        SELECT id, product_name, product_code, category, base_price, 
               currency, unit, description
        FROM pricing
        WHERE category = %s AND is_active = TRUE
        ORDER BY product_name ASC
        """
        return Database.execute_query(query, (category,), fetch_all=True)
    
    @staticmethod
    def update(pricing_id, **kwargs):
        """به‌روزرسانی قیمت"""
        allowed_fields = ['product_name', 'product_code', 'category', 
                         'base_price', 'currency', 'unit', 'description', 'is_active']
        updates = []
        params = []
        
        for field, value in kwargs.items():
            if field in allowed_fields:
                updates.append(f"{field} = %s")
                params.append(value)
        
        if not updates:
            return False
        
        params.append(pricing_id)
        query = f"UPDATE pricing SET {', '.join(updates)} WHERE id = %s"
        
        try:
            Database.execute_query(query, tuple(params), commit=True)
            return True
        except Exception as e:
            print(f"خطا در به‌روزرسانی قیمت: {e}")
            return False
    
    @staticmethod
    def delete(pricing_id):
        """حذف قیمت (غیرفعال کردن)"""
        query = "UPDATE pricing SET is_active = FALSE WHERE id = %s"
        try:
            Database.execute_query(query, (pricing_id,), commit=True)
            return True
        except Exception as e:
            print(f"خطا در حذف قیمت: {e}")
            return False
    
    @staticmethod
    def search(keyword):
        """جستجو در قیمت‌ها"""
        query = """
        SELECT id, product_name, product_code, category, base_price, 
               currency, unit, description
        FROM pricing
        WHERE (product_name LIKE %s OR product_code LIKE %s OR category LIKE %s)
          AND is_active = TRUE
        ORDER BY product_name ASC
        """
        search_term = f"%{keyword}%"
        return Database.execute_query(
            query,
            (search_term, search_term, search_term),
            fetch_all=True
        )


class ClientPricing:
    """مدل قیمت‌گذاری اختصاصی برای هر مشتری"""
    
    @staticmethod
    def create(client_id, pricing_id, custom_price=None, discount_percentage=0):
        """ایجاد قیمت اختصاصی برای مشتری"""
        query = """
        INSERT INTO client_pricing (client_id, pricing_id, custom_price, discount_percentage)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE 
            custom_price = VALUES(custom_price),
            discount_percentage = VALUES(discount_percentage),
            updated_at = CURRENT_TIMESTAMP
        """
        try:
            Database.execute_query(
                query,
                (client_id, pricing_id, custom_price, discount_percentage),
                commit=True
            )
            return True
        except Exception as e:
            print(f"خطا در ایجاد قیمت اختصاصی: {e}")
            return False
    
    @staticmethod
    def get_client_prices(client_id):
        """دریافت تمام قیمت‌های اختصاصی یک مشتری"""
        query = """
        SELECT 
            p.id,
            p.product_name,
            p.product_code,
            p.category,
            p.base_price,
            p.currency,
            p.unit,
            p.description,
            cp.custom_price,
            cp.discount_percentage,
            COALESCE(cp.custom_price, p.base_price) as final_price
        FROM pricing p
        LEFT JOIN client_pricing cp ON p.id = cp.pricing_id AND cp.client_id = %s
        WHERE p.is_active = TRUE
        ORDER BY p.product_name ASC
        """
        return Database.execute_query(query, (client_id,), fetch_all=True)
    
    @staticmethod
    def get_specific_price(client_id, pricing_id):
        """دریافت قیمت اختصاصی برای یک محصول خاص"""
        query = """
        SELECT 
            p.id,
            p.product_name,
            p.base_price,
            cp.custom_price,
            cp.discount_percentage,
            COALESCE(cp.custom_price, p.base_price) as final_price
        FROM pricing p
        LEFT JOIN client_pricing cp ON p.id = cp.pricing_id AND cp.client_id = %s
        WHERE p.id = %s AND p.is_active = TRUE
        """
        return Database.execute_query(query, (client_id, pricing_id), fetch_one=True)
    
    @staticmethod
    def update(client_id, pricing_id, custom_price=None, discount_percentage=None):
        """به‌روزرسانی قیمت اختصاصی"""
        updates = []
        params = []
        
        if custom_price is not None:
            updates.append("custom_price = %s")
            params.append(custom_price)
        
        if discount_percentage is not None:
            updates.append("discount_percentage = %s")
            params.append(discount_percentage)
        
        if not updates:
            return False
        
        params.extend([client_id, pricing_id])
        query = f"""
        UPDATE client_pricing 
        SET {', '.join(updates)}
        WHERE client_id = %s AND pricing_id = %s
        """
        
        try:
            Database.execute_query(query, tuple(params), commit=True)
            return True
        except Exception as e:
            print(f"خطا در به‌روزرسانی قیمت اختصاصی: {e}")
            return False
    
    @staticmethod
    def delete(client_id, pricing_id):
        """حذف قیمت اختصاصی (برگشت به قیمت پایه)"""
        query = """
        DELETE FROM client_pricing 
        WHERE client_id = %s AND pricing_id = %s
        """
        try:
            Database.execute_query(query, (client_id, pricing_id), commit=True)
            return True
        except Exception as e:
            print(f"خطا در حذف قیمت اختصاصی: {e}")
            return False
    
    @staticmethod
    def bulk_update(client_id, pricing_list):
        """
        به‌روزرسانی دسته‌ای قیمت‌های اختصاصی
        pricing_list: لیستی از دیکشنری‌ها شامل pricing_id, custom_price, discount_percentage
        """
        for pricing in pricing_list:
            ClientPricing.create(
                client_id,
                pricing.get('pricing_id'),
                pricing.get('custom_price'),
                pricing.get('discount_percentage', 0)
            )
        return True