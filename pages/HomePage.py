from pages.BasePage import BasePage
from config import url


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(url.BASE_URL)


