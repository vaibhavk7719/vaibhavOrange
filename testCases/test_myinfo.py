import pytest
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_my_info:

 def test_myinfo1(self, setup):
    self.driver = setup
    self.driver.find_element(By.NAME, 'username').send_keys('Admin')
    self.driver.find_element(By.NAME, 'password').send_keys('admin123')
    self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    time.sleep(2)

    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a').click()
    self.driver.find_element(By.NAME, 'firstName').send_keys('kakshi')
    self.driver.find_element(By.NAME, 'middleName').send_keys('samuko')
    self.driver.find_element(By.NAME, 'lastName').send_keys('hatake')
    time.sleep(2)
    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(
        '1123456789')
    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input').send_keys(
        '147258369')
    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input').send_keys(
        '1452')
    time.sleep(4)

 def test_date(self, setup):
       driver = setup
       wait = WebDriverWait(self.driver, 10)
       self.driver.find_element(By.NAME, 'username').send_keys('Admin')
       self.driver.find_element(By.NAME, 'password').send_keys('admin123')
       self.driver.find_element(By.XPATH,
                                '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
       time.sleep(2)
       self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a').click()
       self.driver.find_element(By.CLASS_NAME, 'oxd-input oxd-input--active').click()
       time.sleep(6)
       self.driver.find_element(By.CLASS_NAME, "oxd-icon bi-calendar oxd-date-input-icon").send_keys('10-09-2024')
       time.sleep(4)

       wait.until(EC.presence_of_element_located(By.XPATH)).send_keys(
           "2023-11-20")

