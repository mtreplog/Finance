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
                list.append(str('{: >30}'.format(td)))
            else:
                list.append(str('{: ^12}'.format(td)))
        print()
    return list


c = print_table(soup2)

def clean_list(soup):
    strip = []
    clean = []
    for x in c:
        x = x.strip()
        strip.append(x)
    for x in strip:
        try:
            x = int(re.sub(r'[^\d-]+', '', x))
            clean.append(x)
        except ValueError:
            clean.append(x)
    return clean

l = clean_list(c)
print(l)
for x in range(100):
    if l[x] == 'X':
        l.pop(x)
        l.pop(x+1)
print(l)
#b = {l[i]: l[i+1:i+12] for i in range(0, len(l), 12)}

b = {l[i]: l[i+1:i+12] for i in range(0, len(l), 12)}
