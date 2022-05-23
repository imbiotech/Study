from binance.client import Client
import APIData, time

import binance.enums

client = Client(APIData.APIkey,APIData.APIsecert)
print("logged in!\n")

servertime = client.get_server_time()["serverTime"]
gmtime=time.gmtime(servertime/1000)
print(f"{gmtime.tm_year}-{gmtime.tm_mon}-{gmtime.tm_mday} {gmtime.tm_hour}:{gmtime.tm_min}:{gmtime.tm_sec}")

if client.get_system_status()["status"] == 1:
    time.sleep()

ex = client.get_exchange_info()
sym = client.get_symbol_info("XLMBNB")

for i in sym:
    print(f"{i}:{sym[i]}")






time.sleep()

wallets = client.get_account()["balances"]
for coin in wallets:
    if float(coin["free"])>0 or float(coin["locked"])>0:
        print(coin)

order=client.create_order(
    symbol="XLMBNB",
    side=client.SIDE_SELL, # _BUT; 구매, _SELL; 판매
    type=client.ORDER_TYPE_MARKET, # _MARKET; 시장가 거래,
    quantity=0.05 # BNB가 최소 0.5(~ 2022.05.22 기준 약 2 만 원)개 되도록 거래해야 함
)

trades=client.get_my_trades(
    symbol="XLMBNB"
)

for trade in trades:
    print(trade)



client.get_exchange_info()
# timezone; UTC, 세계시 기준
# serverTime; 서버 시간 출력
# rateLimits; ?
# exchangeFilters; ?
# symbols; ?


client.get_symbol_info("XLMBNB") # BNB/XLM 거래
# symbol; 거래
# status
# baseAsset
# baseAssetPrecision
# quoteAsset
# quotePrecision
# quoteAssetPrecision
# baseCommissionPrecision
# quoteCommissionPrecision
# orderTypes
# icebergAllowed
# ocoAllowed
# quoteOrderQtyMarketAllowed
# allowTrailingStop
# isSpotTradingAllowed
# isMarginTradingAllowed
# filters
# permissions

client.get_account()
# makerCommission
# takerCommission
# buyerCommission
# sellerCommission
# canTrade
# canWithdraw
# canDeposit
# updateTime
# accountType
# balances; 지갑 내 잔고
# permissions



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

SIDE_BUY = 'BUY'
SIDE_SELL = 'SELL'

ORDER_TYPE_LIMIT = 'LIMIT'
ORDER_TYPE_MARKET = 'MARKET'
ORDER_TYPE_STOP_LOSS = 'STOP_LOSS'
ORDER_TYPE_STOP_LOSS_LIMIT = 'STOP_LOSS_LIMIT'
ORDER_TYPE_TAKE_PROFIT = 'TAKE_PROFIT'
ORDER_TYPE_TAKE_PROFIT_LIMIT = 'TAKE_PROFIT_LIMIT'
ORDER_TYPE_LIMIT_MAKER = 'LIMIT_MAKER'

TIME_IN_FORCE_GTC = 'GTC'
TIME_IN_FORCE_IOC = 'IOC'
TIME_IN_FORCE_FOK = 'FOK'

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