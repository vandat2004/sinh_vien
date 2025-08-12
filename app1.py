import requests
import json

# URL API của server Flask (chạy server trước)
API_URL = "http://127.0.0.1:5000/upload"

# Danh sách sinh viên mẫu
students = [
    {"id": "SV001", "name": "Nguyen Van A", "age": 20, "class": "CNTT1"},
    {"id": "SV002", "name": "Tran Thi B", "age": 21, "class": "CNTT1"},
    {"id": "SV003", "name": "Le Van C", "age": 19, "class": "CNTT2"}
]

# Gửi dữ liệu lên server
response = requests.post(API_URL, json=students)

# In kết quả phản hồi từ server
print(response.status_code, response.json())
