from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.pages.employee_page import EmployeePage
from tests.pages.login_page import LoginPage
from tests.utils.employee_factory import create_employee_data


def test_create_employee_minimum_salary(driver):
    login_page = LoginPage(driver)
    employee_page = EmployeePage(driver)
    wait = WebDriverWait(driver, 10)

    login_page.open()

    login_page.login(
        "admin",
        "Admin123!",
    )

    wait.until(
        EC.url_contains("/dashboard")
    )

    employee = create_employee_data(
        first_name="Sofia",
        last_name="Castillo",
        position="QA Analyst",
        salary="0.01",
    )

    employee_page.open_create()

    employee_page.fill_employee(
        employee.first_name,
        employee.last_name,
        employee.email,
        employee.position,
        employee.salary,
    )

    employee_page.submit()

    wait.until(
        EC.url_contains("/dashboard")
    )

    assert "/dashboard" in driver.current_url