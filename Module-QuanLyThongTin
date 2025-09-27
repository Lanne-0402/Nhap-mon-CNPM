import mysql.connector
import re
from datetime import datetime

# ------------------ KẾT NỐI MYSQL ------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lethibaodiep0501@",  # đổi thành mật khẩu MySQL của bạn
    database="systemdb"
)
cursor = conn.cursor()

# ------------------ HÀM KIỂM TRA DỮ LIỆU ------------------

def nhap_ngay(prompt):
    while True:
        val = input(prompt)
        try:
            datetime.strptime(val, "%Y-%m-%d")
            return val
        except ValueError:
            print("❌ Ngày không hợp lệ. Định dạng đúng là YYYY-MM-DD. Vui lòng nhập lại.")

def nhap_email(prompt):
    while True:
        val = input(prompt)
        if re.match(r"[^@]+@[^@]+\.[^@]+", val):
            return val
        else:
            print("❌ Email không hợp lệ. Vui lòng nhập lại.")

def nhap_sdt(prompt):
    while True:
        val = input(prompt)
        if val.isdigit() and 9 <= len(val) <= 11:
            return val
        else:
            print("❌ Số điện thoại phải là số và có độ dài từ 9 đến 11 ký tự. Vui lòng nhập lại.")

def nhap_chuoi(prompt):
    while True:
        val = input(prompt)
        if val.strip():
            return val.strip()
        else:
            print("❌ Không được để trống. Vui lòng nhập lại.")

# ------------------ CÁC HÀM CRUD ------------------

def xem_danh_sach():
    print("\n📋 ĐANG HIỂN THỊ DANH SÁCH NHÂN VIÊN...")
    cursor.execute("SELECT * FROM nhanvien")
    rows = cursor.fetchall()
    if rows:
        print("\n===== DANH SÁCH NHÂN VIÊN =====")
        for row in rows:
            print(f"""
ID: {row[0]}
Họ Tên: {row[2]}
Ngày sinh: {row[3]}
Giới tính: {row[4]}
Địa chỉ: {row[5]}
SĐT: {row[6]}
Email: {row[7]}
Vị trí: {row[8]}
Phòng ban: {row[9]}
Ngày vào làm: {row[10]}
------------------------------""")
    else:
        print("❌ Hiện tại chưa có nhân viên nào trong hệ thống.")


def them_nhan_vien():
    print("\n➕ THÊM NHÂN VIÊN MỚI")

    hoten = nhap_chuoi("Họ và tên: ")
    ngaysinh = nhap_ngay("Ngày sinh (YYYY-MM-DD): ")
    gioitinh = nhap_chuoi("Giới tính: ")
    diachi = nhap_chuoi("Địa chỉ: ")
    sdt = nhap_sdt("Số điện thoại: ")
    email = nhap_email("Email: ")
    vitri = nhap_chuoi("Vị trí: ")
    phongban = nhap_chuoi("Phòng ban: ")
    ngayvaolam = nhap_ngay("Ngày vào làm (YYYY-MM-DD): ")

    print("\n⚠️ Xác nhận thêm nhân viên mới?")
    confirm = input("👉 Nhấn 'y' để thêm, 'n' để hủy: ")

    if confirm.lower() == "y":
        query = """
        INSERT INTO nhanvien (HoTen, NgaySinh, GioiTinh, DiaChi, SoDienThoai, Email, ViTri, PhongBan, NgayVaoLam)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(query, (hoten, ngaysinh, gioitinh, diachi, sdt, email, vitri, phongban, ngayvaolam))
        conn.commit()
        print("✅ Nhân viên mới đã được thêm thành công!")
    else:
        print("❌ Hủy bỏ thao tác thêm nhân viên.")


def cap_nhat_nhan_vien():
    print("\n✏️ CẬP NHẬT THÔNG TIN NHÂN VIÊN")
    nhanvien_id = input("👉 Nhập ID nhân viên cần cập nhật: ")

    print("\n--- CHỌN LOẠI CẬP NHẬT ---")
    print("1. Cập nhật toàn bộ thông tin")
    print("2. Chỉ cập nhật ngày sinh")
    print("3. Chỉ cập nhật địa chỉ")
    print("4. Chỉ cập nhật số điện thoại")
    print("5. Chỉ cập nhật email")
    print("6. Chỉ cập nhật vị trí")
    print("7. Chỉ cập nhật phòng ban")
    print("0. Quay lại menu chính")

    choice = input("👉 Bạn chọn: ")

    query = None
    params = None

    if choice == "1":
        hoten = nhap_chuoi("Họ và tên: ")
        ngaysinh = nhap_ngay("Ngày sinh (YYYY-MM-DD): ")
        gioitinh = nhap_chuoi("Giới tính: ")
        diachi = nhap_chuoi("Địa chỉ: ")
        sdt = nhap_sdt("Số điện thoại: ")
        email = nhap_email("Email: ")
        vitri = nhap_chuoi("Vị trí: ")
        phongban = nhap_chuoi("Phòng ban: ")
        ngayvaolam = nhap_ngay("Ngày vào làm (YYYY-MM-DD): ")

        query = """UPDATE nhanvien 
                   SET HoTen=%s, NgaySinh=%s, GioiTinh=%s, DiaChi=%s, SoDienThoai=%s,
                       Email=%s, ViTri=%s, PhongBan=%s, NgayVaoLam=%s
                   WHERE NhanVienID=%s"""
        params = (hoten, ngaysinh, gioitinh, diachi, sdt, email, vitri, phongban, ngayvaolam, nhanvien_id)

    elif choice == "2":
        val = nhap_ngay("👉 Nhập ngày sinh mới (YYYY-MM-DD): ")
        query = "UPDATE nhanvien SET NgaySinh=%s WHERE NhanVienID=%s"
        params = (val, nhanvien_id)
    elif choice == "3":
        val = nhap_chuoi("👉 Nhập địa chỉ mới: ")
        query = "UPDATE nhanvien SET DiaChi=%s WHERE NhanVienID=%s"
        params = (val, nhanvien_id)
    elif choice == "4":
        val = nhap_sdt("👉 Nhập số điện thoại mới: ")
        query = "UPDATE nhanvien SET SoDienThoai=%s WHERE NhanVienID=%s"
        params = (val, nhanvien_id)
    elif choice == "5":
        val = nhap_email("👉 Nhập email mới: ")
        query = "UPDATE nhanvien SET Email=%s WHERE NhanVienID=%s"
        params = (val, nhanvien_id)
    elif choice == "6":
        val = nhap_chuoi("👉 Nhập vị trí mới: ")
        query = "UPDATE nhanvien SET ViTri=%s WHERE NhanVienID=%s"
        params = (val, nhanvien_id)
    elif choice == "7":
        val = nhap_chuoi("👉 Nhập phòng ban mới: ")
        query = "UPDATE nhanvien SET PhongBan=%s WHERE NhanVienID=%s"
        params = (val, nhanvien_id)
    elif choice == "0":
        return
    else:
        print("❌ Lựa chọn không hợp lệ.")
        return

    if query:
        confirm = input("⚠️ Bạn có chắc muốn cập nhật dữ liệu này? (y/n): ")
        if confirm.lower() == "y":
            cursor.execute(query, params)
            conn.commit()
            print("✅ Cập nhật thành công.")
        else:
            print("❌ Hủy bỏ thao tác cập nhật.")


def xoa_nhan_vien():
    print("\n🗑️ XÓA NHÂN VIÊN")
    nhanvien_id = input("👉 Nhập ID nhân viên cần xóa: ")

    confirm = input(f"⚠️ Bạn có chắc muốn xóa nhân viên ID {nhanvien_id}? (y/n): ")
    if confirm.lower() == "y":
        cursor.execute("DELETE FROM nhanvien WHERE NhanVienID=%s", (nhanvien_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"✅ Nhân viên có ID {nhanvien_id} đã bị xóa.")
        else:
            print("❌ Không tìm thấy nhân viên với ID này.")
    else:
        print("❌ Hủy bỏ thao tác xóa.")

# ------------------ MENU ------------------

def menu():
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ NHÂN VIÊN =====")
        print("👉 Nhấn 1 để XEM danh sách nhân viên")
        print("👉 Nhấn 2 để THÊM nhân viên mới")
        print("👉 Nhấn 3 để CẬP NHẬT thông tin nhân viên")
        print("👉 Nhấn 4 để XÓA nhân viên")
        print("👉 Nhấn 0 để THOÁT chương trình")

        choice = input("➡️ Vui lòng chọn thao tác: ")

        if choice == "1":
            xem_danh_sach()
        elif choice == "2":
            them_nhan_vien()
        elif choice == "3":
            cap_nhat_nhan_vien()
        elif choice == "4":
            xoa_nhan_vien()
        elif choice == "0":
            print("👋 Thoát chương trình. Bye bye!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ, vui lòng chọn lại.")

# ------------------ CHẠY CHƯƠNG TRÌNH ------------------
menu()

# Đóng kết nối
cursor.close()
conn.close()
