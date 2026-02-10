
import sys
import os

# Add project path to sys.path
cwd = os.getcwd()
sys.path.insert(0, cwd)

print("Working directory: " + cwd)
print("Python version: " + sys.version)

# Load environment variables
try:
    from dotenv import load_dotenv
    env_path = os.path.join(cwd, '.env')
    if os.path.exists(env_path):
        load_dotenv(env_path)
        print("Loaded .env file")
except ImportError:
    print("WARNING: python-dotenv not installed")

# Check database environment variables
db_vars = ['DB_HOST', 'DB_USER', 'DB_PASSWORD', 'DB_NAME']
missing = [v for v in db_vars if not os.getenv(v)]
if missing:
    print("WARNING: Missing environment variables: " + str(missing))
else:
    print("All database environment variables are set")

# Import Flask app
try:
    from app import create_app, init_database
    print("Successfully imported app module")
except ImportError as e:
    print("ERROR: Failed to import app: " + str(e))
    raise

# Create application instance
try:
    application = create_app('production')
    print("Flask application created successfully")
except Exception as e:
    print("ERROR: Failed to create app: " + str(e))
    import traceback
    traceback.print_exc()
    raise

# Initialize database
try:
    with application.app_context():
        init_database()
        print("Database initialized successfully")
except Exception as e:
    print("WARNING: Database initialization failed: " + str(e))
    # Continue anyway

# List registered routes
try:
    print("\nRegistered routes:")
    with application.app_context():
        for rule in application.url_map.iter_rules():
            methods = ','.join(sorted(rule.methods - {'HEAD', 'OPTIONS'}))
            print("  " + methods + " -> " + str(rule))
except Exception as e:
    print("Could not list routes: " + str(e))

print("\nPassenger WSGI loaded successfully")

if __name__ == '__main__':
    application.run()