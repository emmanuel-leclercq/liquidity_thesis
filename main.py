# this code will combine all the holdings data into one dataframe, extract a list of ISIN so that
# liquidity data can be retrieved from WRDS or Refinitiv

import os
import numpy as np
import pandas as pd

all_holdings = pd.read_excel(
    """/workspaces/liquidity_thesis/holdings/HYG Holdings 2018-01-31.xlsx""")

all_holdings['Date'] = '2018-01-31'

for file in os.listdir("/workspaces/liquidity_thesis/holdings"):
    if "2018-01-01" not in file:
        if file.endswith(".xlsx"):
            temp = pd.read_excel(
                f'/workspaces/liquidity_thesis/holdings/{file}')
            temp['Date'] = file[13:23]
            all_holdings = pd.concat([all_holdings, temp], axis=0)

print(all_holdings['Date'])
