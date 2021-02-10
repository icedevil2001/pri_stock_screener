
## https://medium.com/fintechexplained/automating-stock-investing-fundamental-analysis-with-python-f854781ee0b4 


import pandas as pd
import yahoo_fin.stock_info as si
from util import Company


class CompanyFundumental(Company):
  def __init__(self, tinker):
    super().__init__(self, tinker)
    self.fundamental_indicators = pd.concat([self.get_statatistics(),
                                             self.get_valuation_stats()
                                             ])

  def get_statatistics(self):
    url = f"https://finance.yahoo.com/quote/{self.tinker}/key-statistics?p={self.tinker}"
    dfs = pd.read_html(url)
    df = pd.concat(dfs[1:])
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
      new_df.loc[idx, self.tinker] = value
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

    df =  si.get_stats_valuation(self.tinker)
    df = df.set_index(df.columns[0])
    new_df = pd.DataFrame(index=selected.keys()).fillna('na')
    for idx in new_df.index:
      try:
        value = df.loc[idx,df.columns[0]]
      except Exception as e:
        value = 'N/A'
      new_df.loc[idx, self.tinker] = value
    # print(df.index)
    return new_df


def fundumental_anaysis(tinkers):
  company_anaylsis =[]
  for tinker in tinkers:
    company_anaylsis.append(CompanyFundumental(tinker).fundamental_indicators)
    print(company_anaylsis)
  return pd.concat(company_anaylsis, axis=1)

