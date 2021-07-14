from selenium.webdriver.common.by import By


class MainPageLocators:
    SERVICES = (By.XPATH, '//header//span[text()="SERVICES"]')
    CONTACT_US = (By.XPATH, '//*[@id="page"]/div[2]/header/ul/li[4]/a')
    AI_DATA_ANNOTATION_SERVICE = (By.XPATH, '//*[@id="page"]/div[2]/header/ul/li[2]/ul/li[2]')

class ContactUsPageLocators:
    NAME = (By.XPATH, '//*[@name="your-name"]')
    EMAIL = (By.XPATH, '//*[@name="your-email"]')
    SUBMIT_BTN = (By.XPATH, '//input[@value="Send Request"]')
