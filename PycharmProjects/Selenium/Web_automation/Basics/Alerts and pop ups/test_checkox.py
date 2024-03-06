import logging
import time

import allure
from selenium.webdriver.support.ui import Select
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_checkbox_testing():
    Logger = logging.getLogger(__name__)
    driver=webdriver.Chrome() #creating session
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    checkboxes=driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")

    for c in checkboxes:
        if not c.is_selected():
            c.click()

    time.sleep(15)