# RUN_LOCAL.md – Hướng dẫn chạy Lab 04 cho team-camera

Tài liệu này mô tả cách clone repo sạch, build image camera, chạy container và kiểm tra health endpoint.

---

## 1. Clone repo

```bash
git clone <repo-url>
cd FIT4110_lab04_nhom_7
```

---

## 2. Cài dependencies cho Newman/Prism/Spectral

```bash
npm install
```

---

## 3. Build Docker image

```bash
docker build -t fit4110/camera-stream:lab04 .
```

---

## 4. Run container

```bash
docker run --rm \
  --name fit4110-camera-lab04 \
  -p 8000:8000 \
  --env-file .env.example \
  fit4110/camera-stream:lab04
```

Mở terminal khác, kiểm tra:

```bash
curl http://localhost:8000/health
```

Kết quả mong đợi:

```json
{
  "status": "ok",
  "service": "camera-stream",
  "version": "0.1.0"
}
```

---

## 5. Chạy Newman test trên container

```bash
npm run test:camera:local
```

Lệnh này chạy bộ Newman camera đã cấu hình trong `package.json`.

Report sinh tại:

```text
reports/newman-lab04-local.xml
reports/newman-lab04-local.html
```

---

## 6. Dừng container

Nếu không dùng `--rm` hoặc container còn chạy:

```bash
docker stop fit4110-camera-lab04
```

---

## 7. Lệnh nhanh

```bash
make build
make run
make test-docker
make stop
```

### Ghi chú cho team-camera

- Dockerfile phải chạy `camera_stream_service.main:app`.
- `SERVICE_NAME` trong `.env.example` nên là `camera-stream` để `/health` trả về đúng tên service.
- Nếu service camera của bạn có thêm endpoint nghiệp vụ, hãy bổ sung vào collection Newman và ghi rõ trong mục này.
