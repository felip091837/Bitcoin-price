#!/usr/bin/python

#felipesi - 2020

import requests
import json
import time
import locale

api = 'https://blockchain.info/ticker'
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def get_value():
    response =  requests.get(api)
    data = json.loads(response.content)
    value = data['BRL']['last']
    brl = locale.currency(value, grouping=True, symbol=None)
    return brl

def view():
    value = get_value()
    new_price = True
    print "1 BTC = %s BRL"%value

    while True:
        current_value = get_value()
        if current_value < value:
            print "[-] DOWN, 1 BTC = %s BRL [-]"%current_value
            new_price = True
        elif current_value > value:
            print "[+] UP, 1 BTC = %s [+]"%current_value
            new_price = True
        else:
            if new_price == True:
                print "--Waiting new price--\n"
                new_price = False
        value = current_value
        time.sleep(1)

view()
