#!/usr/bin/python3

import sys
import requests
from decimal import Decimal


def getCrytpo(name, icon):
    '''Parses json response and outputs value to polybar'''
    json = requests.get(
            f'https://api.coingecko.com/api/v3/coins/{name}',
            ).json()["market_data"]
    local_price = round(Decimal(json["current_price"]['usd']))
    sys.stdout.write(f'{icon}{local_price} ')


'''
Icons:
    fonts: cryptocoins
    bitcoin:     
    ethereum:    
    monero: 

    fonts: material design icons
    bitcoin-icons: 󰠓
    ethereum-icons: 󰡪
'''


getCrytpo('bitcoin', '󰠓 ')
getCrytpo('ethereum', ' ')
getCrytpo('monero', ' ')
