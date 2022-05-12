import matplotlib.pyplot as plt
import matplotlib

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


plt.show()
