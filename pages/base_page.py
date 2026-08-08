import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Базовые действия, общие для всех страниц сервиса."""

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def text(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator)).text

    def click_if_visible(self, locator):
        elements = self.driver.find_elements(*locator)
        if elements and elements[0].is_displayed():
            elements[0].click()

    def scroll_to(self, locator):
        element = self.wait.until(ec.presence_of_element_located(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element,
        )

    def click_via_javascript(self, locator):
        element = self.wait.until(ec.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def click_and_switch_to_new_window(self, locator):
        old_windows = set(self.driver.window_handles)
        self.click(locator)
        self.wait.until(ec.new_window_is_opened(old_windows))
        new_window = (set(self.driver.window_handles) - old_windows).pop()
        self.driver.switch_to.window(new_window)

    def current_url_is(self, expected_url, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(ec.url_to_be(expected_url))
            return True
        except TimeoutException:
            return False

    def current_url_contains(self, fragment, timeout=20):
        try:
            WebDriverWait(self.driver, timeout).until(ec.url_contains(fragment))
            return True
        except TimeoutException:
            return False

    def is_visible(self, locator):
        try:
            self.wait.until(ec.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
