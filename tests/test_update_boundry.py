import uuid

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.pages.login_page import LoginPage
from tests.pages.employee_page import EmployeePage
from tests.pages.edit_employee_page import EditEmployeePage

def test_update_employee_duplicate_email(driver):

    login_page = LoginPage(driver)
    employee_page = EmployeePage(driver)
    edit_page = EditEmployeePage(driver)

    login_page.open()

    login_page.login(
        "admin",
        "Admin123!"
    )

    assert "/dashboard" in driver.current_url

    email_one = (
        f"duplicate.one.{uuid.uuid4().hex[:8]}@test.com"
    )

    email_two = (
        f"duplicate.two.{uuid.uuid4().hex[:8]}@test.com"
    )

    employee_page.open_create()

    employee_page.fill_employee(
        "Employee",
        "One",
        email_one,
        "QA Tester",
        "2500"
    )

    employee_page.submit()

    WebDriverWait(driver, 5).until(
        EC.url_contains("/dashboard")
    )

    assert "/dashboard" in driver.current_url

    employee_page.open_create()

    employee_page.fill_employee(
        "Employee",
        "Two",
        email_two,
        "Developer",
        "3000"
    )

    employee_page.submit()

    WebDriverWait(driver, 5).until(
        EC.url_contains("/dashboard")
    )

    assert "/dashboard" in driver.current_url

    driver.get(
        "http://127.0.0.1:8000/employees/"
    )

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "tbody tr")
        )
    )

    rows = driver.find_elements(
        By.CSS_SELECTOR,
        "tbody tr"
    )

    employee_one_id = None

    for row in rows:

        if "Employee One" in row.text:

            employee_one_id = row.find_element(
                By.TAG_NAME,
                "td"
            ).text

            break

    assert employee_one_id is not None

    edit_page.open(employee_one_id)

    edit_page.update_employee(
        "Employee",
        "One",
        email_two,
        "Senior QA Tester",
        "3500"
    )

    edit_page.submit()

    assert f"/employees/{employee_one_id}/edit" in driver.current_url

    body = driver.find_element(
        By.TAG_NAME,
        "body"
    ).text

    assert "already exists" in body
