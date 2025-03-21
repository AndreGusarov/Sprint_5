from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *

import random

def test_success_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*NAME_INPUT).send_keys('Test_Name')
    driver.find_element(*EMAIL_INPUT).send_keys(f"Test_user{random.randint(1,999)}@ya.ru")
    driver.find_element(*PASSWORD_INPUT).send_keys(random.randint(100000, 999999))
    driver.find_element(*REGISTRATION_BUTTON).click()
    
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LOGIN_ELEMENT_TEXT))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


def test_password_validation(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*PASSWORD_INPUT).send_keys('123')
    driver.find_element(*REGISTRATION_BUTTON).click()

    assert driver.find_element(*REGISTRATION_ERROR_MESSAGE).text == 'Некорректный пароль'
