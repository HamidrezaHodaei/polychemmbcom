import pymysql
from pymysql.cursors import DictCursor
from config import Config

class Database:
    """MySQL database connection management class"""
    
    @staticmethod
    def get_connection():
        """Create database connection"""
        try:
            connection = pymysql.connect(
                host=Config.MYSQL_HOST,
                user=Config.MYSQL_USER,
                password=Config.MYSQL_PASSWORD,
                database=Config.MYSQL_DB,
                port=Config.MYSQL_PORT,
                cursorclass=DictCursor,
                charset='utf8mb4'
            )
            return connection
        except pymysql.Error as e:
            print(f"Database connection error: {e}")
            raise
    
    @staticmethod
    def execute_query(query, params=None, fetch_one=False, fetch_all=False, commit=False):
        """
        Execute query in database
        
        Args:
            query: SQL query
            params: Query parameters
            fetch_one: Return one record
            fetch_all: Return all records
            commit: Commit changes (for INSERT, UPDATE, DELETE)
        
        Returns:
            Query result
        """
        connection = None
        cursor = None
        try:
            connection = Database.get_connection()
            cursor = connection.cursor()
            
            cursor.execute(query, params or ())
            
            if commit:
                connection.commit()
                return cursor.lastrowid
            
            if fetch_one:
                return cursor.fetchone()
            
            if fetch_all:
                return cursor.fetchall()
            
            return None
            
        except pymysql.Error as e:
            if connection:
                connection.rollback()
            print(f"Query execution error: {e}")
            raise
            
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
    
    @staticmethod
    def init_database():
        """Create initial database tables"""
        
        # Admins table
        admin_table = """
        CREATE TABLE IF NOT EXISTS admins (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            email VARCHAR(100),
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            is_active BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            INDEX idx_username (username),
            INDEX idx_email (email)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
        """
        
        # Clients table
        client_table = """
        CREATE TABLE IF NOT EXISTS clients (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            email VARCHAR(100),
            company_name VARCHAR(100),
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            phone VARCHAR(20),
            address TEXT,
            profile_image VARCHAR(255),
            is_active BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            INDEX idx_username (username),
            INDEX idx_email (email),
            INDEX idx_company (company_name)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
        """
        
        # General pricing table
        pricing_table = """
        CREATE TABLE IF NOT EXISTS pricing (
            id INT AUTO_INCREMENT PRIMARY KEY,
            product_name VARCHAR(100) NOT NULL,
            product_code VARCHAR(50),
            category VARCHAR(50),
            base_price DECIMAL(10, 2) NOT NULL,
            currency VARCHAR(10) DEFAULT 'USD',
            unit VARCHAR(20) DEFAULT 'kg',
            description TEXT,
            is_active BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            INDEX idx_product_code (product_code),
            INDEX idx_category (category)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
        """
        
        # Client-specific pricing table
        client_pricing_table = """
        CREATE TABLE IF NOT EXISTS client_pricing (
            id INT AUTO_INCREMENT PRIMARY KEY,
            client_id INT NOT NULL,
            pricing_id INT NOT NULL,
            custom_price DECIMAL(10, 2),
            discount_percentage DECIMAL(5, 2) DEFAULT 0,
            is_active BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE,
            FOREIGN KEY (pricing_id) REFERENCES pricing(id) ON DELETE CASCADE,
            UNIQUE KEY unique_client_pricing (client_id, pricing_id),
            INDEX idx_client (client_id),
            INDEX idx_pricing (pricing_id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
        """
        
        # Login log table
        login_log_table = """
        CREATE TABLE IF NOT EXISTS login_logs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_type ENUM('admin', 'client') NOT NULL,
            user_id INT NOT NULL,
            username VARCHAR(50) NOT NULL,
            ip_address VARCHAR(45),
            location VARCHAR(100),
            success BOOLEAN DEFAULT TRUE,
            login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_user_type_id (user_type, user_id),
            INDEX idx_login_time (login_time)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
        """
        
        try:
            Database.execute_query(admin_table, commit=True)
            print("Table admins created")
            
            Database.execute_query(client_table, commit=True)
            print("Table clients created")
            
            Database.execute_query(pricing_table, commit=True)
            print("Table pricing created")
            
            Database.execute_query(client_pricing_table, commit=True)
            print("Table client_pricing created")
            
            Database.execute_query(login_log_table, commit=True)
            print("Table login_logs created")
            
            print("\nAll tables created successfully!")
            
        except Exception as e:
            print(f"Error creating tables: {e}")
            raise