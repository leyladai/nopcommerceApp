from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        serv_obj = Service(r"C:\Users\sdai\AppData\Local\Programs\Python\Python310\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
        print('Launching chrome browser......')
    elif browser == 'firefox':
        serv_obj = Service(r"C:\Users\sdai\AppData\Local\Programs\Python\Python310\Lib\site-packages\selenium\webdriver\firefox\geckodriver.exe")
        driver = webdriver.Firefox(service=serv_obj)
        print('Launching firefox browser......')
    return driver

def pytest_addoption(parser): # This will get the value from CLI/hooks
    parser.addoption('--browser')

@pytest.fixture()
def browser(request): # This will return the Browser value to setup method
    return request.config.getoption('--browser')

######## pytest HTML Report ########

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Shengqi Dai'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)

