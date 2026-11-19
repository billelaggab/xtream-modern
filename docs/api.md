# Xtream Codes Modern - API Documentation

## Base URL

```
http://localhost:8000
```

## Authentication

Most endpoints require JWT authentication. Include the token in the Authorization header:

```
Authorization: Bearer <token>
```

## Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register new user |
| POST | `/auth/login` | Login and get token |

#### Register User
```bash
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username": "user1", "email": "user1@example.com", "password": "securepassword123"}'
```

#### Login
```bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "user1", "password": "securepassword123"}'
```

---

### Users

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/users` | List all users |
| GET | `/users/{user_id}` | Get user by ID |
| POST | `/users` | Create user |
| PUT | `/users/{user_id}` | Update user |
| DELETE | `/users/{user_id}` | Delete user |

---

### Streams (Live Channels)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/streams` | List all streams |
| GET | `/streams/{stream_id}` | Get stream details |
| POST | `/streams` | Create new stream |
| PUT | `/streams/{stream_id}` | Update stream |
| DELETE | `/streams/{stream_id}` | Delete stream |

#### Create Stream
```bash
curl -X POST http://localhost:8000/streams \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"channel_name": "Sports HD", "bitrate_kbps": 2500}'
```

---

### Subscriptions

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/subscriptions` | List all subscriptions |
| GET | `/subscriptions/{id}` | Get subscription |
| POST | `/subscriptions` | Create subscription |
| PUT | `/subscriptions/{id}` | Update subscription |
| DELETE | `/subscriptions/{id}` | Delete subscription |

---

### Notifications

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/notifications?user_id={id}` | List user notifications |
| POST | `/notifications` | Create notification |
| PUT | `/notifications/{id}` | Mark as read |
| DELETE | `/notifications/{id}` | Delete notification |

---

### Health Check

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Service health check |

```bash
curl http://localhost:8000/health
# {"status": "healthy"}
```

---

## Error Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

Error format:
```json
{
  "detail": "Error message"
}
```

---

## RTMP Streaming URLs

### Publishing Stream (OBS/ffmpeg)

```
rtmp://your-server.com:1935/live/STREAM_KEY
```

### Playing Stream (HLS)

```
http://your-server.com/hls/STREAM_KEY.m3u8
```

### Playing Stream (MPEG-DASH)

```
http://your-server.com/dash/STREAM_KEY.mpd
```