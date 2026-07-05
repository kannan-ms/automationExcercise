from pages.home_page import HomePage
from pages.login_page import LoginPage
from test_data.user_data import UserData
from utils.data_generator import generate_user_data


class TestAuthentication:

    def test_login_user_with_correct_email_and_password(self, driver):
        user_data = generate_user_data()
        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        home_page.open_home_page()
        home_page.go_to_login_page()
        login_page.register_user(user_data)
        login_page.logout()
        login_page.login(user_data["email"], user_data["password"])

        assert "Logged in as" in login_page.get_logged_in_text()

    def test_login_user_with_incorrect_email_and_password(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        home_page.open_home_page()
        home_page.go_to_login_page()
        login_page.login(UserData.INVALID_EMAIL, UserData.INVALID_PASSWORD)

        assert login_page.get_error_message() == "Your email or password is incorrect!"

    def test_logout_user(self, driver):
        user_data = generate_user_data()
        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        home_page.open_home_page()
        home_page.go_to_login_page()
        login_page.register_user(user_data)

        assert login_page.is_logout_visible()

        login_page.logout()

        assert login_page.is_login_form_visible()
