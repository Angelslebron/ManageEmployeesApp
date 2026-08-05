import uuid

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.pages.login_page import LoginPage
from tests.pages.employee_page import EmployeePage


def test_delete_employee_cancel(driver):

    login_page = LoginPage(driver)
    employee_page = EmployeePage(driver)

    login_page.open()

    login_page.login(
        "admin",
        "Admin123!"
    )

    assert "/dashboard" in driver.current_url

    unique_email = (
        f"cancel.delete.{uuid.uuid4().hex[:8]}@test.com"
    )

    employee_page.open_create()

    employee_page.fill_employee(
        "Cancel",
        "Test",
        unique_email,
        "QA Tester",
        "2500"
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

    employee_row = None

    for row in rows:

        if "Cancel Test" in row.text:

            employee_row = row
            break

    assert employee_row is not None

    delete_form = employee_row.find_element(
        By.CSS_SELECTOR,
        "form"
    )

    delete_button = delete_form.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']"
    )

    delete_button.click()

    WebDriverWait(driver, 5).until(
        EC.alert_is_present()
    )

    alert = driver.switch_to.alert

    alert.dismiss()

    assert "/employees/" in driver.current_url

    body = driver.find_element(
        By.TAG_NAME,
        "body"
    ).text

    assert "Cancel Test" in body
