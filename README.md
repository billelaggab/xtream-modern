# Xtream Codes Modern (v2.0) - نسخة المعاد بناءها

هذا المستودع هو **نسخة معاد بناءها (Rebuild)** من مشروع Xtream UI الأصلي. تم استخراج المبادئ الأساسية والبنية التحتية من مستودع `xtreamui_mirror` و `xtreamui-things`، وإعادة تطويرها بالكامل باستخدام **المكتبات الحديثة** (Python 3، PHP 8، MariaDB الحديثة) والبنية النظيفة.

## 🎯 الهدف من المشروع

1. **التوافق الكامل** مع الإصدارات الحديثة من Ubuntu Server (22.04 / 24.04 LTS).
2. **إزالة المكتبات المعطوبة** (libcurl3, libpng12, Python 2) واستبدالها بالحلول الحديثة.
3. **تحسين الأمان** وترقية قاعدة البيانات والكود لمنع الثغرات الشائعة.
4. **توحيد جميع مكونات المشروع** في مستودع واحد سهل الاستخدام.

## 🏗️ البنية التحتية (Architecture)

```text
xtream-modern/
├── docs/                 # مستندات المشروع، خطة التطوير، الشروحات
├── installer/            # سكربت التثبيت المتكامل (Python 3)
│   ├── requirements.txt  # مكتبات Python المطلوبة
│   └── install.py        # سكربت التثبيت الرئيسي
├── database/             # هيكل قاعدة البيانات الحديثة (schema.sql + Migrations)
├── backend/              # خدمة الـ API (FastAPI + Python 3)
│   ├── app/
│   │   ├── main.py       # نقطة الدخول الرئيسية
│   │   ├── core/         # الإعدادات، الأمان، الاستثناءات
│   │   ├── services/     # منطق الأعمال (Auth, Users, Streams, VOD, Subscriptions, Notifications)
│   │   ├── routers/      # واجهات API (RESTful endpoints)
│   │   ├── schemas.py    # نماذج Pydantic للتحقق
│   │   ├── models.py     # نماذج البيانات
│   │   └── database.py   # اتصال قاعدة البيانات
│   ├── requirements.txt  # مكتبات Backend
│   └── Dockerfile        # صورة Docker للـ Backend
├── panel/                # لوحة التحكم الإدارية (PHP 8.2+)
│   ├── index.php         # نقطة الدخول مع نظام التوجيه
│   ├── config.php        # إعدادات التطبيق
│   ├── config/
│   │   ├── database.php  # فئة Database (PDO)
│   │   └── helpers.php   # دوال مساعدة
│   └── pages/
│       ├── dashboard.php     # لوحة التحكم الرئيسية
│       ├── users.php         # إدارة المستخدمين
│       ├── streams.php       # إدارة البث المباشر
│       ├── vod.php           # مكتبة VOD
│       ├── subscriptions.php # الاشتراكات
│       ├── settings.php      # إعدادات النظام
│       └── 404.php           # صفحة خطأ
├── frontend/             # واجهة المستخدم (React/Next.js placeholder)
│   └── index.html        # صفحة الترحيب
├── docker/               # ملفات Docker و Docker Compose
│   ├── docker-compose.yml    # Orchestration للخدمات
│   └── nginx/
│       ├── nginx.conf    # إعدادات Nginx مع RTMP
│       ├── php.ini       # إعدادات PHP-FPM
│       └── conf.d/
│           └── default.conf  # موقع Nginx الافتراضي
├── scripts/              # سكربتات مساعدة
│   └── clearlogs.sh      # تنظيف السجلات
├── .gitignore            # ملفات مستثناة من Git
└── README.md             # هذا الملف
```

## 📚 التقنيات المستخدمة (Tech Stack)

| المكوّن | النسخة القديمة (Legacy) | **النسخة الجديدة (Modern)** |
| :--- | :--- | :--- |
| **خادم الويب** | Nginx (مع RTMP) | Nginx + nginx-rtmp-module (محدث) |
| **اللغة (سكربتات)** | Python 2 | **Python 3.11+** (مكتبات حديثة) |
| **قاعدة البيانات** | MySQL/MariaDB (إعدادات قديمة) | **MariaDB 10.x+** (صيغة حديثة + migrations) |
| **واجهة الإدارة** | PHP 5.6 / 7.0 | **PHP 8.2+** (PDO،Prepared Statements) |
| **الـ API الخلفي** | غير موجود | **FastAPI 0.104+** (Async،JWT Auth) |
| **الاتصال بقاعدة البيانات** | mysql-connector (قديم) | `pymysql` / `sqlalchemy` (حديث) |
| **التنظيم** | تثبيت مباشر على النظام | **Docker Compose** (Containerized) |

## 🚀 البدء السريع

### 1. التشغيل السريع (Docker - مُوصى به)

```bash
cd xtream-modern
docker-compose -f docker/docker-compose.yml up -d

# التحقق من الحالة
docker-compose -f docker/docker-compose.yml ps

# عرض السجلات
docker-compose -f docker/docker-compose.yml logs -f
```

**الخدمات المتاحة بعد التشغيل:**
| الخدمة | المنفذ | الوصف |
|--------|--------|-------|
| Nginx + PHP Panel | 80 | لوحة التحكم الإدارية |
| FastAPI Backend | 8000 | واجهة برمجة التطبيقات |
| MariaDB | 3306 | قاعدة البيانات |
| Nginx RTMP | 1935 | بث RTMP |

### 2. التثبيت اليدوي (على Ubuntu 22.04 / 24.04)

```bash
# 1. تحديث النظام وتثبيت التبعيات
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y \
    docker.io docker-compose \
    nginx libnginx-mod-http-geoip nginx-module-rtmp \
    mariadb-server \
    ffmpeg \
    python3 python3-pip python3-venv

# 2. إعداد قاعدة البيانات
sudo mysql_secure_installation
sudo mysql -u root -p -e "
CREATE DATABASE xstream_codes CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'xtreamcodes'@'%' IDENTIFIED BY 'xtream123';
GRANT ALL PRIVILEGES ON xstream_codes.* TO 'xtreamcodes'@'%';
FLUSH PRIVILEGES;
"

# 3. استيراد هيكل قاعدة البيانات
mysql -u xtreamcodes -p xstream_codes < database/schema.sql

# 4. تشغيل Backend
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000

# 5. إعداد Nginx و PHP
sudo cp docker/nginx/nginx.conf /etc/nginx/nginx.conf
sudo cp docker/nginx/conf.d/default.conf /etc/nginx/conf.d/
sudo cp docker/nginx/php.ini /etc/php/8.2/fpm/php.ini
sudo cp -r panel /var/www/html
sudo chown -R www-data:www-data /var/www/html
sudo systemctl restart nginx php8.2-fpm
```

## 📂 هيكل الملفات المهمة

### قاعدة البيانات (`database/`)
- `schema.sql`: يحتوي على هيكل الجداول الكامل (Users, Live Streams, VOD, Categories, Subscriptions, Notifications) مع المفاتيح الأجنبية والفهرسة المحسّنة، متوافق مع MariaDB الحديثة.

### Backend API (`backend/`)
- `main.py`: نقطة الدخول FastAPI مع CORS وجميع المسارات.
- `app/services/`: منطق الأعمال المفصول (Auth, User, Stream, VOD, Subscription, Notification, Media).
- `app/routers/`: نقاط نهاية RESTful لكل خدمة.
- `app/schemas.py`: نماذج Pydantic للتحقق من صحة البيانات.
- `app/core/security.py`: تشفير كلمات المرور (bcrypt) وJWT tokens.
- `Dockerfile`: صورة Docker محسّنة للإنتاج.

### لوحة التحكم (`panel/`)
- **جاهزة بالكامل وتعمل مع PHP 8.2+** ✅
- `index.php`: نظام توجيه بسيط يعتمد على `$_GET['page']`.
- `config/database.php`: فئة `Database` باستخدام PDO مع Prepared Statements.
- `config/helpers.php`: دوال مساعدة (CSRF، Sanitization، Flash messages، إلخ).
- `pages/`: ست صفحات كاملة (Dashboard، Users، Streams، VOD، Subscriptions، Settings) مع تصميم داكن حديث ومتجاوب.

### Docker (`docker/`)
- `docker-compose.yml`: يربط 4 خدمات (Database، Nginx، PHP-FPM، API) مع Health Checks.
- `nginx/nginx.conf`: إعداد Nginx مع وحدة RTMP للبث المباشر (HLS output).
- `nginx/conf.d/default.conf`: مضيف افتراضي يخدم لوحة PHP ويُحيل `/api` إلى FastAPI.

### Skripts (`scripts/`)
- `clearlogs.sh`: سكربت لتنظيف سجلات النظام (nginx، mysql، xtream، journalctl) - يعمل كـ root.

## 🔜 الخطط المستقبلية (Roadmap)

| الميزة | الحالة | الملاحظات |
|----------|--------|-----------|
| ✅ الترقية الكاملة لـ PHP 8 في `panel/` | **مكتملة** | جميع الملفات تستخدم PHP 8.2+ syntax |
| ✅ Backend API حديث (FastAPI) | **مكتملة** | مع JWT Auth، خدمات مفصولة، Docker |
| ✅ Docker Compose للتشغيل السريع | **مكتملة** | 4 خدمات مع Health Checks |
| 🔄 واجهة أمامية مستقبلية (React/Next.js) | **مخطط لها** | مجلد `frontend/` موجود كـ placeholder |
| ⏳ نظام اختبارات آلية (pytest + phpunit) | **مخطط لها** | هيكل `tests/` جاهز للإضافة |
| ⏳ CI/CD Pipeline (GitHub Actions) | **مخطط لها** | للبناء والنشر التلقائي |
| ⏳ دعم Hardware Acceleration (GPU/FFmpeg) | **مخطط لها** | في إعدادات Nginx RTMP |
| ⏳ لوحة إحصائيات وتحليلات متقدمة | **مخطط لها** | باستخدام Grafana/Prometheus |

## 📄 المستندات

- `docs/architecture.md` - هندسة النظام التفصيلية ومخطط تدفق البيانات.
- `docs/deployment.md` - دليل النشر الكامل (Docker + يدوي + Systemd + SSL).
- `docs/api.md` - مستندات الـ API الكاملة (Endpoints، Auth، أمثلة curl، RTMP URLs).

## 🔧 متغيرات البيئة

أنشئ ملف `.env` في جذر المشروع (مطلوب للإنتاج):

```env
# Database
DATABASE_URL=mysql://xtreamcodes:xtream123@database:3306/xstream_codes
DB_HOST=database
DB_PORT=3306
DB_USER=xtreamcodes
DB_PASS=xtream123
DB_NAME=xstream_codes

# Security
SECRET_KEY=your-super-secret-key-change-in-production
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# App
APP_NAME=Xtream Codes Modern
APP_VERSION=2.0.0
APP_URL=https://your-domain.com
```

## 🛡️ الأمان

- **جميع استعلامات قاعدة البيانات** تستخدم Prepared Statements (PDO في PHP، SQLAlchemy في Python).
- **كلمات المرور** مشفرة بـ bcrypt (via passlib).
- **المصادقة** عبر JWT Tokens مع انتهاء صلاحية قابل للتكوين.
- **CSRF Protection** في لوحة PHP.
- **Security Headers** في Nginx (X-Frame-Options، X-XSS-Protection، X-Content-Type-Options).
- **Input Sanitization** في جميع نقاط الإدخال.

## 🧪 الاختبار

```bash
# Backend tests
cd backend
source venv/bin/activate
pytest app/ -v --cov=app

# PHP syntax check
php -l panel/index.php
php -l panel/config/database.php
# ... باقي الملفات
```

## 📝 الترخيص

هذا المشروع مبني على أعمال `emre1393/xtreamui_mirror` و `emre1393/xtreamui-things` المرخصة تحت **GPL-3.0**.

> ⚠️ **ملاحظة هامة**: يجب استخدام هذا المشروع بشكل قانوني والامتثال لقوانين حقوق الملكية الفكرية والبث في بلدك قبل أي استخدام تجاري.

---

## 📞 المساهمة والدعم

1. **Fork** المستودع
2. أنشئ **Branch** لميزتك الجديدة
3. اكتب **Tests** للكود الجديد
4. أرسل **Pull Request** مع وصف واضح للتغييرات

للأسئلة التقنية، افتح **Issue** في المستودع.