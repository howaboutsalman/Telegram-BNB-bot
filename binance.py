#//////////////////////////////////////////////////////////////////////
import binance.client
from binance.client import Client 
import config as API_BNB
import websockets
import requests
import json
Pkey = API_BNB.Pkey
Skey = API_BNB.Skey
#//////////////////////////////////////////////////////////////////////
def getBalance():
    client = Client(api_key=Pkey,api_secret=Skey)
    Coins = ["SOLUSDT","ETHUSDT","HNTUSDT","LSKUSDT","TRBUSDT","CELOUSDT","DOGEUSDT","NEOUSDT","LINKUSDT","BNBUSDT"]
    info = info = client.get_all_tickers()
    Get_spot = str(client.get_account_snapshot(type='SPOT'))
    Totalbalance = 0
    for x in info:
        for my_coins in Coins:
            if my_coins == x["symbol"]:
                formatsymob= x["symbol"]
                get_balance = client.get_asset_balance(asset= formatsymob.replace("USDT",""))
                USDTBalance= float(x["price"]) * float(get_balance["free"])
                Totalbalance = Totalbalance + USDTBalance
    return Totalbalance
    
def getcoinbaalance(coin):
    client = Client(api_key=Pkey,api_secret=Skey)
    #choice the coin for showing the balance of it
    coin = coin
    #call all info of the choiced Coin
    blanace = client.get_asset_balance(asset= coin)
    #set value for the variable FreeBalance 
    FreeBalance = float(blanace['free'])
    #get all traded Order
    Symbole = str(blanace['asset']) + 'USDT'
    coinprise = client.get_avg_price(symbol= Symbole)
    coinprise = coinprise['price']  
    return f"{Symbole}: {FreeBalance}\nin USDT: {round(float(coinprise)*FreeBalance, 2)}"
