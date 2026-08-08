from selenium.webdriver.common.by import By


class HeaderLocators:
    SCOOTER_LOGO = (By.CSS_SELECTOR, "a[class*='Header_LogoScooter']")
    YANDEX_LOGO = (By.CSS_SELECTOR, "a[class*='Header_LogoYandex']")
