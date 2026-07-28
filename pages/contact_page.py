from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class ContactPage(BasePage):
    CONTACT_US_HEADING = (By.XPATH, "//h2[contains(.,'Contact Us')]")
    GET_IN_TOUCH_TEXT = (By.XPATH, "//h2[contains(.,'Get In Touch')]")
    NAME_INPUT = (By.CSS_SELECTOR, "[data-qa='name']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "[data-qa='email']")
    SUBJECT_INPUT = (By.CSS_SELECTOR, "[data-qa='subject']")
    MESSAGE_INPUT = (By.CSS_SELECTOR, "[data-qa='message']")
    FILE_INPUT = (By.CSS_SELECTOR, "input[name='upload_file']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[data-qa='submit-button']")
    SUCCESS_MESSAGE = (By.XPATH, "//*[contains(text(),'Success! Your details have been submitted successfully.')]")

    def is_contact_us_visible(self):
        return self.is_visible(self.CONTACT_US_HEADING)

    def is_get_in_touch_visible(self):
        return self.is_visible(self.GET_IN_TOUCH_TEXT)

    def fill_contact_form(self, name, email, subject, message, file_path=None):
        self.type_text(self.NAME_INPUT, name)
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.SUBJECT_INPUT, subject)
        self.type_text(self.MESSAGE_INPUT, message)

        if file_path:
            self.driver.find_element(*self.FILE_INPUT).send_keys(file_path)

    def submit_contact_form(self):
        self.js_click(self.SUBMIT_BUTTON)

    def get_submission_message(self):
        try:
            alert = WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            message = alert.text
            alert.accept()
            return message
        except TimeoutException:
            if self.driver.find_elements(*self.SUCCESS_MESSAGE):
                return self.get_text(self.SUCCESS_MESSAGE)

        return ""