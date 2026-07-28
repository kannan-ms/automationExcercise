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
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//a[contains(@class,'check_out')]")
    CHECKOUT_MODAL = (By.ID, "checkoutModal")
    CHECKOUT_TITLE = (By.XPATH, "//div[@id='checkoutModal']//h4[contains(.,'Checkout')]")
    CHECKOUT_PROMPT = (
        By.XPATH,
        "//div[@id='checkoutModal']//p[contains(.,'Register / Login account to proceed on checkout.')]")
    CHECKOUT_LOGIN_LINK = (By.XPATH, "//div[@id='checkoutModal']//a[@href='/login']")
    CONTINUE_ON_CART_BUTTON = (By.XPATH, "//div[@id='checkoutModal']//button[contains(.,'Continue On Cart')]")

    def _row_by_product_name(self, product_name):
        return (
            By.XPATH,
            f"//tr[.//td[contains(@class, 'cart_description')]//a[normalize-space()='{product_name}']]"
        )

    def _name_cell_by_product_name(self, product_name):
        return (
            By.XPATH,
            f"//tr[.//td[contains(@class, 'cart_description')]//a[normalize-space()='{product_name}']]//td[contains(@class, 'cart_description')]//a"
        )

    def _quantity_cell_by_product_name(self, product_name):
        return (
            By.XPATH,
            f"//tr[.//td[contains(@class, 'cart_description')]//a[normalize-space()='{product_name}']]//td[contains(@class, 'cart_quantity')]//button"
        )

    def _total_cell_by_product_name(self, product_name):
        return (
            By.XPATH,
            f"//tr[.//td[contains(@class, 'cart_description')]//a[normalize-space()='{product_name}']]//td[contains(@class, 'cart_total')]"
        )

    def is_blue_top_visible(self):
        return self.is_visible(self.BLUE_TOP_ROW)

    def get_blue_top_name(self):
        return self.get_text(self.BLUE_TOP_NAME)

    def get_blue_top_quantity(self):
        return self.get_text(self.BLUE_TOP_QUANTITY)

    def is_product_visible(self, product_name):
        return len(self.driver.find_elements(*self._row_by_product_name(product_name))) > 0

    def get_product_name(self, product_name):
        return self.get_text(self._name_cell_by_product_name(product_name))

    def get_product_quantity(self, product_name):
        return self.get_text(self._quantity_cell_by_product_name(product_name))

    def get_product_total(self, product_name):
        return self.get_text(self._total_cell_by_product_name(product_name))

    def get_cart_item_names(self):
        return [row.find_element(By.CSS_SELECTOR, "td.cart_description a").text for row in self.find_all(self.CART_ROWS)]

    def get_cart_items_count(self):
        return len(self.driver.find_elements(*self.CART_ROWS))

    def remove_blue_top(self):
        self.click(self.BLUE_TOP_REMOVE)

    def wait_until_blue_top_removed(self):
        return self.wait_until_invisible(self.BLUE_TOP_ROW)

    def is_empty_cart_message_visible(self):
        elements = self.driver.find_elements(*self.EMPTY_CART_TEXT)
        return bool(elements) and elements[0].is_displayed()

    def proceed_to_checkout(self):
        self.click(self.PROCEED_TO_CHECKOUT_BUTTON)

    def is_checkout_modal_visible(self):
        return self.is_visible(self.CHECKOUT_MODAL)

    def get_checkout_title(self):
        return self.get_text(self.CHECKOUT_TITLE)

    def get_checkout_prompt(self):
        return self.get_text(self.CHECKOUT_PROMPT)

    def is_checkout_login_link_visible(self):
        return self.is_visible(self.CHECKOUT_LOGIN_LINK)

    def continue_on_cart(self):
        self.click(self.CONTINUE_ON_CART_BUTTON)
