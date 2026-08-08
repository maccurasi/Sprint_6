from selenium.webdriver.common.by import By


class RentalDetailsPageLocators:
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    AVAILABLE_DAY = (
        By.CSS_SELECTOR,
        ".react-datepicker__day:not(.react-datepicker__day--disabled)"
        ":not(.react-datepicker__day--outside-month)",
    )
    PERIOD = (By.CLASS_NAME, "Dropdown-control")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER = (
        By.XPATH,
        "//div[contains(@class,'Order_Buttons')]//button[text()='Заказать']",
    )
    CONFIRM = (
        By.XPATH,
        "//div[contains(@class,'Order_Modal')]//button[text()='Да']",
    )
    SUCCESS_MODAL_HEADER = (By.CSS_SELECTOR, "div[class*='Order_ModalHeader']")

    @staticmethod
    def rental_period(period):
        return (
            By.XPATH,
            f"//div[contains(@class,'Dropdown-option') and text()='{period}']",
        )

    @staticmethod
    def scooter_colour(colour):
        return By.ID, colour
