import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info('******** Test_001_Login ********')
        self.logger.info('******** Verifying Home Page Title ********')
        self.driver = setup
        self.logger.info('******** Opening URL ********')
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == 'Your store. Login':
            self.logger.info('******** Home Page Title Case Passed ********')
            self.driver.close()
            assert True
        else:
            self.logger.info('******** Home Page Title Case Failed ********')
            self.driver.save_screenshot('.\\Screenshots\\'+'test_homePageTitle.png')
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info('******** Verifying Login Test ********')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == 'Dashboard / nopCommerce administration':
            self.logger.info('******** Login Case Passed ********')
            self.driver.close()
            assert True
        else:
            self.logger.info('******** Login Case Failed ********')
            self.driver.save_screenshot('.\\Screenshots\\' + 'test_login.png')
            self.driver.close()
            assert False
