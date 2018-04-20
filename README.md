portfolio-assessment
----
This repository contains a python module for building your own portfolio assessment pipeline. 

## Install

1. Clone the repo 
```
git clone https://github.com/suewoon/portfolio-assessment.git
```

2. Install requirements 
```
pipenv install
```

## USAGE 
### 1. Get Alpha Advantage API
This `alphavantage` module contains a client for [Alpha Advantage API](https://www.alphavantage.co/documentation/). Since this client has limited usage, only requests for stock market related data are available. Get your free api key [here](https://www.alphavantage.co/support/#api-key) and set your environment variable. 

```
vim ~/.bash_profile
export ALHPHA_ADVANTAGE=your-api-key-here
source ~/.bash_profile
``` 

Initialize client instance with a list of symbols, which could be stocks in your portflio.
Requests for symbols will be issued asynchronously and corresponding json 
responses will be returned in generator type.
```python
from alphavantage.avstockclient import AlphaVantageStockClient
# specify stock symbols you'd like to get information about
symbols=['aapl', 'amzn', 'spot', 'nvda','intu', 'hrs', 'ibm', 'msft']
client = AlphaVantageStockClient(symbols=symbols)
responses = client.get_get_daily() # generator
```

## 2. Make pipeline 