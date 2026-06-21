from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    SEARCHED_PRODUCTS_TEXT = (By.XPATH, "//h2[contains(text(),'Searched Products')]")
    PRODUCT_ITEMS = (By.XPATH, "//div[contains(@class,'product-image-wrapper')]")

    def search_product(self, product_name):
        self.type_text(self.SEARCH_INPUT, product_name)
        self.js_click(self.SEARCH_BUTTON)

    def is_searched_products_visible(self):
        return self.is_visible(self.SEARCHED_PRODUCTS_TEXT)

    def get_product_count(self):
        return len(self.driver.find_elements(*self.PRODUCT_ITEMS))