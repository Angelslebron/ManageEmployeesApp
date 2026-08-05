from tests.pages.login_page import LoginPage
from tests.pages.employee_page import EmployeePage


def test_create_employee_zero_salary(driver):

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
        "Boundary",
        "Test",
        "boundary.salary@test.com",
        "QA Tester",
        "0"
    )

    employee_page.submit()

    assert "/employees/" in driver.current_url