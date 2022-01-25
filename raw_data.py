import os
import datetime
import time
pwd = os.getcwd()

curr_usdt_price = "32.16 INR"

temp_format_usdt_price = ""
for char in curr_usdt_price:
    if char.isdigit():
        temp_format_usdt_price += (char)

usdt_price = float(temp_format_usdt_price) / 100


curr_time = time.strftime('%H:%M:%S %d/%m/%y', time.localtime())
PATH = (pwd + "/Cryptocurrenct-price-bot/chromedriver")
