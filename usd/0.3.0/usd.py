#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import argparse
from datetime import datetime

def args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument( '--option', default='table' )
    args = parser.parse_args()
    return args.option

def table():
    json = getData()
    value = "{:>8}"
    print()
    print('| 💵 |  Compra  | Promedio |   Venta  |')
    print('|----|----------|----------|----------|')

    # Monedas
    monedas = {
        'oficial': {'emoji': '🟢' },
        'blue': {'emoji':'🔵' }
    }

    for moneda in monedas:
        compra = value.format(json[moneda]['value_buy'])
        promedio= value.format(json[moneda]['value_avg'])
        venta = value.format(json[moneda]['value_sell'])
        print(f"| {monedas[moneda]['emoji'] } | {compra} | {promedio} | {venta} |")

    print()

    date_time_str = json['last_update'] # 2021-11-05T19:55:45.223856-03:00
    date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S.%f%z')

    print("Actualizado: %s" % date_time_obj.strftime("%d/%m/%Y %H:%M"))

def getData():
    URL = 'https://api.bluelytics.com.ar/v2/latest'
    json = requests.get(URL).json()
    return json

def blue():
    value = "{:>8}"
    json = getData()
    curr = {
        "buy": json['blue']['value_buy'],
        "avg": json['blue']['value_avg'],
        "sell": json['blue']['value_sell']
    }
    return curr

def main():
    options = args()
    if options == 'table':
        table()
    if options == 'blue-average':
        print(blue()['avg'])

main()