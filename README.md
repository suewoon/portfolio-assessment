Stock Price Analysis 
----
[Alpha Vantage](https://www.alphavantage.co/) offers free api calls which enables to fetch financial data such as stock time series and numerous technical indicators. This repository contains a python script which can download stock time series data as a .csv file format in the disk. 

## Install
### 
1. Clone the repo 
```
git clone https://github.com/suewoon/stock-price-analysis.git
``` 
You can query for a specific symbol but sometimes   If you want to get the lastest nasdaq symbol list, download directly from NasdaqTrader.com
```
wget ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqlisted.txt
```

## USAGE 
### 1. Get Alpha Advantage API
We'll use [Alpha Advantage API](https://www.alphavantage.co/documentation/). It's free and offer historical equity data as well as the realtime one. 
Get your free api key [here](https://www.alphavantage.co/support/#api-key) and set your environment variable.  
```
vim ~/.bash_profile
export ALHPHA_ADVANTAGE=your-api-key-here
source ~/.bash_profile
``` 
### 2. Download data 
#### 2-1. Download Stock Time Series 
This will download time series data by each symbol and save it as a csv file to `prices/[FUNCTION]/` directory. 
Without any arguments, it downloads `TIME_SERIES_DAILY_ADJUSTED` data in full. 
```
python download_data.py 
```
Available functions: TIME_SERIES_INTRADAY, TIME_SERIES_DAILY, TIME_SERIES_DAILY_ADJUSTED, TIME_SERIES_WEEKLY,
TIME_SERIES_WEEKLY_ADJUSTED, TIME_SERIES_MONTHLY, TIME_SERIES_MONTHLY_ADJUSTED
```
usage: [-h] [--func FUNCTION] [--outputsize OUTPUTSIZE]

CLI argument for downloading stock time series data

optional arguments:
  -h, --help            show this help message and exit
  --func FUNCTION       function for stock time series data,
                        TIME_SERIES_DAILY_ADJUSTED by defult
  --outputsize OUTPUTSIZE
                        outputsize, compact(recent 100 data points) or full,
                        full by default
```
See more details about [time series data](https://www.alphavantage.co/documentation/) 
#### 2-2 Logging  
When the script is running, you can see debug level logs on the console and logs written into `info.log` and `erros.log` in your working directory. 
This script uses `logging.json` as a logging configuration by default but you can change logging configuration to a spefic file using `LOG_CFG` arguments 
```bash
LOG_CFG=[your_logging.json] python download_data.py
```