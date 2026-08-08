import allure

from locators.rental_details_page import RentalDetailsPageLocators
from pages.base_page import BasePage


class RentalDetailsPage(BasePage):
    @allure.step("Заполнить условия аренды")
    def fill_rental_details(self, order):
        self.click(RentalDetailsPageLocators.DATE)
        self.click(RentalDetailsPageLocators.AVAILABLE_DAY)
        self.click(RentalDetailsPageLocators.PERIOD)
        self.click(RentalDetailsPageLocators.rental_period(order["period"]))
        self.click(RentalDetailsPageLocators.scooter_colour(order["colour"]))
        self.type(RentalDetailsPageLocators.COMMENT, order["comment"])

    @allure.step("Отправить и подтвердить заказ")
    def submit_order(self):
        self.click(RentalDetailsPageLocators.ORDER)
        self.click(RentalDetailsPageLocators.CONFIRM)

    def is_success_modal_displayed(self):
        return self.is_visible(RentalDetailsPageLocators.SUCCESS_MODAL_HEADER)

    def success_message(self):
        return self.text(RentalDetailsPageLocators.SUCCESS_MODAL_HEADER)
