from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


# s = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service =s )


on = True
while on:
    def five_seconds():
        time.sleep(5)
        cdp = "D:\PythonForHackers_PhDSecurity\developer\chromedriver_win32\chromedriver.exe"

        driver =  webdriver.Chrome(executable_path = cdp)

        driver.get("https://www.amazon.com/s?k=watch&crid=1PAHMKA9N0H8A&sprefix=w%2Caps%2C729&ref=nb_sb_noss_2")

        price = driver.find_element(By.CLASS_NAME, "a-price-whole")
        print(price)

        driver.quit()

    five_seconds()
