import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver=webdriver.Chrome()
    yield driver

def test_open_verify_url_title(driver):
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert "Login - VWO" == driver.title

