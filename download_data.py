import requests 
import concurrent.futures 
import csv
import datetime
import os 
import time
import logging
import logging.config
import json 
import argparse


base_url = 'https://www.alphavantage.co/query?'
api_key = os.environ.get('ALPHA_ADVANTAGE', None)
params = {'function':'TIME_SERIES_DAILY_ADJUSTED',
              'outputsize':'full',
              'datatype':'csv',
             'apikey': api_key}

# logging in json format 
def setup_logging(default_path='logging.json', default_level=logging.INFO, env_key='LOG_CFG'):
    """Setup logging configuration
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

def download_data(symbol):
	"""Return symbol and csv format of daily adjusted(date, open, high, low, close, split/dividend-adjusted close, 
	volume) in a tuple

	:param symbol: the symbol we want to get the data of 
	"""
	params['symbol'] = symbol 
	response = requests.get(base_url, params=params)
	result = None
	
	if response.status_code == 200:
		logging.info("Getting response content of {}".format(symbol))
		data = response.content.decode('utf-8')
		result = [data.split(',') for data in data.split('\r\n')]
	else:
		try:
			response.raise_for_status()
		except Exception as e:
			logging.error('[!] HTTP {0} calling [{1}]'.format(response.status_code, base_url)
				, exc_info=True)
	return symbol, result 

def write_data_to_csv(symbol, result):
	"""Write data into disk as a csv format, skip if it already exists
	"""
	path = os.path.join('prices',params['function'])
	path = path+"/{}_daily_adjusted_{}.csv".format(symbol.lower(), datetime.date.today().strftime("%Y%m%d"))
	if os.path.isfile(path): # skip if it exitst
		logging.info("File already exits, skip writing..")
	else: 
		with open(path, "w+") as f:
			writer = csv.writer(f, delimiter=',')
			writer.writerows(result)
			logging.info("Done writing {} data into disk...".format(symbol))

if __name__ == '__main__':
	# get args 
	arg_parser = argparse.ArgumentParser(prog='', description='CLI argument for downloading stock time series data')
	arg_parser.add_argument('--func', dest='function', help='function for stock time series data, TIME_SERIES_DAILY_ADJUSTED by default', required=False)
	arg_parser.add_argument('--outputsize', dest='outputsize', help='outputsize, compact(recent 100 data points) or full, full by default', required=False)
	args = arg_parser.parse_args()
	if outputsize: params['outputsize'] = args.outputsize
	if function: params['function'] = args.function

	# setup log 
	setup_logging()
	logger = logging.getLogger(__name__)	
	
	# check api key is valid 
	if not api_key:
		try:
			raise ValueError("API key is not valid, get your Alpha Vantage API key here"
				"https://www.alphavantage.co/support/#api-key")
		except Exception as e:
			logger.error('Failed to get valid API key', exc_info=True)

	# open listed stock on nasdaq 
	with open("./nasdaqlisted.txt", 'r') as f:
		logger.info('Start reading nasdaq list..')
		stock_listed = f.read()
	symbols = [line.split('|')[0] for line in stock_listed.split("\n")[1:]]

	# split all the stocks into a chunk unit
	ind = list(range(0, len(symbols), len(symbols)//100))
	for i in range(len(ind)-25):
		try:
			with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
				logger.debug('Start #{}chunk executing...'.format(i+1))
				result = executor.map(download_data, symbols[ind[i]:ind[i+1]])
				result = list(result)
				for r in result:
					write_data_to_csv(symbol=r[0], result=r[1]) 
		except Exception as e:
			logger.error('Failed downloading a file', exc_info=True)
		time.sleep(0.5)

        