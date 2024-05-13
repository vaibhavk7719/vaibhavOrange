import pytest
from  selenium import  webdriver

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    driver.implicitly_wait(10)
    yield driver
    driver.quit()