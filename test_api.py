import requests
import sys

BASE_URL = "http://127.0.0.1:8000"
ROOT_URL = f"{BASE_URL}/"
HEALTH_URL = f"{BASE_URL}/health"
GENERATE_URL = f"{BASE_URL}/generate"

def test_root():
    """Kiểm thử endpoint GET /"""
    try:
        res = requests.get(ROOT_URL, timeout=5)
        if res.status_code == 200:
            print("✓ [GET /] Thành công:", res.json()["message"])
            return True
        else:
            print(f"✗ [GET /] Lỗi: {res.status_code}")
            return False
    except Exception as e:
        print(f"✗ [GET /] Lỗi kết nối: {e}")
        return False

def check_server():
    """Kiểm tra endpoint GET /health"""
    try:
        res = requests.get(HEALTH_URL, timeout=5)
        if res.status_code == 200:
            print(f"✓ [GET /health] Server FastAPI đang chạy bình thường (Model: {res.json()['model']})")
            return True
        else:
            print(f"✗ [GET /health] Server trả về lỗi: {res.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("✗ Lỗi: Không thể kết nối đến server.")
        print("   Hãy chắc chắn bạn đã chạy lệnh: uvicorn main:app --reload")
        return False
    except requests.exceptions.Timeout:
        print("✗ Lỗi: Timeout - Server không phản hồi")
        return False

def test_generate(prompt):
    """Kiểm thử endpoint POST /generate"""
    try:
        res = requests.post(GENERATE_URL, json={"prompt": prompt}, timeout=30)
        if res.status_code == 200:
            return res.json()["answer"]
        else:
            return f"[Lỗi {res.status_code}] {res.json().get('detail', 'Không xác định')}"
    except requests.exceptions.Timeout:
        return "[Lỗi] Timeout - Mô hình mất quá lâu để xử lý"
    except Exception as e:
        return f"[Lỗi] {str(e)}"

# Main
if __name__ == "__main__":
    print("KIỂM THỬ TỔNG THỂ API TRỢ LÝ AI TIẾNG VIỆT".center(70))
    
    print("\n[BƯỚC 1] KIỂM TRA TRẠNG THÁI HỆ THỐNG")
    print("-" * 30)
    if not check_server():
        sys.exit(1)
    test_root()
    
    print("\n[BƯỚC 2] KIỂM THỬ CHỨC NĂNG HỎI ĐÁP (AI GENERATION)")
    print("-" * 30)
    
    # Thử nghiệm 1
    print(">> Thử nghiệm 1: Hỏi kiến thức nền tảng")
    print("   [Câu hỏi]: API là gì?")
    answer1 = test_generate("Hãy giải thích ngắn gọn API là gì cho một người mới bắt đầu học lập trình.")
    print(f"   [Trả lời]: {answer1}\n")
    
    # Thử nghiệm 2
    print(">> Thử nghiệm 2: Lời khuyên học tập")
    print("   [Câu hỏi]: Kỹ năng cho sinh viên IT năm 2?")
    answer2 = test_generate("Sinh viên năm 2 ngành Công nghệ thông tin thì nên tập trung học những môn và kỹ năng nào?")
    print(f"   [Trả lời]: {answer2}")

    print("KIỂM THỬ HOÀN TẤT!".center(70))