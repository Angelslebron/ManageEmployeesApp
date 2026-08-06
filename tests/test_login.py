from tests.pages.login_page import LoginPage


def test_open_application(driver):

    driver.get(
        "http://127.0.0.1:8000/login"
    )

    assert "Login" in driver.title


def test_happy(driver, screenshot):

    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(
        "admin",
        "Admin123!"
    )

    assert "/dashboard" in driver.current_url

    screenshot("login_happy")

def test_negative(driver, screenshot):

    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(
        "admin",
        "WrongPassword123!"
    )

    assert "/login" in driver.current_url

    assert (
        login_page.get_error_message()
        == "Invalid username or password."
    )

    screenshot("login_negative")

def test_boundary(driver, screenshot):

    login_page = LoginPage(driver)

    login_page.open()

    login_page.click_login()

    username_input = driver.find_element(
        *login_page.USERNAME_INPUT
    )

    password_input = driver.find_element(
        *login_page.PASSWORD_INPUT
    )

    assert username_input.get_attribute("value") == ""
    assert password_input.get_attribute("value") == ""

    assert username_input.get_attribute("required") is not None
    assert password_input.get_attribute("required") is not None

    screenshot("login_boundary")