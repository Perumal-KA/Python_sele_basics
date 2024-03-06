import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_user_login():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.idrive360.com/enterprise/login")

    username=driver.find_element(By.ID,"username")
    username.send_keys("augtest_040823@idrive.com")

    password=driver.find_element(By.XPATH,"//*[@id='password]")
    password.send_keys("123456")

    login_button=driver.find_element(By.ID,"btn-login")
    login_button.click()