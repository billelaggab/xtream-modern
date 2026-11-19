-- xstream-modern/database/schema.sql
-- هيكل قاعدة البيانات الحديثة لـ Xtream Codes
-- متوافق مع MariaDB 10.x+

CREATE DATABASE IF NOT EXISTS xstream_codes CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE xstream_codes;

-- ============================================================
-- الجداول الأساسية
-- ============================================================

-- جدول المستخدمين (Users)
CREATE TABLE IF NOT EXISTS users (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash CHAR(60) NOT NULL, -- Base64 encoded hash
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    role ENUM('admin', 'user', 'viewer') DEFAULT 'user'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='المستخدمون في النظام';

-- جدول القنوات/البث المباشر (Live Streams / Channels)
CREATE TABLE IF NOT EXISTS live_streams (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id INT UNSIGNED NOT NULL,
    channel_name VARCHAR(255) NOT NULL,
    status ENUM('live', 'paused', 'completed', 'deleted') DEFAULT 'live',
    start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    end_time TIMESTAMP NULL,
    bitrate_kbps INT UNSIGNED DEFAULT 1280,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_status (status),
    INDEX idx_channel_name (channel_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='قنوات البث المباشر النشطة';

-- جدول الفيديو على الطلب (VOD)
CREATE TABLE IF NOT EXISTS vod (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id INT UNSIGNED NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    duration_minutes INT UNSIGNED NOT NULL,
    file_path VARCHAR(500) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id),
    INDEX idx_title (title)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='محتوى الفيديو على الطلب';

-- جدول الفئات/التصنيفات (Categories)
CREATE TABLE IF NOT EXISTS categories (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    parent_category_id INT UNSIGNED NULL,
    path VARCHAR(256) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_category_id) REFERENCES categories(id) ON DELETE SET NULL,
    INDEX idx_name (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='الفئات التصنيفية';

-- جدول الوسائط/الأصول (Media Assets)
CREATE TABLE IF NOT EXISTS media_assets (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    asset_type ENUM('video', 'image', 'audio', 'file') NOT NULL,
    asset_name VARCHAR(255) NOT NULL,
    source_url VARCHAR(500) NOT NULL,
    size_bytes BIGINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_asset_name (asset_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='أصول الوسائط';

-- جدول الاشتراكات (Subscriptions)
CREATE TABLE IF NOT EXISTS subscriptions (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id INT UNSIGNED NOT NULL,
    channel_id INT UNSIGNED NOT NULL,
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ended_at TIMESTAMP NULL,
    status ENUM('active', 'cancelled') DEFAULT 'active',
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (channel_id) REFERENCES live_streams(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id),
    INDEX idx_channel_id (channel_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='اشتراكات المستخدمين في القنوات';

-- جدول الإشعارات (Notifications)
CREATE TABLE IF NOT EXISTS notifications (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id INT UNSIGNED NOT NULL,
    message TEXT NOT NULL,
    read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='إشعارات المستخدم';

-- ============================================================
-- ملاحظات
-- ============================================================
-- هذا الهيكل مصمم ليكون قابلاً للتوسع (Scalable) ويتوافق مع أفضل الممارسات الحديثة:
-- • استخدام AUTO_INCREMENT وPRIMARY KEY.
-- • إضافة فهارس (Indexes) على الأعمدة المستخدمة في البحث.
-- • دعم المفاتيح الخارجية (Foreign Keys) لضمان سلامة البيانات.
-- • استخدام UTF-8MB4 (يضمن دعم الأحرف العربية).
-- • ملاحظة: تم تصحيح الأخطاء النحوية من النسخة الأولى للملف.
-- ============================================================