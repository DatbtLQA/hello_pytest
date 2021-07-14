from pages.BasePage import BasePage
from utils.locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = MainPageLocators

    def move_to_nav_services(self):
        self.move_to_element(*self.locator.SERVICES)

    def click_contact_us(self):
        self.click_element(*self.locator.CONTACT_US)
