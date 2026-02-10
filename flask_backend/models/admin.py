import bcrypt
from utils.database import Database

class Admin:
    """Admin model for database operations"""
    
    @staticmethod
    def hash_password(password):
        """Hash password using bcrypt"""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    @staticmethod
    def verify_password(password, hashed):
        """Verify password against hash"""
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
    
    @staticmethod
    def create(username, password, email=None, first_name=None, last_name=None):
        """Create new admin"""
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
            print(f"Error creating admin: {e}")
            return None
    
    @staticmethod
    def find_by_username(username):
        """Find admin by username"""
        query = """
        SELECT id, username, password_hash, email, first_name, last_name, is_active
        FROM admins
        WHERE username = %s AND is_active = TRUE
        """
        return Database.execute_query(query, (username,), fetch_one=True)
    
    @staticmethod
    def find_by_id(admin_id):
        """Find admin by ID"""
        query = """
        SELECT id, username, email, first_name, last_name, is_active, created_at
        FROM admins
        WHERE id = %s
        """
        return Database.execute_query(query, (admin_id,), fetch_one=True)
    
    @staticmethod
    def get_all():
        """Get all admins"""
        query = """
        SELECT id, username, email, first_name, last_name, is_active, created_at, updated_at
        FROM admins
        ORDER BY created_at DESC
        """
        return Database.execute_query(query, fetch_all=True)
    
    @staticmethod
    def update(admin_id, **kwargs):
        """Update admin information"""
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
            print(f"Error updating admin: {e}")
            return False
    
    @staticmethod
    def update_password(admin_id, new_password):
        """Change admin password"""
        query = "UPDATE admins SET password_hash = %s WHERE id = %s"
        password_hash = Admin.hash_password(new_password)
        
        try:
            Database.execute_query(query, (password_hash, admin_id), commit=True)
            return True
        except Exception as e:
            print(f"Error updating password: {e}")
            return False
    
    @staticmethod
    def delete(admin_id):
        """Delete admin (disable)"""
        query = "UPDATE admins SET is_active = FALSE WHERE id = %s"
        try:
            Database.execute_query(query, (admin_id,), commit=True)
            return True
        except Exception as e:
            print(f"Error deleting admin: {e}")
            return False
    
    @staticmethod
    def authenticate(username, password):
        """Authenticate admin"""
        admin = Admin.find_by_username(username)
        
        if not admin:
            return None
        
        if Admin.verify_password(password, admin['password_hash']):
            admin.pop('password_hash', None)
            return admin
        
        return None