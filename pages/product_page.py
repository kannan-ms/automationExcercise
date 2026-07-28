from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config import BASE_URL
from urllib.parse import quote

class ProductPage(BasePage):
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    ALL_PRODUCTS_TEXT = (By.XPATH, "//h2[contains(text(),'All Products')]")
    SEARCHED_PRODUCTS_TEXT = (By.XPATH, "//h2[contains(text(),'Searched Products')]")
    FILTERED_PRODUCTS_TEXT = (By.XPATH, "//h2[contains(@class,'title')]")
    PRODUCT_ITEMS = (By.XPATH, "//div[contains(@class,'product-image-wrapper')]")
    PRODUCT_NAMES = (By.XPATH, "//div[contains(@class,'productinfo')]/p")
    VIEW_FIRST_PRODUCT = (By.XPATH, "(//a[contains(@href,'/product_details/')])[1]")
    PRODUCT_DETAILS_CONTAINER = (By.CSS_SELECTOR, "div.product-information")
    PRODUCT_DETAIL_NAME = (By.CSS_SELECTOR, "div.product-information h2")
    PRODUCT_DETAIL_PRICE = (By.CSS_SELECTOR, "div.product-information span > span")
    PRODUCT_DETAIL_CATEGORY = (By.XPATH, "//div[@class='product-information']//p[contains(.,'Category:')]")
    PRODUCT_DETAIL_AVAILABILITY = (By.XPATH, "//div[@class='product-information']//p[contains(.,'Availability:')]")
    PRODUCT_DETAIL_QUANTITY = (By.ID, "quantity")
    PRODUCT_DETAIL_ADD_TO_CART = (By.XPATH, "//div[@class='product-information']//button[contains(.,'Add to cart')]")
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

    def open_category_products(self, category_id):
        self.open_url(f"{BASE_URL}/category_products/{category_id}")

    def open_brand_products(self, brand_name):
        self.open_url(f"{BASE_URL}/brand_products/{quote(brand_name, safe='')}")

    def is_all_products_visible(self):
        return self.is_visible(self.ALL_PRODUCTS_TEXT)

    def open_first_product_details(self):
        self.click(self.VIEW_FIRST_PRODUCT)

    def is_product_details_visible(self):
        return self.is_visible(self.PRODUCT_DETAILS_CONTAINER)

    def is_searched_products_visible(self):
        return self.is_visible(self.SEARCHED_PRODUCTS_TEXT)

    def get_filtered_products_heading(self):
        return self.get_text(self.FILTERED_PRODUCTS_TEXT)

    def get_product_names(self):
        return [element.text for element in self.find_all(self.PRODUCT_NAMES) if element.text.strip()]

    def is_product_visible(self, product_name):
        return any(product_name.lower() in name.lower() for name in self.get_product_names())

    def get_product_count(self):
        return len(self.driver.find_elements(*self.PRODUCT_ITEMS))

    def get_product_detail_name(self):
        return self.get_text(self.PRODUCT_DETAIL_NAME)

    def get_product_detail_price(self):
        return self.get_text(self.PRODUCT_DETAIL_PRICE)

    def get_product_detail_category(self):
        return self.get_text(self.PRODUCT_DETAIL_CATEGORY)

    def get_product_detail_availability(self):
        return self.get_text(self.PRODUCT_DETAIL_AVAILABILITY)

    def set_product_quantity(self, quantity):
        self.type_text(self.PRODUCT_DETAIL_QUANTITY, str(quantity))

    def add_current_product_to_cart(self):
        self.js_click(self.PRODUCT_DETAIL_ADD_TO_CART)

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

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