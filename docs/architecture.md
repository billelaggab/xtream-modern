# Xtream Codes Modern - Architecture

## Overview

The Xtream Codes Modern project is a complete rebuild of the legacy Xtream UI system. It is designed to run on modern Ubuntu Server distributions (22.04 LTS / 24.04 LTS) and uses clean, modern technologies.

## System Architecture

### Components

1. **Installer (`/installer`)**: Python 3 installation script.
2. **Database (`/database`)**: MariaDB schema with migrations.
3. **Backend (`/backend`)**: FastAPI-based RESTful API.
4. **Panel (`/panel`)**: PHP 8 admin panel.
5. **Nginx (`/docker/nginx`)**: Web server with RTMP streaming support.
6. **Frontend (`/frontend`)**: Modern React/Next.js UI (optional).

### Data Flow

```
User Request -> Nginx -> PHP Panel (if PHP) OR FastAPI Backend -> MariaDB
```

### Deployment

The project is containerized using Docker Compose.

```bash
cd xtream-modern
docker-compose up -d
```

### Tech Stack

| Layer | Technology | Version |
|-------|-----------|---------|
| OS | Ubuntu Server | 22.04 / 24.04 LTS |
| Database | MariaDB | 10.x+ |
| Backend | FastAPI | 0.104+ |
| Frontend | PHP 8 / React | 8.2 / 18+ |
| Web Server | Nginx | latest |
| Container | Docker | latest |