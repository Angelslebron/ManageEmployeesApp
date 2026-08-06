from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    URL = "http://127.0.0.1:8000/login"

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.ID, "login-error")

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            10
        )

    def open(self):

        self.driver.get(self.URL)

    def enter_username(self, username):

        username_input = self.wait.until(
            EC.visibility_of_element_located(
                self.USERNAME_INPUT
            )
        )

        username_input.clear()
        username_input.send_keys(username)

    def enter_password(self, password):

        password_input = self.wait.until(
            EC.visibility_of_element_located(
                self.PASSWORD_INPUT
            )
        )

        password_input.clear()
        password_input.send_keys(password)

    def click_login(self):

        login_button = self.wait.until(
            EC.element_to_be_clickable(
                self.LOGIN_BUTTON
            )
        )

        login_button.click()

    def login(self, username, password):

        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.ERROR_MESSAGE
            )
        ).text