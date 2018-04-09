import concurrent.futures
import os 
import time
import logging
import numpy as np 
from dateutil.parser import parse 
from statistics import mean

class AlphaVantageData(object):
	_FUNC_RETURN_COLUMN = {
	'TIME_SERIES_INTRADAY':['timestamp', 'open', 'high', 'low', 'close', 'volume'],
	'TIME_SERIES_DAILY':['timestamp', 'open', 'high', 'low', 'close', 'volume'],
	'TIME_SERIES_DAILY_ADJUSTED': ['timestamp','open','high','low','close','adjusted_close'
	,'volume','dividend_amount','split_coefficient']}

	def __init__(self, func):
		"""Initialize the class
		:param func: function for Alpha Vanatage API, type of dataset 
		TIME_SERIES_DAILY_ADJUSTED
		"""
		self.func = func
		self.prices = {}
		self.prices_columnwise = {}

	def readfile_helper(self, filename):
		"""Read csv file from from disk 
		:param filename: filename to read 
		:returns tuple (symbol, data rows)
		"""
		symbol = filename.split('_')[0]
		rows = []
		path = os.path.join('prices', self.datatype, filename)
		with open(path) as f:
			logging.debug("Reading file {}".format(filename))
			rows = f.read().strip()
			rows = [line.split(',') for line in rows]
		return symbol, rows

	def readfile(self, max_workers=4):
		"""Read csv file from disk using multi thread 
		"""
		filenames = [f for f in os.listdir('prices/'+self.datatype) if f.endswith(".csv")]
		try:
			pool = concurrent.futures.ThreadPoolExecutor(max_workers)
			self.prices = pool.map(self.readfile_helper, filenames)
			self.prices = dict(list(self.prices))
		except Exception as e:
			logging.error("Error occured during reading a file", exc_info=True)

	def transform_columnwise(self):
		"""Transform row based data into column based 
		"""
		prices_columnwise = {}
		
		try:
			for symbol, rows in self.prices.items():
				logging.debug("Transforming data for {}".format(symbol))
				headers = rows[0]	# header 
				column_data = {}
				for idx, col_name in enumerate(headers):	# parse data
					values = [p[idx] for p in rows[1:]]
					if idx == 0:	# timestamp type 
						values = [float(v) for v in values]
					else:	# float type 
						values = [parse(v) for v in values]
					column_data[col_name] = values
			prices_columnwise[symbol] = column_data
		except Exception as e:
			logging.error("Error occurred during transforming a dat", exc_info=True)
		self.prices_columnwise = prices_columnwise

	def get_take_average(self, idx_1, idx_2=None):
		"""Take average of a single column or difference between two
		:param idx_1: column index 1
		:param idx_2: column index 2 (optional)
		"""
		average = {}
		columns = AlphaVantageData._FUNC_RETURN_COLUMN[self.func]
		try:
			col_1 = columns[idx_1]
			if not idx_2:	# average of column idx_1
				for symbol, values in self.prices_columnwise.items():
					average[symbol] = mean(values[col_1])
			else:	# average of column (idx_1 - idx_2)
				col_2 = columns[idx_2]
				for symbol, values in self.prices_columnwise.items():
					average[symbol] = mean([i-j for i, j in zip(values[col_1],values[col_2])])
		except Exception as e:
			logging.error("Error occurred during taking average", exc_info=True)
		return average 

	def get_most_traded(self):
		"""Return the most traded stock for each time unit(daily, weekly..)
		"""
		trades = {}
		for symbol, values in self.prices_columnwise.items():
			for i, date in enumerate(values['timestamp']):
				if date not in trades:
					trades[date] = []
				trades[date].append([symbol, values['volume'][i]])
		most_traded = []
		for k, v in trades.items():
			ordered = sorted(v, key=lambda x:x[1])
			most_traded.append([k, ordered[-1][0]])
		return most_traded

	def get_most_profitable(self, timestamp, inflation=None):
		"""Return what would have been the most profitable stock now 
		if you had bought before
		:param timestamp: date bought the stock 
		:param inflation: inflation rate between now and the given timestamp
		"""
		most_profitable = []
		timestamp = parse(timestamp)
		if not inflation: inflation = 1 
		logging.info('Start computing most profitable stocks')
		try:
			for symbol, values in self.prices_columnwise.items():
				idx = values['timestamp'].index(timestamp)
				percentage = (values['close'][-1] - 
					values['close'][idx]*inflation)/(values['close'][idx]*inflation)
				most_profitable.append([symbol, percentage*100])
			most_profitable = sorted(most_profitable, key=lambda x: x[1], reverse=True)
		except Exception as e:
			logging.err("Error occurred during getting would have been the most profitable stocks", exc_info=True)
		logging.info('Done computing most profitable stocks')
		return most_profitable

	def get_best_to_short(self):
		"""Return what whould have been the best time for short selling 
		"""
		#TO-DO

	def get_biggest_change_between(self, timstamp):
		"""Return which stocks have the biggest changes between the closing price and
		the next day open 
		"""
		#TO-DO

	def get_steady_increases(self, symbol):
		"""Return time periods when the stock prices in steady increase 
		"""
		#TO-DO

	def get_steady_decreases(self, symbol):
		"""Return time periods when the stock prices in steady decrease 
		"""
		#TO-DO
	



