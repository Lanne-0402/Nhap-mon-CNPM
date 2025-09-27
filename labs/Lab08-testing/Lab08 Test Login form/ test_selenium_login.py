import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "http://127.0.0.1:5500/index.html"

def make_driver(headless=False):
    opts = ChromeOptions()
    if headless:
        opts.add_argument("--headless=new")
    # Nếu dùng Chrome portable, mở dòng dưới và sửa đường dẫn:
    # opts.binary_location = r"C:\browsers\chrome\chrome.exe"
    return webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=opts
    )

@pytest.fixture
def browser():
    driver = make_driver(headless=False)
    yield driver
    driver.quit()

def wait_visible(browser, locator, timeout=5):
    return WebDriverWait(browser, timeout).until(
        EC.visibility_of_element_located(locator)
    )

def click_login(browser, timeout=5):
    """Bấm nút submit của form login (không cần id loginBtn)."""
    btn = WebDriverWait(browser, timeout).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "form#loginForm button[type='submit']"))
    )
    btn.click()

def test_login_success(browser):
    browser.get(BASE_URL)
    # đảm bảo form đã render
    wait_visible(browser, (By.ID, "loginForm"))
    browser.find_element(By.ID, "username").send_keys("nv001")
    browser.find_element(By.ID, "password").send_keys("123456")
    click_login(browser)
    msg = wait_visible(browser, (By.ID, "formMsg")).text
    assert "Đăng nhập thành công" in msg

def test_login_fail(browser):
    browser.get(BASE_URL)
    wait_visible(browser, (By.ID, "loginForm"))
    browser.find_element(By.ID, "username").send_keys("nv001")
    browser.find_element(By.ID, "password").send_keys("sai_mat_khau")
    click_login(browser)
    msg = wait_visible(browser, (By.ID, "formMsg")).text
    assert "Sai username hoặc password." in msg

def test_cancel_clears_form(browser):
    browser.get(BASE_URL)
    wait_visible(browser, (By.ID, "loginForm"))
    u = browser.find_element(By.ID, "username")
    p = browser.find_element(By.ID, "password")
    u.send_keys("abc")
    p.send_keys("xyz")
    browser.find_element(By.ID, "btnCancel").click()
    msg = wait_visible(browser, (By.ID, "formMsg")).text
    assert "Đã xóa dữ liệu nhập." in msg
    assert browser.find_element(By.ID, "username").get_attribute("value") == ""
    assert browser.find_element(By.ID, "password").get_attribute("value") == ""

def test_remember_me_localstorage(browser):
    browser.get(BASE_URL)
    wait_visible(browser, (By.ID, "loginForm"))
    browser.find_element(By.ID, "username").clear()
    browser.find_element(By.ID, "username").send_keys("hr01")
    browser.find_element(By.ID, "password").send_keys("sai1")
    browser.find_element(By.ID, "remember").click()
    click_login(browser)
    browser.refresh()
    wait_visible(browser, (By.ID, "username"))
    saved = browser.find_element(By.ID, "username").get_attribute("value")
    assert saved == "hr01"

def test_toggle_password_visibility(browser):
    browser.get(BASE_URL)
    wait_visible(browser, (By.ID, "loginForm"))
    pwd = browser.find_element(By.ID, "password")
    toggle = browser.find_element(By.ID, "togglePwd")
    assert pwd.get_attribute("type") == "password"
    toggle.click()
    assert pwd.get_attribute("type") == "text"
    toggle.click()
    assert pwd.get_attribute("type") == "password"

