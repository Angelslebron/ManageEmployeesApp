import os

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():

    options = Options()

    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        options=options
    )

    yield driver

    driver.quit()


@pytest.fixture
def screenshot(driver):

    def capture(name):

        os.makedirs(
            "screenshots",
            exist_ok=True
        )

        path = os.path.join(
            "screenshots",
            f"{name}.png"
        )

        driver.save_screenshot(path)

    return capture