from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.pages.employee_page import EmployeePage
from tests.pages.login_page import LoginPage
from tests.utils.employee_factory import create_employee_data


def test_delete_employee_happy(driver):
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
        first_name="Mateo",
        last_name="Herrera",
        position="Support Specialist",
        salary="2800",
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

    rows = driver.find_elements(
        By.CSS_SELECTOR,
        "tbody tr",
    )

    employee_row = None

    for row in rows:
        if employee.email in row.text:
            employee_row = row
            break

    assert employee_row is not None, (
        f"Employee with email {employee.email} "
        "was not found."
    )

    delete_button = employee_row.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']",
    )

    delete_button.click()

    wait.until(
        EC.alert_is_present()
    )

    driver.switch_to.alert.accept()

    wait.until(
        EC.url_contains("/employees/")
    )

    wait.until_not(
        EC.text_to_be_present_in_element(
            (By.TAG_NAME, "body"),
            employee.email,
        )
    )

    body = driver.find_element(
        By.TAG_NAME,
        "body",
    ).text

    assert employee.email not in body