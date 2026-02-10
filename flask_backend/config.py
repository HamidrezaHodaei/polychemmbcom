# config.py - Production Version for cPanel
import os
from datetime import timedelta

class Config:
    """تنظیمات اصلی برنامه"""
    
    # ✅ Database Configuration - از Environment Variables
    MYSQL_HOST = os.getenv('DB_HOST', 'localhost')
    MYSQL_USER = os.getenv('DB_USER', 'polychemadmin')  # 👈 بعداً تغییر بده
    MYSQL_PASSWORD = os.getenv('DB_PASSWORD', 'Sales2026')  # 👈 بعداً تغییر بده
    MYSQL_DB = os.getenv('DB_NAME', 'price-database')  # 👈 بعداً تغییر بده
    MYSQL_PORT = int(os.getenv('DB_PORT', 3306))
    
    # ✅ JWT Configuration
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'change-this-in-production-' + os.urandom(24).hex())
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    
    JWT_TOKEN_LOCATION = ['headers']
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'
    
    # ✅ Flask Configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'change-this-secret-key-' + os.urandom(24).hex())
    DEBUG = False  # 👈 در production حتماً False
    
    # ✅ CORS - دامنه واقعی سایتت رو اینجا بذار
    CORS_ORIGINS = [
        'https://polychemmb.com',  # 👈 دامنه اصلی
        'https://www.polychemmb.com',  # 👈 با www
        'http://polychemmb.com',  # 👈 بدون SSL (اختیاری)
    ]
    
    # ✅ Server Configuration
    HOST = '0.0.0.0'
    PORT = int(os.getenv('PORT', 5000))


class DevelopmentConfig(Config):
    """تنظیمات محیط توسعه - فقط برای لوکال"""
    DEBUG = True
    TESTING = False
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Mauve2412'
    MYSQL_DB = 'polychem_data_base'
    CORS_ORIGINS = ['http://localhost:3000', 'http://localhost:8080', '*']


class ProductionConfig(Config):
    """تنظیمات محیط تولید - برای سرور"""
    DEBUG = False
    TESTING = False
    
    # ✅ اجباری: باید از Environment Variables استفاده بشه
    @classmethod
    def validate_production_config(cls):
        """بررسی تنظیمات مهم در production"""
        required_vars = ['DB_HOST', 'DB_USER', 'DB_PASSWORD', 'DB_NAME']
        missing = [var for var in required_vars if not os.getenv(var)]
        
        if missing:
            raise RuntimeError(
                f"❌ Missing required environment variables: {', '.join(missing)}\n"
                f"Please set them in cPanel Python App settings or .env file"
            )


# ✅ انتخاب تنظیمات بر اساس محیط
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


# ✅ Helper function برای گرفتن config
def get_config(config_name=None):
    """دریافت تنظیمات بر اساس محیط"""
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'production')
    
    selected_config = config.get(config_name, config['default'])
    
    # بررسی تنظیمات production
    if config_name == 'production':
        selected_config.validate_production_config()
    
    return selected_config