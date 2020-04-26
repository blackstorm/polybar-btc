#!/usr/bin/env python3

import json,sys,requests

response = requests.get('https://api.huobi.pro/market/trade?symbol=btcusdt')
data = response.json()
price = data['tick']['data'][0]['price']
sys.stdout.write("BTC: $" + str(price))
sys.stdout.flush()
