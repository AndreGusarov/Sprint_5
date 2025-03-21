import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *

def test_scroll_to_sauces(driver, login):
    driver = login 
    driver.find_element(*SAUCES_TAB).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(SAUCES_TEXT))
    sauces_text = driver.find_element(*SAUCES_TEXT).text
    
    assert sauces_text == "Соусы"

def test_scroll_to_filling(driver, login):
    driver = login
    driver.find_element(*FILLING_TAB).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(FILLING_TAB))
    filling_text = driver.find_element(*FILLING_TEXT).text

    assert filling_text == "Начинки"

def test_scroll_to_bun(driver, login):
    driver = login
    driver.find_element(*FILLING_TAB).click()
    driver.find_element(*BUN_TAB).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BUN_TAB))
    bun_text = driver.find_element(*BUN_TEXT).text

    assert bun_text == "Булки"