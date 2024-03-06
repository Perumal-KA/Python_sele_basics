import time
import logging

import allure
from selenium.webdriver.support.ui import Select
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure_pytest


@pytest.mark.negative
@allure.feature()
def test_login_katalon_negative():
    Logger = logging.getLogger(__name__)
    driver=webdriver.Chrome() #creating session
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.implicitly_wait(20)


    link=driver.find_element(By.LINK_TEXT,"Make Appointment")
    link.click()

    username=driver.find_element(By.ID,"txt-username")
    username.send_keys("John Doe")

    password=driver.find_element(By.NAME,"password")
    password.send_keys("ThisIsNotAPas")

    login_button=driver.find_element(By.ID,"btn-login")
    login_button.click()

    error_message=driver.find_element(By.CSS_SELECTOR,"p.lead.text-danger")
    assert "Login failed! Please ensure the username and password are valid" in error_message.text


@pytest.mark.positive
@allure.feature()
def test_login_katalon():
    Logger = logging.getLogger(__name__)
    driver=webdriver.Chrome() #creating session
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")


    link=driver.find_element(By.LINK_TEXT,"Make Appointment")
    link.click()

    username=driver.find_element(By.ID,"txt-username")
    username.send_keys("John Doe")

    password=driver.find_element(By.NAME,"password")
    password.send_keys("ThisIsNotAPassword")

    login_button=driver.find_element(By.ID,"btn-login")
    login_button.click()



    dropdown=Select(driver.find_element(By.ID,"combo_facility"))
    dropdown.select_by_visible_text("Hongkong CURA Healthcare Center")



    driver.find_element(By.ID,"chk_hospotal_readmission").click()
    driver.find_element(By.ID, "radio_program_medicaid").click()
    driver.find_element(By.ID,"txt_visit_date").send_keys("18/11/1997")
    driver.find_element(By.NAME,"comment").send_keys("i have cold and dry cough")

    driver.find_element(By.ID,"btn-book-appointment").click()

    heading_h2=driver.find_element(By.TAG_NAME,"h2")
    assert "Appointment Confirmation" in heading_h2.text


