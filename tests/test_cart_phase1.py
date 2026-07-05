from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


class TestCartPhase1:

    def test_add_products_in_cart(self, driver):
        home_page = HomePage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)

        home_page.open_home_page()
        home_page.go_to_products_page()

        product_page.add_blue_top_to_cart()
        product_page.continue_shopping()
        product_page.add_second_product_to_cart()
        product_page.open_cart_from_popup()

        assert cart_page.get_cart_items_count() >= 2

    def test_remove_products_from_cart(self, driver):
        home_page = HomePage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)

        home_page.open_home_page()
        home_page.go_to_products_page()
        product_page.add_blue_top_to_cart()
        product_page.open_cart_from_popup()

        assert cart_page.is_blue_top_visible()

        cart_page.remove_blue_top()
        cart_page.wait_until_blue_top_removed()

        assert cart_page.is_empty_cart_message_visible() or cart_page.get_cart_items_count() == 0
