import requests 
import csv
import os 
import time

api_url = 'https://www.alphavantage.co/query?'
api_key = os.environ['ALPHA_ADVANTAGE']
params = {'function':'TIME_SERIES_DAILY_ADJUSTED',
              'outputsize':'full',
              'datatype':'csv',
             'apikey': api_key}

def download_data_full(symbol):
    '''
    download the full-length time series of 
    up to 20 years of historical data for a symbol
    '''
    params['symbol'] = symbol 

    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        data = response.content.decode('utf-8')
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url))
    result = [data.split(',') for data in data.split('\r\n')]
    return result 

with open("./Guided Project_ Analyzing Stock Prices/nasdaqlisted.txt", 'r') as f:
    stock_listed = f.read()


for line in stock_listed.split("\n")[1:10]:
    symbol = line.split("|")[0]
    print("Downloading {}".format(symbol))
    try:
        result = download_data_full(symbol)
        with open("prices/{}_daily_adjusted.csv".format(symbol.lower()), "w+") as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerows(result)
    except Exception as e:
        print(e)
    time.sleep(1)