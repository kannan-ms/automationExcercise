from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config import BASE_URL

#all the functions are come under the category of the HomePage Class
class HomePage(BasePage):
    LOGO = (By.XPATH, "//img[@alt='Website for automation practice']")
    PRODUCTS_LINK = (By.XPATH, "//a[@href='/products']")
    SIGNUP_LOGIN_LINK = (By.XPATH, "//a[@href='/login']")

    def open_home_page(self):
        self.open_url(BASE_URL)

    def is_logo_visible(self):
        return self.is_visible(self.LOGO)

    def go_to_products_page(self):
        self.click(self.PRODUCTS_LINK)

    def go_to_login_page(self):
        self.click(self.SIGNUP_LOGIN_LINK)