import pytest
import mock_module as mock

def test_them_nhan_vien():
    nv = mock.them_nhan_vien(
        "Nguyen Van A", "1995-01-01", "Nam",
        "Ha Noi", "0912345678", "a@gmail.com",
        "Dev", "IT", "2020-01-01"
    )
    assert nv["NhanVienID"] == 1
    assert nv["HoTen"] == "Nguyen Van A"
    assert len(mock.xem_danh_sach()) == 1

def test_cap_nhat_nhan_vien():
    nv = mock.cap_nhat_nhan_vien(1, "DiaChi", "Sai Gon")
    assert nv["DiaChi"] == "Sai Gon"

def test_xoa_nhan_vien():
    result = mock.xoa_nhan_vien(1)
    assert result is True
    assert len(mock.xem_danh_sach()) == 0

# ===== Kiểm tra lỗi nhập liệu =====
def test_ngay_sai():
    with pytest.raises(ValueError):
        mock.nhap_ngay("2025-02-30")

def test_email_sai():
    with pytest.raises(ValueError):
        mock.nhap_email("abc.com")

def test_sdt_sai():
    with pytest.raises(ValueError):
        mock.nhap_sdt("12ab")

def test_chuoi_trong():
    with pytest.raises(ValueError):
        mock.nhap_chuoi("   ")
