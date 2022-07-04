from function import *
from binance_lib.streams import *

asyncio.run(on_client())
# wallets, data = asyncio.run(on_client())
#
# count=0
# while count<10:
#     new_wallets = getWallet
#     new_data = asyncio.run(getData())
#     if wallets != new_wallets:
#         wallets = new_wallets
#         print("지갑 업데이트")
#     if data != new_data:
#         data = new_data
#         market("buy", 0.0005)
#     count+=1

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




