import pytest
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from config import url
import json
from utils import helper


def get_user_data():
    file_name = helper.get_absolute_path('data/input/data.txt')
    with open(file_name, 'r') as json_file:
        json_object = json.load(json_file)
    return json_object

@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    web_driver.set_window_position(0, 0)
    web_driver.set_window_size(2048, 1768)
    web_driver.get(url.BASE_URL)
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.fixture(params=get_user_data(), scope="class")
def user_data(request):
    return request.param
