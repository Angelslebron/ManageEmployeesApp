import uuid

from tests.pages.login_page import LoginPage
from tests.pages.employee_page import EmployeePage
from tests.pages.edit_employee_page import EditEmployeePage


def test_update_employee_happy(driver):

    login_page = LoginPage(driver)
    employee_page = EmployeePage(driver)
    edit_page = EditEmployeePage(driver)

    login_page.open()

    login_page.login(
        "admin",
        "Admin123!"
    )

    assert "/dashboard" in driver.current_url

    unique_email = (
        f"update.{uuid.uuid4().hex[:8]}@test.com"
    )

    employee_page.open_create()

    employee_page.fill_employee(
        "John",
        "Original",
        unique_email,
        "QA Tester",
        "2500"
    )

    employee_page.submit()

    assert "/dashboard" in driver.current_url

    employee_page.open_list()

    employee_id = employee_page.get_employee_id_by_email(
        unique_email
    )

    assert employee_id is not None

    edit_page.open(employee_id)

    edit_page.update_employee(
        "John Updated",
        "Selenium",
        unique_email,
        "Senior QA Tester",
        "3000"
    )

    edit_page.submit()

    assert "/employees/" in driver.current_url

    body = driver.find_element(
        "tag name",
        "body"
    ).text

    assert "John Updated" in body
    assert unique_email in body
    assert "Senior QA Tester" in body
