#!/usr/bin/python3

import sys
import requests
from decimal import Decimal


def getFiat(currency, baseCurrency='USD'):
    '''Parses json response and outputs value to polybar'''
    return round(Decimal(requests.get(
        f'https://freecurrencyrates.com/api/action.php?do=cvals&\
                iso={currency}&f={baseCurrency}&v=1&s=cbr',
        ).json()[f'{currency}']), 2)


sys.stdout.write(f'󰆱{getFiat("RUB")} ')
sys.stdout.write(f'󰡥{getFiat("KZT")}({getFiat("KZT", "RUB")}) ')
sys.stdout.write(f'󰞼{getFiat("JPY")} ')
sys.stdout.write(f'󰞿{getFiat("HKD")}')
