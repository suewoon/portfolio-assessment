Stock Price Analysis 
----




Install
----
1. Clone the repo 
```bash
git clone 
``` 
If you want to get the lastest nasdaq symbol list, download directly from NasdaqTrader.com
```bash
wget ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqlisted.txt
```


USAGE 
----
### 1. Get Alpha Advantage API
We'll use [Alpha Advantage API](https://www.alphavantage.co/documentation/). It's free and offer historical equity data as well as the realtime one. 
Get your free api key [here](https://www.alphavantage.co/support/#api-key) and set your environment variable.  
```bash
vim ~/.bash_profile
export ALHPHA_ADVANTAGE_KEY=your-api-key-here
source ~/.bash_profile
``` 

### 2. Download Stock Time Series Data 
This will download time series data by each symbol and save it as a csv file to `prices` directory. 
#### 2-1. Daily Adjusted
[daily adjusted](https://www.alphavantage.co/documentation/#dailyadj)
```python
python download_daily_adjusted.py 
```

#### 2-2. Weekly Adjusted
[weekly adjusted](https://www.alphavantage.co/documentation/#weeklyadj)

3. 

