import requests 
import concurrent.futures 
import csv
import os 

api_url = 'https://www.alphavantage.co/query?'
api_key =os.environ['ALPHA_ADVANTAGE']
params = {'function':'TIME_SERIES_DAILY_ADJUSTED',
              'outputsize':'full',
              'datatype':'csv',
             'apikey': api_key}

def get_data(symbol):
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
	return symbol, result 

def download_data(symbol, result):
	with open("prices/{}_daily_adjusted.csv".format(symbol.lower()), "w+") as f:
	    writer = csv.writer(f, delimiter=',')
	    writer.writerows(result)

if __name__ == '__main__':
	with open("./Guided Project_ Analyzing Stock Prices/nasdaqlisted.txt", 'r') as f:
		stock_listed = f.read()

	symbols = [line.split('|')[0] for line in stock_listed.split("\n")[1:10]]
	pool = concurrent.futures.ThreadPoolExecutor(max_workers=4)
	result = pool.map(download_file, symbol)
	result = list(result)

	download_data
        