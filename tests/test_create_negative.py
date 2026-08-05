from tests.pages.login_page import LoginPage
from tests.pages.employee_page import EmployeePage


def test_create_employee_duplicate_email(driver):

    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(
        "admin",
        "Admin123!"
    )

    assert "/dashboard" in driver.current_url

    employee_page = EmployeePage(driver)

    employee_page.open_create()

    employee_page.fill_employee(
        "John",
        "Duplicate",
        "john.selenium@test.com",
        "QA Tester",
        "2500"
    )

    employee_page.submit()

    assert "/employees/" in driver.current_url

    error_message = driver.find_element(
        "class name",
        "error-message"
    )

    assert "already exists" in error_message.text