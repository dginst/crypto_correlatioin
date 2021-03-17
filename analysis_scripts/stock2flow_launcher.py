from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from btc_analysis.mongo_func import mongo_coll_drop, mongo_upload
from btc_analysis.stock2flow_func import (S2F_definition, complete_model,
                                          days_to_halving)
from btc_analysis.config import HALVING_DATE

mongo_coll_drop("S2F")

# ----------
# data gathering
# ---------
initial_data = pd.read_csv(
    Path("source_data", "initial_data_S2F.csv"), sep="|")

BTC_prices = pd.read_csv(
    Path("source_data", "BTC_price.csv"), sep="|")


# -----------------------

slope, intercept = S2F_definition(initial_data)

final_df = complete_model(slope, intercept)

mongo_upload(final_df, "collection_S2F")

price_df = days_to_halving(BTC_prices, HALVING_DATE)


mongo_upload(price_df, "collection_S2F_BTC")

# _x = final_df["Date"]
# _y = final_df["S2F price"]

# plt.figure(figsize=(12, 8))
# plt.title('stock to Flow')
# plt.xlabel('Date')
# plt.ylabel('Price')
# plt.plot(_x, _y, 'steelblue', linewidth=3)

# plt.show()
