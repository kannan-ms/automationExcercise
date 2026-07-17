from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    BLUE_TOP_ROW = (By.XPATH, "//tr[contains(@id, 'product-1')]")
    BLUE_TOP_NAME = (
        By.XPATH,
        "//tr[contains(@id, 'product-1')]//td[contains(@class, 'cart_description')]//a"
    )
    BLUE_TOP_QUANTITY = (
        By.XPATH,
        "//tr[contains(@id, 'product-1')]//td[contains(@class, 'cart_quantity')]//button"
    )
    CART_ROWS = (By.CSS_SELECTOR, "tr[id^='product-']")
    BLUE_TOP_REMOVE = (By.CSS_SELECTOR, "tr#product-1 a.cart_quantity_delete")
    EMPTY_CART_TEXT = (By.XPATH, "//p[contains(text(),'Cart is empty!')]")

    def is_blue_top_visible(self):
        return self.is_visible(self.BLUE_TOP_ROW)

    def get_blue_top_name(self):
        return self.get_text(self.BLUE_TOP_NAME)

    def get_blue_top_quantity(self):
        return self.get_text(self.BLUE_TOP_QUANTITY)

    def get_cart_items_count(self):
        return len(self.driver.find_elements(*self.CART_ROWS))

    def remove_blue_top(self):
        self.click(self.BLUE_TOP_REMOVE)

    def wait_until_blue_top_removed(self):
        return self.wait_until_invisible(self.BLUE_TOP_ROW)

    def is_empty_cart_message_visible(self):
        elements = self.driver.find_elements(*self.EMPTY_CART_TEXT)
        return bool(elements) and elements[0].is_displayed()
    #here i'm add something like a command to make some changes in the project code