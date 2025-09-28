import re
from datetime import datetime, date

# CSDL giả lập 
mock_db = []
_id_counter = 1

# ================== HÀM KIỂM TRA DỮ LIỆU ==================

def nhap_chuoi(chuoi: str) -> str:
    if not chuoi or chuoi.strip() == "":
        raise ValueError("Chuỗi không được để trống.")

    # Xóa khoảng trắng dư
    chuoi = chuoi.strip()

    # Không chứa số hoặc ký tự đặc biệt
    if not re.match(r"^[A-Za-zÀ-ỹ\s]+$", chuoi):
        raise ValueError("Chuỗi chỉ được chứa chữ cái và khoảng trắng.")

    return chuoi


def nhap_ngay(chuoi: str) -> date:
    try:
        d = datetime.strptime(chuoi, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Ngày không đúng định dạng YYYY-MM-DD.")

    if d > date.today():
        raise ValueError("Ngày không hợp lệ (tương lai).")
    return d


def nhap_email(email: str) -> str:
    if not email or "@" not in email:
        raise ValueError("Email không hợp lệ.")

    # Regex cơ bản: phải có tên@domain
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        raise ValueError("Email không hợp lệ.")
    return email


def nhap_sdt(sdt: str) -> str:
    if not sdt.isdigit():
        raise ValueError("Số điện thoại chỉ được chứa chữ số.")
    if len(sdt) < 9 or len(sdt) > 15:
        raise ValueError("Số điện thoại phải từ 9–15 số.")
    return sdt

# ================== CÁC HÀM CRUD ==================

def xem_danh_sach():
    return mock_db

def them_nhan_vien(HoTen, NgaySinh, GioiTinh, DiaChi, SoDienThoai,
                   Email, ChucVu, PhongBan, NgayVaoLam):
    global _id_counter, mock_db

    nv = {
        "NhanVienID": _id_counter,
        "HoTen": nhap_chuoi(HoTen),
        "NgaySinh": str(nhap_ngay(NgaySinh)),
        "GioiTinh": nhap_chuoi(GioiTinh),
        "DiaChi": nhap_chuoi(DiaChi),
        "SoDienThoai": nhap_sdt(SoDienThoai),
        "Email": nhap_email(Email),
        "ChucVu": nhap_chuoi(ChucVu),
        "PhongBan": nhap_chuoi(PhongBan),
        "NgayVaoLam": str(nhap_ngay(NgayVaoLam))
    }
    mock_db.append(nv)
    _id_counter += 1
    return nv

def cap_nhat_nhan_vien(nhanvien_id, field, new_value):
    global mock_db

    for nv in mock_db:
        if nv["NhanVienID"] == nhanvien_id:
            if field not in nv:
                raise ValueError("Trường không tồn tại.")
            if not new_value or str(new_value).strip() == "":
                raise ValueError("Giá trị cập nhật không được để trống.")
            nv[field] = new_value
            return nv

    raise ValueError("Không tìm thấy nhân viên.")

def xoa_nhan_vien(nhanvien_id):
    global mock_db
    for nv in mock_db:
        if nv["NhanVienID"] == nhanvien_id:
            mock_db.remove(nv)
            return True
    raise ValueError("Không tìm thấy nhân viên.")

# ===== Reset cho test =====
def reset_db():
    global mock_db, _id_counter
    mock_db = []
    _id_counter = 1