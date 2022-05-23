import time
from APIData import APIkey_U, APIsecert_U
import pandas as pd
import pyupbit
from pyupbit import WebSocketManager
import requests
import sys
from PyQt5.QtWidgets import * # window를 설정하는 module
from PyQt5.QtGui import *

class custom_window(QMainWindow):
    def __init__(self):
        super().__init__()
        #1920*1080
        size = 600
        self.setGeometry(int(960-size/2),int(540-size/2),size,size)
        self.setWindowTitle("custom_window")
        # self.setWindowIcon(QIcon("appIcon.png"))
        BTC_label = QLabel("BTC Price:", self) # 줄글 생성
        self.BTC_lineEdit = QLineEdit(self)
        self.BTC_lineEdit.move(80,0)
        BTC_Button = QPushButton("Check Price", self) # 버튼 생성
        BTC_Button.move(200,0)
        BTC_Button.clicked.connect(self.check_price)

    def check_price(self):
        price = 1111
        self.BTC_lineEdit.setText(str(price))


app = QApplication(sys.argv) # QApplication의 instance 지정; app
c_window = custom_window()
c_window.show()
app.exec_() # exec_ method 호출, 이벤트 루프를 형성하여 window 출력 후 종료 시까지 프로그램이 계속 실행 상태 유지







# 캔들 데이터 덥데이트 및 적용 함수
def get_candle_data(markets, string, count):
    # ticker=검색할 마켓, interval=단위지정, count=봉 개수
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
pyup = pyupbit.Upbit(access=APIkey_U,secret=APIsecert_U)

# 지갑 확인
wallets = pyupbit.Upbit.get_balances(pyup)

# 거래 대상 지정
MARKET="KRW-JST"

# 캔들 정보 지정
INTERVAL="minutes1"
COUNT=600


print("before end")
exit()
# 계속 실행
while True:
    if get_candle_data(MARKET,INTERVAL,COUNT) == True:
        # 5평선이 20평선보다 높을 때 실행
        print("")
    time.sleep(10)








