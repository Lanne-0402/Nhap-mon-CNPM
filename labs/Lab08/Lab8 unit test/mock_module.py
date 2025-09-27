import re
from datetime import datetime

# CSDL giả lập 
mock_db = []
auto_id = 1

# ================== HÀM KIỂM TRA DỮ LIỆU ==================

def nhap_ngay(val: str):
    try:
        datetime.strptime(val, "%Y-%m-%d")
        return val
    except ValueError:
        raise ValueError("Ngày không hợp lệ. Định dạng đúng là YYYY-MM-DD.")

def nhap_email(val: str):
    if re.match(r"[^@]+@[^@]+\.[^@]+", val):
        return val
    else:
        raise ValueError("Email không hợp lệ.")

def nhap_sdt(val: str):
    if val.isdigit() and 9 <= len(val) <= 11:
        return val
    else:
        raise ValueError("Số điện thoại phải là số và có 9-11 ký tự.")

def nhap_chuoi(val: str):
    if val.strip():
        return val.strip()
    else:
        raise ValueError("Không được để trống.")

# ================== CÁC HÀM CRUD ==================

def xem_danh_sach():
    return mock_db

def them_nhan_vien(hoten, ngaysinh, gioitinh, diachi, sdt, email, vitri, phongban, ngayvaolam):
    global auto_id
    record = {
        "NhanVienID": auto_id,
        "HoTen": nhap_chuoi(hoten),
        "NgaySinh": nhap_ngay(ngaysinh),
        "GioiTinh": nhap_chuoi(gioitinh),
        "DiaChi": nhap_chuoi(diachi),
        "SoDienThoai": nhap_sdt(sdt),
        "Email": nhap_email(email),
        "ViTri": nhap_chuoi(vitri),
        "PhongBan": nhap_chuoi(phongban),
        "NgayVaoLam": nhap_ngay(ngayvaolam)
    }
    mock_db.append(record)
    auto_id += 1
    return record

def cap_nhat_nhan_vien(nhanvien_id, field, new_value):
    for nv in mock_db:
        if nv["NhanVienID"] == nhanvien_id:
            if field in nv:
                nv[field] = new_value
                return nv
            else:
                raise KeyError("Trường không tồn tại.")
    raise KeyError("Không tìm thấy nhân viên.")

def xoa_nhan_vien(nhanvien_id):
    global mock_db
    before = len(mock_db)
    mock_db = [nv for nv in mock_db if nv["NhanVienID"] != nhanvien_id]
    return len(mock_db) < before
