from bs4 import BeautifulSoup
import requests
import re
import json
import pandas as pd

url1 = 'http://financials.morningstar.com/finan/financials/getFinancePart.html?&callback=xxx&t=AAPL'
url2 = 'http://financials.morningstar.com/finan/financials/getKeyStatPart.html?&callback=xxx&t=AAPL'

soup1 = BeautifulSoup(json.loads(re.findall(r'xxx\((.*)\)', requests.get(url1).text)[0])['componentData'], 'lxml')
soup2 = BeautifulSoup(json.loads(re.findall(r'xxx\((.*)\)', requests.get(url2).text)[0])['componentData'], 'lxml')

df = pd.read_html(soup2.prettify())

cdf = []
for x in df:
    cdf.append(x.dropna())

MarginofSales = cdf[0]
Profit = cdf[1]
Growth = cdf[2]
CashFlow = cdf[3]
BalanceSheet = cdf[4]
Liquidity = cdf[5]
Efficiency = cdf[6]

print(Profit)
