
## https://medium.com/fintechexplained/automating-stock-investing-fundamental-analysis-with-python-f854781ee0b4 


import pandas as pd
import yahoo_fin.stock_info as si


class Company:
  def __init__(self, symbol):
    self.symbol = symbol
    self.fundamental_indicators = pd.concat([self.get_statatistics(),
                                             self.get_valuation_stats()
                                             ])

  def get_statatistics(self):
    url = f"https://finance.yahoo.com/quote/{self.symbol}/key-statistics?p={self.symbol}"
    dfs = pandas.read_html(url)
    df = pandas.concat(dfs[1:])
    df = df.set_index(0)
    selected = {
      'Gross Profit (ttm)': 'GrossProfit',
      'Profit Margin': 'ProfitMargin',
      'Operating Margin (ttm)': 'OperMargin',
      'Current Ratio (mrq)': 'CurrentRatio',
      'Payout Ratio 4': 'DivPayoutRatio',

      'Return on Assets (ttm)': 'ROA',
      'Return on Equity (ttm)': 'ROE',
      'Total Cash Per Share (mrq)': 'Cash/Share',
      'Book Value Per Share (mrq)': 'Book/Share',
      'Total Debt/Equity (mrq)': 'Debt/Equity',
      'Levered Free Cash Flow (ttm)': 'LeveredFreeCash',
      }
    new_df = pd.DataFrame(index=selected.keys())
    for idx in new_df.index:
      try:
        value = df.loc[idx,df.columns[0]]
      except Exception as e:
        value = 'N/A'
      new_df.loc[idx, self.symbol] = value
    # print(df.index)
    return new_df

  def get_valuation_stats(self):
    selected = {
      'Market Cap (intraday) 5': 'Market Cap',
      'Price/Sales (ttm)': 'Price/Sales (ttm)',
      'Trailing P/E': 'P/E (trailing)',
      'PEG Ratio (5 yr expected) 1': 'PEG (5 yr expected)',
      'Price/Book (mrq)': 'Price/Book',

      }

    df =  si.get_stats_valuation(self.symbol).set_index(0)
    new_df = pd.DataFrame(index=selected.keys()).fillna('na')
    for idx in new_df.index:
      try:
        value = df.loc[idx,df.columns[0]]
      except Exception as e:
        value = 'N/A'
      new_df.loc[idx, self.symbol] = value
    # print(df.index)
    return new_df


companies = ['AAPL', "ROK"]


df = pd.concat([Company(company).fundamental_indicators for company in companies],axis=1)
print(df)