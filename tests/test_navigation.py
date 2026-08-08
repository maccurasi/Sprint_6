import allure

from data import BASE_URL
from pages.header import Header


@allure.feature("Навигация по логотипам")
class TestHeaderNavigation:
    @allure.title("Логотип Самоката возвращает на главную страницу")
    def test_scooter_logo_opens_home_page(self, driver):
        header = Header(driver)
        header.open(f"{BASE_URL}order")
        header.click_scooter_logo()
        assert header.current_url_is(BASE_URL)

    @allure.title("Логотип Яндекса открывает Дзен в новом окне")
    def test_yandex_logo_opens_dzen_in_new_window(self, driver):
        header = Header(driver)
        header.open(BASE_URL)
        header.click_yandex_logo_and_switch()
        assert header.current_url_contains("dzen.ru")
