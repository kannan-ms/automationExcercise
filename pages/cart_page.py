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

    def is_blue_top_visible(self):
        return self.is_visible(self.BLUE_TOP_ROW)

    def get_blue_top_name(self):
        return self.get_text(self.BLUE_TOP_NAME)

    def get_blue_top_quantity(self):
        return self.get_text(self.BLUE_TOP_QUANTITY)