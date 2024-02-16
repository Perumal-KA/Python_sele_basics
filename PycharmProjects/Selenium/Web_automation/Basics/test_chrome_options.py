import pytest
from selenium import webdriver
import logging

#chrome options
#customize chrome like window size,chrome with extension,JS disabled.

def test_login():
    chrome_options=webdriver.ChromeOptions()
    extension_path="/Users/kfperuma/Downloads/adblocker1.crx"
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_extension(extension_path)
    chrome_options.add_argument("--headless=new")
    driver= webdriver.Chrome(options=chrome_options)
    driver.get("https://app.vwo.com")
