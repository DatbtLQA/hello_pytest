import time
from tests.BaseTest import BaseTest
from pages.MainPage import MainPage
import pytest
from config import url



@pytest.mark.usefixtures("init_driver")
class TestServiceDetail(BaseTest):
    def test_open_service_item(self):
        self.driver.get(url.BASE_URL)
        main_page = MainPage(self.driver)
        main_page.move_to_nav_services()
        main_page.click_element(*main_page.locator.AI_DATA_ANNOTATION_SERVICE)
        time.sleep(5)
        assert self.driver.current_url == "https://www.lotus-qa.com/services/data-annotation-service/"