from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# https://github.com/udoy382

cdp = "D:\PythonForHackers_PhDSecurity\developer\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(executable_path=cdp)
driver.get("https://github.com/udoy382")
time.sleep(2)
res = driver.find_elements(By.CLASS_NAME, "repo")

for i in res:
    print(i.text)

driver.quit()