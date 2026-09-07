"""
Passenger WSGI file for cPanel deployment
این فایل باید در root directory پروژه Flask قرار بگیره
"""

import sys
import os

# ✅ CRITICAL: مسیر پروژه رو اضافه کن
# این مسیر رو بعد از اپلود به cPanel باید تنظیم کنی
INTERP = os.path.join(os.environ['HOME'], 'virtualenv', 'polychem', '3.11', 'bin', 'python3')

# ✅ بررسی وجود Python interpreter
if os.path.isfile(INTERP):
    execfile(INTERP, {'__file__': INTERP})

# ✅ اضافه کردن مسیر پروژه به sys.path
cwd = os.getcwd()
sys.path.insert(0, cwd)

# ✅ Import کردن Flask app
from app import create_app, init_database

# ✅ ایجاد application
application = create_app('production')

# ✅ راه‌اندازی دیتابیس (اگر لازمه)
with application.app_context():
    try:
        init_database()
        print("✅ Database initialized successfully")
    except Exception as e:
        print(f"⚠️ Database init warning: {e}")

# ✅ این متغیر رو Passenger استفاده می‌کنه
if __name__ == '__main__':
    application.run()