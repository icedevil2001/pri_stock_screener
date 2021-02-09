# from typing_extensions import ParamSpec
# from screener.util import period
import talib
from util import period
from pandas_datareader import data as pdr
from yahoo_fin import stock_info as si
import numpy as np

#hammer, engulfing, piercing_line,  inverted_hammer, moring_star, doji_start


class Company:
    patterns = [
        'CDL3LINESTRIKE','CDL3WHITESOLDIERS', 
        'CDLBREAKAWAY', 'CDLDARKCLOUDCOVER'
        'CDLDOJI', 'CDLDOJISTAR','CDLDRAGONFLYDOJI',
        'CDLEVENINGDOJISTAR', 'CDLHAMMER', 'CDLHANGINGMAN',
        'CDLLONGLEGGEDDOJI', 'CDLMORNINGDOJISTAR',
        'CDLMORNINGSTAR', 'CDLSHOOTINGSTAR',
    ]


    def __init__(self, tinker, df=None):
        self.tinker = tinker
        
        self.df = self.process(df )
        # self.patterns = patterns


    def process(self, df):
        for pattern in Company.patterns:
            func = getattr(talib, pattern, None)
            if func:
                df[pattern] = func(df.Open, df.High, df.Low, df.Close)

        return df 


stock = 'AAPL,FB,MSFT,BAC,UPS'.strip(',')
# data = get_stock(stock, drop_columns=[])
print(stock)
start_date, end_date  = period()
df = pdr.get_data_yahoo(['AAPL',"FB"], start=start_date, end=end_date )

data = pdr.get_data_yahoo("AAPL", start=start_date, end=end_date)
# data = (df.iloc[:,df.columns.get_level_values(1)=='AAPL'])
print(data.columns)
# print(data['Open']), data['High'], data['Low'], data['Close'])

data['HAMMER'] = (talib.CDLHAMMER(
    data['Open'],
    data['High'],
    data['Low'],
    data['Close'])
    )

print(data)

print(Company(tinker='APPL', df=data).df)