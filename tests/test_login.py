import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *

def test_login_from_main_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*LOGIN_BUTTON_MP).click()
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
    
def test_login_from_lk_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*LK_BUTTON).click()
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

def test_login_from_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*LOGIN_LINK).click()
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

def test_login_from_forgot_psw(driver):
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    driver.find_element(*LOGIN_LINK).click()
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

def test_login(login):
    assert login.find_element(*ORDER_BUTTON).is_displayed()