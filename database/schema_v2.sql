-- ===============================
-- Database: polychem_db
-- Compatible with MySQL 5.7 / 8.x
-- ===============================

USE polychem_db;

-- ===============================
-- جدول کاربران (Clients)
-- ===============================
CREATE TABLE IF NOT EXISTS clients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,

    -- اطلاعات شخصی
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone VARCHAR(20),
    mobile VARCHAR(20),

    -- اطلاعات شرکت
    company_name VARCHAR(100),
    industry VARCHAR(100),
    website VARCHAR(255),

    -- آدرس
    address TEXT,
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code VARCHAR(20),
    country VARCHAR(100) DEFAULT 'Iran',

    -- تنظیمات
    profile_image TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    email_notifications BOOLEAN DEFAULT TRUE,
    sms_notifications BOOLEAN DEFAULT FALSE,

    -- تاریخ‌ها
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    last_login TIMESTAMP NULL,

    -- ایجاد شده توسط ادمین
    created_by_admin_id INT NULL,

    INDEX idx_username (username),
    INDEX idx_email (email),
    INDEX idx_company (company_name),
    INDEX idx_active (is_active)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ===============================
-- جدول Session کاربران
-- ===============================
CREATE TABLE IF NOT EXISTS client_sessions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    token VARCHAR(255) UNIQUE NOT NULL,
    refresh_token VARCHAR(255) UNIQUE NOT NULL,
    expires_at TIMESTAMP NOT NULL,
    ip_address VARCHAR(45),
    user_agent TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    INDEX idx_token (token),
    INDEX idx_client_expires (client_id, expires_at),

    CONSTRAINT fk_sessions_client
        FOREIGN KEY (client_id) REFERENCES clients(id)
        ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ===============================
-- لاگ ورود کاربران
-- ===============================
CREATE TABLE IF NOT EXISTS client_login_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NULL,
    username VARCHAR(50),
    action VARCHAR(50) NOT NULL,
    ip_address VARCHAR(45),
    user_agent TEXT,
    success BOOLEAN DEFAULT FALSE,
    failure_reason VARCHAR(255),
    location VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    INDEX idx_client_id (client_id),
    INDEX idx_created (created_at),
    INDEX idx_success (success)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ===============================
-- تنظیمات کاربران
-- ===============================
CREATE TABLE IF NOT EXISTS client_settings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT UNIQUE NOT NULL,

    -- نمایش
    theme VARCHAR(20) DEFAULT 'light',
    language VARCHAR(10) DEFAULT 'en',

    -- اعلان‌ها
    order_updates BOOLEAN DEFAULT TRUE,
    price_alerts BOOLEAN DEFAULT FALSE,
    marketing_emails BOOLEAN DEFAULT FALSE,

    -- امنیت
    two_factor_enabled BOOLEAN DEFAULT FALSE,
    two_factor_secret VARCHAR(100),

    settings_json JSON,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_settings_client
        FOREIGN KEY (client_id) REFERENCES clients(id)
        ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ===============================
-- آدرس‌های اضافی کاربران
-- ===============================
CREATE TABLE IF NOT EXISTS client_addresses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    address_type ENUM('office', 'factory', 'billing', 'shipping', 'other') NOT NULL,
    label VARCHAR(100),
    address TEXT,
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code VARCHAR(20),
    country VARCHAR(100) DEFAULT 'Iran',
    phone VARCHAR(20),
    email VARCHAR(100),
    is_default BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    INDEX idx_client_type (client_id, address_type),

    CONSTRAINT fk_addresses_client
        FOREIGN KEY (client_id) REFERENCES clients(id)
        ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ===============================
-- افزودن ستون user_type به admins (ایمن)
-- ===============================
SET @column_exists := (
    SELECT COUNT(*)
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = DATABASE()
      AND TABLE_NAME = 'admins'
      AND COLUMN_NAME = 'user_type'
);

SET @sql := IF(
    @column_exists = 0,
    'ALTER TABLE admins ADD COLUMN user_type ENUM("admin","superadmin") DEFAULT "admin"',
    'SELECT 1'
);

PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

-- ===============================
-- Event پاک‌سازی Session منقضی
-- ===============================
SET GLOBAL event_scheduler = ON;

DROP EVENT IF EXISTS cleanup_expired_client_sessions;
CREATE EVENT cleanup_expired_client_sessions
ON SCHEDULE EVERY 6 HOUR
DO
    DELETE FROM client_sessions WHERE expires_at < NOW();

-- ===============================
-- View آمار کاربران
-- ===============================
CREATE OR REPLACE VIEW client_statistics AS
SELECT
    c.id,
    c.username,
    c.email,
    c.company_name,
    c.is_active,
    c.created_at,
    c.last_login,
    COUNT(DISTINCT cs.id) AS total_sessions,
    COUNT(DISTINCT CASE WHEN cll.success = TRUE THEN cll.id END) AS successful_logins,
    COUNT(DISTINCT CASE WHEN cll.success = FALSE THEN cll.id END) AS failed_logins
FROM clients c
LEFT JOIN client_sessions cs ON c.id = cs.client_id
LEFT JOIN client_login_logs cll ON c.id = cll.client_id
GROUP BY c.id;

-- ===============================
-- کاربر نمونه
-- ===============================
INSERT IGNORE INTO clients (
    username,
    email,
    password_hash,
    first_name,
    last_name,
    phone,
    company_name,
    industry
) VALUES (
    'testclient',
    'client@polychemmb.com',
    '$2a$10$PeOQayiftlD5586DmNs8HuGDIeNthc3YHCPJ7EauByUtsGunnQmya',
    'Test',
    'Client',
    '09123456789',
    'Test Company',
    'Manufacturing'
);
