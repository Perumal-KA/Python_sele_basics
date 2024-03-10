import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_web_tables():
    driver=webdriver.Chrome()
    driver.get('https://awesomeqa.com/webtable.html')
    time.sleep(0)

    row=driver.find_elements(By.XPATH,'//table[@id="customers"]/tbody/tr')
    row_count=len(row)
    print("Number of row:",row_count)

    #row1 = driver.find_elements(By.TAG_NAME, 'tr')
    #row_count = len(row1)
    #print("Number of row:", row_count)

    coloum3 = driver.find_elements(By.XPATH, '//table[@id="customers"]/tbody/tr[2]/td')
    coloum_count = len(coloum3)
    print("Number of coloum:", coloum_count)

    #coloum=driver.find_elements(By.XPATH,'//table[@id="customers"]/tbody/tr/th')
    #coloum_count=len(coloum)
    #print("Number of coloum:",coloum_count)

    #coloum2= driver.find_elements(By.TAG_NAME, 'th')
    #coloum_count = len(coloum2)
    #print("Number of coloum:", coloum_count)

    get_country=driver.find_element(By.XPATH,'//td[normalize-space()="Helen Bennett"]//following::td[1]')
    print(get_country.text)

    first_part="//table[@id='customers']/tbody/tr["
    second_part="]/td["
    third_part="]"

    for i in range(2,row_count+1):
        for j in range(1,coloum_count+1):
            dynamic_xpath= f"{first_part}{i}{second_part}{j}{third_part}"
            data=driver.find_element(By.XPATH,dynamic_xpath).text
            
            if "Helen Bennett" in data:
                country_path = f"{dynamic_xpath}/following-sibling::td"
                country_text = driver.find_element(By.XPATH, country_path)

                print(f"Helen Bennett is in - {country_text.text}")





    driver.quit()

