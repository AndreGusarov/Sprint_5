import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *

def test_navigation_via_lk_button(driver, login):
    driver = login
    driver.find_element(*LK_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

def test_navigation_from_lk_to_contructor(driver, login):
    driver = login
    driver.find_element(*LK_BUTTON).click()
    driver.find_element(*CONSTRUCTOR_BUTTON).click()
  
    assert driver.find_element(*ORDER_BUTTON).is_displayed()
    
def test_navigation_from_lk_to_contructor_via_main_logo(driver, login):
    driver = login
    driver.find_element(*LK_BUTTON).click()
    driver.find_element(*MAIN_LOGO).click()

    assert driver.find_element(*ORDER_BUTTON).is_displayed()

def test_logout(driver, login):
    driver = login
    driver.find_element(*LK_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((LOGOUT_BUTTON)))
    driver.find_element(*LOGOUT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
