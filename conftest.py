import os

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver():
    options = Options()
    if os.getenv("HEADLESS") == "1":
        options.add_argument("-headless")
    browser = webdriver.Firefox(options=options)
    browser.set_window_size(1440, 1000)
    yield browser
    if browser.session_id:
        allure.attach(
            browser.get_screenshot_as_png(),
            name="Последнее состояние страницы",
            attachment_type=allure.attachment_type.PNG,
        )
    browser.quit()
