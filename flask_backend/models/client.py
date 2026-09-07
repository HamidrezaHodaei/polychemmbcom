import bcrypt
from utils.database import Database

class Client:
    """مدل کلاینت برای عملیات دیتابیس"""
    
    @staticmethod
    def hash_password(password):
        """هش کردن رمز عبور"""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    @staticmethod
    def verify_password(password, hashed):
        """بررسی صحت رمز عبور"""
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
    
    @staticmethod
    def create(username, password, email=None, company_name=None, first_name=None, 
               last_name=None, phone=None, address=None):
        """ایجاد کلاینت جدید"""
        query = """
        INSERT INTO clients (username, password_hash, email, company_name, 
                           first_name, last_name, phone, address)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        password_hash = Client.hash_password(password)
        
        try:
            client_id = Database.execute_query(
                query,
                (username, password_hash, email, company_name, first_name, 
                 last_name, phone, address),
                commit=True
            )
            return client_id
        except Exception as e:
            print(f"خطا در ایجاد کلاینت: {e}")
            return None
    
    @staticmethod
    def find_by_username(username):
        """پیدا کردن کلاینت با username"""
        query = """
        SELECT id, username, password_hash, email, company_name, first_name, 
               last_name, phone, address, profile_image, is_active
        FROM clients
        WHERE username = %s AND is_active = TRUE
        """
        return Database.execute_query(query, (username,), fetch_one=True)
    
    @staticmethod
    def find_by_id(client_id):
        """پیدا کردن کلاینت با ID"""
        query = """
        SELECT id, username, email, company_name, first_name, last_name, 
               phone, address, profile_image, is_active, created_at
        FROM clients
        WHERE id = %s
        """
        return Database.execute_query(query, (client_id,), fetch_one=True)
    
    @staticmethod
    def get_all():
        """دریافت لیست تمام کلاینت‌ها"""
        query = """
        SELECT id, username, email, company_name, first_name, last_name, 
               phone, is_active, created_at, updated_at
        FROM clients
        ORDER BY created_at DESC
        """
        return Database.execute_query(query, fetch_all=True)
    
    @staticmethod
    def update(client_id, **kwargs):
        """به‌روزرسانی اطلاعات کلاینت"""
        allowed_fields = ['email', 'company_name', 'first_name', 'last_name', 
                         'phone', 'address', 'profile_image', 'is_active']
        updates = []
        params = []
        
        for field, value in kwargs.items():
            if field in allowed_fields:
                updates.append(f"{field} = %s")
                params.append(value)
        
        if not updates:
            return False
        
        params.append(client_id)
        query = f"UPDATE clients SET {', '.join(updates)} WHERE id = %s"
        
        try:
            Database.execute_query(query, tuple(params), commit=True)
            return True
        except Exception as e:
            print(f"خطا در به‌روزرسانی کلاینت: {e}")
            return False
    
    @staticmethod
    def update_password(client_id, new_password):
        """تغییر رمز عبور کلاینت"""
        query = "UPDATE clients SET password_hash = %s WHERE id = %s"
        password_hash = Client.hash_password(new_password)
        
        try:
            Database.execute_query(query, (password_hash, client_id), commit=True)
            return True
        except Exception as e:
            print(f"خطا در تغییر رمز عبور: {e}")
            return False
    
    @staticmethod
    def delete(client_id):
        """حذف کلاینت (غیرفعال کردن)"""
        query = "UPDATE clients SET is_active = FALSE WHERE id = %s"
        try:
            Database.execute_query(query, (client_id,), commit=True)
            return True
        except Exception as e:
            print(f"خطا در حذف کلاینت: {e}")
            return False
    
    @staticmethod
    def authenticate(username, password):
        """احراز هویت کلاینت"""
        client = Client.find_by_username(username)
        
        if not client:
            return None
        
        if Client.verify_password(password, client['password_hash']):
            client.pop('password_hash', None)
            return client
        
        return None
    
    @staticmethod
    def search(keyword):
        """جستجو در کلاینت‌ها"""
        query = """
        SELECT id, username, email, company_name, first_name, last_name, 
               phone, is_active, created_at
        FROM clients
        WHERE username LIKE %s 
           OR email LIKE %s 
           OR company_name LIKE %s
           OR first_name LIKE %s
           OR last_name LIKE %s
        ORDER BY created_at DESC
        """
        search_term = f"%{keyword}%"
        return Database.execute_query(
            query, 
            (search_term, search_term, search_term, search_term, search_term),
            fetch_all=True
        )