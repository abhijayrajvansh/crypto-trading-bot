#/
#    author:   abhijayrajvansh
#    created:  24.01.2022 19:52:03
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

# driver setup:
driver = webdriver.Chrome(service = PATH, options = chromeOptions)
driver.maximize_window()
# driver.minimize_window()

driver.get(url) # launches the broswer and open url
time.sleep(5) # very important everything to load before exicuting commands // safe at 5

def login():
    driver.find_element(By.XPATH, "//span[normalize-space()='Login']").click()
    driver.find_element(By.XPATH, "//input[@id='mat-input-4']").send_keys("abhijayrajvansh01@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='mat-input-5']").send_keys("@BJ@crypto!2711")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(60)
    print("Successfully Logged In!")
# login()


#Commands:
global curr_usdt_price
global safe_low_point
global safe_high_point

# Sensitive end points to observer fluctuatios: RESET at 00.00 and 100.00
safe_low_point = 00.00
safe_high_point = 100.00

def USDTINR(): #tether
    global curr_usdt_price

    usdtprice = driver.find_element(By.XPATH, "//p[@class='table__data current-price -fw-bolder']").text # Current Crypto Price - working
    curr_usdt_price = usdtprice
    # usdt24h = driver.find_element(By.XPATH, "//p[@class='value -c-red']").text # 24 hours percentage change - NOT working
    curr_time = time.strftime('%H:%M:%S %d/%m/%y', time.localtime())

    print("Current USDT-INR : " + usdtprice + " | " + curr_time)


def BuyUSDT():
    global safe_low_point
    # Buy()
    print()
    print("######################   ⬇   USDT Value Dropped Below Low Margin   ⬇  ######################")
    print("********************** | Buying USDT worth of Rs.100 - Checkout done | **********************")
    print()

    safe_low_point -= 0.01
    print("Updated Low Margin Value : " + str(safe_low_point) + " USDT")

def sell():
    driver.find_element(By.XPATH, "//button[normalize-space()='SELL USDT']").click() # checking out ...
    driver.find_element(By.XPATH, "//input[@id='mat-input-2']").send_keys(100) # filling order value ...
    driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click() # cancelling ...


def SellUSDT():
    global safe_high_point
    # sell()
    print()
    print("######################    ⬆   USDT Value Rose Above High Margin   ⬆    ######################")
    print("********************** | Selling USDT worth of Rs.100 - Checkout done | **********************")
    print()

    safe_high_point += 0.01
    print("Updated High Margin Value : " + str(safe_high_point) + " USDT")


def comparision(): # resolve between comparator of curr value and safe value points - done

    # Conversion
    temp_format_usdt_price = ""
    for char in curr_usdt_price:
        if char.isdigit():
            temp_format_usdt_price += (char)

    usdt_price = float(temp_format_usdt_price) / 100 #Mathematical value of curr_usdt

    if usdt_price <= safe_low_point:
        
        BuyUSDT()

    elif usdt_price >= safe_high_point:
        
        SellUSDT()

    else:
        print("Incoming Orders: Buying At: " + str(safe_low_point) + " | Selling At: " + str(safe_high_point))

# def debug():
#     USDTINR()
#     comparision()
# debug()
    
# Actual Running time:
# while True:
#     try:
#         time.sleep(1) # live update sec interval
#         USDTINR()
#         comparision()
#         print()
#     except Exception as e:
#         driver.quit()
#         break

# Debug Running time with errors:
while True:
    time.sleep(3) # live update sec interval
    USDTINR()
    comparision()
    print()
