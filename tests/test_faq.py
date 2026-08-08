import allure
import pytest

from data import BASE_URL, FAQ_ANSWERS
from pages.home_page import HomePage


@allure.feature("Вопросы о важном")
class TestFaq:
    @pytest.mark.parametrize(
        "index, expected",
        list(enumerate(FAQ_ANSWERS)),
        ids=[f"faq-{number}" for number in range(1, len(FAQ_ANSWERS) + 1)],
    )
    @allure.title("Ответ FAQ №{index} соответствует вопросу")
    def test_faq_answer_opens(self, driver, index, expected):
        page = HomePage(driver)
        page.open(BASE_URL)
        page.accept_cookies()
        page.open_faq(index)
        assert page.get_faq_answer(index) == expected
