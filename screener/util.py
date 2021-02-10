#stock_screener.py

from pandas_datareader import data as pdr
from yahoo_fin import stock_info as si
# import yahoo_fin
#from pandas import ExcelWriter
import yfinance as yf
import pandas as pd
# import requests
import datetime
import time
from pprint import pprint
from collections import OrderedDict

import base64

# def calc_relative_strength(df):
#   ## relative gain and losses
#   df['close_shift'] = df['adj_close'].shift(1)
#   ## Gains (true) and Losses (False)
#   df['gains'] = df.apply(lambda x: x['adj_close'] if x['adj_close'] >= x['close_shift'] else 0, axis=1)
#   df['loss'] = df.apply(lambda x: x['adj_close'] if x['adj_close'] <= x['close_shift'] else 0, axis=1)

#   avg_gain = df['gains'].mean()
#   avg_losses = df['loss'].mean()

#   return avg_gain / avg_losses
  
# def rs_rating(stock_rs_strange_value, index_rs_strange_value):
#   # print(f'Stock RS:{stock_rs_strange_value}, Index RS:{index_rs_strange_value}')
#   return 100 * ( stock_rs_strange_value / index_rs_strange_value )

# class Moving_avg:
#   # self.index_strange = index_strange 
#   def __init__(self, stockname, df,  index_strange, min_rs_rating=70):
#     self.stockname = stockname
#     self.df = df
    
#     # self.stock_data = get_stock(stockname)

#     self.df = self.calc_moving_avg(self.df)
#     self.price = self.df['adj_close'][-1]
#     self.sma50 = self.df["SMA_50"][-1]
#     self.sma150 = self.df["SMA_150"][-1]
#     self.sma200 = self.df["SMA_200"][-1]
#     self.index_rs_strange = index_strange
#     self.stock_rs_strange = calc_relative_strength(self.df)
#     self.rs_rating = rs_rating(self.stock_rs_strange, self.index_rs_strange)
#     self.min_rs_rating = min_rs_rating
#     self.low_of_52week = self.df["adj_close"][-260:].min()
#     self.high_of_52week = self.df["adj_close"][-260:].max()

#     try:
#       ## Need to double check this 
#       ## should SMA trending up for at least 1 month (ideally 4-5 months)
#         self.sma200_20 = df["SMA_200"][-20]
#     except:
#         self.sma200_20 = 0

#   def as_dict(self):
#     try:
#         company_name = yf.Ticker(self.stockname).info['longName']
#     except:
#         company_name = self.stockname
#     # return self.__dict__
#     return OrderedDict([
#        ('Company Name', company_name),
#        ('Ticker', self.stockname),
#        ('Current Price', self.price),
#        ('RS Rating', self.rs_rating),
#        ('SMA 50 Day', self.sma50),
#        ('SMA 150 Day', self.sma150),
#        ('SMA 200 Day', self.sma200),
#        ('52 Week Low', self.low_of_52week),
#        ('52 Week High', self.high_of_52week),
#        ])

#   def calc_moving_avg(self, df):
#     for x in [50,150,200]:
#       df["SMA_"+str(x)] = round(df['adj_close'].rolling(window=x).mean(), 2)
#     return df
  

#   def avg_volume(self):
#     return self.df['volume'].mean()

#   def condition1(self):
#     # Condition 1: Current Price > 150 SMA and > 200 SMA
#     if (self.price > self.sma150 and self.price > self.sma200):
#       return True

#   def condition2(self):
#     # Condition 2: 150 SMA and > 200 SMA
#     if (self.sma150 > self.sma200):
#       return True

#   def condition3(self):
#     # Condition 3: 200 SMA trending up for at least 1 month (ideally 4-5 months)
#     if self.sma200 > self.sma200_20:
#       return True 
  
#   def condition4(self):
#     # Condition 4: 50 SMA> 150 SMA and 50 SMA> 200 SMA
#     if self.sma50 > self.sma150 > self.sma200:
#       return True

#   def condition5(self):
#     # Condition 5: Current Price > 50 SMA
#     if self.price > self.sma50:
#       return True 
  
#   def condition6(self):
#     # Condition 6: Current Price is at least 30% above 52 week low (Many of the best are up 100-300% before coming out of consolidation)
#     if self.price >= (1.3 * self.low_of_52week):
#       return True
  
#   def condition7(self):
#   # Condition 7: Current Price is within 25% of 52 week high
#     if self.price >= (0.75 * self.high_of_52week):
#       return True
  
#   def condition8(self):
#   # Condiction 8: IBD RS_Rating greater than 70
#     if self.rs_rating >=self.min_rs_rating:
#       return True

#   def all_conditions(self):
#     if all(
#         [self.condition1(),
#           self.condition2(),
#           self.condition3(),
#           self.condition4(),
#           self.condition5(),
#           self.condition6(),
#           self.condition7(),
#           self.condition8()]):
#       return True

# def filedownload(df):
#     csv = df.to_csv(index=False)
#     b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
#     href = f'<a href="data:file/csv;base64,{b64}" download="MM_stock_screener.csv">Download CSV File</a>'
#     return href    

# def stock_screener(index_tinker_name='S&P500', min_vol=5e6, min_price=0, days=365, min_rs_rating=70,):
# # help(si)
#   ## fix for yahoo_fin
#   start_date, end_date = period(days)
#   yf.pdr_override()

#   index_tinker = {
#     'DOW': 'DOW',
#     'NASDAQ': '^IXIC', 
#     "S&P500": '^GSPC'
#   }

#   index_list = {
#     'DOW': si.tickers_sp500(),
#     'NASDAQ': si.tickers_nasdaq(),
#     "S&P500": si.tickers_sp500()
#   }
#   # st.header(f'Stock Screener {index_tinker_name}')
#   # stocklist = si.tickers_sp500()
#   min_volume = min_vol
#   # index_name = '^GSPC' # SPY or S&P 500
#   stocklist = index_list.get(index_tinker_name)[:]

#   index_rs_strange_value = calc_relative_strength(
#                 get_stock(
#                   index_tinker[index_tinker_name], days
#                   )
#                 )

#   final = []
#   index = []

#   exclude_list = []
#   all_data = []
#   latest_iteration = st.empty()
#   having_break = st.empty()
#   bar = st.progress(0)
#   total = len(stocklist)

#   for num, stock_name in enumerate(stocklist):
#     print(f"checking {num}:{stock_name}")
#     if stock_name in exclude_list:
#       continue
#       FAILED = False
#     df = get_stock(stock_name)
#     # print('**',df)
#     if df is False:
#       print(f'SKIPPED to download {stock_name} {num}')
#       continue

#     stock_meta = Moving_avg(stock_name, df, index_rs_strange_value, min_rs_rating)
#     time.sleep(0.2)

#     if stock_meta.all_conditions():
#       print(f'Passed conditions: {stock_name}')
#       final.append(stock_meta.as_dict())
#     else:
#       print(f'Failed conditions: {stock_name}')  
#       # all_data.append(stock_meta.as_dict())
    
#     latest_iteration.text(f'Stocks Processed: {(num+1)}/{total}')
#     bar.progress((num+1)/total)
  

#     if num == 0:
#       continue
#     if num % 10 == 0:
#       for i in list(range(5))[::-1]:
#         having_break.text(f'waiting for {i}sec')
#         time.sleep(1)
#       # having_break = st.empty()
#     if num % 100 == 0:
#       for i in list(range(3))[::-1]:
#         having_break.text(f'waiting for {i}min')
#         time.sleep(60)
#       # having_break = st.empty()
#       # time.sleep(5*60)

#   final_df = pd.DataFrame(final)
#   final_df['price_change_highest'] = 100 * ( 1- ( final_df["Curren t Price"]/final_df['52 Week High'] ) )
#   # all_data_df = pd.DataFrame(all_data)
#   return final_df 


# # df_download(final_df), unsafe_allow_html=True

# def df_download(df, filename='', index=False):
#   csv = df.to_csv(index=index)
#   b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
#   href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">Download CSV File</a>'
#   return href



##########################################


# def df_download(df, filename, index=False):
#   path = Path('../exported') / filename 
#   csv = df.to_csv(path, index=index)
#   # b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
#   href = f'href="data:file/csv;base64,{b64}" download="{filename}"'

#   return href


class Company:
  def __init__(self, tinker, days=365):
    self.tinker = str(tinker).strip().upper()
    self.start_date, self.end_date =  self.period(days)
  
  def period(self, days=365):
    '''
    return start and end dates
    '''
    start_date = datetime.datetime.now() - datetime.timedelta(days=365)
    end_date = datetime.date.today()
    return start_date, end_date 




class StockData(Company):
  # TODO: add processing for UK stocks
  
  def __init__(self, tinker=None, ):
    super().__init__(tinker)
    
  def get_stock_data(self):
    try: 
      df = pdr.get_data_yahoo(self.tinker, start=self.start_date, end=self.end_date )
    except:
      return False
    if len(df) < 2:
      print('Less 2')
      return False
    return df

  def get_multiple_stocks_data(self, multiple_tinkers):
    if multiple_tinkers and  isinstance(multiple_tinkers, list):
      multiple_tinkers = list(map(str.upper, multiple_tinkers))
      return pdr.get_data_yahoo(multiple_tinkers, start=self.start_date, end=self.end_date)
    else:
      raise ValueError('Please provide a list of tinkers')

  def munch_df(self, df):
    ## multi-index-column to single level columns 
    if len(df.columns[0])==2:  
      df = df.iloc[:,df.columns.get_level_values(1)==f"{self.tinker}"]
      df.columns = ([x[0] for x in df.columns])
      return df
    else:
      return df

