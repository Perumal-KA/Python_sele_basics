
import logging

import allure
from selenium.webdriver.support.ui import Select
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert


def test_alerts_testing():
    Logger = logging.getLogger(__name__)
    driver=webdriver.Chrome() #creating session
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    alert_button=driver.find_element(By.XPATH,"//*[text()='Click for JS Alert']")
    alert_button.click()

    wait=WebDriverWait(driver,10)
    wait.until(EC.alert_is_present())
    alert=driver.switch_to.alert
    alert.accept()

    result=driver.find_element(By.XPATH,"//p[@id='result']")
    print(result.text)
