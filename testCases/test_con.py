import time

import pytest
from selenium import  webdriver
from  selenium.webdriver.chrome import  webdriver
from selenium.webdriver.common.by import By


class Test_creenshot:

   def test_shot(self,setup):
      self.driver = setup
      self.driver.find_element(By.NAME, 'username').send_keys('Admin')
      self.driver.find_element(By.NAME, 'password').send_keys('admin123')
      self.driver.find_element(By.XPATH,
                               '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
      self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a').click()
      time.sleep(2)
      section = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div')
      section.screenshot('C:\\Users\\Admin\\PycharmProjects\\pytest_project\\Screenshot\\section.png')
      time.sleep(3)

      self.driver.save_screenshot('C:\\Users\\Admin\\PycharmProjects\\pytest_project\\Screenshot\\myinfopsge.jpg')


   def test_dip(self,setup):
        self.driver = setup
        self.driver.find_element(By.NAME, 'username').send_keys('Admin')
        self.driver.find_element(By.NAME, 'password').send_keys('admin123')
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a').click()
        time.sleep(2)
        profile = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[1]/div[2]/div')

        try:
            if profile.is_displayed():
               assert True
        except:
               assert False

   def test_name(self,setup):
       self.driver = setup
       time.sleep(2)
       Title = self.driver.title
       print('title is',Title)
       time.sleep(2)
       URL = self.driver.current_url
       print('url is',URL)