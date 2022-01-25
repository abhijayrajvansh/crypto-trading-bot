
from functools import total_ordering


usdt_price = 81.43
safe_low_BID = 80.00


safe_high_BID = safe_low_BID + ((safe_low_BID * 1.2) / 100)

print("Low BID : " + str(safe_low_BID))
print("High BID : " + str(safe_high_BID))
print()
bot_money = 100

total_profit = 0

def BuyUSDT():
    print("buying usdt...")

def SellUSDT():
    print("selling usdt...")

if usdt_price <= safe_low_BID and bot_money != 0:
    BuyUSDT()
elif usdt_price >= safe_high_BID and bot_money == 0:
    SellUSDT()
else:
    print("looking for elevation...")

selling_usdt_worth_rupees = bot_money + ((bot_money * 1.2) / 100)
total_profit += ((bot_money * 1.2) / 100) - ((bot_money * 0.2) / 100)
print(total_profit)

