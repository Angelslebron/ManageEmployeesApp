from tests.pages.login_page import LoginPage


def test_login_success(driver):

    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(
        "admin",
        "Admin123!"
    )

    assert "/dashboard" in driver.current_url