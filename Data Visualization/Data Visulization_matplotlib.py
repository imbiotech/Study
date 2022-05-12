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
# matplotlib.rcParams["font.family"] = "Malgun Gothic" # 한글 폰트 지정
# matplotlib.rcParams["font.size"] = 15 # 글자 크기 설정
# matplotlib.rcParams["axes.unicode_minus"] = False # 한글 폰트 사용 시 마이너스가 깨지는 현상 방지
# plt.title("꺾은선 그래프", fontdict={"family":"HYGungSo-Bold","size":20}) # 개별 폰트 설정

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
plt.figure(facecolor="grey")
plt.plot(x, y)








plt.show()
#