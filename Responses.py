from Binance import getBalance, getcoinbaalance
from datetime import datetime

def respons(input_text):
    My_Balance = 'your total balance ist ' + str(round(getBalance(),2)) + ' $'
    return My_Balance

def spot_value(input_text):
    user_message = str(input_text).lower()
    if user_message in ("bnb","lsk","doge","hnt","trb","shib","link","icp","neo","eth","btc"):
        my_coin = getcoinbaalance(user_message)
        return my_coin
    else:
        return "Not supported value! choice on of the following coins bnb, lsk, doge, hnt, trb, shiba, link, icp, neo, eth, btc"