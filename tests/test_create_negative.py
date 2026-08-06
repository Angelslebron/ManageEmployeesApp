from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.pages.employee_page import EmployeePage
from tests.pages.login_page import LoginPage
from tests.utils.employee_factory import create_employee_data


def test_create_employee_duplicate_email(driver):
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

    existing_employee = create_employee_data(
        first_name="Daniel",
        last_name="Reyes",
        position="Backend Developer",
        salary="3500",
    )

    employee_page.open_create()

    employee_page.fill_employee(
        existing_employee.first_name,
        existing_employee.last_name,
        existing_employee.email,
        existing_employee.position,
        existing_employee.salary,
    )

    employee_page.submit()

    wait.until(
        EC.url_contains("/dashboard")
    )

    duplicate_employee = create_employee_data(
        first_name="Camila",
        last_name="Fernandez",
        position="Product Analyst",
        salary="3300",
    )

    employee_page.open_create()

    employee_page.fill_employee(
        duplicate_employee.first_name,
        duplicate_employee.last_name,
        existing_employee.email,
        duplicate_employee.position,
        duplicate_employee.salary,
    )

    employee_page.submit()

    error_message = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "error-message")
        )
    )

    assert "/employees/" in driver.current_url
    assert "already exists" in error_message.text