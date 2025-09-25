🔶 Mô tả sơ đồ lớp - Class Diagram 

1. Lớp User

* Thuộc tính:
- ID User : int
- Tên người dùng : String
- Mật khẩu : String
- Vai trò : String

* Phương thức:
- + Đăng nhập()
- + Đăng xuất()

* Ý nghĩa: Lớp cơ sở, chứa thông tin đăng nhập và vai trò chung của tất cả người dùng hệ thống.

2. Lớp Nhân viên

* Thuộc tính:
 - ID nhân viên : int
 - Tên : String
 - Vị trí phòng ban : String

* Phương thức:
- + Checkin/Checkout()
- + Xem lịch sử chấm công()
- + Yêu cầu / Khiếu nại()

Quan hệ:

Kế thừa từ User.

Liên kết với Checkin/Checkout.

Tạo Yêu cầu chỉnh sửa chấm công.

Ý nghĩa: Đại diện cho nhân viên trong hệ thống, có thể chấm công và gửi khiếu nại nếu có sai sót.

2.3. Lớp Quản lý

Phương thức:

+ Quản lý nhân viên()

+ Quản lý ca làm việc()

+ Thống kê giờ công()

+ Phản hồi yêu cầu/khiếu nại()

Quan hệ:

Kế thừa từ User.

Liên kết với Nhân viên, Quản lý ca, Quản lý nhân viên, và Báo cáo chấm công.

Ý nghĩa: Quản lý chịu trách nhiệm điều hành, theo dõi hoạt động chấm công và xử lý yêu cầu chỉnh sửa.

2.4. Lớp Admin

Phương thức:

+ Quản lý hệ thống()

+ Báo cáo và xuất file()

+ Vận hành và cải tiến App()

Quan hệ: Kế thừa từ User.

Ý nghĩa: Admin quản trị cấp cao, đảm bảo hệ thống vận hành, xử lý báo cáo tổng thể và bảo trì hệ thống.

2.5. Lớp Checkin/Checkout

Thuộc tính:

QR chấm công : String

Ngày chấm công : Date

Thời gian chấm công : Time

Trạng thái nhân viên chấm công : String

Phương thức:

+ Ghi lại báo cáo chấm công()

Quan hệ:

Liên kết với Nhân viên.

Dữ liệu được sử dụng trong Báo cáo chấm công.

Ý nghĩa: Ghi nhận dữ liệu chấm công hàng ngày của nhân viên.

2.6. Lớp Yêu cầu chỉnh sửa chấm công

Thuộc tính:

ID nhân viên : int

Xác nhận yêu cầu : boolean

ID chấm công : int

Nguyên nhân : String

Trạng thái cập nhật : String

Phương thức:

+ Đệ trình yêu cầu()

+ Phê duyệt / Từ chối yêu cầu()

Quan hệ:

Gắn với Nhân viên.

Được xử lý bởi Quản lý.

Ý nghĩa: Giúp nhân viên yêu cầu sửa đổi dữ liệu chấm công khi có sai sót.

2.7. Lớp Quản lý ca

Thuộc tính:

Thông tin ca làm : String

Ngày : Date

Giờ bắt đầu : Time

Giờ kết thúc : Time

Phương thức:

+ Đăng ký ca làm việc()

+ Cập nhật ca làm việc()

Quan hệ: Liên kết với Quản lý.

Ý nghĩa: Đại diện cho lịch làm việc, cho phép quản lý phân ca và chỉnh sửa ca làm việc.

2.8. Lớp Quản lý nhân viên

Thuộc tính:

Thông tin nhân viên : String

Thông tin ca làm : String

Phương thức:

+ Thêm thông tin nhân viên()

+ Xóa thông tin nhân viên()

+ Sửa thông tin nhân viên()

Quan hệ: Hỗ trợ Quản lý.

Ý nghĩa: Chức năng quản lý thông tin nhân viên và ca làm việc.

2.9. Lớp Báo cáo chấm công

Thuộc tính:

ID báo cáo : int

Format và dữ liệu : String

Nội dung báo cáo : String

Phương thức:

+ Kết quả báo cáo()

+ Xuất file()

Quan hệ:

Nhận dữ liệu từ Checkin/Checkout.

Được Quản lý và Admin sử dụng.

Ý nghĩa: Sinh báo cáo từ dữ liệu chấm công, hỗ trợ xuất file cho quản lý hoặc admin.

3. Mối quan hệ chính

Kế thừa (Generalization):
User → Nhân viên, Quản lý, Admin.

Kết hợp (Association/Composition):

Nhân viên ↔ Checkin/Checkout (1..*).

Quản lý ↔ Quản lý nhân viên, Quản lý ca, Báo cáo chấm công.

Nhân viên ↔ Yêu cầu chỉnh sửa chấm công.

Tương tác nghiệp vụ:
 - Nhân viên checkin/checkout → dữ liệu ghi nhận → báo cáo chấm công → quản lý phê duyệt/kiểm tra → admin vận hành toàn hệ thống.
