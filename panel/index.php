<?php
// Xtream Codes Modern - Admin Panel
# نسخة خفيفة من لوحة التحكم القديمة مع تحديثات PHP 8

// تثبيت مسار الخطأ الفادح
error_reporting(E_ALL);
ini_set('display_errors', 0);

// مسار اللوحة
$ROOT_PATH = __DIR__;
$WEB_ROOT = '/';

// تكوين الجلسة
if (session_status() === PHP_SESSION_NONE) {
    session_set_cookie_params(3600, '/');
    session_name('xtream_codes_session');
    session_start();
}

// اتصالات قاعدة البيانات
require_once $ROOT_PATH . '/config/database.php';
require_once $ROOT_PATH . '/config/helpers.php';

// أنظمة التوجيه
$request = $_GET['page'] ?? 'dashboard';

// تنظيف المدخلات
$page = preg_replace('/[^a-zA-Z0-9_]/', '', $request);

// التحقق من الصلاحيات للمستخدم
$username = $_SESSION['username'] ?? null;
$role = $_SESSION['role'] ?? 'user';

// تضمين ملفات اللوحة حسب الصفحة المطلوبة
switch ($page) {
    case 'dashboard':
        require_once $ROOT_PATH . '/pages/dashboard.php';
        break;
    case 'users':
        require_once $ROOT_PATH . '/pages/users.php';
        break;
    case 'streams':
        require_once $ROOT_PATH . '/pages/streams.php';
        break;
    case 'vod':
        require_once $ROOT_PATH . '/pages/vod.php';
        break;
    case 'subscriptions':
        require_once $ROOT_PATH . '/pages/subscriptions.php';
        break;
    case 'settings':
        require_once $ROOT_PATH . '/pages/settings.php';
        break;
    case 'logout':
        session_destroy();
        header('Location: ' . $WEB_ROOT);
        exit;
    default:
        require_once $ROOT_PATH . '/pages/404.php';
        break;
}
?>