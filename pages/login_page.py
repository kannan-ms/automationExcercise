from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_EMAIL = (By.XPATH, "//input[@data-qa='login-email']")
    LOGIN_PASSWORD = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")
    LOGIN_ERROR = (By.XPATH, "//p[contains(text(),'Your email or password is incorrect!')]")
    LOGGED_IN_TEXT = (By.XPATH, "//a[contains(text(),'Logged in as')]")
    LOGOUT_LINK = (By.XPATH, "//a[@href='/logout']")
    LOGIN_TO_ACCOUNT_TEXT = (By.XPATH, "//h2[contains(text(),'Login to your account')]")
    SIGNUP_NAME = (By.XPATH, "//input[@data-qa='signup-name']")
    SIGNUP_EMAIL = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")
    ACCOUNT_INFO_TEXT = (By.XPATH, "//b[contains(text(),'Enter Account Information')]")
    GENDER_MALE = (By.ID, "id_gender1")
    PASSWORD = (By.XPATH, "//input[@data-qa='password']")
    DAYS = (By.ID, "days")
    MONTHS = (By.ID, "months")
    YEARS = (By.ID, "years")
    FIRST_NAME = (By.XPATH, "//input[@data-qa='first_name']")
    LAST_NAME = (By.XPATH, "//input[@data-qa='last_name']")
    COMPANY = (By.XPATH, "//input[@data-qa='company']")
    ADDRESS1 = (By.XPATH, "//input[@data-qa='address']")
    ADDRESS2 = (By.XPATH, "//input[@data-qa='address2']")
    COUNTRY = (By.XPATH, "//select[@data-qa='country']")
    STATE = (By.XPATH, "//input[@data-qa='state']")
    CITY = (By.XPATH, "//input[@data-qa='city']")
    ZIPCODE = (By.XPATH, "//input[@data-qa='zipcode']")
    MOBILE_NUMBER = (By.XPATH, "//input[@data-qa='mobile_number']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@data-qa='create-account']")
    ACCOUNT_CREATED_TEXT = (By.XPATH, "//b[contains(text(),'Account Created!')]")
    CONTINUE_BUTTON = (By.XPATH, "//a[@data-qa='continue-button']")

    def login(self, email, password):
        self.type_text(self.LOGIN_EMAIL, email)
        self.type_text(self.LOGIN_PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.LOGIN_ERROR)

    def get_logged_in_text(self):
        return self.get_text(self.LOGGED_IN_TEXT)

    def logout(self):
        self.click(self.LOGOUT_LINK)

    def is_logout_visible(self):
        return self.is_visible(self.LOGOUT_LINK)

    def is_login_form_visible(self):
        return self.is_visible(self.LOGIN_TO_ACCOUNT_TEXT)

    def register_user(self, user_data):
        self.type_text(self.SIGNUP_NAME, user_data["name"])
        self.type_text(self.SIGNUP_EMAIL, user_data["email"])
        self.click(self.SIGNUP_BUTTON)

        self.is_visible(self.ACCOUNT_INFO_TEXT)
        self.click(self.GENDER_MALE)
        self.type_text(self.PASSWORD, user_data["password"])
        self.select_by_visible_text(self.DAYS, "1")
        self.select_by_visible_text(self.MONTHS, "January")
        self.select_by_visible_text(self.YEARS, "1999")

        self.type_text(self.FIRST_NAME, user_data["first_name"])
        self.type_text(self.LAST_NAME, user_data["last_name"])
        self.type_text(self.COMPANY, user_data["company"])
        self.type_text(self.ADDRESS1, user_data["address1"])
        self.type_text(self.ADDRESS2, user_data["address2"])
        self.select_by_visible_text(self.COUNTRY, user_data["country"])
        self.type_text(self.STATE, user_data["state"])
        self.type_text(self.CITY, user_data["city"])
        self.type_text(self.ZIPCODE, user_data["zipcode"])
        self.type_text(self.MOBILE_NUMBER, user_data["mobile_number"])
        self.click(self.CREATE_ACCOUNT_BUTTON)

        self.is_visible(self.ACCOUNT_CREATED_TEXT)
        self.click(self.CONTINUE_BUTTON)

    def is_logged_in(self):
        return self.is_visible(self.LOGGED_IN_TEXT)