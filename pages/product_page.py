from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    ALL_PRODUCTS_TEXT = (By.XPATH, "//h2[contains(text(),'All Products')]")
    SEARCHED_PRODUCTS_TEXT = (By.XPATH, "//h2[contains(text(),'Searched Products')]")
    PRODUCT_ITEMS = (By.XPATH, "//div[contains(@class,'product-image-wrapper')]")
    VIEW_FIRST_PRODUCT = (By.XPATH, "(//a[contains(@href,'/product_details/')])[1]")
    PRODUCT_DETAILS_CONTAINER = (By.CSS_SELECTOR, "div.product-information")
    FIRST_PRODUCT_ADD_TO_CART = (
    By.XPATH,
    "(//a[@data-product-id='1' and contains(@class, 'add-to-cart')])[1]"
)
    SECOND_PRODUCT_ADD_TO_CART = (
        By.XPATH,
        "(//a[@data-product-id='2' and contains(@class, 'add-to-cart')])[1]"
    )

    CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//button[contains(text(),'Continue Shopping')]")
    VIEW_CART_LINK = (By.CSS_SELECTOR, "div.modal-content a[href='/view_cart']")

    def search_product(self, product_name):
        self.type_text(self.SEARCH_INPUT, product_name)
        self.js_click(self.SEARCH_BUTTON)

    def is_all_products_visible(self):
        return self.is_visible(self.ALL_PRODUCTS_TEXT)

    def open_first_product_details(self):
        self.click(self.VIEW_FIRST_PRODUCT)

    def is_product_details_visible(self):
        return self.is_visible(self.PRODUCT_DETAILS_CONTAINER)

    def is_searched_products_visible(self):
        return self.is_visible(self.SEARCHED_PRODUCTS_TEXT)

    def get_product_count(self):
        return len(self.driver.find_elements(*self.PRODUCT_ITEMS))

    def add_blue_top_to_cart(self):
        self.js_click(self.FIRST_PRODUCT_ADD_TO_CART)
        self.is_visible(self.CONTINUE_SHOPPING_BUTTON)

    def add_second_product_to_cart(self):
        self.js_click(self.SECOND_PRODUCT_ADD_TO_CART)
        self.is_visible(self.CONTINUE_SHOPPING_BUTTON)

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)

    def open_cart_from_popup(self):
        self.click(self.VIEW_CART_LINK)