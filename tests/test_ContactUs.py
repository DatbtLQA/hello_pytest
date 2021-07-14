import pytest

from config import app_string
from tests.BaseTest import BaseTest
from pages.ContactUsPage import ContactUsPage
from pages.HomePage import HomePage
from pages.MainPage import MainPage

@pytest.mark.usefixtures("init_driver")
class TestContactUs():
    # def test_open_contact_us(self):
    #     main_page = MainPage(self.driver)
    #     main_page.click_contact_us()
    #     assert self.driver.title == app_string.CONTACT_US_TITLE

    @pytest.mark.usefixtures("user_data")
    def test_send_contact_us_fail(self, user_data):
        mainpage = MainPage(self.driver)
        mainpage.click_contact_us()
        contact_us_page = ContactUsPage(self.driver)
        contact_us_page.input_name(user_data['name'])
        contact_us_page.input_email(user_data['email'])
        contact_us_page.send_request()
        contact_us_page.page_should_contain_text(app_string.FIELD_ERROR)

