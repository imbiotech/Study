import matplotlib.pyplot as plt
import matplotlib

# matplotlib; 다양한 형태의 그래프를 통해서 데이터 시각화를 할 수 있는 라이브러리

# 1. 그래프 기본

x = [1, 2, 3]
y = [2, 4, 8]
plt.plot(x,y)

# 그래프 제목 설정(Title)
plt.title("Line graph")

# 한글 폰트 설정
matplotlib.rcParams["font.family"] = "Malgun Gothic" # 한글 폰트 지정
matplotlib.rcParams["font.size"] = 15 # 글자 크기 설정
matplotlib.rcParams["axes.unicode_minus"] = False # 한글 폰트 사용 시 마이너스가 깨지는 현상 방지
# plt.title("꺾은선 그래프", fontdict={"family":"HYGungSo-Bold","size":20}) # 개별 폰트 설정

# plt.plot([-1, 0, 1],[-5, -1, 2])


# 2. 축

# 축 라벨링
plt.xlabel("X-axis", color = "red", loc="right")
plt.ylabel("Y-axis", color = "#00aa00", loc="top")

# 축 범위 설정 및 눈금 추가
plt.xticks([1,2,3])
plt.yticks([3,6,9,12])





plt.show()
#