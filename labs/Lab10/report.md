# 🕒 Mini App Quản Lý Chấm Công

## 1. Giới thiệu
Mini App Quản Lý Chấm Công được xây dựng từ các Lab trước, với mục tiêu:
- Quản lý tài khoản người dùng (nhân viên, quản lý).
- Hỗ trợ chấm công, đăng nhập/đăng xuất ca làm.
- Lưu trữ dữ liệu trên cơ sở dữ liệu quan hệ.
- Cung cấp giao diện web đơn giản, dễ sử dụng.
- Đảm bảo tính chính xác và bảo mật thông tin.

## 2. Mô hình UML 

## 3. Database & code minh hoạ 

## 4. Kết quả test & sprint report 


---

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
- Kiểm tra input password đổi từ `"password"` sang `"text"`.
![Kết quả Test Login](labs/Lab08-testing/Lab08%20Test%20Login%20form/Pass.jpg)

## 5. Kết luận & định hướng mở rộng 
