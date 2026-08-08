import allure

from locators.customer_details_page import CustomerDetailsPageLocators
from pages.base_page import BasePage


class CustomerDetailsPage(BasePage):
    @allure.step("Заполнить данные заказчика")
    def fill_customer_details(self, order):
        self.type(CustomerDetailsPageLocators.FIRST_NAME, order["first_name"])
        self.type(CustomerDetailsPageLocators.LAST_NAME, order["last_name"])
        self.type(CustomerDetailsPageLocators.ADDRESS, order["address"])
        self.type(CustomerDetailsPageLocators.METRO, order["metro"])
        self.click(CustomerDetailsPageLocators.metro_station(order["metro"]))
        self.type(CustomerDetailsPageLocators.PHONE, order["phone"])

    @allure.step("Перейти к условиям аренды")
    def click_next_button(self):
        self.click(CustomerDetailsPageLocators.NEXT)
