import requests

# URL API của server Flask (thay SV002 bằng mã bạn muốn tìm)
student_id = "SV002"
API_URL = f"http://127.0.0.1:5000/student/{student_id}"

# Gửi request GET để lấy dữ liệu
response = requests.get(API_URL)

# In kết quả
if response.status_code == 200:
    print("Thông tin sinh viên:", response.json())
else:
    print("Lỗi:", response.json())
