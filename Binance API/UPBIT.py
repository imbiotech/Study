import time
import APIData
import pandas as pd
import pyupbit
from pyupbit import WebSocketManager

# 캔들 데이터 덥데이트 및 적용 함수
def get_candle_data(markets, string, count):
    df = pyupbit.get_ohlcv(ticker=markets, interval=string, count=count)
    new_df = pd.DataFrame(columns=df.columns)

    for i in range(int(df.shape[0] / 10)):
        df_open = df.iloc[i]["open"]
        df_high = df.iloc[i:i + 9]["high"].max()
        df_low = df.iloc[i:i + 9]["low"].min()
        df_close = df.iloc[i + 9]["close"]
        df_volume = df.iloc[i:i + 9]["volume"].sum()
        df_value = df.iloc[i:i + 9]["value"].sum()
        new_df.loc[i] = {
            "open": df_open,
            "high": df_high,
            "low": df_low,
            "close": df_close,
            "volume": df_volume,
            "value": df_value
        }
    FILTER = list(map((lambda x: x % 10 == 9), range(df.shape[0])))
    new_df["time"] = df[FILTER].index
    new_df.set_index("time", inplace=True)

    ma5 = new_df.iloc[:5]["close"].mean()
    ma20 = new_df.iloc[:20]["close"].mean()
    print(new_df.index[-1], ma5, ma20)
    return ma5>ma20

# pyupbit 로그인
pyup = pyupbit.Upbit(access=APIData.APIkey_U,secret=APIData.APIsecert_U)

# 지갑 확인
wallets = pyupbit.Upbit.get_balances(pyup)
# for i in wallets:
#     print(i)

# 캔들 데이터
# ticker=검색할 마켓, interval=단위지정, count=봉 개수, to=None):
MARKET="KRW-JST"
INTERVAL="minutes1"
COUNT=600

# upwm = pyupbit.WebSocketManager("ticker", MARKET)

# data=upwm.get()







from pybithumb import WebSocketManager
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
import time


class Worker(QThread):
    recv = pyqtSignal(str)
    def run(self):
        # create websocket for Bithumb
        wm = WebSocketManager("ticker", ["BTC_KRW"])
        while True:
            data = wm.get()
            self.recv.emit(data['content']['closePrice'])


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel("BTC", self)
        label.move(20, 20)

        self.price = QLabel("-", self)
        self.price.move(80, 20)
        self.price.resize(60, 20)

        button = QPushButton("Run", self)
        button.move(20, 50)
        button.clicked.connect(self.click_btn)

        self.th = Worker()
        self.th.recv.connect(self.receive_msg)

    @pyqtSlot(str)
    def receive_msg(self, msg):
        print(msg)
        self.price.setText(msg)

    def click_btn(self):
       self.th.start()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = App()
   ex.show()
   app.exec_()









time.sleep()
# 계속 실행
while True:
    if get_candle_data(MARKET,INTERVAL,COUNT) == True:
        # 5평선이 20평선보다 높을 때 실행
        print("")
    time.sleep(10)








