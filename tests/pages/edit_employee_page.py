from selenium.webdriver.common.by import By


class EditEmployeePage:

    FIRST_NAME = (
        By.ID,
        "first_name"
    )

    LAST_NAME = (
        By.ID,
        "last_name"
    )

    EMAIL = (
        By.ID,
        "email"
    )

    POSITION = (
        By.ID,
        "position"
    )

    SALARY = (
        By.ID,
        "salary"
    )

    UPDATE_BUTTON = (
        By.CSS_SELECTOR,
        "button[type='submit']"
    )

    ERROR_MESSAGE = (
        By.CLASS_NAME,
        "error-message"
    )

    def __init__(self, driver):

        self.driver = driver

    def open(self, employee_id):

        self.driver.get(
            f"http://127.0.0.1:8000/employees/{employee_id}/edit"
        )

    def update_employee(
        self,
        first_name,
        last_name,
        email,
        position,
        salary
    ):

        self.driver.find_element(
            *self.FIRST_NAME
        ).clear()

        self.driver.find_element(
            *self.FIRST_NAME
        ).send_keys(first_name)

        self.driver.find_element(
            *self.LAST_NAME
        ).clear()

        self.driver.find_element(
            *self.LAST_NAME
        ).send_keys(last_name)

        self.driver.find_element(
            *self.EMAIL
        ).clear()

        self.driver.find_element(
            *self.EMAIL
        ).send_keys(email)

        self.driver.find_element(
            *self.POSITION
        ).clear()

        self.driver.find_element(
            *self.POSITION
        ).send_keys(position)

        self.driver.find_element(
            *self.SALARY
        ).clear()

        self.driver.find_element(
            *self.SALARY
        ).send_keys(salary)

    def submit(self):

        self.driver.find_element(
            *self.UPDATE_BUTTON
        ).click()
