from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config import BASE_URL

#all the functions are come under the category of the HomePage Class
class HomePage(BasePage):
    LOGO = (By.XPATH, "//img[@alt='Website for automation practice']")
    PRODUCTS_LINK = (By.XPATH, "//a[@href='/products']")
    SIGNUP_LOGIN_LINK = (By.XPATH, "//a[@href='/login']")
    CART_LINK = (By.XPATH, "//a[@href='/view_cart']")
    CONTACT_US_LINK = (By.XPATH, "//a[@href='/contact_us']")
    SUBSCRIPTION_EMAIL = (By.ID, "susbscribe_email")
    SUBSCRIBE_BUTTON = (By.ID, "subscribe")
    SUBSCRIPTION_SUCCESS_MESSAGE = (By.XPATH, "//div[@id='success-subscribe']//div[contains(@class,'alert-success')]")

    def open_home_page(self):
        self.open_url(BASE_URL)

    def is_logo_visible(self):
        return self.is_visible(self.LOGO)

    def go_to_products_page(self):
        self.click(self.PRODUCTS_LINK)

    def go_to_login_page(self):
        self.click(self.SIGNUP_LOGIN_LINK)

    def go_to_cart_page(self):
        self.click(self.CART_LINK)

    def go_to_contact_page(self):
        self.click(self.CONTACT_US_LINK)

    def scroll_to_footer(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def subscribe(self, email):
        self.scroll_to_footer()
        self.type_text(self.SUBSCRIPTION_EMAIL, email)
        self.js_click(self.SUBSCRIBE_BUTTON)

    def get_subscription_success_message(self):
        return self.get_text(self.SUBSCRIPTION_SUCCESS_MESSAGE)

    def is_subscription_success_visible(self):
        return self.is_visible(self.SUBSCRIPTION_SUCCESS_MESSAGE)