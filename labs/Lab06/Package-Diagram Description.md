1. 🗂 Các gói trong sơ đồ gói App

Quản lý người dùng
  Bao gồm: Admin, Quản lý, Nhân viên
  Thể hiện các loại vai trò người dùng trong hệ thống.
  Các quan hệ “kế thừa” (extends) giữa Admin, Quản lý, Nhân viên từ User thể hiện sự phân cấp vai trò.

Quản lý chấm công
  Bao gồm: Check-in/Check-out, Yêu cầu chỉnh sửa chấm công, Báo cáo chấm công.
  Đây là module nghiệp vụ chính của app: ghi nhận chấm công, xử lý yêu cầu chỉnh sửa, xuất báo cáo.

Quản lý nhân viên
  Bao gồm: Quản lý nhân viên (thêm/sửa/xóa).
  Liên quan trực tiếp đến việc cập nhật thông tin nhân sự trong hệ thống.

Quản lý ca làm việc
  Bao gồm: Ca làm việc.
  Dùng cho việc phân ca, lịch làm việc, cập nhật ca làm việc cho nhân viên.

User (gói bên ngoài)
  Thể hiện người dùng cuối (người sử dụng app) sẽ truy cập vào hệ thống, kết nối với module “Quản lý người dùng”.

🔗 Quan hệ giữa các gói

  User → Quản lý người dùng:
  Người dùng bên ngoài đăng nhập vào hệ thống qua module quản lý người dùng.

  Quản lý người dùng → Quản lý chấm công:
  Tài khoản nhân viên/ quản lý sẽ thực hiện check-in/out, gửi yêu cầu chỉnh sửa, xem báo cáo.

  Quản lý người dùng → Quản lý nhân viên:
  Quản lý/ admin có thể cập nhật thông tin nhân viên.

  Quản lý người dùng → Quản lý ca làm việc:
  Quản lý sẽ phân ca, điều chỉnh ca làm việc cho nhân viên.

2. 🗂 Các gói trong sơ đồ

User (người dùng bên ngoài)
  Đại diện cho người sử dụng hệ thống (Admin hoặc Quản lý).
  Truy cập vào module "Quản lý người dùng".

Quản lý người dùng
  Đây là gói chức năng tổng quát chứa toàn bộ các vai trò và phòng ban.
  Bên trong có các package nhỏ hơn:

Phòng ban:
  Đại diện cho đơn vị quản lý.
  Bên trong có lớp Quản lý, thể hiện người có quyền quản lý trong phòng ban.

Quản lý nhân viên:
  Module chuyên xử lý các chức năng thêm, sửa, xóa nhân viên.
  Bên trong chứa Nhân viên (Employee) – đối tượng được quản lý.

Quản lý ca làm việc
  Bao gồm Ca làm việc.
  Liên quan chặt chẽ đến nhân viên (mỗi nhân viên sẽ được gán ca làm việc).

🔗 Quan hệ giữa các gói
  User → Quản lý người dùng: Người dùng đăng nhập hệ thống và thao tác với module quản lý.
  Quản lý → Quản lý nhân viên: Người quản lý có quyền thêm, sửa, xóa thông tin nhân viên.
  Quản lý nhân viên → Nhân viên: Thể hiện mối quan hệ bao chứa (nhân viên nằm trong phạm vi quản lý).
  Quản lý người dùng → Quản lý ca làm việc: Từ hệ thống người dùng có thể truy cập và gán ca làm việc cho nhân viên.
