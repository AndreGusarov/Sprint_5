import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from tests.locators import *
from data.urls import *

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    driver.get(URL_LOGIN)
    driver.find_element(*EMAIL_INPUT).send_keys('test1234@ya.ru')
    driver.find_element(*PASSWORD_INPUT).send_keys('Test1234')
    driver.find_element(*ENTER_BUTTON).click()
    
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ORDER_BUTTON))
    return driver