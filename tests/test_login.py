import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from data.urls import *

class TestStellarBurgersLogin:
   
    def test_login_from_main_page(self, driver):
        driver.get(URL_MAIN_PAGE)
        driver.find_element(*LOGIN_BUTTON_MP).click()
        assert driver.current_url == URL_LOGIN
    
    def test_login_from_lk_button(self, driver):
        driver.get(URL_MAIN_PAGE)
        driver.find_element(*LK_BUTTON).click()
        assert driver.current_url ==URL_LOGIN

    def test_login_from_registration(self, driver):
        driver.get(URL_REGISTER)
        driver.find_element(*LOGIN_LINK).click()
        assert driver.current_url == URL_LOGIN

    def test_login_from_forgot_psw(self, driver):
        driver.get(URL_FORGOR_PSW)
        driver.find_element(*LOGIN_LINK).click()
        assert driver.current_url == URL_LOGIN

    def test_login(self, login):
        assert login.find_element(*ORDER_BUTTON).is_displayed()