import uuid

from tests.pages.login_page import LoginPage
from tests.pages.employee_page import EmployeePage


def test_create_employee_happy(driver):

    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(
        "admin",
        "Admin123!"
    )

    assert "/dashboard" in driver.current_url

    employee_page = EmployeePage(driver)

    employee_page.open_create()

    unique_email = (
        f"john.selenium.{uuid.uuid4().hex[:8]}@test.com"
    )

    employee_page.fill_employee(
        "John",
        "Selenium",
        unique_email,
        "QA Tester",
        "2500"
    )

    employee_page.submit()

    assert "/dashboard" in driver.current_url
