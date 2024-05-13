import pytest
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
import time

from selenium.webdriver.common.by import By

class Test_demo1:
    def test_dodo(self,setup):
        self.driver = setup
        self.driver.find_element(By.NAME, 'username').send_keys('Admin')
        self.driver.find_element(By.NAME, 'password').send_keys('admin123')
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a').click()

        time.sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input').send_keys('2004/11/20')
        time.sleep(4)

    def test_bithdate(self,setup):
        self.driver = setup
        self.driver.find_element(By.NAME, 'username').send_keys('Admin')
        self.driver.find_element(By.NAME, 'password').send_keys('admin123')
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a').click()

        time.sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input').send_keys('1997-11-20')
        time.sleep(3)


