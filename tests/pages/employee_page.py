from selenium.webdriver.common.by import By


class EmployeePage:

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

    CREATE_BUTTON = (
        By.CSS_SELECTOR,
        "button[type='submit']"
    )

    def __init__(self, driver):

        self.driver = driver

    def open_create(self):

        self.driver.get(
            "http://127.0.0.1:8000/employees/create"
        )

    def open_list(self):

        self.driver.get(
            "http://127.0.0.1:8000/employees/"
        )

    def fill_employee(
        self,
        first_name,
        last_name,
        email,
        position,
        salary
    ):

        self.driver.find_element(
            *self.FIRST_NAME
        ).send_keys(first_name)

        self.driver.find_element(
            *self.LAST_NAME
        ).send_keys(last_name)

        self.driver.find_element(
            *self.EMAIL
        ).send_keys(email)

        self.driver.find_element(
            *self.POSITION
        ).send_keys(position)

        self.driver.find_element(
            *self.SALARY
        ).send_keys(salary)

    def submit(self):

        self.driver.find_element(
            *self.CREATE_BUTTON
        ).click()

    def get_employee_id_by_email(self, email):

        rows = self.driver.find_elements(
            By.CSS_SELECTOR,
            "tbody tr"
        )

        for row in rows:

            if email in row.text:

                cells = row.find_elements(
                    By.TAG_NAME,
                    "td"
                )

                return cells[0].text

        return None
