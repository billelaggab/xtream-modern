<?php
// Xtream Codes Modern - Panel Configuration

// Database Configuration
define('DB_HOST', getenv('DB_HOST') ?: 'database');
define('DB_PORT', getenv('DB_PORT') ?: '3306');
define('DB_USER', getenv('DB_USER') ?: 'xtreamcodes');
define('DB_PASS', getenv('DB_PASS') ?: 'xtream123');
define('DB_NAME', getenv('DB_NAME') ?: 'xstream_codes');

// App Configuration
define('APP_NAME', 'Xtream Codes Modern');
define('APP_VERSION', '2.0.0');
define('APP_URL', getenv('APP_URL') ?: 'http://localhost');

// Session
define('SESSION_TIMEOUT', 7200); // 2 hours

// Upload settings
define('MAX_UPLOAD_SIZE', 512 * 1024 * 1024); // 512MB

// Timezone
date_default_timezone_set('UTC');