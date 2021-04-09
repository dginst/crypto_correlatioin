from btc_analysis.config import DB_NAME, VOLA_DAY_LIST
from btc_analysis.market_data import historical_vola, ewm_volatility
from btc_analysis.mongo_func import mongo_coll_drop, mongo_upload, query_mongo
from btc_analysis.dashboard_func import dash_volatility_df

mongo_coll_drop("vola")

return_df = query_mongo(DB_NAME, "all_returns_y")
logret_df = query_mongo(DB_NAME, "all_logreturns_y")

hist_vola_252 = historical_vola(return_df, logret_df, 252)
hist_vola_90 = historical_vola(return_df, logret_df, 90)
hist_vola_30 = historical_vola(return_df, logret_df, 30)
ewm_vola = ewm_volatility(return_df)

mongo_upload(hist_vola_252, "collection_volatility_252")
mongo_upload(hist_vola_90, "collection_volatility_90")
mongo_upload(hist_vola_30, "collection_volatility_30")
mongo_upload(ewm_vola, "collection_volatility_ewm")


# --------

dash_volatility_df(VOLA_DAY_LIST)
