import grequests 
import requests
import os 
import inspect 
from functools import wraps
import logging 

class AlphaVantageDecorator:
	_ENDPOINT = 'https://www.alphavantage.co/query?'

	def __init__(self, symbols, num_sessions=10):
		self.apikey = os.environ.get('ALPHA_ADVANTAGE', None)
		if not self.auth:
			raise ValueError("cannot find alphavantage api key")
		if not isinstance(symbols, list) or len(symbols) == 0:
			raise TypeError("symbols must be a list consists of more than one symbol")
		self.symbols = symbols 
		self.num_seesions = num_sessions 
		self.sessions = [requests.Session() for i in range(self.num_sessions)]


	@classmethod
	def _return_response(cls, func):
		"""Decorator for issuing multiple http requests 
		"""
		argspec = inspect.getfullargspec(func)
		@wraps(func)
		def wrapper(self, *args, **kwargs):
			func_name = func(self, *args, **kwargs)
			params = {'apikey':self.apikey, 'function':func_name}
			base_url = AlphaVantageDecorator._ENDPOINT

			for arg_name in argspec.args[1:]: # requests parameters setting from arguments 
				if (arg_name in kwargs) and kwargs[arg_name]: # only specified parameters 
					params[arg_name] = kwargs[arg_name]

			reqs = []
			session_group = 0
			
			try:
				for symbol in self.symbols:
					params['symbol'] = symbol
					reqs.append(grequests.get(base_url,
						session=self.sessions[session_group % self.num_sessions],
						params=params))
					session_group += 1
					assert(len(reqs)>0), "empty requests"
				responses = grequests.imap(reqs, size=self.num_sessions)
			except Exception as e:
				pass

			if not responses: 
				raise ValueError("empty responses")
			return (r.json() for r in responses if r.status_cod==200)

	@classmethod 
	def _logger(cls, func):
		"""Logger for info and debugging
		"""
		@wraps(func)
		def wrapper(self, *args, **kwargs):
			logging.info('func - {}, args - {}, kwargs - {}'.format(func.__name__, args, kwargs))
			return func(*args, **kwargs)

		return wrapper