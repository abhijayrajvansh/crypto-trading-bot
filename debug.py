import os
import datetime
import time

pwd = os.getcwd()

curr_time = time.strftime('%H:%M:%S %d/%m/%y', time.localtime())

PATH = (pwd + "/Cryptocurrenct-price-bot/chromedriver")
print("Curr DIR : " + PATH)
print(curr_time)