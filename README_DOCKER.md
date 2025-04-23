# 🐳 Docker Compose Setup for MySQL, Redis, and MongoDB

This project contains a Docker Compose setup to run MySQL, Redis, and MongoDB containers with environment configuration via `.env`, data persistence using Docker volumes, and optional access credentials.

---

## 📦 Services Overview

### 1. **MySQL**

- **Image**: `mysql:8.0`
- **Auth plugin**: `mysql_native_password`
- **Ports**: `3306:3306`
- **Volumes**: Persistent volume at `db_data:/var/lib/mysql`
- **Environment variables (from `.env`)**:
  ```env
  MYSQL_ROOT_PASSWORD=your_root_password
  MYSQL_DATABASE=your_db
  MYSQL_USER=your_user
  MYSQL_PASSWORD=your_password
  ```
- **Kiểm tra MySQL**:
  ```bash
  docker exec -it <mysql_container_id_or_name> mysql -u root -p
  # nhập mật khẩu từ MYSQL_ROOT_PASSWORD
  show databases;
  ```

### 2. **Redis**

- **Image**: `redis:latest` hoặc `redis:6.2-alpine`
- **Ports**: `6379:6379`
- **Authentication**:
  - Set qua `--requirepass ${REDIS_PASSWORD}`
  - Ví dụ `.env`:
    ```env
    REDIS_PASSWORD=your_redis_password
    ```
- **Volumes**: Persistent Redis data:
  ```yaml
  volumes:
    - cache:/data
  ```
- **Kiểm tra Redis**:

  ```bash
  docker exec -it <redis_container_id_or_name> redis-cli
  # Kiểm tra kết nối
  ping
  # Output: PONG

  # Đăng nhập với password
  auth your_redis_password
  ```

### 3. **MongoDB**

- **Image**: `mongo:latest`
- **Ports**: Custom từ `.env`, ví dụ: `27017:27017`
- **Volumes**:
  - `./database:/data/db`
  - `./mongo-init.js:/docker-entrypoint-initdb.d/mongo-init.js:ro`
- **Environment variables (from `.env`)**:
  ```env
  database_name=your_db
  admin_user=admin
  admin_password=admin123
  db_user=user
  db_password=password
  db_port=27017
  ```
- **Kiểm tra MongoDB**:
  ```bash
  docker exec -it <mongo_container_id_or_name> mongosh -u admin -p admin123
  # Xem các database
  show dbs
  ```

---

## 📁 Docker Compose File (Summary)

```yaml
version: "3.8"

services:
  db:
    image: mysql:8.0
    command: --default-authentication-plugin=mysql_native_password
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_DATABASE: ${MYSQL_DATABASE}
      MYSQL_USER: ${MYSQL_USER}
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
    ports:
      - "3306:3306"
    volumes:
      - db_data:/var/lib/mysql

  cache:
    image: redis:latest
    restart: always
    command: redis-server --requirepass ${REDIS_PASSWORD}
    environment:
      REDIS_PASSWORD: ${REDIS_PASSWORD}
    ports:
      - "6379:6379"
    volumes:
      - cache:/data

  mongodb:
    image: mongo:latest
    container_name: ${database_name}
    environment:
      MONGO_INITDB_ROOT_USERNAME: ${admin_user}
      MONGO_INITDB_ROOT_PASSWORD: ${admin_password}
      MONGO_INITDB_DATABASE: ${database_name}
      DB_USERNAME: ${db_user}
      DB_PASSWORD: ${db_password}
      DB_PORT: ${db_port}
    volumes:
      - ./database:/data/db
      - ./mongo-init.js:/docker-entrypoint-initdb.d/mongo-init.js:ro
    ports:
      - ${db_port}:${db_port}

volumes:
  db_data:
  cache:
```

---

## 📚 Ghi chú

- Redis không hỗ trợ tạo user bằng mặc định — chỉ có `requirepass`.
- Volume sẽ giúp giữ data kể cả khi bạn `docker-compose down` hoặc container restart.
- `command` dùng để truyền lệnh khởi động cho service container.
- `volumes` dùng để mount dữ liệu ra ngoài container.

---

## ✨ Chạy Docker Compose

```bash
# Build và chạy nền
docker-compose up -d
```

> Mọi biến được định nghĩa trong `.env` file. Bạn nên tạo file `.env` với nội dung phù hợp trước khi chạy.

---

✅ Nếu cần file mẫu `.env` hoặc script khởi tạo Mongo, mình có thể bổ sung nhé!
