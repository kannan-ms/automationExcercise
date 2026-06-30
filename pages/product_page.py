from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    SEARCHED_PRODUCTS_TEXT = (By.XPATH, "//h2[contains(text(),'Searched Products')]")
    PRODUCT_ITEMS = (By.XPATH, "//div[contains(@class,'product-image-wrapper')]")
    FIRST_PRODUCT_ADD_TO_CART = (
    By.XPATH,
    "(//a[@data-product-id='1' and contains(@class, 'add-to-cart')])[1]"
)

    VIEW_CART_LINK = (By.XPATH, "//a[@href='/view_cart']")
    def search_product(self, product_name):
        self.type_text(self.SEARCH_INPUT, product_name)
        self.js_click(self.SEARCH_BUTTON)

    def is_searched_products_visible(self):
        return self.is_visible(self.SEARCHED_PRODUCTS_TEXT)

    def get_product_count(self):
        return len(self.driver.find_elements(*self.PRODUCT_ITEMS))
    def add_blue_top_to_cart(self):
        self.js_click(self.FIRST_PRODUCT_ADD_TO_CART)

    def open_cart_from_popup(self):
        self.click(self.VIEW_CART_LINK)