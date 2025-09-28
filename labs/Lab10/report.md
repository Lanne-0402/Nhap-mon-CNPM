# 🕒 Mini App Quản Lý Chấm Công

## 1. Giới thiệu
Mini App Quản Lý Chấm Công được xây dựng từ các Lab trước, với mục tiêu:
- Quản lý tài khoản người dùng (nhân viên, quản lý).
- Hỗ trợ chấm công, đăng nhập/đăng xuất ca làm.
- Lưu trữ dữ liệu trên cơ sở dữ liệu quan hệ.
- Cung cấp giao diện web đơn giản, dễ sử dụng.
- Đảm bảo tính chính xác và bảo mật thông tin.
---
## 2. Mô hình UML 
---
## 3. Database & code minh hoạ 
---
## 4. Kết quả test & sprint report 


### A. Kết quả Test Login
#### ✅ Login thành công (`test_login_success`)
- Nhập đúng username/password (ví dụ: `nv001` / `123456`).
- Bấm **Login**.
- Kiểm tra hiển thị thông báo:  
  `"Đăng nhập thành công! (demo)"`.

#### ❌ Login sai (`test_login_fail`)
- Nhập đúng username nhưng password sai.
- Bấm **Login**.
- Kiểm tra hiển thị:  
  `"Sai username hoặc password."`.

#### 🧹 Cancel xoá form (`test_cancel_clears_form`)
- Nhập username/password.
- Bấm **Cancel**.
- Form phải reset về rỗng + có thông báo:  
  `"Đã xóa dữ liệu nhập."`.

#### 💾 Remember me lưu LocalStorage (`test_remember_me_localstorage`)
- Nhập username + tick **Remember me**.
- **Login** → refresh trang.
- Username vẫn được tự động điền lại từ LocalStorage.

#### 👁 Toggle hiển thị mật khẩu (`test_toggle_password_visibility`)
- Nhập mật khẩu.
- Bấm nút 👁 (toggle).
![Kết quả Test Login](../Lab08-testing/Lab08%20Test%20Login%20form/Pass.jpg)


---
## 5. Kết luận & định hướng mở rộng 
**Kết luận:**
Mini App chấm công nhân viên đã được xây dựng và triển khai với các chức năng cơ bản như: quản lý thông tin nhân viên, ghi nhận giờ vào/ra, quản lý ca làm việc, xuất báo cáo chấm công theo ngày/tháng/năm. Ứng dụng giúp giảm thiểu sai sót trong việc quản lý thời gian làm việc, đồng thời hỗ trợ bộ phận nhân sự theo dõi dữ liệu một cách trực quan, nhanh chóng và chính xác. Qua quá trình phát triển, nhóm đã áp dụng UML để phân tích hệ thống, xây dựng cơ sở dữ liệu, viết code minh họa, kiểm thử và tổng hợp sprint report nhằm đảm bảo tiến độ và chất lượng sản phẩm.

**Định hướng mở rộng:**
- Bổ sung tính năng phân quyền (Admin, Nhân viên, Quản lý).
- Tích hợp tính năng chấm công bằng GPS hoặc nhận diện khuôn mặt để tăng độ tin cậy.
- Xuất báo cáo đa dạng hơn (PDF, Excel) và cho phép thống kê nâng cao (tăng ca, nghỉ phép).
- Kết nối với hệ thống tính lương để tự động hóa quy trình nhân sự.
- Tối ưu giao diện người dùng trên cả web và mobile nhằm nâng cao trải nghiệm sử dụng.
