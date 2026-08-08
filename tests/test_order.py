import allure
import pytest

from data import BASE_URL, ORDERS
from pages.customer_details_page import CustomerDetailsPage
from pages.home_page import HomePage
from pages.rental_details_page import RentalDetailsPage


@allure.feature("Заказ самоката")
class TestOrder:
    @pytest.mark.smoke
    @pytest.mark.parametrize("order", ORDERS, ids=("top-black", "bottom-grey"))
    @allure.title("Успешный заказ, точка входа: {order[entry]}")
    def test_successful_order(self, driver, order):
        home = HomePage(driver)
        home.open(BASE_URL)
        home.accept_cookies()
        home.start_order(order["entry"])

        customer = CustomerDetailsPage(driver)
        customer.fill_customer_details(order)
        customer.click_next_button()

        rental = RentalDetailsPage(driver)
        rental.fill_rental_details(order)
        rental.submit_order()

        assert rental.is_success_modal_displayed()
