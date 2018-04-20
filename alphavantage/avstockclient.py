from avdecorator import AlphaVantageDecorator as avd

class AlphaVantageStockClient(avd):

	@avd._return_response
	def get_intraday(self, interval, outputsize=None):
		"""Returns intraday timeseries (timestamp, open, high, low, close, volume) of 
		equities specified  updated 
		
		Args:
		interval (str): time interval two consecutive data points in the time series. 
		The follwing are supported, 1min, 5min, 15min, 30min, 60min
		outputsize (str, optional): compact or full, compact by default 
		"""
		return "TIME_SERIES_INTRADAY"

	@avd._return_response
	def get_daily(self, outputsize=None):
		"""Returns daily time series(date, daily open, daily high, daily low, 
		daily close, daily volume) of equities specified 
		
		Args:
		outputsize (str, optional): compact or full, compact by default 
		"""
		return "TIME_SERIES_DAILY"

	@avd._return_response
	def get_daily_adjusted(self, outputsize=None):
		"""Returns daily time series (date, daily open, daily high, daily low, daily close,
		 daily volume, daily adjusted close, and split/dividend events) of equities specified

		Args:
		outputsize (str, optional): compact or full, compact by default 
		"""
		return "TIME_SERIES_DAILY_ADJUSTED"

	@avd._return_response
	def get_weekly(self, outputsize=None):
		"""eturns weekly time series (last trading day of each week, weekly open, weekly high, 
		weekly low, weekly close, weekly volume) of equities specified

		Args:
		outputsize (str, optional): compact or full, compact by default 
		"""
		return "TIME_SERIES_WEEKLY"

	@avd._return_response
	def get_batch_stock_quotes(self):
		"""Returns mutliple stock quotes during US market hours, updated realtime

		Args:
		symbols (str): up to 100 symbols seperated by comma. If more than 100 symbols are included, 
		the API will return quotes for the first 100 symbols.
		"""
		return "BATCH_STOCK_QUOTES"

	@avd._return_response
	def get_sma(self, interval, time_period, series_type):
		"""Returns the simple moving average (SMA) for equities specified

		Args:
		interval(str): Time interval between two consecutive data points in the time series(
		1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)
		time_perioed(int): Number of data points used to calculate each sma value. 
		series_type(str): desired price type in the time series(close, open, high, low)
		"""
		return "SMA"

	@avd._return_response
	def get_ema(self, interval, time_period, series_type):
		"""Returns the exponential moving average (EMA) values for equities specified

		Args:
		interval(str): Time interval between two consecutive data points in the time series(
		1min, 5min, 15min, 30min, 60min, daily, weekly, monthly)
		time_perioed(int): Number of data points used to calculate each ema value. 
		series_type(str): desired price type in the time series(close, open, high, low)
		"""
		return "EMA"

	@avd._return_response
	def get_macd(self, interval, series_type, fastperiod=None, slowperiod=None, signalperiod=None):
		"""Returns the moving average convergence / divergence (MACD) values for equities specified

		Args:
		interval(str): Time interval between two consecutive data points in the time series
		series_type(str): desired price type in the time series(close, open, high, low)
		fastperiod(int, optional): 12 by default
		slowperiod(int, optional): 26 by default
		signalperiod(int, optional): 9 by default 	  
		"""
		return "MACD"

	@avd._return_response
	def get_rsi(self, interval, time_period, series_type):
		"""Returns relative strength index (RSI) values

		Args:
		interval(str): Time interval between two consecutive data points in the time series
		series_type(str): desired price type in the time series(close, open, high, low)
		"""
		return "RSI"

	@avd._return_response
	def get_adx(self, interval, time_period, series_type):
		"""Returns relative strength index (RSI) values

		Args:
		interval(str): Time interval between two consecutive data points in the time series
		time_perioed(int): Number of data points used to calculate each adx value. 
		"""
		return "ADX"

	@avd._return_response
	def get_stoch(self, interval, fastkperiod=None, slowkperiod=None, slowdperiod=None, slowkmatype=None, slowdmatype=None):
		"""Returns the stochastic oscillator (STOCH) values for equities specified 

		Args:
		interval(str): Time interval between two consecutive data points in the time series
		fastkperiod(int, optional): The time period of the fastk moving average. Positive integers are accepted. By default, 5
		slowkperiod(int, optional): The time period of the slowk moving average. Positive integers are accepted. By default, 3
		slowdperiod(int, optional): The time period of the slowd moving average. Positive integers are accepted. By default, 3
		slowkmatype(int, optional): Moving average type for the slowk moving average. By default, slowkmatype=0. Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA), 1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA), 3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA), 5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 7 = Kaufman Adaptive Moving Average (KAMA), 8 = MESA Adaptive Moving Average (MAMA)
		slowdmatype(int, optional): Moving average type for the slowd moving average. By default, slowdmatype=0. Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA), 1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA), 3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA), 5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 7 = Kaufman Adaptive Moving Average (KAMA), 8 = MESA Adaptive Moving Average (MAMA)
		"""
		return "STOCHF"

	@avd._return_response
	def get_cci(self, interval, time_period):
		"""Returns relative strength index (RSI) values

		Args:
		interval(str): Time interval between two consecutive data points in the time series
		time_perioed(int): Number of data points used to calculate each cci value. 
		"""
		return "CCI"

	@avd._return_response
	def get_aroon(self, interval, time_period):
		"""Returns relative strength index (RSI) values

		Args:
		interval(str): Time interval between two consecutive data points in the time series
		time_perioed(int): Number of data points used to calculate each arooon value. 
		"""
		return "AROON"

	@avd._return_response
	def get_brands(self, interval, time_period, series_type, nbdevup=None, nbdevdn=None, matype=None):
		"""Returns the Bollinger bands
		
		Args:
		interval(str): Time interval between two consecutive data points in the time series
		time_perioed(int): Number of data points used to calculate each BRANDS value
		series_type(str): desired price type in the time series(close, open, high, low)
		nbdevup(int, optional):The standard deviation multiplier of the upper band. Positive integers are accepted. By default, nbdevup=2
		nbdevdn(int, optional):The standard deviation multiplier of the lower band. Positive integers are accepted. By default, nbdevdn=2
		matype(int, optional): Moving average type of the time series. By default, matype=0. Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA), 1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA), 3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA), 5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 7 = Kaufman Adaptive Moving Average (KAMA), 8 = MESA Adaptive Moving Average (MAMA).
		"""
		return "BRANDS"

	@avd._return_response
	def get_ad(self, interval, time_period):
		"""Returns the Chaikin A/D line (AD) values

		Args:
		interval(str): Time interval between two consecutive data points in the time series
		"""
		return "AD"

	@avd._return_response
	def get_obv(self, interval, time_period):
		"""Returns the on balance volume (OBV) values.

		Args:
		interval(str): Time interval between two consecutive data points in the time series
		"""
		return "OBV"

	@avd._return_response
	def add_symbol(self, symbol):
		"""Adds a new symbol to the list 
		"""
		symbol = symbol.lower()
		if symbol not in self.symbols:
			self.symbols.append(symbol)
		return True

