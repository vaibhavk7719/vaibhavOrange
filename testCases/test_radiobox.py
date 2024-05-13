import  pytest
from selenium import  webdriver
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
import time
class Test_radio:
    def test_box(self, setup):
        self.driver = setup
        self.driver.find_element(By.NAME, 'username').send_keys('Admin')
        self.driver.find_element(By.NAME, 'password').send_keys('admin123')
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button').click()

    def test_scroll(self,setup):
        self.driver = setup
        self.driver.find_element(By.NAME, 'username').send_keys('Admin')
        self.driver.find_element(By.NAME, 'password').send_keys('admin123')
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a').click()
        time.sleep(3)
        till = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[3]/p[1]')
        self.driver.execute_script("arguments[0].scrollIntoView();",till)

    def test_second_scroll(self,setup):
        self.driver= setup
        self.driver.find_element(By.NAME, 'username').send_keys('Admin')
        self.driver.find_element(By.NAME, 'password').send_keys('admin123')
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a').click()
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,500)","")
        time.sleep(3)