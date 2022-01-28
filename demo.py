#/
#    author:   abhijayrajvansh
#    created:  26.01.2022 01:12:16
#/
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options #to by-pass chrome broswer notification
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import os
import datetime
import time

pwd = os.getcwd()
PATH = Service(pwd + "/chromedriver")

# url = input("Enter Cryptocoin Link : ")
url = "https://coindcx.com/trade/BTCINR"

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
    driver.find_element(By.XPATH, "//input[@id='mat-input-4']").send_keys("")
    driver.find_element(By.XPATH, "//input[@id='mat-input-5']").send_keys("")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(40)
    print("``````````````````````````````````````````")
    print("| Successfully Logged In To CoinDCX Acc! |")
    print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")


# Coin Details:
global cryptoname
global cryptoprice

# Global Variables:
global curr_coin_price
global safe_low_BID
global safe_high_BID
global bot_money
global initial_allowed_money_to_bot
global brokerage_amt
global total_profit
global elevation_amount
global flag
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
total_profit = 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BIDING_MARGIN~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Sensitive end points to observer fluctuatios: RESET at 00.00 and 100.00
print()
safe_low_BID = 80.00
# safe_low_BID = input("Enter Low BID Value : ")
# safe_low_BID = float(safe_low_BID)

safe_high_BID = safe_low_BID + ((safe_low_BID * 1.5) / 100) # Automatic High BID will be set to 1.5% increase (0.2 & 0.2 brokerage_amount)
print("High BID Margin Set To : " + str(safe_high_BID) + " At 1.4% increase")
# safe_high_BID = input("Enter High BID Value : ")
# safe_high_BID = float(safe_high_BID)

percent_increase = (100 * (safe_high_BID - safe_low_BID)) / safe_low_BID
elevation_amount = 1 # 0.1 value so huge fluctuation


# Trading Parameters
print()
bot_money = 100 #money given to bot for trading
# bot_money = input("Enter Bot Money : ") # Bot allowed money to buy worth in rupees
# bot_money = float(bot_money)

initial_allowed_money_to_bot = bot_money
selling_coins_worth_rupees = bot_money + ((bot_money * (percent_increase - 0.1)) / 100) # calculation required for 1.4% increase
#highest bidding ka percent diff with low is selling...

# Start from buying or selling: 
flag = 0 # 0: to start from buying order | 1: to start from selling order

# 0.2 % of each trade for paying as brokerage money to exchange:
brokerage_amt = 0

def BIDING_MARGIN():
    print("Low BID Margin : " + str(safe_low_BID) + " | High BID Margin : " + str(safe_high_BID))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  CRYPTOCURRENCY ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def CRYPTOCURRENCY(): #Coin
    global cryptoname
    global curr_coin_price

    cryptoname = driver.find_element(By.XPATH, "//span[@class='-fw-bold -c-hide-on-portrait']").text
    cryptoprice = driver.find_element(By.XPATH, "//p[@class='table__data current-price -fw-bolder']").text # Current Crypto Price - working
    curr_coin_price = cryptoprice
    curr_time = time.strftime('%H:%M:%S %d/%m/%y', time.localtime())

    # print("Current " + cryptoname + " : " + cryptoprice + " | " + curr_time)
    print("~~~~~~~~~~~~~~~~~~~~(" + curr_time + ")~~~~~~~~~~~~~~~~~~~~")
    print("Coin Name      : " + cryptoname + "   | Curr Coin Price : " + cryptoprice)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  BUY AREA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def BuyCRYPTO():
    global safe_low_BID
    global bot_money
    global brokerage_amt
    # Buy()
    print("\nExecuting Buying Order ...\n")
    print("######################    ⬇   " + cryptoname + " Value Dropped Below Low Margin   ⬇   ######################")
    print("********************** | Buying " + cryptoname + " worth of Rs." + str(bot_money) + " - Checkout done | **********************\n")

    brokerage_amt += ((bot_money * 0.2) / 100)
    bot_money = 0 # now its time to sell coins, yeaayy!


    # print("Updated Low Margin Value : " + str(safe_low_BID) + " " + cryptoname)
    # safe_low_BID -= elevation_amount
def buy():
    print()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  SELL AREA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def SellCRYPTO():
    global safe_high_BID
    global bot_money
    global total_profit
    global brokerage_amt
    print("\nExecuting Selling Order ...\n")
    # sell()
    print("######################    ⬆   " + cryptoname + " Value Rose Above High Margin   ⬆    ######################")
    print("********************** | Selling " + cryptoname + " worth of Rs." + str(selling_coins_worth_rupees) + " - Checkout done | **********************" + '\n')
    # print("Updated High Margin Value : " + str(safe_high_BID) + " " + cryptoname)

    bot_money = initial_allowed_money_to_bot # now its time to buy, lessgoo!
    # total_profit += ((bot_money * (percent_increase)) / 100) - ((bot_money * 0.2) / 100)
    brokerage_amt += ((selling_coins_worth_rupees * 0.2) / 100)
    total_profit += selling_coins_worth_rupees - bot_money - brokerage_amt
    # safe_high_BID += elevation_amount

def sell():
    print()
    # driver.find_element(By.XPATH, "//button[normalize-space()='SELL USDT']").click() # checking out ...
    # driver.find_element(By.XPATH, "//input[@id='mat-input-2']").send_keys(selling_coins_worth_rupees) # filling order value ...
    # driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click() # cancelling ...




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ COMPARATOR ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def COMPARISION(): # resolve between comparator of curr value and safe value points - done
    global flag
    # Conversion
    temp_format_coin_price = ""
    for char in curr_coin_price:
        if char.isdigit():
            temp_format_coin_price += (char)

    coin_price = float(temp_format_coin_price) / 100 #Mathematical value of curr_crypto_coin

    if coin_price <= safe_low_BID and bot_money != 0:
        BuyCRYPTO()
        flag = 1

    elif coin_price >= safe_high_BID and bot_money == 0:
        SellCRYPTO()
        flag = 0

    else:
        if flag == 0:
            print("       Incoming Buying Order At : " + str(safe_low_BID) + " " + cryptoname)
        else:
            print("       Incoming Selling Order At : " + str(safe_high_BID) + " " + cryptoname)

    print("```````````````````````````````````````````````````````````")
    print("| Profit So Far: " + str(total_profit))
    print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUGGER ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# login()

# driver.find_element(By.XPATH, "//button[@class='cta cta--red']").click()
# time.sleep(3)

# text = driver.find_element(By.Cryptocurrency-Price-Bot , "cdk-drag d-buy-sell-bottomsheet-everything c-buy-sell-bottomsheet")

# driver.find_element(By.XPATH, "//input[@id='mat-input-7']").send_keys(6969)

# driver.find_element(By.XPATH, "//input[@id='mat-input-1']").send_keys(123)
# assert "DragnDrop" in driver.title





# driver.find_element(By.XPATH, '//*[@id="mat-radio-8"]/label/span[1]/span[1]').click()



# Debug Running time with errors:
# while True:
#     time.sleep(1)
#     CRYPTOCURRENCY()
#     BIDING_MARGIN()
#     COMPARISION()
#     print('\n\n')
    
# Actual Running time:
# while True:
#     try:
#         time.sleep(1)
#         CRYPTOCURRENCY()
#         BIDING_MARGIN()
#         COMPARISION()
#         print('\n')
#     except Exception as e:
#         driver.quit()
#         break
