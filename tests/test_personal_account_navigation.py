import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from data.urls import *

class TestStellarBurgersNavigation:

    def test_navigation_via_lk_button(self, driver, login):
        driver = login
        driver.find_element(*LK_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(URL_PROFILE))
        assert driver.current_url == URL_PROFILE

    def test_navigation_from_lk_to_contructor(self, driver, login):
        driver = login
        driver.find_element(*LK_BUTTON).click()
        driver.find_element(*CONSTRUCTOR_BUTTON).click()
  
        assert driver.find_element(*ORDER_BUTTON).is_displayed()
    
    def test_navigation_from_lk_to_contructor_via_main_logo(self, driver, login):
        driver = login
        driver.find_element(*LK_BUTTON).click()
        driver.find_element(*MAIN_LOGO).click()

        assert driver.find_element(*ORDER_BUTTON).is_displayed()

    def test_logout(self, driver, login):
        driver = login
        driver.find_element(*LK_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((LOGOUT_BUTTON)))
        driver.find_element(*LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(URL_LOGIN))
        assert driver.current_url == URL_LOGIN
