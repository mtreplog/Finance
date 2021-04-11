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
cdf2 = []
for x in df:
    cdf.append(x.dropna())
for x in df2:
    cdf2.append(x.dropna())


MarginofSales = pd.DataFrame(cdf[0])
Profit = pd.DataFrame(cdf[1])
Growth = pd.DataFrame(cdf[2])
CashFlow = pd.DataFrame(cdf[3])
BalanceSheet = pd.DataFrame(cdf[4])
Liquidity = pd.DataFrame(cdf[5])
Efficiency = pd.DataFrame(cdf[6])
Financials = pd.DataFrame(cdf2[0])
print(Liquidity)



def columnsdate(x):
    df = x
    df.columns = [(datetime.strptime(x[:4],'%Y')).year if x[0] == '2' else x for x in df.columns]
    return df


def Leaders(x):
       df = x
       df = df.set_index('Liquidity/Financial Health')
       #df[change] = df.pct_change()

       df = df.replace('-',np.NaN)
       return df

def CleanDF():
    df = CleanDF(Liquidity).T
    df1 = CleanDF(Profit).T
    DE=df['Debt/Equity']
    CR=df['Current Ratio']
    ROE = df1['Return on Equity %']
    dit = {'D/E':DE, 'Current Ratio':CR,'ROE':ROE}
    df=pd.DataFrame(data=dit)
    DE.plot()
    CR.plot()
    print(df)
    return print("1) D/E ratio of below .5 is preferred. Debt can disrupt even the best business because it limits flexbility \n 2) To maintain flexiblity you should also make sure that you are getting more cash in than what is going out. This can be measured by teh current ratio, which should be great than 1.5 \n 3)Vigilant leaders also aim to make a decent ROE Above 8% consistently over a period of ten years is a strong indication of great management")





def Stable():
    df8 = CleanDF(Financials).T
    df1 = CleanDF(Profit).T
    ROE = df1['Return on Equity %']
    Dividend = df8['Dividends  USD']
    Book = df8['Book Value Per Share *  USD']
    EPS = df8['Earnings Per Share  USD']
    dit = {'ROE':ROE, 'Dividend':Dividend,'Book Value':Book,'EPS':EPS}
    df=pd.DataFrame(data=dit)
    #df.plot(subplots=True, figsize=(6, 6)); plt.legend(loc='best')
    fig, axes = plt.subplots(nrows=2, ncols=2)
    df['ROE'].plot(ax=axes[0,0]); axes[0,0].set_title('ROE')
    df['Dividend'].plot(ax=axes[0,1]); axes[0,1].set_title('Dividend')
    df['Book Value'].plot(ax=axes[1,0]); axes[1,0].set_title('Book Value')
    df['EPS'].plot(ax=axes[1,1]); axes[1,1].set_title('EPS')
    return df
Stable()
