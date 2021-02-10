# from typing_extensions import ParamSpec
# from screener.util import period
import talib
from .util import StockData 
from pandas_datareader import data as pdr
from yahoo_fin import stock_info as si
import numpy as np
import pandas as pd



class CompanyPattern(StockData):
    indicators = {
        'CDL3LINESTRIKE': "3 Line Strike",
        'CDL3WHITESOLDIERS': "3 White Soldiers",
        'CDLBREAKAWAY': "Break Away",
        'CDLDARKCLOUDCOVER': "Dark Cloud Cover",
        'CDLDOJI': "Doji",
        'CDLDOJISTAR': "Doji Star",
        'CDLDRAGONFLYDOJI': "Dragon Fly Doji",
        'CDLEVENINGDOJISTAR': "Evening Doji Star",
        'CDLHAMMER': "Hammer",
        'CDLHANGINGMAN': "Hanging Man",
        'CDLLONGLEGGEDDOJI': "Long Legged Doji",
        'CDLMORNINGDOJISTAR': "Moring Doji Start",
        'CDLMORNINGSTAR': "Morning Start",
        'CDLSHOOTINGSTAR': "Stooting Star"
    }

    def __init__(self, tinker):
        super().__init__(tinker)
        self.data = self.get_stock_data()
        
    def find_candstick_patterns(self):

        for pattern in CompanyPattern.indicators.keys():
            func = getattr(talib, pattern, None)
            if func:
                self.data[CompanyPattern.indicators[pattern]] = func(self.data['Open'], self.data["High"], self.data["Low"], self.data["Close"])
        return self.data

    def results(self, show_last_xday=3):

        data = self.find_candstick_patterns().iloc[-show_last_xday:, 6:].replace(0, np.nan).dropna(how="all", axis=1 )
        data = data.replace(100, 'Bullish')
        data = data.replace(-100, 'Bearish')
        return data

for stock in 'AAPL,FB,MSFT,BAC,UPS'.split(','):
    indi = CompanyPattern(stock)
    print(indi.tinker)
    print(indi.results())