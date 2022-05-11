import pandas

# Pandas = 파이썬에서 사용하는 데이터 분석 라이브러리

# 01. Series (1차원 데이터)

# Series 객체 생성 e.g) 1~4월까지 평균 온도 데이터 (-20, -10, 10, 20)
temp = pandas.Series([-20,-10,10,20])
# 0   -20
# 1   -10
# 2    10
# 3    20
# dtype: int64

# Series 객체 생성 + index 지정
temp = pandas.Series([-20,-10,10,20],index=["Jan","Feb","Mar","Apr"])
# Jan   -20
# Feb   -10
# Mar    10
# Apr    20
# dtype: int64


# 02. Data Frame (2차원 데이터)

# Data 객체 생성, Dict 형으로 생성 e.g) 슬램덩크 주요 인물 8명에 대한 데이터
# Data Frame 객체 생성
data = {
    '이름': ['채치수', '정대만', '송태섭', '서태웅', '강백호', '변덕규', '황태산', '윤대협'],
    '학교': ['북산고', '북산고', '북산고', '북산고', '북산고', '능남고', '능남고', '능남고'],
    '키': [197, 184, 168, 187, 188, 202, 188, 190],
    '국어': [90, 40, 80, 40, 15, 80, 55, 100],
    '영어': [85, 35, 75, 60, 20, 100, 65, 85],
    '수학': [100, 50, 70, 70, 10, 95, 45, 90],
    '과학': [95, 55, 80, 75, 35, 85, 40, 95],
    '사회': [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기': ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}
df1 = pandas.DataFrame(data)
#     이름   학교    키   국어   영어   수학  과학  사회        SW특기
# 0  채치수  북산고  197   90   85  100  95  85      Python
# 1  정대만  북산고  184   40   35   50  55  25        Java
# 2  송태섭  북산고  168   80   75   70  80  75  Javascript
# 3  서태웅  북산고  187   40   60   70  75  80
# 4  강백호  북산고  188   15   20   10  35  10
# 5  변덕규  능남고  202   80  100   95  85  80           C
# 6  황태산  능남고  188   55   65   45  40  35      PYTHON
# 7  윤대협  능남고  190  100   85   90  95  95          C#

# dataframe 접근법
df1["이름"]
# 0    채치수
# 1    정대만
# 2    송태섭
# 3    서태웅
# 4    강백호
# 5    변덕규
# 6    황태산
# 7    윤대협

df1[["이름", "키"]]
#     이름    키
# 0  채치수  197
# 1  정대만  184
# 2  송태섭  168
# 3  서태웅  187
# 4  강백호  188
# 5  변덕규  202
# 6  황태산  188
# 7  윤대협  190

# Data Frame 객체 생성 + index 지정
df2 = pandas.DataFrame(data, index=["1번","2번","3번","4번","5번","6번","7번","8번"])
#  이름   학교    키   국어   영어   수학  과학  사회        SW특기
# 1번  채치수  북산고  197   90   85  100  95  85      Python
# 2번  정대만  북산고  184   40   35   50  55  25        Java
# 3번  송태섭  북산고  168   80   75   70  80  75  Javascript
# 4번  서태웅  북산고  187   40   60   70  75  80
# 6번  변덕규  능남고  202   80  100   95  85  80           C
# 7번  황태산  능남고  188   55   65   45  40  35      PYTHON
# 8번  윤대협  능남고  190  100   85   90  95  95          C#

# Data Frame 객체 생성 + column 지정
df3 = pandas.DataFrame(data, columns=["이름","학교"])
# 이름   학교
# 0  채치수  북산고
# 1  정대만  북산고
# 2  송태섭  북산고
# 3  서태웅  북산고
# 4  강백호  북산고
# 5  변덕규  능남고
# 6  황태산  능남고
# 7  윤대협  능남고


# 03. Index (데이터 접근을 위한 주소값)
df2.index.name = "지원번호"
#        이름   학교    키   국어   영어   수학  과학  사회        SW특기
# 지원번호
# 1번    채치수  북산고  197   90   85  100  95  85      Python
# 2번    정대만  북산고  184   40   35   50  55  25        Java
# 3번    송태섭  북산고  168   80   75   70  80  75  Javascript
# 4번    서태웅  북산고  187   40   60   70  75  80
# 5번    강백호  북산고  188   15   20   10  35  10
# 6번    변덕규  능남고  202   80  100   95  85  80           C
# 7번    황태산  능남고  188   55   65   45  40  35      PYTHON
# 8번    윤대협  능남고  190  100   85   90  95  95          C#

# index 초기화
# print(df.reset_index(drop=True, inplace=True))
df2.reset_index(drop=True, inplace=True)
#     이름   학교    키   국어   영어   수학  과학  사회        SW특기
# 0  채치수  북산고  197   90   85  100  95  85      Python
# 1  정대만  북산고  184   40   35   50  55  25        Java
# 2  송태섭  북산고  168   80   75   70  80  75  Javascript
# 3  서태웅  북산고  187   40   60   70  75  80
# 4  강백호  북산고  188   15   20   10  35  10
# 5  변덕규  능남고  202   80  100   95  85  80           C
# 6  황태산  능남고  188   55   65   45  40  35      PYTHON
# 7  윤대협  능남고  190  100   85   90  95  95          C#

# 지정한 column의 index를 설정할 수 있음
df2.set_index("이름",inplace=True)
#       학교    키   국어   영어   수학  과학  사회        SW특기
# 이름
# 채치수  북산고  197   90   85  100  95  85      Python
# 정대만  북산고  184   40   35   50  55  25        Java
# 송태섭  북산고  168   80   75   70  80  75  Javascript
# 서태웅  북산고  187   40   60   70  75  80
# 강백호  북산고  188   15   20   10  35  10
# 변덕규  능남고  202   80  100   95  85  80           C
# 황태산  능남고  188   55   65   45  40  35      PYTHON
# 윤대협  능남고  190  100   85   90  95  95          C#

# index를 차순 정렬이 가능함
df2.sort_index()
#       학교    키   국어   영어   수학  과학  사회        SW특기
# 이름
# 채치수  북산고  197   90   85  100  95  85      Python
# 정대만  북산고  184   40   35   50  55  25        Java
# 송태섭  북산고  168   80   75   70  80  75  Javascript
# 서태웅  북산고  187   40   60   70  75  80
# 강백호  북산고  188   15   20   10  35  10
# 변덕규  능남고  202   80  100   95  85  80           C
# 황태산  능남고  188   55   65   45  40  35      PYTHON
# 윤대협  능남고  190  100   85   90  95  95          C#

df2.sort_index(ascending=False)
#       학교    키   국어   영어   수학  과학  사회        SW특기
# 이름
# 채치수  북산고  197   90   85  100  95  85      Python
# 정대만  북산고  184   40   35   50  55  25        Java
# 송태섭  북산고  168   80   75   70  80  75  Javascript
# 서태웅  북산고  187   40   60   70  75  80
# 강백호  북산고  188   15   20   10  35  10
# 변덕규  능남고  202   80  100   95  85  80           C
# 황태산  능남고  188   55   65   45  40  35      PYTHON
# 윤대협  능남고  190  100   85   90  95  95          C#


# 04. File 저장 및 열기 (Dataframe 객체를 excel, csv, txt 등의 형식으로 저장 및 열기 진행)
df = pandas.DataFrame(data)

# csv 파일 저장 및 열기
df.to_csv("csv_.csv",encoding="utf-16")
csv_ = pandas.read_csv("csv_.csv",encoding="utf-16",skiprows=4) # skiprows = 1; 첫 행부터 1개 행을 건너뛴 상태로 읽음
#    3  서태웅  북산고  187   40   60  70  75  80 Unnamed: 9
# 0  4  강백호  북산고  188   15   20  10  35  10        NaN
# 1  5  변덕규  능남고  202   80  100  95  85  80          C
# 2  6  황태산  능남고  188   55   65  45  40  35     PYTHON
# 3  7  윤대협  능남고  190  100   85  90  95  95         C#

csv_ = pandas.read_csv("csv_.csv",encoding="utf-16",skiprows=[1,5,7]) # skiprows = [1,3,5]; 해당 행을 지우고 읽음
#    Unnamed: 0   이름   학교    키   국어   영어  수학  과학  사회        SW특기
# 0           1  정대만  북산고  184   40   35  50  55  25        Java
# 1           2  송태섭  북산고  168   80   75  70  80  75  Javascript
# 2           3  서태웅  북산고  187   40   60  70  75  80         NaN
# 3           5  변덕규  능남고  202   80  100  95  85  80           C
# 4           7  윤대협  능남고  190  100   85  90  95  95          C#

csv_ = pandas.read_csv("csv_.csv",encoding="utf-16",skiprows=2, nrows=3) # nrows = 4; skiprows 이후 첫 행부터 4개 행을 읽음
# Unnamed: 0   이름   학교    키  국어  영어   수학  과학  사회        SW특기
# 0           0  채치수  북산고  197  90  85  100  95  85      Python
# 1           1  정대만  북산고  184  40  35   50  55  25        Java
# 2           2  송태섭  북산고  168  80  75   70  80  75  Javascript

# excel 파일 저장 및 열기
# df.to_excel("excel_.xlsx")
# excel_ = pandas.read_excel("excel_.xlsx")
#    Unnamed: 0   이름   학교    키   국어   영어   수학  과학  사회        SW특기
# 0           0  채치수  북산고  197   90   85  100  95  85      Python
# 1           1  정대만  북산고  184   40   35   50  55  25        Java
# 2           2  송태섭  북산고  168   80   75   70  80  75  Javascript
# 3           3  서태웅  북산고  187   40   60   70  75  80         NaN
# 4           4  강백호  북산고  188   15   20   10  35  10         NaN
# 5           5  변덕규  능남고  202   80  100   95  85  80           C
# 6           6  황태산  능남고  188   55   65   45  40  35      PYTHON
# 7           7  윤대협  능남고  190  100   85   90  95  95          C#

# txt 파일 저장 및 열기
# df.to_csv("csv_.txt",encoding="utf-16")
# text_ = pandas.read_csv("csv_.txt",encoding="utf-16",index_col=0) # index_col = HEADER; Header에 홰당하는 컬럼을 index로 사용
#     이름   학교    키   국어   영어   수학  과학  사회        SW특기
# 0  채치수  북산고  197   90   85  100  95  85      Python
# 1  정대만  북산고  184   40   35   50  55  25        Java
# 2  송태섭  북산고  168   80   75   70  80  75  Javascript
# 3  서태웅  북산고  187   40   60   70  75  80         NaN
# 4  강백호  북산고  188   15   20   10  35  10         NaN
# 5  변덕규  능남고  202   80  100   95  85  80           C
# 6  황태산  능남고  188   55   65   45  40  35      PYTHON
# 7  윤대협  능남고  190  100   85   90  95  95          C#

# text_.set_index("이름",inplace=True) # .set_index(HEADER, inplace=True); Header 지정
#       학교    키   국어   영어   수학  과학  사회        SW특기
# 이름
# 채치수  북산고  197   90   85  100  95  85      Python
# 정대만  북산고  184   40   35   50  55  25        Java
# 송태섭  북산고  168   80   75   70  80  75  Javascript
# 서태웅  북산고  187   40   60   70  75  80         NaN
# 강백호  북산고  188   15   20   10  35  10         NaN
# 변덕규  능남고  202   80  100   95  85  80           C
# 황태산  능남고  188   55   65   45  40  35      PYTHON
# 윤대협  능남고  190  100   85   90  95  95          C#


# 05. 데이터 확인
csv_ = pandas.read_csv("csv_.csv",encoding="utf-16")

# DataFrame 확인
# .describe(); 계산 가능한 데이터에 대해서 column 별 개수, 평균, 표준편차, 최소/최대값 등의 정보 출력
csv_.describe()
#        Unnamed: 0           키          국어  ...          수학         과학         사회
# count     8.00000    8.000000    8.000000  ...    8.000000   8.000000   8.000000
# mean      3.50000  188.000000   62.500000  ...   66.250000  70.000000  60.625000
# std       2.44949    9.985704   29.519969  ...   30.325614  23.754699  32.120032
# min       0.00000  168.000000   15.000000  ...   10.000000  35.000000  10.000000
# 25%       1.75000  186.250000   40.000000  ...   48.750000  51.250000  32.500000
# 50%       3.50000  188.000000   67.500000  ...   70.000000  77.500000  77.500000
# 75%       5.25000  191.750000   82.500000  ...   91.250000  87.500000  81.250000
# max       7.00000  202.000000  100.000000  ...  100.000000  95.000000  95.000000

# .info(); 각 column 별 데이터 개수 및 형태 출력
# csv_.info(); # print 안 해도 됨
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 8 entries, 0 to 7
# Data columns (total 10 columns):
#  #   Column      Non-Null Count  Dtype
# ---  ------      --------------  -----
#  0   Unnamed: 0  8 non-null      int64
#  1   이름          8 non-null      object
#  2   학교          8 non-null      object
#  3   키           8 non-null      int64
#  4   국어          8 non-null      int64
#  5   영어          8 non-null      int64
#  6   수학          8 non-null      int64
#  7   과학          8 non-null      int64
#  8   사회          8 non-null      int64
#  9   SW특기        6 non-null      object
# dtypes: int64(7), object(3)
# memory usage: 768.0+ bytes

# .head(); 첫 5개 rows의 data를 가져옴, head(8)
csv_.head()
#    Unnamed: 0   이름   학교    키  국어  영어   수학  과학  사회        SW특기
# 0           0  채치수  북산고  197  90  85  100  95  85      Python
# 1           1  정대만  북산고  184  40  35   50  55  25        Java
# 2           2  송태섭  북산고  168  80  75   70  80  75  Javascript
# 3           3  서태웅  북산고  187  40  60   70  75  80         NaN
# 4           4  강백호  북산고  188  15  20   10  35  10         NaN

# .tail(); 마지막 5개 rows의 data를 가져옴
csv_.tail()
# Unnamed: 0   이름   학교    키   국어   영어  수학  과학  사회    SW특기
# 3           3  서태웅  북산고  187   40   60  70  75  80     NaN
# 4           4  강백호  북산고  188   15   20  10  35  10     NaN
# 5           5  변덕규  능남고  202   80  100  95  85  80       C
# 6           6  황태산  능남고  188   55   65  45  40  35  PYTHON
# 7           7  윤대협  능남고  190  100   85  90  95  95      C#

# .columes; 컬럼 확인
csv_.columns
# Index(['Unnamed: 0', '이름', '학교', '키', '국어', '영어', '수학', '과학', '사회', 'SW특기'], dtype='object')

# .values; 값 확인
csv_.values
# [[0 '채치수' '북산고' 197 90 85 100 95 85 'Python']
#  [1 '정대만' '북산고' 184 40 35 50 55 25 'Java']
#  [2 '송태섭' '북산고' 168 80 75 70 80 75 'Javascript']
#  [3 '서태웅' '북산고' 187 40 60 70 75 80 nan]
#  [4 '강백호' '북산고' 188 15 20 10 35 10 nan]
#  [5 '변덕규' '능남고' 202 80 100 95 85 80 'C']
#  [6 '황태산' '능남고' 188 55 65 45 40 35 'PYTHON']
#  [7 '윤대협' '능남고' 190 100 85 90 95 95 'C#']]

# .shapes; (row, column) 으로 표시
csv_.shape
# (8, 10)

# Series 확인
# .min(); 최소값
csv_["키"].min()
# 168

# .max(); 최대값
csv_["키"].max()
# 202

# .nlargest(n); 최대값부터 n개의 값을 가져옴
csv_["키"].nlargest(3)
# 5    202
# 0    197
# 7    190
# Name: 키, dtype: int64

# .mean(); 평균
csv_["키"].mean()
# 188.0

# .sum(); 합산
csv_["키"].sum()
# 1504

# .count(); 유효 데이터 개수
csv_["SW특기"].count()
# 6

# .unique(); 중복값 제거 후 list 출력
csv_["학교"].unique()
# ['북산고' '능남고']

# .nunique(); unique 원소의 개수 출력
csv_["학교"].nunique()
# 2


# 06. 데이터 선택(기본)

# Column 선택(label)
# DataFrame[key]; 선택된 key 값의 Column 호출
csv_["키"]
# 0    197
# 1    184
# 2    168
# 3    187
# 4    188
# 5    202
# 6    188
# 7    190
# Name: 키, dtype: int64

# DataFrame[[Key1, Key2, Key3]]; 선택된 key 값들의 Column을 호출
csv_[["이름","키"]]
#     이름    키
# 0  채치수  197
# 1  정대만  184
# 2  송태섭  168
# 3  서태웅  187
# 4  강백호  188
# 5  변덕규  202
# 6  황태산  188
# 7  윤대협  190

# Column 선택(정수 index)
# .columns[n]; n-1번 째 column의 이름을 호출 (음수로 역순서 호출 가능)
csv_.columns[2]
# 학교

# DataFrame[DataFrame.columns[n]]; n-1번 째 Column의 값을 호출
csv_[csv_.columns[2]]
# 0    북산고
# 1    북산고
# 2    북산고
# 3    북산고
# 4    북산고
# 5    능남고
# 6    능남고
# 7    능남고

# slicing
# DataFrame[Key][x:y]; 선택된 Key 값의 Column에서 x~y-1번 째 값을 호출
csv_["키"][2:5]
# 2    168
# 3    187
# 4    188
# Name: 키, dtype: int64

# DataFrame[x:y]; 전체 테이블에서 x~y-1번 째 값을 호출
csv_[2:5]
#    Unnamed: 0   이름   학교    키  국어  영어  수학  과학  사회        SW특기
# 2           2  송태섭  북산고  168  80  75  70  80  75  Javascript
# 3           3  서태웅  북산고  187  40  60  70  75  80         NaN
# 4           4  강백호  북산고  188  15  20  10  35  10         NaN


# 07. 데이터 선택(loc); 이름을 이용하여 원하는 row, column을 선택

# .loc[Rowkey]; 선택된 Key 값의 Row 호출
csv_.loc[3]
# Unnamed: 0      3
# 이름            서태웅
# 학교            북산고
# 키             187
# 국어             40
# 영어             60
# 수학             70
# 과학             75
# 사회             80
# SW특기          NaN
# Name: 3, dtype: object

# .loc[Rowkey, Columnkey]; 선택된 Row, Column key로 값 호출
csv_.loc[3,"키"]
# 187

# .loc[[Rowkey1, Rowkey2],[Columnkey1, Columnkey2]; 각각 호출
csv_.loc[[3,5],["이름","키"]]
#     이름    키
# 3  서태웅  187
# 5  변덕규  202

# .loc[Rowkey1:Rowkey2,Columnkey1:Columnkey2]; 범위 호출 *Rowkey2, Columnkey2를 포함한 결과가 호출됨
csv_.loc[3:5,"이름":"키"]
#     이름   학교    키
# 3  서태웅  북산고  187
# 4  강백호  북산고  188
# 5  변덕규  능남고  202


# 08. 데이터 선택(iloc); 위치를 이용하여 원하는 row, column을 선택, integerlocation

# .iloc[n]; n-1번 째 Row 호출
csv_.iloc[4]
# Unnamed: 0      4
# 이름            강백호
# 학교            북산고
# 키             188
# 국어             15
# 영어             20
# 수학             10
# 과학             35
# 사회             10
# SW특기          NaN
# Name: 4, dtype: object

# .iloc[x:y]; x~y-1번 째 Row 호출
csv_.iloc[4:6]
#    Unnamed: 0   이름   학교    키  국어   영어  수학  과학  사회 SW특기
# 4           4  강백호  북산고  188  15   20  10  35  10  NaN
# 5           5  변덕규  능남고  202  80  100  95  85  80    C

# .iloc[x,y]; x번 째 Row, y번 째 Column 호출
csv_.iloc[4,7]
# 35

# .iloc[[x,y],[z,w]]; x,y번 째 Row에서 z,w번 째 Column 호출
csv_.iloc[[4,6],[3,5]]
#      키  영어
# 4  188  20
# 6  188  65

# .iloc[x:y,z:w]; x~y-1번 째 Row에서 z~w-1번 째 Column 호출
csv_.iloc[4:6,3:5]
#      키  국어
# 4  188  15
# 5  202  80


# 09. 데이터 선택(조건); 조건에 해당하는 데이터 선택

# FILTER = (DataFrame[Key] >= Value); DataFrame[FILTER]; 선택된 Column에서 Value와의 크기 비교
# DataFrame[FILTER]; 조건에 해당하는 Row만 호출
FILTER = csv_["키"] >= 185
csv_[FILTER] # = csv_[FILTER = csv_["키"] >= 185], Filter 조건 자체를 넣어도 됨
#    Unnamed: 0   이름   학교    키   국어   영어   수학  과학  사회    SW특기
# 0           0  채치수  북산고  197   90   85  100  95  85  Python
# 3           3  서태웅  북산고  187   40   60   70  75  80     NaN
# 4           4  강백호  북산고  188   15   20   10  35  10     NaN
# 5           5  변덕규  능남고  202   80  100   95  85  80       C
# 6           6  황태산  능남고  188   55   65   45  40  35  PYTHON
# 7           7  윤대협  능남고  190  100   85   90  95  95      C#

# FILTER = DataFrame[Key].str.startswith("str"); DataFrame[FILTER]; 선택된 Column의 값이 "str"로 시작하는 모든 row
FILTER = csv_["학교"].str.startswith("북")
csv_[FILTER]
#    Unnamed: 0   이름   학교    키  국어  영어   수학  과학  사회        SW특기
# 0           0  채치수  북산고  197  90  85  100  95  85      Python
# 1           1  정대만  북산고  184  40  35   50  55  25        Java
# 2           2  송태섭  북산고  168  80  75   70  80  75  Javascript
# 3           3  서태웅  북산고  187  40  60   70  75  80         NaN
# 4           4  강백호  북산고  188  15  20   10  35  10         NaN

# FILTER = DataFrame[Key].str.contains("str", na=False); DataFrame[FILTER]; 선택된 Column의 값이 "str"을 포함하는 모든 row / na=True; NaN을 False로 인식
FILTER = csv_["SW특기"].str.startswith("J", na=False)
csv_[FILTER]
#    Unnamed: 0   이름   학교    키  국어  영어  수학  과학  사회        SW특기
# 1           1  정대만  북산고  184  40  35  50  55  25        Java
# 2           2  송태섭  북산고  168  80  75  70  80  75  Javascript

# DataFrame[-FILTER]; FILTER 조건을 제외한 row
csv_[-FILTER]
#    Unnamed: 0   이름   학교    키   국어   영어   수학  과학  사회    SW특기
# 0           0  채치수  북산고  197   90   85  100  95  85  Python
# 3           3  서태웅  북산고  187   40   60   70  75  80     NaN
# 4           4  강백호  북산고  188   15   20   10  35  10     NaN
# 5           5  변덕규  능남고  202   80  100   95  85  80       C
# 6           6  황태산  능남고  188   55   65   45  40  35  PYTHON
# 7           7  윤대협  능남고  190  100   85   90  95  95      C#

# FILTER = DataFrame[Key].isin(list); DataFrame[FILTER]; 선택된 Column의 값이 list의 값과 일치하는 모든 row
FILTER = csv_["SW특기"].isin(["Java","Javascript"])
csv_[FILTER]
#    Unnamed: 0   이름   학교    키  국어  영어  수학  과학  사회        SW특기
# 1           1  정대만  북산고  184  40  35  50  55  25        Java
# 2           2  송태섭  북산고  168  80  75  70  80  75  Javascript

FILTER = csv_["SW특기"].isin(["python"])
csv_[FILTER]
# Empty DataFrame
# Columns: [Unnamed: 0, 이름, 학교, 키, 국어, 영어, 수학, 과학, 사회, SW특기]
# Index: []

# FILTER = DataFrame[Key].str.lower().isin(list); DataFrame[FILTER]; 선택된 Column의 모든 값을 소문자로 변환한 뒤 list의 값과 일치하는지 비교
FILTER = csv_["SW특기"].str.lower().isin(["python"])
csv_[FILTER]
#    Unnamed: 0   이름   학교    키  국어  영어   수학  과학  사회    SW특기
# 0           0  채치수  북산고  197  90  85  100  95  85  Python
# 6           6  황태산  능남고  188  55  65   45  40  35  PYTHON


# 10. 결측치; 비어있는 데이터

# 데이터 채우기(fillna)
# .fillna("str"); NaN Data를 "str"로 채움
csv_.fillna("NA")
#    Unnamed: 0   이름   학교    키   국어   영어   수학  과학  사회        SW특기
# 0           0  채치수  북산고  197   90   85  100  95  85      Python
# 1           1  정대만  북산고  184   40   35   50  55  25        Java
# 2           2  송태섭  북산고  168   80   75   70  80  75  Javascript
# 3           3  서태웅  북산고  187   40   60   70  75  80          NA
# 4           4  강백호  북산고  188   15   20   10  35  10          NA
# 5           5  변덕규  능남고  202   80  100   95  85  80           C
# 6           6  황태산  능남고  188   55   65   45  40  35      PYTHON
# 7           7  윤대협  능남고  190  100   85   90  95  95          C#

# 데이터 제외하기(drop)
# .dropna(); NaN이 포함된 Row를 삭제
csv_.dropna()
#    Unnamed: 0   이름   학교    키   국어   영어   수학  과학  사회        SW특기
# 0           0  채치수  북산고  197   90   85  100  95  85      Python
# 1           1  정대만  북산고  184   40   35   50  55  25        Java
# 2           2  송태섭  북산고  168   80   75   70  80  75  Javascript
# 5           5  변덕규  능남고  202   80  100   95  85  80           C
# 6           6  황태산  능남고  188   55   65   45  40  35      PYTHON
# 7           7  윤대협  능남고  190  100   85   90  95  95          C#

# .dropna(axis="index" or "columns", how="any" or "all"); axis = "index"는 row 삭제, "columns"은 column 삭제 // how = "any"는 하나라도 NaN이면 삭제, "all"은 전체가 NaN이면 삭제
csv_.dropna(axis="columns",how="any")
#    Unnamed: 0   이름   학교    키   국어   영어   수학  과학  사회
# 0           0  채치수  북산고  197   90   85  100  95  85
# 1           1  정대만  북산고  184   40   35   50  55  25
# 2           2  송태섭  북산고  168   80   75   70  80  75
# 3           3  서태웅  북산고  187   40   60   70  75  80
# 4           4  강백호  북산고  188   15   20   10  35  10
# 5           5  변덕규  능남고  202   80  100   95  85  80
# 6           6  황태산  능남고  188   55   65   45  40  35
# 7           7  윤대협  능남고  190  100   85   90  95  95


# 11. 데이터 정렬

# .sort_values(Key, ascending=True or False); 해당하는 Column을 정렬
csv_.sort_values("키",ascending=True)
#    Unnamed: 0   이름   학교    키   국어   영어   수학  과학  사회        SW특기
# 2           2  송태섭  북산고  168   80   75   70  80  75  Javascript
# 1           1  정대만  북산고  184   40   35   50  55  25        Java
# 3           3  서태웅  북산고  187   40   60   70  75  80         NaN
# 4           4  강백호  북산고  188   15   20   10  35  10         NaN
# 6           6  황태산  능남고  188   55   65   45  40  35      PYTHON
# 7           7  윤대협  능남고  190  100   85   90  95  95          C#
# 0           0  채치수  북산고  197   90   85  100  95  85      Python
# 5           5  변덕규  능남고  202   80  100   95  85  80           C

# .sort_values([Key1, Key2], ascending=False); 해당하는 Columns를 내림 차순으로 정렬하되, 앞쪽부터 우선 순위가 높음
# .sort_values([Key1, Key2], ascending=[True,False]); 해당하는 Columns를 해당하는 차순으로 정렬 // Key1은 오름차순, Key2는 내림차순 정렬됨
csv_.sort_values(["키", "국어"],ascending=[True, False])
#    Unnamed: 0   이름   학교    키   국어   영어   수학  과학  사회        SW특기
# 2           2  송태섭  북산고  168   80   75   70  80  75  Javascript
# 1           1  정대만  북산고  184   40   35   50  55  25        Java
# 3           3  서태웅  북산고  187   40   60   70  75  80         NaN
# 6           6  황태산  능남고  188   55   65   45  40  35      PYTHON
# 4           4  강백호  북산고  188   15   20   10  35  10         NaN
# 7           7  윤대협  능남고  190  100   85   90  95  95          C#
# 0           0  채치수  북산고  197   90   85  100  95  85      Python
# 5           5  변덕규  능남고  202   80  100   95  85  80           C


# 12. 데이터 수정

# Column 수정
# DataFrame[Key].replace({"Value1":"Value2","Value3":"Value4"}); 선택된 Column에서 Value1을 Value2로, Value3을 Value4로 바꿈
csv_["학교"].replace({"북산고":"A학교","능남고":"B학교"})
# 0    A학교
# 1    A학교
# 2    A학교
# 3    A학교
# 4    A학교
# 5    B학교
# 6    B학교
# 7    B학교
# Name: 학교, dtype: object

# DataFrame[Key] = DataFrame[Key].str.lower(); 선택된 Column을 소문자로 치환
csv_["SW특기"].str.lower()
# 0        python
# 1          java
# 2    javascript
# 3           NaN
# 4           NaN
# 5             c
# 6        python
# 7            c#
# Name: SW특기, dtype: object

# DataFrame[Key] = DataFrame[Key] + Value; 선택된 Column 전체에 Value를 더한 값을 입력
csv_["SW특기"] + csv_["학교"]
# 0        Python북산고
# 1          Java북산고
# 2    Javascript북산고
# 3              NaN
# 4              NaN
# 5             C능남고
# 6        PYTHON능남고
# 7            C#능남고

# Column 추가
# DataFrame[NewKey] = ~~~; 해당 식으로 계산하여 NewKey Column을 우측에 추가함
csv_["새 컬럼"]=[1,2,3,4,5,6,7,8]
#    Unnamed: 0   이름   학교    키   국어   영어   수학  과학  사회        SW특기  새 컬럼
# 0           0  채치수  북산고  197   90   85  100  95  85      Python     1
# 1           1  정대만  북산고  184   40   35   50  55  25        Java     2
# 2           2  송태섭  북산고  168   80   75   70  80  75  Javascript     3
# 3           3  서태웅  북산고  187   40   60   70  75  80         NaN     4
# 4           4  강백호  북산고  188   15   20   10  35  10         NaN     5
# 5           5  변덕규  능남고  202   80  100   95  85  80           C     6
# 6           6  황태산  능남고  188   55   65   45  40  35      PYTHON     7
# 7           7  윤대협  능남고  190  100   85   90  95  95          C#     8

# .loc[DataFrame[Key1] > Value1, Key2] = Value2; Key1 Column의 값이 Value1보다 큰 Row를 가져온 후 Key2 Column에 Value2를 넣음
csv_.loc[csv_["국어"]>=90, "수학"] = 200
#    Unnamed: 0   이름   학교    키   국어   영어   수학  과학  사회        SW특기  새 컬럼
# 0           0  채치수  북산고  197   90   85  200  95  85      Python     1
# 1           1  정대만  북산고  184   40   35   50  55  25        Java     2
# 2           2  송태섭  북산고  168   80   75   70  80  75  Javascript     3
# 3           3  서태웅  북산고  187   40   60   70  75  80         NaN     4
# 4           4  강백호  북산고  188   15   20   10  35  10         NaN     5
# 5           5  변덕규  능남고  202   80  100   95  85  80           C     6
# 6           6  황태산  능남고  188   55   65   45  40  35      PYTHON     7
# 7           7  윤대협  능남고  190  100   85  200  95  95          C#     8

# Row 추가
# .loc[NewIndex] = ~~~; 해당 Index로 시작하는 Row를 하단에 추가함
csv_.loc[8] = [8,"박진영","능남고",180,100,100,100,100,100,"python",9]
#    Unnamed: 0   이름   학교    키   국어   영어   수학   과학   사회        SW특기  새 컬럼
# 0           0  채치수  북산고  197   90   85  200   95   85      Python     1
# 1           1  정대만  북산고  184   40   35   50   55   25        Java     2
# 2           2  송태섭  북산고  168   80   75   70   80   75  Javascript     3
# 3           3  서태웅  북산고  187   40   60   70   75   80         NaN     4
# 4           4  강백호  북산고  188   15   20   10   35   10         NaN     5
# 5           5  변덕규  능남고  202   80  100   95   85   80           C     6
# 6           6  황태산  능남고  188   55   65   45   40   35      PYTHON     7
# 7           7  윤대협  능남고  190  100   85  200   95   95          C#     8
# 8           8  박진영  능남고  180  100  100  100  100  100      python     9

# Column 삭제
# .drop(columns=[Keylist]); Keylist에 해당하는 Column을 삭제
csv_.drop(columns=["이름","국어"])
#    Unnamed: 0   학교    키   영어   수학   과학   사회        SW특기  새 컬럼
# 0           0  북산고  197   85  200   95   85      Python     1
# 1           1  북산고  184   35   50   55   25        Java     2
# 2           2  북산고  168   75   70   80   75  Javascript     3
# 3           3  북산고  187   60   70   75   80         NaN     4
# 4           4  북산고  188   20   10   35   10         NaN     5
# 5           5  능남고  202  100   95   85   80           C     6
# 6           6  능남고  188   65   45   40   35      PYTHON     7
# 7           7  능남고  190   85  200   95   95          C#     8
# 8           8  능남고  180  100  100  100  100      python     9

# Row 삭제
# .drop(index=[Keylist]); Keylist에 해당하는 Row를 삭제
csv_.drop(index=[1,5,7])
#    Unnamed: 0   이름   학교    키   국어   영어   수학   과학   사회        SW특기  새 컬럼
# 0           0  채치수  북산고  197   90   85  200   95   85      Python     1
# 2           2  송태섭  북산고  168   80   75   70   80   75  Javascript     3
# 3           3  서태웅  북산고  187   40   60   70   75   80         NaN     4
# 4           4  강백호  북산고  188   15   20   10   35   10         NaN     5
# 6           6  황태산  능남고  188   55   65   45   40   35      PYTHON     7
# 8           8  박진영  능남고  180  100  100  100  100  100      python     9

# .drop(index=DataFrame[FILTER].index); FILTER에 해당하는 index를 확인하여 해당 row를 삭제
FILTER = csv_["SW특기"].str.lower().isin(["python"])
csv_.drop(index=csv_[FILTER].index)
#    Unnamed: 0   이름   학교    키   국어   영어   수학  과학  사회        SW특기  새 컬럼
# 1           1  정대만  북산고  184   40   35   50  55  25        Java     2
# 2           2  송태섭  북산고  168   80   75   70  80  75  Javascript     3
# 3           3  서태웅  북산고  187   40   60   70  75  80         NaN     4
# 4           4  강백호  북산고  188   15   20   10  35  10         NaN     5
# 5           5  변덕규  능남고  202   80  100   95  85  80           C     6
# 7           7  윤대협  능남고  190  100   85  200  95  95          C#     8

# Cell 수정
# .loc[Index, Key] = Value; index row의 Key Column에 해당하는 값을 Value로 업데이트
csv_.loc[3,"SW특기"] = "What"
#    Unnamed: 0   이름   학교    키   국어   영어   수학   과학   사회        SW특기  새 컬럼
# 0           0  채치수  북산고  197   90   85  200   95   85      Python     1
# 1           1  정대만  북산고  184   40   35   50   55   25        Java     2
# 2           2  송태섭  북산고  168   80   75   70   80   75  Javascript     3
# 3           3  서태웅  북산고  187   40   60   70   75   80        What     4
# 4           4  강백호  북산고  188   15   20   10   35   10         NaN     5
# 5           5  변덕규  능남고  202   80  100   95   85   80           C     6
# 6           6  황태산  능남고  188   55   65   45   40   35      PYTHON     7
# 7           7  윤대협  능남고  190  100   85  200   95   95          C#     8
# 8           8  박진영  능남고  180  100  100  100  100  100      python     9

# .loc[Index, [Key1, Key2]] = [Value1, Value2]; index row의 Key1 Column 값은 Value1로, Key2 Column 값은 Value2로 업데이트
csv_.loc[3,["국어","영어","수학","과학","사회"]] = [100,100,100,100,100]
#    Unnamed: 0   이름   학교    키   국어   영어   수학   과학   사회        SW특기  새 컬럼
# 0           0  채치수  북산고  197   90   85  200   95   85      Python     1
# 1           1  정대만  북산고  184   40   35   50   55   25        Java     2
# 2           2  송태섭  북산고  168   80   75   70   80   75  Javascript     3
# 3           3  서태웅  북산고  187  100  100  100  100  100        What     4
# 4           4  강백호  북산고  188   15   20   10   35   10         NaN     5
# 5           5  변덕규  능남고  202   80  100   95   85   80           C     6
# 6           6  황태산  능남고  188   55   65   45   40   35      PYTHON     7
# 7           7  윤대협  능남고  190  100   85  200   95   95          C#     8
# 8           8  박진영  능남고  180  100  100  100  100  100      python     9

# Column 위치 변경
# Columns = list(DataFrame.columns); DataFrame의 Key 값들을 List 형태로 저장
# DataFrame = DataFrame[[Columns[1]]+[Columns[-1]]+Columns[2:4]+.....]; Key값들을 재배열하여 List형태로 만든 뒤 다시 index로 지정
Cols = list(csv_.columns)
csv_ = csv_[[Cols[0]]+[Cols[1]]+[Cols[3]]+[Cols[2]]+Cols[4:-1]]
#    Unnamed: 0   이름    키   학교   국어   영어   수학   과학   사회        SW특기
# 0           0  채치수  197  북산고   90   85  200   95   85      Python
# 1           1  정대만  184  북산고   40   35   50   55   25        Java
# 2           2  송태섭  168  북산고   80   75   70   80   75  Javascript
# 3           3  서태웅  187  북산고  100  100  100  100  100        What
# 4           4  강백호  188  북산고   15   20   10   35   10         NaN
# 5           5  변덕규  202  능남고   80  100   95   85   80           C
# 6           6  황태산  188  능남고   55   65   45   40   35      PYTHON
# 7           7  윤대협  190  능남고  100   85  200   95   95          C#
# 8           8  박진영  180  능남고  100  100  100  100  100      python

# Column 이름 변경
# .columns = [Keys]; 새로운 Key list로 Column의 이름을 바꿈
csv_.columns = ["No.", "Name", "Height", "School", "Korean", "English", "Math", "Science", "Social", "SW"]
#    No. Name  Height School  Korean  English  Math  Science  Social          SW
# 0    0  채치수     197    북산고      90       85   200       95      85      Python
# 1    1  정대만     184    북산고      40       35    50       55      25        Java
# 2    2  송태섭     168    북산고      80       75    70       80      75  Javascript
# 3    3  서태웅     187    북산고     100      100   100      100     100        What
# 4    4  강백호     188    북산고      15       20    10       35      10         NaN
# 5    5  변덕규     202    능남고      80      100    95       85      80           C
# 6    6  황태산     188    능남고      55       65    45       40      35      PYTHON
# 7    7  윤대협     190    능남고     100       85   200       95      95          C#
# 8    8  박진영     180    능남고     100      100   100      100     100      python


# 13. 함수 적용; int 형에 str 데이터를 추가하는 등의 작업을 할 때

# 데이터에 함수 적용(apply)
def add_cm(height): # 키 뒤에 cm를 추가하는 함수
    return str(height) + " cm"
csv_["Height"] = csv_["Height"].apply(add_cm) #; 선택된 Column에 해당 함수를 적용
#    No. Name  Height School  Korean  English  Math  Science  Social          SW
# 0    0  채치수  197 cm    북산고      90       85   200       95      85      Python
# 1    1  정대만  184 cm    북산고      40       35    50       55      25        Java
# 2    2  송태섭  168 cm    북산고      80       75    70       80      75  Javascript
# 3    3  서태웅  187 cm    북산고     100      100   100      100     100        What
# 4    4  강백호  188 cm    북산고      15       20    10       35      10         NaN
# 5    5  변덕규  202 cm    능남고      80      100    95       85      80           C
# 6    6  황태산  188 cm    능남고      55       65    45       40      35      PYTHON
# 7    7  윤대협  190 cm    능남고     100       85   200       95      95          C#
# 8    8  박진영  180 cm    능남고     100      100   100      100     100      python

def capitalize(lang):
    if pandas.notnull(lang): # 데이터 값이 null인지 확인하는 구문
        return lang.capitalize()
    return lang
csv_["SW"] = csv_["SW"].apply(capitalize) # csv_["SW"].str.capitalize()
#    No. Name  Height School  Korean  English  Math  Science  Social          SW
# 0    0  채치수  197 cm    북산고      90       85   200       95      85      Python
# 1    1  정대만  184 cm    북산고      40       35    50       55      25        Java
# 2    2  송태섭  168 cm    북산고      80       75    70       80      75  Javascript
# 3    3  서태웅  187 cm    북산고     100      100   100      100     100        What
# 4    4  강백호  188 cm    북산고      15       20    10       35      10         NaN
# 5    5  변덕규  202 cm    능남고      80      100    95       85      80           C
# 6    6  황태산  188 cm    능남고      55       65    45       40      35      Python
# 7    7  윤대협  190 cm    능남고     100       85   200       95      95          C#
# 8    8  박진영  180 cm    능남고     100      100   100      100     100      Python


# 14. 그룹화; 동일한 값을 가진 데이터끼리 통계값을 산출하기 위해 사용

# .groupby(Key); Key 값을 통해 묶음
csv_.groupby("School")
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000002468B90FAC0>

# .groupby(Key).get_gruop(Value); 묶인 데이터 중 Value 값을 가진 데이터를 가져옴
csv_.groupby("School").get_group("북산고")
#    No. Name  Height School  Korean  English  Math  Science  Social          SW
# 0    0  채치수  197 cm    북산고      90       85   200       95      85      Python
# 1    1  정대만  184 cm    북산고      40       35    50       55      25        Java
# 2    2  송태섭  168 cm    북산고      80       75    70       80      75  Javascript
# 3    3  서태웅  187 cm    북산고     100      100   100      100     100        What
# 4    4  강백호  188 cm    북산고      15       20    10       35      10         NaN

# .groupby(Key).mean(); 묶음마다 데이터의 평균을 가져옴
csv_.groupby("School").mean()
#         No.  Korean  English   Math  Science  Social
# School
# 능남고     6.5   83.75     87.5  110.0     80.0    77.5
# 북산고     2.0   65.00     63.0   86.0     73.0    59.0

# .groupby(Key).size(); 묶음마다 데이터의 사이즈를 가져옴
csv_.groupby("School").size()
# School
# 능남고    4
# 북산고    5
# dtype: int64

# .groupby(Key).size()[Value]; 묶인 데이터 중 Value 값을 가진 데이터의 사이즈를 가져옴
csv_.groupby("School").size()["북산고"]
# 5

# .groupby(Key1)[Key2].mean(); 묶인 데이터 중 Key2의 평균을 가져옴
csv_.groupby("School")["Korean"].mean()
# School
# 능남고    83.75
# 북산고    65.00
# Name: Korean, dtype: float64

# .groupby(Key1)[[Key2,Key3,Key4]].mean(); 묶인 데이터 중 Key2, Key3, Key4의 평균을 가져옴
csv_.groupby("School")[["Korean","English","Math"]].mean()
#         Korean  English   Math
# School
# 능남고      83.75     87.5  110.0
# 북산고      65.00     63.0   86.0

# .groupby([Key1, Key2]); Key1로 묶음을 나눈 뒤, Key2로 다시 묶음
csv_.groupby(["School","SW"])
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000002A6EAC1BEE0>

# .groupby(Key1)[[Key2,Key3,Key4]].count(); 묶인 데이터 중 Key2, Key3, Key4의 데이터 개수를 가져옴. (NaN은 미포함)
csv_.groupby("School")[["Korean","English","Math"]].count()
#         Korean  English  Math
# School
# 능남고          4        4     4
# 북산고          5        5     5

GroupData = csv_.groupby("School")
GroupData["SW"].value_counts()
# School  SW
# 능남고     Python        2
#         C             1
#         C#            1
# 북산고     Java          1
#         Javascript    1
#         Python        1
#         What          1
# Name: SW, dtype: int64

# GroupData[Key2].value_counts(); Key2의 데이터 개수를 Key1으로 그룹화하여 보여줌
GroupData["SW"].value_counts().loc["능남고"]
# SW
# Python    2
# C         1
# C#        1
# Name: SW, dtype: int64

# GroupData[Key2].value_counts(normalize=True).loc[value]; 위 데이터를 %로 전환하여 보여줌
GroupData["SW"].value_counts(normalize=True).loc["능남고"]
# SW
# Python    0.50
# C         0.25
# C#        0.25
# Name: SW, dtype: float64


# 15. Pandas Quiz
data = {
    '영화' : ['명량', '극한직업', '신과함께-죄와 벌', '국제시장', '괴물', '도둑들', '7번방의 선물', '암살'],
    '개봉 연도' : [2014, 2019, 2017, 2014, 2006, 2012, 2013, 2015],
    '관객 수' : [1761, 1626, 1441, 1426, 1301, 1298, 1281, 1270], # (단위 : 만 명)
    '평점' : [8.88, 9.20, 8.73, 9.16, 8.62, 7.64, 8.83, 9.10]
}
df = pandas.DataFrame(data)
#           영화  개봉 연도  관객 수    평점
# 0         명량   2014  1761  8.88
# 1       극한직업   2019  1626  9.20
# 2  신과함께-죄와 벌   2017  1441  8.73
# 3       국제시장   2014  1426  9.16
# 4         괴물   2006  1301  8.62
# 5        도둑들   2012  1298  7.64
# 6    7번방의 선물   2013  1281  8.83
# 7         암살   2015  1270  9.10

# 15-1. 전체 데이터 중에서 "영화" 정보만 출력하시오.
df["영화"]
# 0           명량
# 1         극한직업
# 2    신과함께-죄와 벌
# 3         국제시장
# 4           괴물
# 5          도둑들
# 6      7번방의 선물
# 7           암살
# Name: 영화, dtype: object

# 15-2. 전체 데이터 중에서 "영화", "평점" 정보를 출력하시오.
df[["영화","평점"]]
#           영화    평점
# 0         명량  8.88
# 1       극한직업  9.20
# 2  신과함께-죄와 벌  8.73
# 3       국제시장  9.16
# 4         괴물  8.62
# 5        도둑들  7.64
# 6    7번방의 선물  8.83
# 7         암살  9.10

# 15-3. 2015년 이후에 개봉한 영화 데이터 중에서 "영화", "개봉 연도" 정보를 출력하시오.
df[df["개봉 연도"]>=2015][["영화","개봉 연도"]]
#           영화  개봉 연도
# 1       극한직업   2019
# 2  신과함께-죄와 벌   2017
# 7         암살   2015

# 15-4. 주어진 계산식을 참고하여 "추천 점수" Column을 추가하시오.
df["추천 점수"] = round(df["관객 수"] * df["평점"] / 100,0)
#           영화  개봉 연도  관객 수    평점  추천 점수
# 0         명량   2014  1761  8.88  156.0
# 1       극한직업   2019  1626  9.20  150.0
# 2  신과함께-죄와 벌   2017  1441  8.73  126.0
# 3       국제시장   2014  1426  9.16  131.0
# 4         괴물   2006  1301  8.62  112.0
# 5        도둑들   2012  1298  7.64   99.0
# 6    7번방의 선물   2013  1281  8.83  113.0
# 7         암살   2015  1270  9.10  116.0

# 15-5. 전체 데이터를 "개봉 연도" 기준 내림차순으로 출력하시오.
df.sort_values("개봉 연도",ascending=False)
#           영화  개봉 연도  관객 수    평점  추천 점수
# 1       극한직업   2019  1626  9.20  150.0
# 2  신과함께-죄와 벌   2017  1441  8.73  126.0
# 7         암살   2015  1270  9.10  116.0
# 0         명량   2014  1761  8.88  156.0
# 3       국제시장   2014  1426  9.16  131.0
# 6    7번방의 선물   2013  1281  8.83  113.0
# 5        도둑들   2012  1298  7.64   99.0
# 4         괴물   2006  1301  8.62  112.0
#