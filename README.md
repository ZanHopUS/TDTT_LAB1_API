# [LAB 1] Xây dựng Web API cho Trợ lý ảo AI Tiếng Việt

**Thông tin sinh viên:**
* **Họ và tên:** Trịnh Văn Hợp
* **MSSV:** 24120318
* **Trường:** Đại học Khoa học Tự nhiên, ĐHQG-HCM
* **Môn học:** Tư duy tính toán

---

## 1. Giới thiệu hệ thống
Dự án này triển khai một Web API sử dụng **FastAPI** để khai thác sức mạnh của mô hình ngôn ngữ lớn từ Hugging Face. Hệ thống được xây dựng như một trợ lý ảo thông minh, hỗ trợ giải đáp các thắc mắc về Công nghệ thông tin và đưa ra lời khuyên học tập bằng tiếng Việt một cách logic và súc tích.

**Tính năng chính:**
- API RESTful với FastAPI framework
- Tích hợp mô hình ngôn ngữ lớn Qwen2.5-0.5B-Instruct
- Hỗ trợ chat template chuẩn của AI hiện đại
- Validation đầu vào và xử lý lỗi chi tiết
- Script kiểm thử tự động với error handling

## 2. Thông tin mô hình sử dụng
* **Tên mô hình:** `Qwen/Qwen2.5-0.5B-Instruct`
* **Loại tác vụ:** Hỏi đáp / Sinh văn bản (Instruct/Text Generation)
* **Liên kết Hugging Face:** [Qwen/Qwen2.5-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct)

## 3. Cấu trúc mã nguồn
* `main.py`: Chứa mã nguồn chính của ứng dụng FastAPI và logic xử lý mô hình.
* `config.yaml`: Lưu trữ cấu hình đường dẫn đến mô hình trên Hugging Face.
* `requirements.txt`: Danh sách các thư viện cần thiết để cài đặt môi trường.
* `test_api.py`: Script Python dùng thư viện `requests` để kiểm thử tự động các chức năng API.
* `README.md`: Tài liệu hướng dẫn chi tiết về dự án.

## 4. Hướng dẫn cài đặt và khởi chạy

### Bước 1: Cài đặt thư viện
Mở Terminal tại thư mục dự án và chạy lệnh:
```bash
pip install -r requirements.txt
```

### Bước 2: Khởi chạy ứng dụng
Chạy lệnh sau để khởi động server FastAPI:
```bash
uvicorn main:app --reload
```
Server sẽ chạy tại `http://127.0.0.1:8000`

### Bước 3: Kiểm thử API
- **Interactive API docs (Swagger UI):** http://127.0.0.1:8000/docs
- **ReDoc API docs:** http://127.0.0.1:8000/redoc
- **Chạy script kiểm thử:**
```bash
python test_api.py
```
Script sẽ tự động:
- Kiểm tra server health trước khi test
- Thử nghiệm 2 câu hỏi mẫu về IT và học tập
- Hiển thị kết quả với error handling chi tiết

## 5. Các Endpoint của API

### 1. `GET /` - Thông tin hệ thống
```
URL: http://127.0.0.1:8000/
Response:
{
  "message": "Hệ thống API Trợ lý ảo AI. Sinh viên thực hiện: Trịnh Văn Hợp."
}
```

### 2. `GET /health` - Kiểm tra trạng thái
```
URL: http://127.0.0.1:8000/health
Response:
{
  "status": "ok",
  "model": "Qwen2.5-0.5B-Instruct"
}
```

### 3. `POST /generate` - Tạo câu trả lời từ mô hình AI
```
URL: http://127.0.0.1:8000/generate
Method: POST
Content-Type: application/json
Body:
{
  "prompt": "Hỏi về lập trình Python"
}
Response (Success - 200):
{
  "question": "Hỏi về lập trình Python",
  "answer": "Câu trả lời từ mô hình AI..."
}
```

## 6. Cấu trúc thư mục
```
TDTT_LAB1/
├── main.py              # Ứng dụng FastAPI chính
├── config.yaml          # Cấu hình đường dẫn mô hình
├── requirements.txt     # Các thư viện cần thiết
├── test_api.py          # Script kiểm thử API
└── README.md            # Tài liệu này
```

## 7. Video Demo
Vui lòng xem video minh họa hệ thống tại liên kết dưới đây:

👉 [Chèn link video của bạn tại đây - VD: Link Youtube/Google Drive]