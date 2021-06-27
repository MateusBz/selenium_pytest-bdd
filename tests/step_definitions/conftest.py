import pytest

from selenium import webdriver


@pytest.fixture(params=['firefox', 'chrome'])
def driver_init(request) -> webdriver:
    if request.param == 'firefox':
        web_driver = webdriver.Firefox(executable_path='./drivers/geckodriver')
    if request.param == 'chrome':
        web_driver = webdriver.Chrome(executable_path='./drivers/chromedriver')
    yield web_driver
    web_driver.close()
