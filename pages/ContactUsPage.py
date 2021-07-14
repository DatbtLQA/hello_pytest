from pages.BasePage import BasePage
from utils.locators import ContactUsPageLocators
from data.input.inputs import User
from config import url

class ContactUsPage(BasePage):
    def __init__(self, driver):
        super(ContactUsPage, self).__init__(driver)
        self.locator = ContactUsPageLocators

    def input_name(self, name=User.NAME):
        self.input_element(name, *self.locator.NAME)

    def input_email(self, email=User.EMAIL):
        self.input_element(email, *self.locator.EMAIL)

    def send_request(self):
        self.click_element(*self.locator.SUBMIT_BTN)