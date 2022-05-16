import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np

# matplotlib; 다양한 형태의 그래프를 통해서 데이터 시각화를 할 수 있는 라이브러리

# 1. 그래프 기본

x = [1, 2, 3]
y = [2, 4, 8]
# plt.plot(x,y)

# 그래프 제목 설정(Title)
# plt.title("Line graph")

# 한글 폰트 설정
matplotlib.rcParams["font.family"] = "Malgun Gothic" # 한글 폰트 지정
matplotlib.rcParams["font.size"] = 15 # 글자 크기 설정
matplotlib.rcParams["axes.unicode_minus"] = False # 한글 폰트 사용 시 마이너스가 깨지는 현상 방지
# plt.title("꺾은선 그래프", fontdict={"family":"HYGungSo-Bold","size":20}); 타이틀을 설정하고 타이틀에 대한 폰트 설정을 적용

# plt.plot([-1, 0, 1],[-5, -1, 2])


# 2. 축

# 축 라벨링
# plt.xlabel("X-axis", color = "red", loc="right")
# plt.ylabel("Y-axis", color = "#00aa00", loc="top")

# 축 범위 설정 및 눈금 추가
# plt.xticks([1,2,3])
# plt.yticks([3,6,9,12])


# 3. 범례 (legend)

# 범례 기본 설정
# plt.plot(x, y, label="Random Plot")

# 범례 호출
# plt.legend()

# plt.plot(x, y, label = "범례")

# 범례 위치 지정 각 축을 기준으로 0~1 사이 상대값으로 입력
# plt.legend(loc="upper right") # 우측 상단에 위치, upper right, lower left, best, .....
# plt.legend(loc=(0.5, 0.5))

# 선 굵기 지정
# plt.plot(x, y, linewidth=5)

# 마커(marker)

# 각 marker 표시
# plt.plot(x, y, marker="o")

# line 없이 marker만 표시
# plt.plot(x, y, marker="o", linestyle="None")

# marker 모양 변경(matplotlib.markers 참고), marker의 사이즈 조절, 색깔 변경
# plt.plot(x, y, marker="v", linestyle="None", markersize=5)
# plt.plot(x, y, marker="x", linestyle="None", markersize=5)
# plt.plot(x, y, marker="v", linestyle="None", markersize=7, markeredgecolor="black", markerfacecolor="yellow")

# line style; line의 모양 변경(matplotlib.linestytle 참고), 두께 변경 등
# plt.plot(x, y, linestyle=":"); 점선 표기
# plt.plot(x, y, linestyle="--"); 실선 표기
# plt.plot(x, y, linestyle="-."); 점실선 표기

# color; line의 색 지정, 색 이름 또는 16진법 RGB 코드
# plt.plot(x, y, color="pink"); css color 참고
# plt.plot(x, y, color="#AACC03"); RGB 코드 사용, 앞에 # 붙여야 함
# plt.plot(x, y, color="g"); base color 참고

# 포맷
# plt.plot(x, y, "ro--"); r = 색깔, o = marker 모양, -- = line style
# plt.plot(x, y, "bv:")

# 축약어; mfc = markerfacecolor, ms = markersize, mec = markeredgestyle, ls = linestyle 등
# plt.plot(x, y, marker="o", mfc="red", ms="10", mec="blue", ls="--")

# 투명도; 0~1 사이에서 선의 투명도를 조절. 높을 수록 진함
# plt.plot(x, y, marker="o", mfc="red", ms="10", mec="blue", ls="--", alpha=0.6)

# 그래프 크기; figsize로 직접 가로*세로 지정 가능, dpi로 해상도 조절 가능, .figure 명령어는 최상단에 써줘야 함
# plt.figure(figsize=(10,5), dpi=100)
# plt.plot(x, y, marker="o", mfc="red", ms="10", mec="blue", ls="--")

# 배경색
# plt.figure(facecolor="grey")
# plt.plot(x, y)


# 5. 파일 저장
# plt.plot(x, y)
# plt.savefig("graph_dpi200.png", dpi=200); dpi를 설정해서 해상도를 높일 수 있음


# 6. 텍스트
# plt.plot(x, y, "o-")
# for index, txt in enumerate(y): # index = 0, 1, 2 // txt = 2, 4, 8
#     plt.text(x[index], y[index] + 0.3, txt, ha="center", color="blue") # 해당하는 좌표(x[index], y[index])에 txt를 표시해줌, + 0.3은 높이 조절, ha='center는 가운데 정렬


# 7. 여러 데이터

# COVID-19 백신 종류별 접종 인구
# days = [1, 2, 3]
# AZ = [2, 4, 8]
# PF = [5, 1, 3]
# MD = [1, 2, 5]
#
# plt.plot(days, AZ, "o-", label="AZ")
# plt.plot(days, PF, "s--", label="PF")
# plt.plot(days, MD, "x-.", label="MD")
#
# plt.legend(ncol = 3); 3개 column 만큼의 legend 표시 가능


# 8. 막대 그래프 (기본)

# labels = ["강백호", "서태웅", "정대만"]
# values = [190, 187, 184]
# colors = ["r", "g", "b"]

# plt.bar(labels, values, color="g"); 색 설정
# plt.bar(labels, values, color=colors, alpha=0.8); 색을 지정된 list로 가져옴, alpha로 투명도 설정
# plt.ylim(180.0, 195.0); y값의 최대~최소 지정
# plt.bar(labels, values, width=0.5); 막대의 폭 감소
# plt.bar(labels, values, width=0.3)
# plt.xticks(rotation=45); x축의 눈금 지표를 45도 돌림
# plt.yticks(rotation=45); y축의 눈금 지표를 45도 돌림

# ticks = ["1번 학생", "2번 학생", "3번 학생"]
# plt.bar(labels, values)
# plt.xticks(labels, ticks); x축 눈금을 지정된 list로 대체함


# 9. 막대 그래프 (심화)

labels = ["강백호", "서태웅", "정대만"]
values = [190, 187, 184]
# bar = plt.barh(labels, values)
# plt.xlim(180, 195)
# bar[0].set_hatch("/"); 사선 패턴
# bar[1].set_hatch("x"); 교차선 패턴
# bar[2].set_hatch(".."); 점 패턴
# 더 다양한 패턴은 Hatch style reference 참고

# bar = plt.bar(labels, values)
# plt.ylim(180, 195)
# for index, rect in enumerate(bar):
#     plt.text(index, rect.get_height()+0.3, values[index], ha="center")


# 10. 데이터 프레임 활용

df = pd.read_csv("csv_.csv",encoding="utf-16")
df["지원번호"] = ["1번", "2번", "3번", "4번", "5번", "6번", "7번", "8번"]
df.set_index("지원번호",inplace=True)
#       Unnamed: 0   이름   학교    키   국어   영어   수학  과학  사회        SW특기
# 지원번호
# 1번             0  채치수  북산고  197   90   85  100  95  85      Python
# 2번             1  정대만  북산고  184   40   35   50  55  25        Java
# 3번             2  송태섭  북산고  168   80   75   70  80  75  Javascript
# 4번             3  서태웅  북산고  187   40   60   70  75  80         NaN
# 5번             4  강백호  북산고  188   15   20   10  35  10         NaN
# 6번             5  변덕규  능남고  202   80  100   95  85  80           C
# 7번             6  황태산  능남고  188   55   65   45  40  35      PYTHON
# 8번             7  윤대협  능남고  190  100   85   90  95  95          C#

# plt.plot(df.index, df["키"]); index를 x 데이터로, ["키"]를 y 데이터로
# plt.plot(df.index, df["영어"])
# plt.plot(df.index, df["수학"])

# plt.grid(axis="y", color="purple", alpha=0.2, linestyle="--", linewidth="2") # 데이터에 grid 추가, axis="x" x에만 추가


# 11. 누적 막대 그래프

# 아래와 같이 쓸 경우 데이터가 구분되지 않아 알아보기 어려움
# plt.bar(df["이름"], df["국어"])
# plt.bar(df["이름"], df["영어"])

# plt.bar(df["이름"], df["국어"], label="국어")
# plt.bar(df["이름"], df["영어"], bottom=df["국어"], label="영어") # 국어 데이터 위에 영어 데이터를 쌓음 (국어를 출력하지 않으면 빈칸으로 표시 됨)
# plt.bar(df["이름"], df["수학"], bottom=df["영어"]+df["국어"], label="수학")

# plt.xticks(rotation=60)
# plt.legend(ncol = 3)


# 12. 다중 막대 그래프

# arr = np.arange(5); numpy arange는 배열 형태로 자료가 저장되고
# print(arr+100); 덧셈이나
# print(arr*3); 곱셈을 단순 연산으로 출력할 수 있음.
# arr = arr*3
# print(arr)

# index = np.arange(df.shape[0]); index 부여
# plt.figure(figsize=(10,7))
# plt.bar(index - 0.25, df["국어"], width=0.25, label="국어"); 각 index와 width를 이용하여 각 데이터의 위치 및 크기 조절
# plt.bar(index, df["영어"], width=0.25, label="영어")
# plt.bar(index + 0.25, df["수학"], width=0.25, label="수학")
# plt.legend(ncol=3)
# plt.xticks(index, df["이름"], rotation=45); xticks로 index에 데이터를 직접 넣을 수 있음


# 13. 원 그래프 (기본)

# values = [30, 25, 20, 13, 10, 2]
# labels = ["Python", "Java", "Javascript", "C#", "C/C++", "ETC"]
# (값, labels=라벨링, autopct=표시형식(%.1f는 소수점만, %%는 % 표시), startangle=시작 지점(90이 12시 방향), counterclock=회전방향)
# plt.pie(values, labels=labels, autopct="%.1f%%", startangle=90, counterclock=False)

# explode = [0.2, 0.1, 0, 0, 0, 0]; 원점으로부터 간격을 살짝 벌려줌
# explode = [0.05] * len(values)# [간격 지정] * 데이터 개수로 일괄 지정 가능
# plt.pie(values, labels=labels, explode=explode)
# plt.legend(); pie chart 는 그냥 출력하면 데이터가 겹쳐서 잘 보이지 않음
# plt.legend(loc=(1.2, 0.3), title="언어별 선호도")


# 14. 원 그래프 (심화)

# colors = ["#ffadad","#ffd6a5","#fdffb6","#caffbf","#9bf6ff","#a0c4ff"]
# explode = [0.05] * 6
# plt.pie(values, labels=labels, autopct="%.1f%%", startangle=90, counterclock=False,colors=colors, explode=explode)

# wedgeprops = {"width":0.5, "edgecolor":"w", "linewidth":3}; 도넛 모양의 그래프를 만들 수 있음. width=도넛의 두께, edgecolor=도넛 테두리 색, linewidth=도넛 테두리 굵기
# plt.pie(values, labels=labels, autopct="%.1f%%", startangle=90, counterclock=False,colors=colors, wedgeprops=wedgeprops)

# def custom_autopct(pct): # autopct에 대한 custom 함수를 만들어서 표시 형식에 사용할 수 있음. 지정된 함수는 10% 이상의 데이터만 출력하는 함수
#     return ("%.1f%%" % pct) if pct >= 10 else ""
# plt.pie(values, labels=labels, autopct=custom_autopct, startangle=90, counterclock=False,colors=colors, pctdistance=0.7) #pctdistance=라벨 표시 위치 변경

# DataFrame으로 pie chart 만들기
# group = df.groupby("학교")
# values = [group.size()["북산고"],group.size()["능남고"]]
# labels = ["북산고", "능남고"]
# plt.pie(values,labels=labels)
# plt.title("소속 학교")


# 15. 산점도 그래프

# df["학년"] = [3, 3, 2, 1, 1, 3, 2, 2]
# plt.scatter(df["영어"], df["수학"])
# plt.xlabel("영어 점수")
# plt.ylabel("수학 점수")

# plt.figure(figsize=(7,7))
# df["학년"] = [3, 3, 2, 1, 1, 3, 2, 2]
# sizes = df["학년"] * 500 # 1학년 = 500 / 2학년 = 1000 / 3학년 1500
# plt.scatter(df["영어"], df["수학"], s=sizes, c=df["학년"], cmap="viridis", alpha=0.5) # s=사이즈 지정, c=색을 분류할 대상 지정, cmap=색 지정(matplotlib.cmap 참고)
# plt.xlabel("영어 점수")
# plt.ylabel("수학 점수")
# plt.colorbar(ticks=[1,2,3],label="학년",shrink=0.5, orientation="horizontal")

plt.show()