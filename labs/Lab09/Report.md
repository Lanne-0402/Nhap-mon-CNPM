# 💾 Report – Lab 09: Quản lý dự án ATM trên Jira (Agile)

**1. Giới thiệu** 
-	Mục tiêu: Mô phỏng quản lý phát triển ATM System bằng phương pháp Scrum.
-	Công cụ sử dụng: Jira Software.
-	Project: ATM System
-	Epic: ATM Basic Functions.


**2.	User Stories** 

🔴 Epic 1: Chấm công nhân viên bằng quét QR code
- US1: Là nhân viên, tôi muốn đăng nhập/đăng xuất bằng tài khoản để bảo mật dữ liệu chấm công.
- US2: Là nhân viên, tôi muốn check-in/check-out bằng cách quét QR code để ghi nhận giờ làm việc nhanh chóng.
-	US3: Là nhân viên, tôi muốn xem lại lịch sử chấm công của mình để theo dõi số ngày/giờ đã làm.
-	US4: Là nhân viên, tôi muốn gửi yêu cầu chỉnh sửa bảng chấm công (khi có sai sót) để đảm bảo tính chính xác.

🔴	Epic 2: Quản lý thông tin nhân viên
-	US5: Là quản lý, tôi muốn thêm thông tin nhân viên mới để quản lý đội ngũ.
-	US6: Là quản lý, tôi muốn chỉnh sửa thông tin nhân viên để đảm bảo dữ liệu luôn đúng.
-	US7: Là quản lý, tôi muốn xóa thông tin nhân viên khi họ nghỉ việc để giữ dữ liệu gọn gàng.
-	US8: Là quản lý, tôi muốn tìm kiếm và xem thông tin nhân viên để dễ dàng quản trị.

🔴	Epic 3: Quản lý ca làm việc
-	US9: Là quản lý, tôi muốn tạo ca làm việc mới để sắp xếp lịch cho nhân viên.
-	US10: Là quản lý, tôi muốn chỉnh sửa ca làm việc để cập nhật khi có thay đổi.
-	US11: Là quản lý, tôi muốn phân công ca làm việc cho nhân viên để tối ưu nguồn lực.
-	US12: Là quản lý, tôi muốn xem danh sách ca làm việc để theo dõi tình trạng phân ca.

🔴	Epic 4: Thống kê, tổng hợp báo cáo chấm công theo ngày, tháng, năm
-	US13: Là quản lý, tôi muốn xem báo cáo chấm công theo ngày để quản lý tình hình làm việc hằng ngày.
-	US14: Là quản lý, tôi muốn xem báo cáo chấm công theo tháng để tổng hợp hiệu suất nhân viên.
-	US15: Là quản lý, tôi muốn xem báo cáo chấm công theo năm để phân tích xu hướng dài hạn.
-	US16: Là quản lý, tôi muốn xuất báo cáo chấm công ra file Excel/PDF để lưu trữ và chia sẻ.


**3. Tasks / Subtasks**

🔴	Epic 1: Chấm công nhân viên bằng quét QR code
-	US1: Đăng nhập/Đăng xuất
•	Task 1.1: Thiết kế giao diện đăng nhập/đăng xuất
o	Sub-task: Tạo form nhập username/password
o	Sub-task: Thêm validate thông tin đăng nhập
•	Task 1.2: Viết API xác thực người dùng
o	Sub-task: Kết nối DB kiểm tra tài khoản
o	Sub-task: Xử lý JWT/Session
•	Task 1.3: Test chức năng đăng nhập/đăng xuất


-	US2: Check-in/Check-out bằng QR
•	Task 2.1: Thiết kế giao diện quét QR
o	Sub-task: Tích hợp camera/mã QR scanner
o	Sub-task: Hiển thị kết quả check-in/out thành công/thất bại
•	Task 2.2: API xử lý quét QR
o	Sub-task: Lưu thời gian check-in/out vào DB
o	Sub-task: Kiểm tra hợp lệ (giờ làm, nhân viên hợp lệ)
•	Task 2.3: Test tính năng check-in/out


-	US3: Xem lịch sử chấm công
•	Task 3.1: Thiết kế màn hình lịch sử chấm công
 
o	Sub-task: Hiển thị dữ liệu theo ngày/tháng
o	Sub-task: Cho phép lọc theo khoảng thời gian
•	Task 3.2: API lấy lịch sử chấm công từ DB
•	Task 3.3: Test hiển thị dữ liệu


-	US4: Gửi yêu cầu chỉnh sửa bảng chấm công
•	Task 4.1: Thiết kế form gửi yêu cầu chỉnh sửa
o	Sub-task: Nhập ngày công sai và lý do
o	Sub-task: Validate dữ liệu nhập
•	Task 4.2: API tạo yêu cầu chỉnh sửa
•	Task 4.3: Thông báo gửi tới quản lý
•	Task 4.4: Test toàn bộ luồng yêu cầu chỉnh sửa


🔴	Epic 2: Quản lý thông tin nhân viên
-	US5: Thêm nhân viên mới
•	Task 5.1: Thiết kế form thêm nhân viên
•	Task 5.2: API thêm nhân viên vào DB
•	Task 5.3: Validate dữ liệu (email, số ĐT)
•	Task 5.4: Test chức năng thêm


-	US6: Chỉnh sửa nhân viên
•	Task 6.1: Thiết kế form chỉnh sửa
•	Task 6.2: API cập nhật thông tin nhân viên
•	Task 6.3: Test chức năng chỉnh sửa


-	US7: Xóa nhân viên
•	Task 7.1: Thêm nút xóa + popup xác nhận
•	Task 7.2: API xóa nhân viên theo ID
•	Task 7.3: Test chức năng xóa


-	US8: Tìm kiếm và xem nhân viên
•	Task 8.1: Giao diện tìm kiếm + hiển thị chi tiết nhân viên
•	Task 8.2: API tìm kiếm nhân viên theo tên/ID
 
•	Task 8.3: Test tìm kiếm


🔴	Epic 3: Quản lý ca làm việc
-	US9: Tạo ca làm việc mới
•	Task 9.1: Thiết kế form tạo ca làm việc
•	Task 9.2: API tạo ca mới
•	Task 9.3: Test tạo ca


-	US10: Chỉnh sửa ca làm việc
•	Task 10.1: Giao diện chỉnh sửa ca làm việc
•	Task 10.2: API cập nhật ca làm việc
•	Task 10.3: Test chỉnh sửa ca


-	US11: Phân công ca làm việc
•	Task 11.1: Giao diện phân công ca cho nhân viên
•	Task 11.2: API lưu thông tin phân công
•	Task 11.3: Test phân công


-	US12: Xem danh sách ca làm việc
•	Task 12.1: Giao diện danh sách ca
•	Task 12.2: API lấy danh sách ca từ DB
•	Task 12.3: Test hiển thị danh sách


🔴	Epic 4: Thống kê, tổng hợp báo cáo chấm công
-	US13: Báo cáo theo ngày
•	Task 13.1: API tổng hợp dữ liệu chấm công theo ngày
•	Task 13.2: Giao diện báo cáo ngày
•	Task 13.3: Test báo cáo ngày


-	US14: Báo cáo theo tháng
•	Task 14.1: API tổng hợp dữ liệu chấm công theo tháng
•	Task 14.2: Giao diện báo cáo tháng
•	Task 14.3: Test báo cáo tháng
 
-	US15: Báo cáo theo năm
•	Task 15.1: API tổng hợp dữ liệu năm
•	Task 15.2: Giao diện báo cáo năm
•	Task 15.3: Test báo cáo năm


-	US16: Xuất báo cáo (Excel/PDF)
•	Task 16.1: Chức năng export báo cáo sang Excel
•	Task 16.2: Chức năng export sang PDF
•	Task 16.3: Test export báo cáo

