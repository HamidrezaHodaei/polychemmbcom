import bcrypt
from utils.database import Database

class Admin:
    """مدل ادمین برای عملیات دیتابیس"""
    
    @staticmethod
    def hash_password(password):
        """هش کردن رمز عبور"""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    @staticmethod
    def verify_password(password, hashed):
        """بررسی صحت رمز عبور"""
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
    
    @staticmethod
    def create(username, password, email=None, first_name=None, last_name=None):
        """ایجاد ادمین جدید"""
        query = """
        INSERT INTO admins (username, password_hash, email, first_name, last_name)
        VALUES (%s, %s, %s, %s, %s)
        """
        password_hash = Admin.hash_password(password)
        
        try:
            admin_id = Database.execute_query(
                query,
                (username, password_hash, email, first_name, last_name),
                commit=True
            )
            return admin_id
        except Exception as e:
            print(f"خطا در ایجاد ادمین: {e}")
            return None
    
    @staticmethod
    def find_by_username(username):
        """پیدا کردن ادمین با username"""
        query = """
        SELECT id, username, password_hash, email, first_name, last_name, is_active
        FROM admins
        WHERE username = %s AND is_active = TRUE
        """
        return Database.execute_query(query, (username,), fetch_one=True)
    
    @staticmethod
    def find_by_id(admin_id):
        """پیدا کردن ادمین با ID"""
        query = """
        SELECT id, username, email, first_name, last_name, is_active, created_at
        FROM admins
        WHERE id = %s
        """
        return Database.execute_query(query, (admin_id,), fetch_one=True)
    
    @staticmethod
    def get_all():
        """دریافت لیست تمام ادمین‌ها"""
        query = """
        SELECT id, username, email, first_name, last_name, is_active, created_at, updated_at
        FROM admins
        ORDER BY created_at DESC
        """
        return Database.execute_query(query, fetch_all=True)
    
    @staticmethod
    def update(admin_id, **kwargs):
        """به‌روزرسانی اطلاعات ادمین"""
        allowed_fields = ['email', 'first_name', 'last_name', 'is_active']
        updates = []
        params = []
        
        for field, value in kwargs.items():
            if field in allowed_fields:
                updates.append(f"{field} = %s")
                params.append(value)
        
        if not updates:
            return False
        
        params.append(admin_id)
        query = f"UPDATE admins SET {', '.join(updates)} WHERE id = %s"
        
        try:
            Database.execute_query(query, tuple(params), commit=True)
            return True
        except Exception as e:
            print(f"خطا در به‌روزرسانی ادمین: {e}")
            return False
    
    @staticmethod
    def update_password(admin_id, new_password):
        """تغییر رمز عبور ادمین"""
        query = "UPDATE admins SET password_hash = %s WHERE id = %s"
        password_hash = Admin.hash_password(new_password)
        
        try:
            Database.execute_query(query, (password_hash, admin_id), commit=True)
            return True
        except Exception as e:
            print(f"خطا در تغییر رمز عبور: {e}")
            return False
    
    @staticmethod
    def delete(admin_id):
        """حذف ادمین (غیرفعال کردن)"""
        query = "UPDATE admins SET is_active = FALSE WHERE id = %s"
        try:
            Database.execute_query(query, (admin_id,), commit=True)
            return True
        except Exception as e:
            print(f"خطا در حذف ادمین: {e}")
            return False
    
    @staticmethod
    def authenticate(username, password):
        """احراز هویت ادمین"""
        admin = Admin.find_by_username(username)
        
        if not admin:
            return None
        
        if Admin.verify_password(password, admin['password_hash']):
            admin.pop('password_hash', None)
            return admin
        
        return None