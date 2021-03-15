from bs4 import BeautifulSoup
import requests
import re
import json
import pandas as pd
import csv

url1 = 'http://financials.morningstar.com/finan/financials/getFinancePart.html?&callback=xxx&t={}'
url2 = 'http://financials.morningstar.com/finan/financials/getKeyStatPart.html?&callback=xxx&t={}'

stock = 'FB'

soup1 = BeautifulSoup(json.loads(re.findall(r'xxx\((.*)\)', requests.get(url1.format(stock)).text)[0])['componentData'], 'lxml')
soup2 = BeautifulSoup(json.loads(re.findall(r'xxx\((.*)\)', requests.get(url2.format(stock)).text)[0])['componentData'], 'lxml')



def print_table(soup):
    list = []
    for i, tr in enumerate(soup.select('tr')):
        row_data = [td.text for td in tr.select('td, th') if td.text]
        if not row_data:
            continue
        if len(row_data) < 12:
            row_data = ['X'] + row_data
        for j, td in enumerate(row_data):
            if j==0:
                list.append(str(td))
            else:
                list.append(str(td))
        print()
    return list

c = print_table(soup2)
a=[]
for x in c:
    if x == 'X':
        continue
    elif x == 'Operating Income %':
        continue
    else:
        a.append(x)

b = {a[i]: a[i+1:i+12] for i in range(0, len(a), 12)}

print(c)
