import allure

from locators.header import HeaderLocators
from pages.base_page import BasePage


class Header(BasePage):
    @allure.step("Нажать логотип Самоката")
    def click_scooter_logo(self):
        self.click(HeaderLocators.SCOOTER_LOGO)

    @allure.step("Нажать логотип Яндекса и перейти в новое окно")
    def click_yandex_logo_and_switch(self):
        self.click_and_switch_to_new_window(HeaderLocators.YANDEX_LOGO)
