from function import *
import asyncio
import pandas as pd
from binance_lib.streams import *

client = asyncio.run(on_client())

# 시장가 매매 (side, quantity)
# market(side,quantity)

# 지정가 매매 (side,price,quantity)
# limit(side,price,quantity)

# TP, SL, TPL, SLL (side, quantity, stop_type, price)
# profit_n_loss(PL, side, quantity, stop_type="Delta 500",price=0)





# account_info = r_client.get_account_information() # Future 서버 전용
# symbol = r_client.get_symbol_price_ticker(symbol=SYMBOL)
# for sym in symbol:
#     print(sym)



# sym = client.get_symbol_info(SYMBOL)
# ex = client.get_exchange_info()
# serverTime; 서버 시간 출력
# rateLimits; 최대 거래 제한
# exchangeFilters; ?
# symbols; 각 symbol에 대한 데이터

# 거래 기록 출력
# trades=client.get_my_trades(symbol=SYMBOL)
# for trade in trades:
#     print(trade)



# Binance Constants
SYMBOL_TYPE_SPOT = 'SPOT'

ORDER_STATUS_NEW = 'NEW'
ORDER_STATUS_PARTIALLY_FILLED = 'PARTIALLY_FILLED'
ORDER_STATUS_FILLED = 'FILLED'
ORDER_STATUS_CANCELED = 'CANCELED'
ORDER_STATUS_PENDING_CANCEL = 'PENDING_CANCEL'
ORDER_STATUS_REJECTED = 'REJECTED'
ORDER_STATUS_EXPIRED = 'EXPIRED'

KLINE_INTERVAL_1MINUTE = '1m'
KLINE_INTERVAL_3MINUTE = '3m'
KLINE_INTERVAL_5MINUTE = '5m'
KLINE_INTERVAL_15MINUTE = '15m'
KLINE_INTERVAL_30MINUTE = '30m'
KLINE_INTERVAL_1HOUR = '1h'
KLINE_INTERVAL_2HOUR = '2h'
KLINE_INTERVAL_4HOUR = '4h'
KLINE_INTERVAL_6HOUR = '6h'
KLINE_INTERVAL_8HOUR = '8h'
KLINE_INTERVAL_12HOUR = '12h'
KLINE_INTERVAL_1DAY = '1d'
KLINE_INTERVAL_3DAY = '3d'
KLINE_INTERVAL_1WEEK = '1w'
KLINE_INTERVAL_1MONTH = '1M'

ORDER_RESP_TYPE_ACK = 'ACK'
ORDER_RESP_TYPE_RESULT = 'RESULT'
ORDER_RESP_TYPE_FULL = 'FULL'

# For accessing the data returned by Client.aggregate_trades().
AGG_ID             = 'a'
AGG_PRICE          = 'p'
AGG_QUANTITY       = 'q'
AGG_FIRST_TRADE_ID = 'f'
AGG_LAST_TRADE_ID  = 'l'
AGG_TIME           = 'T'
AGG_BUYER_MAKES    = 'm'
AGG_BEST_MATCH     = 'M'