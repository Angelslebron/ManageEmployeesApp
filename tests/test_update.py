from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.pages.edit_employee_page import EditEmployeePage
from tests.pages.employee_page import EmployeePage
from tests.pages.login_page import LoginPage
from tests.utils.employee_factory import create_employee_data


def test_update_employee_happy(driver):
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
        first_name="Valeria",
        last_name="Santos",
        position="QA Analyst",
        salary="2750",
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

    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "tbody tr")
        )
    )

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

    updated_position = "Senior QA Engineer"
    updated_salary = "3600"

    edit_page.update_employee(
        employee.first_name,
        employee.last_name,
        employee.email,
        updated_position,
        updated_salary,
    )

    edit_page.submit()

    wait.until(
        EC.url_contains("/employees/")
    )

    wait.until(
        EC.text_to_be_present_in_element(
            (By.TAG_NAME, "body"),
            updated_position,
        )
    )

    body = driver.find_element(
        By.TAG_NAME,
        "body",
    ).text

    assert employee.full_name in body
    assert employee.email in body
    assert updated_position in body