from pages.home_page import HomePage
from pages.product_page import ProductPage


class TestProducts:

    def test_verify_all_products_and_product_detail_page(self, driver):
        home_page = HomePage(driver)
        product_page = ProductPage(driver)

        home_page.open_home_page()
        home_page.go_to_products_page()

        assert product_page.is_all_products_visible()
        assert product_page.get_product_count() > 0

        product_page.open_first_product_details()

        assert "/product_details/" in driver.current_url
        assert product_page.is_product_details_visible()

    def test_search_product(self, driver):
        home_page = HomePage(driver)
        product_page = ProductPage(driver)

        home_page.open_home_page()
        home_page.go_to_products_page()
        product_page.search_product("dress")

        assert product_page.is_searched_products_visible()
        assert product_page.get_product_count() > 0
