from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_EMAIL = (By.XPATH, "//input[@data-qa='login-email']")
    LOGIN_PASSWORD = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")
    LOGIN_ERROR = (By.XPATH, "//p[contains(text(),'Your email or password is incorrect!')]")

    def login(self, email, password):
        self.type_text(self.LOGIN_EMAIL, email)
        self.type_text(self.LOGIN_PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.LOGIN_ERROR)