from selenium.webdriver.common.by import By
from config.url import *
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.base_url = BASE_URL

    def wait_element_presence(self, *locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def find_element(self, *locator):
        return self.wait_element_presence(*locator)

    def click_element(self, *locator):
        self.find_element(*locator).click()

    def input_element(self, input, *locator):
        self.find_element(*locator).send_keys(input)

    def get_all_text_in_page(self):
        return self.driver.find_element_by_tag_name("body").text

    def page_should_contain_text(self, text):
        byXpath = By.XPATH, "//*[contains(text(), '"+text+"')]"
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(byXpath))

    def move_to_element(self, *locator):
        action = webdriver.ActionChains(self.driver)
        ele = self.find_element(*locator)
        action.move_to_element(ele)
        action.perform()

