from selenium.webdriver.common.by import By


class HomePageLocators:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    TOP_ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']",
    )
    BOTTOM_ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'Home_FinishButton')]//button[text()='Заказать']",
    )

    @staticmethod
    def faq_question(index):
        return By.ID, f"accordion__heading-{index}"

    @staticmethod
    def faq_answer(index):
        return By.ID, f"accordion__panel-{index}"
