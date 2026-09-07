#/ config.py
import os
from datetime import timedelta

class Config:
    """تنظیمات اصلی برنامه"""
    
    # Database Configuration
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'Mauve2412')  # رمز MySQL خود را اینجا قرار دهید
    MYSQL_DB = os.getenv('MYSQL_DB', 'polychem_data_base')
    MYSQL_PORT = int(os.getenv('MYSQL_PORT', 3306))
    
    # JWT Configuration - این‌ها خیلی مهم هستند!
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'polychem-super-secret-key-2025-#$%^&*')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)  # 24 ساعت
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)  # 30 روز
    
    # تنظیمات اضافی JWT
    JWT_TOKEN_LOCATION = ['headers']
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'
    
    # Flask Configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'flask-polychem-secret-2025')
    DEBUG = os.getenv('DEBUG', 'True') == 'True'
    
    # CORS Configuration - اضافه کردن localhost:8080 برای Vue
    CORS_ORIGINS = ['http://localhost:3000', 'http://localhost:3001', 'http://localhost:8080', 'http://127.0.0.1:8080']
    
    # Server Configuration
    HOST = os.getenv('FLASK_HOST', '0.0.0.0')
    PORT = int(os.getenv('FLASK_PORT', 8080))


class DevelopmentConfig(Config):
    """تنظیمات محیط توسعه"""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """تنظیمات محیط تولید"""
    DEBUG = False
    TESTING = False
    # در production حتماً از متغیرهای محیطی استفاده کنید


# انتخاب تنظیمات بر اساس محیط
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}