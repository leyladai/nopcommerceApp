import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = './/TestData/LoginData.xlsx'
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info('******** Test_002_DDT_Login ********')
        self.logger.info('******** Verifying Login DDT Test ********')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print('Number of rows: ',self.rows)
        lst_status = []


        for r in range(2,self.rows+1):
            self.username = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            if act_title == 'Dashboard / nopCommerce administration':
                if self.exp == 'Pass':
                    self.logger.info('******** Login Case Passed ********')
                    self.lp.clickLogout()
                    lst_status.append('PASS')
                elif self.exp == 'Fail':
                    self.logger.info('******** Login Case Failed ********')
                    self.lp.clickLogout()
                    lst_status.append('FAIL')
            else:
                if self.exp == 'Pass':
                    self.logger.info('******** Login Case Failed ********')
                    lst_status.append('FAIL')
                elif self.exp == 'Fail':
                    self.logger.info('******** Login Case Passed ********')
                    lst_status.append('PASS')

        if "Fail" not in lst_status:
            self.logger.info('******** DDT Login test passed ********')
            self.driver.close()
            assert True
        else:
            self.logger.info('******** DDT Login test failed ********')
            self.driver.close()
            assert False

        self.logger.info('******** Completed Test_002_DDT_Login ********')
