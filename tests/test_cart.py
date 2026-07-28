from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from utils.data_generator import generate_user_data


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

    def test_remove_product_from_cart(self, driver):
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

    def test_add_multiple_products_to_cart(self, driver):
        home_page = HomePage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)

        home_page.open_home_page()
        home_page.go_to_products_page()

        product_page.add_blue_top_to_cart()
        product_page.continue_shopping()
        product_page.add_second_product_to_cart()
        product_page.open_cart_from_popup()

        assert cart_page.get_cart_items_count() == 2
        assert cart_page.is_product_visible("Blue Top")
        assert cart_page.is_product_visible("Men Tshirt")

    def test_update_product_quantity_in_cart(self, driver):
        home_page = HomePage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)

        home_page.open_home_page()
        home_page.go_to_products_page()
        product_page.open_first_product_details()
        product_page.set_product_quantity(4)
        product_page.add_current_product_to_cart()
        product_page.open_cart_from_popup()

        assert cart_page.is_product_visible("Blue Top")
        assert cart_page.get_product_quantity("Blue Top") == "4"
        assert "2000" in cart_page.get_product_total("Blue Top")

    def test_continue_shopping_adds_second_product(self, driver):
        home_page = HomePage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)

        home_page.open_home_page()
        home_page.go_to_products_page()

        product_page.add_blue_top_to_cart()
        product_page.continue_shopping()
        assert product_page.is_all_products_visible()

        product_page.add_second_product_to_cart()
        product_page.open_cart_from_popup()

        assert cart_page.is_product_visible("Blue Top")
        assert cart_page.is_product_visible("Men Tshirt")
        assert cart_page.get_cart_items_count() == 2

    def test_cart_persists_after_login(self, driver):
        user_data = generate_user_data()
        home_page = HomePage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)
        login_page = LoginPage(driver)

        home_page.open_home_page()
        home_page.go_to_products_page()
        product_page.add_blue_top_to_cart()
        product_page.open_cart_from_popup()

        assert cart_page.is_blue_top_visible()

        home_page.go_to_login_page()
        login_page.register_user(user_data)

        home_page.go_to_cart_page()

        assert login_page.is_logged_in()
        assert cart_page.is_blue_top_visible()

    def test_proceed_to_checkout_flow(self, driver):
        home_page = HomePage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)

        home_page.open_home_page()
        home_page.go_to_products_page()
        product_page.add_blue_top_to_cart()
        product_page.open_cart_from_popup()

        cart_page.proceed_to_checkout()

        assert cart_page.is_checkout_modal_visible()
        assert cart_page.get_checkout_title() == "Checkout"
        assert "Register / Login account to proceed on checkout." in cart_page.get_checkout_prompt()
        assert cart_page.is_checkout_login_link_visible()