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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ LOGIN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def login():
    driver.find_element(By.XPATH, "//span[normalize-space()='Login']").click()
    driver.find_element(By.XPATH, "//input[@id='mat-input-4']").send_keys("abhijayrajvansh01@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='mat-input-5']").send_keys("@BJ@crypto!2711")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(60)
    print("Successfully Logged In To CoinDCX Acc!")
    print()






# Global Variables
global curr_usdt_price
global safe_low_BID
global safe_high_BID
global bot_money
global initial_allowed_money_to_bot
global total_profit
global elevation_amount
global flag
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
global initial_bal
global available_bal



# Starting values: (wallet)
initial_bal = 100.00 # to be updated with driver 
available_bal = 00.00
total_profit = 0



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BIDING~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Sensitive end points to observer fluctuatios: RESET at 00.00 and 100.00
safe_low_BID = 00.00
safe_high_BID = 100.00

elevation_amount = 1 # 0.1 value so huge fluctuation


# Trading Parameters
bot_money = 100.00 # Bot allowed money to buy worth in rupees
initial_allowed_money_to_bot = bot_money
selling_usdt_worth_rupees = bot_money + ((bot_money * 1.2) / 100) # calculation required for 1.2% increase
flag = 0



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  CRYPTOCURRENCY ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def USDTINR(): # Tether
    global curr_usdt_price

    usdtprice = driver.find_element(By.XPATH, "//p[@class='table__data current-price -fw-bolder']").text # Current Crypto Price - working
    curr_usdt_price = usdtprice
    # usdt24h = driver.find_element(By.XPATH, "//p[@class='value -c-red']").text # 24 hours percentage change - NOT working
    curr_time = time.strftime('%H:%M:%S %d/%m/%y', time.localtime())

    print("Profit So Far: " + str(total_profit))
    print("Current USDT-INR : " + usdtprice + " | " + curr_time)




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  BUY AREA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def BuyUSDT():
    global safe_low_BID
    global bot_money
    # Buy()
    print()
    print("######################    ⬇   USDT Value Dropped Below Low Margin   ⬇   ######################")
    print("********************** | Buying USDT worth of Rs." + str(bot_money) + " - Checkout done | **********************")
    print()
    print("Updated Low Margin Value : " + str(safe_low_BID) + " USDT")

    bot_money = 0 # now its time to sell

    # safe_low_BID -= elevation_amount


def buy():
    print()




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  SELL AREA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def SellUSDT():
    global safe_high_BID
    global bot_money
    global total_profit
    # sell()
    print()
    print("######################    ⬆   USDT Value Rose Above High Margin   ⬆    ######################")
    print("********************** | Selling USDT worth of Rs." + str(selling_usdt_worth_rupees) + " - Checkout done | **********************")
    print()
    print("Updated High Margin Value : " + str(safe_high_BID) + " USDT")

    bot_money = initial_allowed_money_to_bot
    total_profit += ((bot_money * 1.2) / 100) - ((bot_money * 0.2) / 100)

    # safe_high_BID += elevation_amount

def sell():
    print()
    # driver.find_element(By.XPATH, "//button[normalize-space()='SELL USDT']").click() # checking out ...
    # driver.find_element(By.XPATH, "//input[@id='mat-input-2']").send_keys(selling_usdt_worth_rupees) # filling order value ...
    # driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click() # cancelling ...




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ COMPARATOR ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def comparision(): # resolve between comparator of curr value and safe value points - done
    global flag
    # Conversion
    temp_format_usdt_price = ""
    for char in curr_usdt_price:
        if char.isdigit():
            temp_format_usdt_price += (char)

    usdt_price = float(temp_format_usdt_price) / 100 #Mathematical value of curr_usdt


    if usdt_price <= safe_low_BID and bot_money != 0:
        BuyUSDT()
        flag = 1

    elif usdt_price >= safe_high_BID and bot_money == 0:
        SellUSDT()
        flag = 0

    else:
        if flag == 0:
            print("Incoming Orders: Buying At: " + str(safe_low_BID))
        else:
            print("Incoming Orders: Selling At: " + str(safe_high_BID))




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUGGER ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#login()



def debug():
    time.sleep(1)
    USDTINR()
    comparision()
    print()

# for i in range(11): # Testing bot
#     debug()

# Debug Running time with errors:
while True:
    time.sleep(1)
    USDTINR()
    comparision()
    print()
    
# Actual Running time:
# while True:
#     try:
#         time.sleep(1)
#         USDTINR()
#         comparision()
#         print()
#     except Exception as e:
#         driver.quit()
#         break

