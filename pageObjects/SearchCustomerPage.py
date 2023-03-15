from selenium.webdriver.common.by import By

class SearchCustomer():
    # Add customer Page
    txtEmail_id = "SearchEmail"
    txtFirstName_id="SearchFirstName"
    txtLastName_id="SearchLastName"
    btnSearch_id="search-customers"
    # tblSearchResults_xpath="//table[@role='grid']"
    tblSearchResults_xpath = "//div[@class='card card-default']//div[@class='card-body']"
    # table_xpath="//table[@id='customers-grid']"
    table_xpath = "//div[@id='customers-grid_wrapper']"
    tableRows_xpath="//div[@id='customers-grid_wrapper']//tbody/tr"
    tableColumns_xpath="//div[@id='customers-grid_wrapper']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.txtEmail_id).clear()
        self.driver.find_element(By.ID,self.txtEmail_id).send_keys(email)

    def setFirstName(self,fname):
        self.driver.find_element(By.ID,self.txtFirstName_id).clear()
        self.driver.find_element(By.ID,self.txtFirstName_id).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.ID,self.txtLastName_id).clear()
        self.driver.find_element(By.ID,self.txtLastName_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.ID,self.btnSearch_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.tableColumns_xpath))

    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
          table = self.driver.find_element(By.XPATH,self.table_xpath)
          # emailid=table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
          emailid = table.find_element(By.XPATH,"//div[@id='customers-grid_wrapper']//tbody/tr["+str(r)+"]/td[2]").text
          if emailid == email:
              flag = True
              break
        return flag

    def searchCustomerByName(self,Name):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
          table = self.driver.find_element(By.XPATH,self.table_xpath)
          # name=table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
          name = table.find_element(By.XPATH,"//div[@id='customers-grid_wrapper']//tbody/tr["+str(r)+"]/td[3]").text
          if name == Name:
              flag = True
              break
        return flag

