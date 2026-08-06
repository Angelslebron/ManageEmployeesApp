from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.pages.edit_employee_page import EditEmployeePage
from tests.pages.employee_page import EmployeePage
from tests.pages.login_page import LoginPage
from tests.utils.employee_factory import create_employee_data


def test_update_employee_duplicate_email(driver):
    login_page = LoginPage(driver)
    employee_page = EmployeePage(driver)
    edit_page = EditEmployeePage(driver)
    wait = WebDriverWait(driver, 10)

    login_page.open()
    login_page.login(
        "admin",
        "Admin123!",
    )

    wait.until(
        EC.url_contains("/dashboard")
    )

    employee_one = create_employee_data(
        first_name="Natalia",
        last_name="Rivera",
        position="QA Analyst",
        salary="2900",
    )

    employee_two = create_employee_data(
        first_name="Sebastian",
        last_name="Morales",
        position="Software Developer",
        salary="3700",
    )

    for employee in (
        employee_one,
        employee_two,
    ):
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

    employee_page.open_list()

    employee_one_id = (
        employee_page.get_employee_id_by_email(
            employee_one.email
        )
    )

    assert employee_one_id is not None

    edit_page.open(employee_one_id)

    wait.until(
        EC.url_contains(
            f"/employees/{employee_one_id}/edit"
        )
    )

    edit_page.update_employee(
        employee_one.first_name,
        employee_one.last_name,
        employee_two.email,
        "Senior QA Engineer",
        "3800",
    )

    edit_page.submit()

    error_message = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "error-message")
        )
    )

    assert (
        f"/employees/{employee_one_id}/edit"
        in driver.current_url
    )

    assert "already exists" in error_message.text