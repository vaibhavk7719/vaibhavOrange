import time
import pytest
from selenium import  webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.chrome import webdriver

class Test_title:

     def test_titile1(self,setup):
      self.driver = setup
      if self.driver.title == 'OrangeHRM':
        assert True
      else:
        assert False

     def test_login1(self,setup):
         self.driver = setup
         self.driver.find_element(By.NAME,'username').send_keys('Admin')
         self.driver.find_element(By.NAME,'password').send_keys('admin123')
         self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
         time.sleep(2)


