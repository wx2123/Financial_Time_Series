# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""""""""

Gateway to financial time series analysis

Created on Thu Mar  5 10:26:32 2020

@author: Wujian

"""""""""""""""""""""""""""""""""""""""""""""""""""""


"""""""""""""""""""""""""""""""""""""""""""""""""""""
In the past, you can download data from Yahoo!Finance
"""""""""""""""""""""""""""""""""""""""""""""""""""""


import pandas as pd
BA = pd.read_csv("D:/2002_Fin_TS/BA.csv")
BA.tail(30)
BA.info()
BA.describe()
BAclose = BA['Adj Close']
BAclose.plot()


# Import some packages
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as pdr
# pip install pandas_datareader if you don't have it

# Set start and end date
start='2010-12-31'
end='2020-03-23'

#import datetime
#end=datetime.date.today()

"""""""""""""""""""""""""""""""""""""""""""""""""""""
Now, you can read stock data online
"""""""""""""""""""""""""""""""""""""""""""""""""""""

TSLA = pdr.get_data_yahoo('Tsla', start=start, end=end)
BA = pdr.get_data_yahoo('BA', start=start, end=end)


# Manipulate data with Pandas: Stock X-Ray!
TSLA.info
TSLA.head()
TSLA.shape
TSLA.Close
TSLA.Close.head()
TSLA.Close.tail()

TSLA['Adj Close'].head()
TSLA['Adj Close'].tail()

TSLA.iloc[10:13]

TSLA[['Close','Volume']].head()

BA[['Close','Adj Close']].head()
BA[['Close','Adj Close']].tail()


#TSLA.loc[3:8,['Close','Volume']]

TSLA.Volume # shares


# basic statistics
TSLA['Close'].mean()
TSLA['Close'].min()
TSLA['Close'].max()
TSLA['Close'].describe()

# add new variables to dataframe
TSLA['pct_return'] = TSLA['Close'].pct_change()
TSLA.head()
TSLA['pct_return'].describe()


TSLA['log_price'] = np.log(TSLA.Close)
TSLA['log_return'] = TSLA['log_price'].diff()
TSLA.head()

# Data filter
high = (TSLA['pct_return'] > 0.18)
TSLA_high = TSLA[high]
TSLA_high.head(10)

# Test for normality
from scipy.stats import shapiro
stat, p = shapiro(TSLA['log_return'].dropna())
print('Statistics=%.3f, p=%.3f' % (stat, p))

# Explain in plain English
alpha = 0.05
if p > alpha:
	print('Sample looks Gaussian (fail to reject H0)')
else:
	print('Sample does not look Gaussian (reject H0)')


# Data visualization

import matplotlib.dates as mdate

plt.plot(TSLA.Close,'r',linewidth=0.8, markersize=12,label='Tesla Stock price')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Price')
ax = plt.gca()   
ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))  
plt.xticks(pd.date_range(start,end,freq='2y')) 
plt.yticks(fontsize=10,rotation=0)
plt.xlim(start,end)
plt.grid(c='k',linestyle='--')
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.show()



plt.plot(TSLA.pct_return,'r',linewidth=0.8, markersize=12,label='Tesla pct return')
plt.legend()
plt.xlabel('Date')
plt.ylabel('pct return')
ax = plt.gca()   #
ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))  # 
plt.xticks(pd.date_range(start,end,freq='2y')) #
plt.yticks(fontsize=10,rotation=0)
plt.xlim(start,end)
plt.grid(c='k',linestyle='--')
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.show()

plt.plot(TSLA.log_return,'r',linewidth=0.8, markersize=12,label='Tesla log return')
plt.legend()
plt.xlabel('Date')
plt.ylabel('log return')
ax = plt.gca()   #
ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))  # 
plt.xticks(pd.date_range(start,end,freq='2y')) #
plt.yticks(fontsize=10,rotation=0)
plt.xlim(start,end)
plt.grid(c='k',linestyle='--')
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.show()


"""""""""""""""""""""""""""""""""""""""""""""""""""""
More financial products: 
    
    Stock ETF
    Bond ETF
    Commodity ETF
    Volatility ETF

"""""""""""""""""""""""""""""""""""""""""""""""""""""


SPY = pdr.get_data_yahoo('SPY', start='2010-12-31', end=end)
DIA = pdr.get_data_yahoo('DIA', start='2010-12-31', end=end)
QQQ = pdr.get_data_yahoo('QQQ', start='2010-12-31', end=end)
IWM = pdr.get_data_yahoo('IWM', start='2010-12-31', end='2020-03-23')


plt.plot(SPY.Close,'r',linewidth=0.8, markersize=12,label='S&P 500 ETF')
plt.plot(DIA.Close,'b',linewidth=0.9, markersize=12,label='Dow Jones Industrial Average ETF')
plt.plot(QQQ.Close,'g:',linewidth=0.8, markersize=6,label='NASDAQ ETF')
plt.plot(IWM.Close,'k-.',linewidth=0.9, markersize=6,label='Russel 2000 ETF')

plt.legend()
plt.xlabel('Date')
plt.ylabel('Price')
ax = plt.gca()   #
ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))  # 
plt.xticks(pd.date_range(start,end,freq='2y')) #
plt.yticks(fontsize=10,rotation=0)
plt.xlim(start,end)
plt.grid(c='k',linestyle='--')
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.show()


MCD = pdr.get_data_yahoo('MCD', start='2010-12-31', end='2020-03-23')
VIX = pdr.get_data_yahoo('^VIX', start='2010-12-31', end='2020-3-23')
SP500 = pdr.get_data_yahoo('^GSPC', start='2010-12-31', end='2020-3-23')

plt.plot(VIX.Close,'r',label='VIX')


plt.plot(VIX.Close,'r',label='Starbucks')


# Leveraged ETF

import pandas_datareader as pdr
from datetime import datetime
UPRO = pdr.get_data_yahoo('UPRO', start='2010-12-31', end=end) # 3 times Long S&P
UDOW = pdr.get_data_yahoo('UDOW', start='2010-12-31', end=end) # 3 times Long DOW
TQQQ = pdr.get_data_yahoo('TQQQ', start='2010-12-31', end=end) # 3 times Long Nasdaq
URTY = pdr.get_data_yahoo('URTY', start='2010-12-31', end=end) # 3 times Long Russell2000

plt.plot(UPRO.Close,'k',label='3X S&P 500 ETF')
plt.plot(UDOW.Close,'b',label='3X Dow Jones Industrial Average ETF')
plt.plot(TQQQ.Close,'r',label='3X NASDAQ ETF')
plt.plot(URTY.Close,'g',label='3X Russel 2000 ETF')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Price')
ax = plt.gca()   #
ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))  #
plt.xticks(pd.date_range(start,end,freq='2y')) #
plt.yticks(fontsize=10,rotation=0)
plt.xlim(start,end)
plt.grid(c='k',linestyle='--')
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.show()


# Fixed income ETF

import pandas_datareader as pdr
from datetime import datetime
TLT = pdr.get_data_yahoo('TLT', start='2010-12-31', end='2019-11-19')
MBB = pdr.get_data_yahoo('MBB', start='2010-12-31', end='2019-11-19')
GNMA = pdr.get_data_yahoo('GNMA', start='2010-12-31', end='2019-11-19')

plt.plot(TLT.Close,'k',label='TLT')
plt.plot(MBB.Close,'b',label='MBB')
plt.plot(GNMA.Close,'r',label='GNMA')

plt.legend()
plt.xlabel('Date')
plt.ylabel('Price')
ax = plt.gca()   #
ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))  # 
plt.xticks(pd.date_range(start,end,freq='2y')) #
plt.yticks(fontsize=10,rotation=0)
plt.xlim(start,end)
plt.grid(c='k',linestyle='--')
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.show()


# Commodity ETF

import pandas_datareader as pdr
from datetime import datetime
GLD = pdr.get_data_yahoo('GLD', start='2010-12-31', end='2019-11-19')
SLV = pdr.get_data_yahoo('SLV', start='2010-12-31', end='2019-11-19')
USO = pdr.get_data_yahoo('USO', start='2010-12-31', end='2019-11-19')
UNG = pdr.get_data_yahoo('UNG', start='2010-12-31', end='2019-11-19')


plt.plot(GLD.Close,'k',label='GLD')
plt.plot(SLV.Close,'b',label='SLV')

plt.legend()
plt.xlabel('Date')
plt.ylabel('Price')
ax = plt.gca()   #
ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))  # 
plt.xticks(pd.date_range(start,end,freq='2y')) #
plt.yticks(fontsize=10,rotation=0)
plt.xlim(start,end)
plt.grid(c='k',linestyle='--')
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.show()


plt.plot(USO.Close,'r',label='USO')
plt.plot(UNG.Close,'g',label='UNG')

plt.legend()
plt.xlabel('Date')
plt.ylabel('Price')
ax = plt.gca()   #
ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))  # 
plt.xticks(pd.date_range(start,end,freq='2y')) #
plt.yticks(fontsize=10,rotation=0)
plt.xlim(start,end)
plt.grid(c='k',linestyle='--')
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.show()



# Volatility ETF

start='2019-12-31'
VXX = pdr.get_data_yahoo('VXX', start='2019-12-31', end='2020-3-24')

plt.plot(VXX.Close,'r',label='VXX')

plt.legend()
plt.xlabel('Date')
plt.ylabel('Price')
ax = plt.gca()   #
ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))  # 
plt.xticks(pd.date_range(start,end,freq='2w')) #
plt.yticks(fontsize=10,rotation=0)
plt.xlim(start,end)
plt.grid(c='k',linestyle='--')
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.show()


