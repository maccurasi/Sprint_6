import allure

from locators.home_page import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    @allure.step("Принять cookies, если баннер отображается")
    def accept_cookies(self):
        self.click_if_visible(HomePageLocators.COOKIE_BUTTON)

    @allure.step("Открыть ответ FAQ с индексом {index}")
    def open_faq(self, index):
        question = HomePageLocators.faq_question(index)
        self.scroll_to(question)
        # На учебном стенде декоративное изображение перекрывает accordion в Firefox.
        self.click_via_javascript(question)

    def get_faq_answer(self, index):
        return self.text(HomePageLocators.faq_answer(index))

    @allure.step("Начать заказ через точку входа: {entry}")
    def start_order(self, entry):
        locator = (
            HomePageLocators.TOP_ORDER_BUTTON
            if entry == "top"
            else HomePageLocators.BOTTOM_ORDER_BUTTON
        )
        if entry == "bottom":
            self.scroll_to(locator)
        self.click(locator)
