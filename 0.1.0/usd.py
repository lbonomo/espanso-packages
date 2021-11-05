#!/usr/bin/env python
import requests

URL = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
# API Alternativa 'https://api.bluelytics.com.ar/v2/latest'
json = requests.get(URL).json()
value = "{:>8}"
print()
print(' 💵 |  Compra  |   Venta  |')
print('----|----------|----------|')

for index, emoji in enumerate(('🟢', '🔵')):
    compra = value.format(json[index]['casa']['compra'][:-1])
    venta = value.format(json[index]['casa']['venta'][:-1])

    print(f" {emoji} | {compra} | {venta} |")

print()
