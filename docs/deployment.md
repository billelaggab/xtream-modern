# Xtream Codes Modern - Deployment Guide

## Prerequisites

- Ubuntu Server 22.04 LTS / 24.04 LTS
- Docker & Docker Compose installed
- Minimum 2 GB RAM
- Minimum 10 GB disk space

## Quick Start (Docker Compose)

```bash
# Clone the repository
git clone https://github.com/your-org/xtream-modern.git
cd xtream-modern

# Start all services
docker-compose -f docker/docker-compose.yml up -d

# Check status
docker-compose -f docker/docker-compose.yml ps

# View logs
docker-compose -f docker/docker-compose.yml logs -f
```

## Manual Installation (Production)

### 1. System Preparation

```bash
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y \
    docker.io docker-compose \
    nginx libnginx-mod-http-geoip nginx-module-rtmp \
    mariadb-server \
    ffmpeg \
    python3 python3-pip
```

### 2. Database Setup

```bash
sudo mysql_secure_installation

# Create database
sudo mysql -u root -p -e "
CREATE DATABASE xstream_codes CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'xtreamcodes'@'%' IDENTIFIED BY 'xtream123';
GRANT ALL PRIVILEGES ON xstream_codes.* TO 'xtreamcodes'@'%';
FLUSH PRIVILEGES;
"

# Import schema
mysql -u xtreamcodes -p xstream_codes < database/schema.sql
```

### 3. Backend Setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Nginx Configuration

```bash
sudo cp docker/nginx/nginx.conf /etc/nginx/nginx.conf
sudo cp docker/nginx/conf.d/* /etc/nginx/conf.d/
sudo nginx -t
sudo systemctl restart nginx
```

### 5. Panel Deployment

```bash
sudo cp -r panel /var/www/html
sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 755 /var/www/html
```

### 6. Systemd Services (Optional)

```bash
# Backend service
sudo tee /etc/systemd/system/xtream-api.service <<EOF
[Unit]
Description=Xtream API Service
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/opt/xtream-modern/backend
ExecStart=/opt/xtream-modern/backend/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable xtream-api
sudo systemctl start xtream-api
```

## Environment Variables

Create `.env` file in root:

```env
DATABASE_URL=mysql://xtreamcodes:xtream123@localhost:3306/xstream_codes
SECRET_KEY=your-secret-key-here
ACCESS_TOKEN_EXPIRE_MINUTES=1440
```

## SSL/TLS Configuration

Use Let's Encrypt:

```bash
sudo apt-get install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

## Health Checks

```bash
# Database
mysqladmin ping -h localhost -u xtreamcodes -p

# API
curl http://localhost:8000/health

# Panel
curl http://localhost/

# Nginx RTMP
curl http://localhost:1935
```

## Backup Strategy

```bash
# Database backup
mysqldump -u xtreamcodes -p xstream_codes > backup_$(date +%F).sql

# Panel files backup
tar -czf panel_backup_$(date +%F).tar.gz /var/www/html
```

## Troubleshooting

- **MariaDB connection refused**: Check `bind-address` in `/etc/mysql/my.cnf`
- **Nginx RTMP not working**: Verify `nginx-module-rtmp` is installed
- **Permission errors**: Ensure `www-data` owns `/var/www/html`