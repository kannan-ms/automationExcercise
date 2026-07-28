from pages.home_page import HomePage
from pages.product_page import ProductPage


class TestProducts:
    #these two are the functions for testing the products page
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
    #this one is specifically for search product functionality
    def test_search_product(self, driver):
        home_page = HomePage(driver)
        product_page = ProductPage(driver)

        home_page.open_home_page()
        home_page.go_to_products_page()
        product_page.search_product("dress")

        assert product_page.is_searched_products_visible()
        assert product_page.get_product_count() > 0

    def test_all_products_page_loads_successfully(self, driver):
        home_page = HomePage(driver)
        product_page = ProductPage(driver)

        home_page.open_home_page()
        home_page.go_to_products_page()

        assert product_page.is_all_products_visible()
        assert product_page.get_product_count() > 0

    def test_brand_filter_functionality(self, driver):
        home_page = HomePage(driver)
        product_page = ProductPage(driver)

        home_page.open_home_page()
        home_page.go_to_products_page()
        product_page.open_brand_products("Polo")

        assert "BRAND - POLO PRODUCTS" in product_page.get_filtered_products_heading()
        assert product_page.get_product_count() > 0
        assert product_page.is_product_visible("Blue Top")

    def test_category_filter_functionality(self, driver):
        home_page = HomePage(driver)
        product_page = ProductPage(driver)

        home_page.open_home_page()
        home_page.go_to_products_page()
        product_page.open_category_products(1)

        assert "WOMEN - DRESS PRODUCTS" in product_page.get_filtered_products_heading()
        assert product_page.get_product_count() > 0
        assert product_page.is_product_visible("Sleeveless Dress")

    def test_scroll_to_top_button(self, driver):
        home_page = HomePage(driver)
        product_page = ProductPage(driver)

        home_page.open_home_page()
        home_page.go_to_products_page()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        product_page.scroll_to_top()

        assert driver.execute_script("return window.pageYOffset;") == 0

    def test_search_existing_product(self, driver):
        home_page = HomePage(driver)
        product_page = ProductPage(driver)

        home_page.open_home_page()
        home_page.go_to_products_page()
        product_page.search_product("Blue Top")

        assert product_page.is_searched_products_visible()
        assert product_page.get_product_count() > 0
        assert product_page.is_product_visible("Blue Top")

    def test_search_non_existing_product(self, driver):
        home_page = HomePage(driver)
        product_page = ProductPage(driver)

        home_page.open_home_page()
        home_page.go_to_products_page()
        product_page.search_product("zzzzzzzznotfound")

        assert product_page.is_searched_products_visible()
        assert product_page.get_product_count() == 0

    def test_view_product_details(self, driver):
        home_page = HomePage(driver)
        product_page = ProductPage(driver)

        home_page.open_home_page()
        home_page.go_to_products_page()
        product_page.open_first_product_details()

        assert "/product_details/" in driver.current_url
        assert product_page.is_product_details_visible()
        assert product_page.get_product_detail_name() == "Blue Top"
        assert product_page.get_product_detail_price() == "Rs. 500"
        assert "Availability:" in product_page.get_product_detail_availability()
        assert "Category:" in product_page.get_product_detail_category()
