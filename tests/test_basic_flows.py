from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


class TestBasicFlows:

    def test_home_page_loads_successfully(self, driver):
        home_page = HomePage(driver)

        home_page.open_home_page()

        assert home_page.is_logo_visible()
        assert "automationexercise" in driver.current_url

    def test_invalid_login_shows_error_message(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        home_page.open_home_page()
        home_page.go_to_login_page()
        login_page.login("wronguser@test.com", "wrongpassword")

        assert login_page.get_error_message() == "Your email or password is incorrect!"

    def test_search_product(self, driver):
        home_page = HomePage(driver)
        product_page = ProductPage(driver)

        home_page.open_home_page()
        home_page.go_to_products_page()
        product_page.search_product("dress")

        assert product_page.is_searched_products_visible()
        assert product_page.get_product_count() > 0