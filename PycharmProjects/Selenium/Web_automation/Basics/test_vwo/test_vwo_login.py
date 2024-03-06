import time
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_timesheet():
    Logger = logging.getLogger(__name__)
    driver=webdriver.Chrome() #creating session
    driver.maximize_window()
    driver.get("http://qstimesheet.corp.amazon.com/auths/") #getting link

    email_address_ele=driver.find_element(By.NAME,"user")
    password_ele=driver.find_element(By.NAME,"pass")
    sing_in_button=driver.find_element(By.NAME,"login")

    email_address_ele.send_keys("kfperuma")
    password_ele.send_keys("Asdf@1897")
    sing_in_button.click()
    time.sleep(5)
    Logger.info("tirle is --> "+ driver.title)
    assert "timesheet" == driver.title


