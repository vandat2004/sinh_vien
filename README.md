Hệ thống Quản lý Sinh viên – Kết nối Flask và SQL Server
1. Tổng quan
Bài tập này xây dựng một hệ thống quản lý sinh viên được chia thành hai ứng dụng Flask độc lập:
Ứng dụng A: Đóng vai trò quản trị, cho phép thêm, chỉnh sửa, xóa và tìm kiếm sinh viên. Ứng dụng này lưu dữ liệu trực tiếp vào SQL Server và đồng thời cung cấp API RESTful cho bên ngoài truy cập.
Ứng dụng B: Hoạt động như một client web, truy vấn API của Ứng dụng A để lấy danh sách sinh viên và thông tin chi tiết từng người.
Hai ứng dụng trao đổi dữ liệu thông qua HTTP JSON API, giúp hệ thống tách biệt giữa phần quản trị và phần hiển thị.

2. Chức năng chính
Ứng dụng A – Quản lý và cung cấp API
Giao diện web:
Thêm mới sinh viên.
Chỉnh sửa thông tin sinh viên hiện có.
Xóa sinh viên khỏi hệ thống.
Tìm kiếm theo mã hoặc tên sinh viên.
API JSON:
GET /api/students → Lấy toàn bộ danh sách sinh viên.
GET /api/student/<id> → Lấy thông tin sinh viên cụ thể.
POST /api/student → Thêm sinh viên mới.
PUT /api/student/<id> → Cập nhật thông tin sinh viên.
DELETE /api/student/<id> → Xóa sinh viên theo mã.
Dữ liệu được lưu và truy xuất từ Microsoft SQL Server.

Ứng dụng B – Xem thông tin từ API
Kết nối đến API của Ứng dụng A bằng thư viện requests.
Hiển thị danh sách sinh viên trên web với giao diện Bootstrap.
Xem chi tiết thông tin từng sinh viên.
Tìm kiếm sinh viên theo mã hoặc tên, dựa vào dữ liệu trả về từ API.

3. Công nghệ sử dụng
Ngôn ngữ: Python 3
Framework: Flask
Cơ sở dữ liệu: Microsoft SQL Server
Thư viện Python:
flask → Xây dựng ứng dụng web và API
pyodbc → Kết nối SQL Server
requests → Gọi API từ Ứng dụng B
Frontend:
HTML + Bootstrap 5
CSS tùy chỉnh
