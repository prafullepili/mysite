import pandas as pd
import requests
from WxPortfolio.models import Coins, TransactionCurrency


def result(url):
    hitResponse = requests.get(url)
    return hitResponse.json()

def getLiveData():
    url = 'https://api.wazirx.com/api/v2/tickers'
    jsonData = result(url)
    df = pd.DataFrame(jsonData).loc[['last','name'],:]
    return df

def hit(full=False):
    url = 'https://api.wazirx.com/api/v2/tickers'
    jsonData = result(url)
    if full:
        df = pd.DataFrame(jsonData).loc[:,:]
    else:
        df = pd.DataFrame(jsonData).loc[['last','base_unit','name'],:]
    return df

def units(coin,hitagain=False):
    global df
    if hitagain:
        df = hit('https://api.wazirx.com/api/v2/market-status').T
    if coin:
        return df[df['base_unit'] == coin]
    else:
        return None

def get_assets():
    allassetsResponse = result("https://api.wazirx.com/api/v2/market-status")
    allAssets = pd.DataFrame(allassetsResponse['assets'])
    return allAssets

def run():
    assets = get_assets()
    print("Runing again")
    crs = ['inr','usdt','wrx','btc']
    for cr in crs:
        ts = TransactionCurrency.objects.create(name=cr)
        ts.save()
    hitagain = True
    for coinCode in dict(assets[['type','name']].values).keys():
        for unit in units(coinCode,hitagain).T.columns:
            hitagain = False
            currency = unit.replace(coinCode,'')
            tc = TransactionCurrency.objects.get(name=currency)
            if tc:
                coin = Coins.objects.create(
                    basename = coinCode,
                    fullname = f"{dict(assets[['type','name']].values)[coinCode]}",
                    code = f"{coinCode}{tc}",
                    tc = tc
                    )
                print(coin.id)
                coin.save()