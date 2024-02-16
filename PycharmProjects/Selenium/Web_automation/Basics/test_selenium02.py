import pytest
from selenium import webdriver
import logging
@pytest.fixture()
def driver():
    driver=webdriver.Chrome()
    yield driver

def test_open_verify_url_title(driver):
    Logger = logging.getLogger(__name__)
    driver.get("https://admin.ring.com")
    print(driver.title)
    Logger.info("this is information")
    Logger.warning("this is warning")
    Logger.error("this is error")
    Logger.critical("this is critical")
    assert "Login | Ring-Admin" == driver.title

