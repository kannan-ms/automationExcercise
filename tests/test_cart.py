from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


class TestCart:

    def test_add_blue_top_to_cart(self, driver):
        home_page = HomePage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)

        home_page.open_home_page()
        home_page.go_to_products_page()

        product_page.add_blue_top_to_cart()
        product_page.open_cart_from_popup()

        assert cart_page.is_blue_top_visible()
        assert cart_page.get_blue_top_name() == "Blue Top"
        assert cart_page.get_blue_top_quantity() == "1"