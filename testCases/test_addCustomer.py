import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random
from selenium.webdriver.common.by import By

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info('**** Test_003_AddCustomer ****')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info('**** Login successfully ****')
        self.logger.info('**** Start Add Customer Test ****')

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.driver.implicitly_wait(5)
        self.addcust.clickOnCustomersMenuItem()
        self.driver.implicitly_wait(5)
        self.addcust.clickOnAddnew()
        self.driver.implicitly_wait(5)

        self.logger.info('**** Providing Customer Info')
        self.email = random_generator() + '@gmail.com'
        self.addcust.setEmail(self.email)
        self.addcust.setPassword('test123')
        self.addcust.setCustomerRoles('Guests')
        self.addcust.setManagerOfVendor('Vendor 2')
        self.addcust.setGender('Male')
        self.addcust.setFirstName('Shengqi')
        self.addcust.setLastName('Dai')
        self.addcust.setDob('11/19/1996') #Format: MM/DD/YYYY
        self.addcust.setCompanyName('busyQA')
        self.addcust.setAdminContent('This is for testing')
        self.addcust.clickOnSave()

        self.logger.info('**** Saving customer info ****')
        self.logger.info('**** Add customer validation started ****')

        self.msg = self.driver.find_element(By.TAG_NAME,'body').text
        print(self.msg)

        if 'customer has been added successfully.' in self.msg:
            self.logger.info('**** Add customer Test Passed ****')
            assert True
        else:
            self.driver.save_screenshot('.\\Screenshots\\' + 'test_addCustomer_scr.png')
            self.logger.error('**** Add customer Test Failed ****')
            assert False

        self.driver.close()
        self.logger.info('**** Ending Add customer test ****')


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


