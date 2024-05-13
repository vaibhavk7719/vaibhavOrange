import  pytest
from  selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains


import time


class Test_fun:
    def test_action(self,setup):
        self.driver = setup
        self.driver.find_element(By.NAME, 'username').send_keys('Admin')
        self.driver.find_element(By.NAME, 'password').send_keys('admin123')
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a').click()
        time.sleep(3)
        action = ActionChains(self.driver)
        dodo = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[9]/a')
        action.context_click(dodo).perform()
        time.sleep(3)
        action.move_to_element(dodo).click().perform()
        time.sleep(3)

    def test_alert (self,setup):
        self.driver = setup
        self.driver.find_element(By.NAME, 'username').send_keys('Admin')
        self.driver.find_element(By.NAME, 'password').send_keys('admin123')
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(4)
        self.driver.switch_to.alert().accept
        time.sleep(2)

    def test_link(self,setup):
        self.driver= setup
        self.driver.find_element(By.NAME, 'username').send_keys('Admin')
        self.driver.find_element(By.NAME, 'password').send_keys('admin123')
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a').click()
        all_links=self.driver.find_elements(By.TAG_NAME,'a')
        print(len(all_links))

        for links in all_links:
            href = links.get_attribute('href')
            if href:
                print(f"links url :{href}")

