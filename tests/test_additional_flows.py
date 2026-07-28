import os
import tempfile

from pages.contact_page import ContactPage
from pages.home_page import HomePage


class TestContactAndSubscription:
    def test_contact_us_form(self, driver):
        home_page = HomePage(driver)
        contact_page = ContactPage(driver)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
            temp_file.write(b"sample upload")
            temp_file_path = temp_file.name

        try:
            home_page.open_home_page()
            home_page.go_to_contact_page()

            assert contact_page.is_contact_us_visible()
            assert contact_page.is_get_in_touch_visible()

            contact_page.fill_contact_form(
                name="Test User",
                email=f"test{os.getpid()}@mailinator.com",
                subject="Automation Inquiry",
                message="This is a test message.",
                file_path=temp_file_path,
            )
            contact_page.submit_contact_form()

            submission_message = contact_page.get_submission_message()

            assert submission_message == "Press OK to proceed!"
        finally:
            if os.path.exists(temp_file_path):
                os.unlink(temp_file_path)

    def test_subscription_feature(self, driver):
        home_page = HomePage(driver)

        home_page.open_home_page()
        home_page.subscribe(f"sub{os.getpid()}@mailinator.com")

        assert home_page.is_subscription_success_visible()
        assert home_page.get_subscription_success_message() == "You have been successfully subscribed!"