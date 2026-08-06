from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.pages.edit_employee_page import EditEmployeePage
from tests.pages.employee_page import EmployeePage
from tests.pages.login_page import LoginPage
from tests.utils.employee_factory import create_employee_data


def test_update_employee_zero_salary(driver):
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

    employee = create_employee_data(
        first_name="Lucia",
        last_name="Mendoza",
        position="Financial Analyst",
        salary="3200",
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

    employee_page.open_list()

    employee_id = (
        employee_page.get_employee_id_by_email(
            employee.email
        )
    )

    assert employee_id is not None

    edit_page.open(employee_id)

    wait.until(
        EC.url_contains(
            f"/employees/{employee_id}/edit"
        )
    )

    edit_page.update_employee(
        employee.first_name,
        employee.last_name,
        employee.email,
        "Senior Financial Analyst",
        "0",
    )

    edit_page.submit()

    salary_input = wait.until(
        EC.presence_of_element_located(
            (By.ID, "salary")
        )
    )

    validation_message = driver.execute_script(
        "return arguments[0].validationMessage;",
        salary_input,
    )

    assert (
        f"/employees/{employee_id}/edit"
        in driver.current_url
    )

    assert salary_input.get_attribute("value") == "0"
    assert validation_message 