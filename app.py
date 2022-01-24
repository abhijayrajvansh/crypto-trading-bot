#/
#    author:   abhijayrajvansh
#    created:  24.01.2022 12:05:16
#/
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options #to by-pass chrome broswer notification
from selenium.webdriver.common.by import By
import os
import datetime
import time

pwd = os.getcwd()

PATH = Service(pwd + "/chromedriver")
url = "https://coindcx.com/trade/USDTINR"

# Handling Chrome Options:
chromeOptions = Options()
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument("--disable-notifications")
# chromeOptions.add_experimental_option("prefs", { "profile.default_content_setting_values.notifications": 2 }) 

driver = webdriver.Chrome(service = PATH, options = chromeOptions)
driver.maximize_window()
driver.get(url) # launches the broswer and open url
time.sleep(5) # very important to load before exicuting commands

#Commands:
def USDTINR(): #tether

    usdtprice = driver.find_element(By.XPATH, "//span[@class='latest-trade-price']").text # Current Crypto Price - working
    usdt24h = driver.find_element(By.XPATH, "//p[@class='value -c-red']").text # 24 hours percentage change - working
    curr_time = time.strftime('%H:%M:%S %d/%m/%y', time.localtime())

    print("USDT-INR : " + usdtprice + " | 24h-Change : " + usdt24h + " | " + curr_time)

while True:
    try:
        time.sleep(1)
        USDTINR()
        print()
    except Exception as e:
        driver.quit()
        break
