import pytest
import mock_module as mock

# ===== Fixture để reset dữ liệu trước mỗi test =====
@pytest.fixture(autouse=True)
def reset_data():
    mock.mock_db = []
    mock._id_counter = 1
    yield
    mock.mock_db = []
    mock._id_counter = 1


# ===== Test thêm nhân viên =====
def test_them_nhan_vien_hop_le():
    nv = mock.them_nhan_vien(
        "Nguyen Van A", "1995-01-01", "Nam",
        "Ha Noi", "0912345678", "a@gmail.com",
        "Dev", "IT", "2020-01-01"
    )
    assert nv["NhanVienID"] == 1
    assert nv["HoTen"] == "Nguyen Van A"
    assert len(mock.xem_danh_sach()) == 1

def test_them_nhan_vien_thieu_ten():
    with pytest.raises(ValueError):
        mock.them_nhan_vien(
            "", "1995-01-01", "Nam",
            "Ha Noi", "0912345678", "a@gmail.com",
            "Dev", "IT", "2020-01-01"
        )

# == Kiểm tra cập nhật nhân viên ==
def test_cap_nhat_nhan_vien_hop_le():
    nv = mock.them_nhan_vien("Nguyen Van A", "1995-01-01", "Nam",
                              "Ha Noi", "0912345678", "a@gmail.com",
                              "Dev", "IT", "2020-01-01")
    nv = mock.cap_nhat_nhan_vien(1, "DiaChi", "Sai Gon")
    assert nv["DiaChi"] == "Sai Gon"

def test_cap_nhat_nhan_vien_khong_ton_tai():
    with pytest.raises(ValueError):
        mock.cap_nhat_nhan_vien(999, "DiaChi", "Da Nang")

def test_cap_nhat_truong_khong_hop_le():
    nv = mock.them_nhan_vien("Nguyen Van A", "1995-01-01", "Nam",
                              "Ha Noi", "0912345678", "a@gmail.com",
                              "Dev", "IT", "2020-01-01")
    with pytest.raises(ValueError):
        mock.cap_nhat_nhan_vien(1, "SoThich", "Bong da")

def test_cap_nhat_gia_tri_trong():
    nv = mock.them_nhan_vien("Nguyen Van A", "1995-01-01", "Nam",
                              "Ha Noi", "0912345678", "a@gmail.com",
                              "Dev", "IT", "2020-01-01")
    with pytest.raises(ValueError):
        mock.cap_nhat_nhan_vien(1, "HoTen", "")

# == Kiểm tra xóa nhân viên ==
def test_xoa_nhan_vien():
    nv = mock.them_nhan_vien("Nguyen Van A", "1995-01-01", "Nam",
                              "Ha Noi", "0912345678", "a@gmail.com",
                              "Dev", "IT", "2020-01-01")
    result = mock.xoa_nhan_vien(1)
    assert result is True
    assert len(mock.xem_danh_sach()) == 0

def test_xoa_nhan_vien_khong_ton_tai():
    with pytest.raises(ValueError):
        mock.xoa_nhan_vien(999)

# ===== Kiểm tra ngày tháng =====
def test_ngay_hop_le():
    ngay = mock.nhap_ngay("2020-12-31")
    assert str(ngay) == "2020-12-31"

def test_ngay_sai_dinh_dang():
    with pytest.raises(ValueError):
        mock.nhap_ngay("2020/12/31")

def test_ngay_tuong_lai():
    with pytest.raises(ValueError):
        mock.nhap_ngay("2100-01-01")

# == kiểm tra email ==
def test_email_hop_le():
    email = mock.nhap_email("test@gmail.com")
    assert email == "test@gmail.com"

def test_email_thieu_a_cong():
    with pytest.raises(ValueError):
        mock.nhap_email("abc.com")

def test_email_sai_domain():
    with pytest.raises(ValueError):
        mock.nhap_email("abc@gmail")

def test_email_trong():
    with pytest.raises(ValueError):
        mock.nhap_email("")

# == kiểm tra số điện thoại ==
def test_sdt_hop_le():
    sdt = mock.nhap_sdt("0912345678")
    assert sdt == "0912345678"

def test_sdt_chua_chu():
    with pytest.raises(ValueError):
        mock.nhap_sdt("12ab")

def test_sdt_qua_ngan():
    with pytest.raises(ValueError):
        mock.nhap_sdt("123")

def test_sdt_qua_dai():
    with pytest.raises(ValueError):
        mock.nhap_sdt("012345678901234567890")

def test_sdt_ky_tu_dac_biet():
    with pytest.raises(ValueError):
        mock.nhap_sdt("0912-345-678")

# == kiểm tra chuỗi ==
def test_chuoi_hop_le():
    chuoi = mock.nhap_chuoi("Nguyen Van A")
    assert chuoi == "Nguyen Van A"

def test_chuoi_trong():
    with pytest.raises(ValueError):
        mock.nhap_chuoi("")

def test_chuoi_toan_khoang_trang():
    with pytest.raises(ValueError):
        mock.nhap_chuoi("   ")

def test_chuoi_co_khoang_trang_du():
    chuoi = mock.nhap_chuoi("   Le Diep   ")
    assert chuoi == "Le Diep"

def test_chuoi_chua_ky_tu_dac_biet():
    with pytest.raises(ValueError):
        mock.nhap_chuoi("Nguyen@VanA")

def test_chuoi_chua_so():
    with pytest.raises(ValueError):
        mock.nhap_chuoi("Nguyen123")
