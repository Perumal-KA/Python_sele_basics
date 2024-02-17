import time
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_vwo():
    Logger = logging.getLogger(__name__)
    driver=webdriver.Chrome() #creating session
    driver.maximize_window()
    driver.get("http://app.vwo.com")


    link=driver.find_element(By.LINK_TEXT,"Start a free trial")
    link.click()