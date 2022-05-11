import pandas
import csv


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
dataframe1 = pandas.DataFrame(data)
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
# print(dataframe["이름"])
# print(dataframe[["이름", "키"]])

# Data Frame 객체 생성 + index 지정
dataframe2 = pandas.DataFrame(data, index=["1번","2번","3번","4번","5번","6번","7번","8번"])
#  이름   학교    키   국어   영어   수학  과학  사회        SW특기
# 1번  채치수  북산고  197   90   85  100  95  85      Python
# 2번  정대만  북산고  184   40   35   50  55  25        Java
# 3번  송태섭  북산고  168   80   75   70  80  75  Javascript
# 4번  서태웅  북산고  187   40   60   70  75  80
# 5번  강백호  북산고  188   15   20   10  35  10
# 6번  변덕규  능남고  202   80  100   95  85  80           C
# 7번  황태산  능남고  188   55   65   45  40  35      PYTHON
# 8번  윤대협  능남고  190  100   85   90  95  95          C#

# Data Frame 객체 생성 + column 지정
dataframe3 = pandas.DataFrame(data, columns=["이름","학교"])
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
df = dataframe2
df.index.name = "지원번호"
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
# dataframe2 = dataframe2.reset_index(drop=True)
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
df = dataframe2
# print(df.set_index("이름",inplace=True))
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
df = dataframe2
df.set_index("이름",inplace=True)
# print(df.sort_index()) #기본 오름차순
# print(df.sort_index(ascending=False)) #내림차순


# 04. File 저장 및 열기 (Dataframe 객체를 excel, csv, txt 등의 형식으로 저장 및 열기 진행)
df = pandas.DataFrame(data)

# csv 파일 저장 및 열기
df.to_csv("D:\Python\pj\Data_Visulaization\CSV1.csv",encoding="utf-16")
csv_ = pandas.read_csv("D:\Python\pj\Data_Visulaization\CSV1.csv",encoding="utf-16",skiprows=4) # skiprows = 1; 첫 행부터 1개 행을 건너뛴 상태로 읽음
csv_ = pandas.read_csv("D:\Python\pj\Data_Visulaization\CSV1.csv",encoding="utf-16",skiprows=[1,5,7]) # skiprows = [1,3,5]; 해당 행을 지우고 읽음
csv_ = pandas.read_csv("D:\Python\pj\Data_Visulaization\CSV1.csv",encoding="utf-16",nrows=3) # nrows = 4; skiprows 이후 첫 행부터 4개 행을 읽음

# excel 파일 저장 및 열기
df.to_excel("D:\Python\pj\Data_Visulaization\excel.xlsx")
xl_ = pandas.read_excel("D:\Python\pj\Data_Visulaization\excel.xlsx")

# txt 파일 저장 및 열기
df.to_csv("D:\Python\pj\Data_Visulaization\CSV1.txt",encoding="utf-16")
text_ = pandas.read_csv("D:\Python\pj\Data_Visulaization\CSV1.txt",encoding="utf-16",index_col=0) # index_col = HEADER; Header에 홰당하는 컬럼을 index로 사용
text_.set_index("이름",inplace=True) # .set_index(HEADER, inplace=True); Header 지정


# 05. 데이터 확인
csv_ = pandas.read_csv("D:\Python\pj\Data_Visulaization\CSV1.csv",encoding="utf-16")

# DataFrame 확인
# .describe(); 계산 가능한 데이터에 대해서 column 별 개수, 평균, 표준편차, 최소/최대값 등의 정보 출력
# .info(); 각 column 별 데이터 개수 및 형태 출력
# .head(); 첫 5개 rows의 data를 가져옴, head(8)
# .tail(); 마지막 5개 rows의 data를 가져옴
# .columes; 컬럼 확인
# .values; 값 확인
# .shapes; (row, column) 으로 표시

# Series 확인
# .min(); 최소값
# .max(); 최대값
# .nlargest(n); 최대값부터 n개의 값을 가져옴
# .mean(); 평균
# .sum(); 합산
# .count(); 유효 데이터 개수
# .unique(); 중복값 제거 후 list 출력
# .nunique(); unique 원소의 개수 출력


# 06. 데이터 선택(기본)

# Column 선택(label)
# DataFrame[key]; 선택된 key 값의 Column 호출
# DataFrame[[Key1, Key2, Key3]]; 선택된 key 값들의 Column을 호출

# Column 선택(정수 index)
# .columns[n]; n-1번 째 column의 이름을 호출 (음수로 역순서 호출 가능)
# DataFrame[DataFrame.columns[n]]; n-1번 째 Column의 값을 호출

# slicing
# DataFrame[Key][x:y]; 선택된 Key 값의 Column에서 x~y-1번 째 값을 호출
# DataFrame[x:y]; 전체 테이블에서 x~y-1번 째 값을 호출


# 07. 데이터 선택(loc); 이름을 이용하여 원하는 row, column을 선택

# .loc[Rowkey]; 선택된 Key 값의 Row 호출
# .loc[Rowkey, Columnkey]; 선택된 Row, Column key로 값 호출
# .loc[[Rowkey1, Rowkey2],[Columnkey1, Columnkey2]; 각각 호출
# .loc[Rowkey1:Rowkey2,Columnkey1:Columnkey2]; 범위 호출 *Rowkey2, Columnkey2를 포함한 결과가 호출됨


# 08. 데이터 선택(iloc); 위치를 이용하여 원하는 row, column을 선택, integerlocation

# .iloc[n]; n-1번 째 Row 호출
# .iloc[x:y]; x~y-1번 째 Row 호출
# .iloc[x,y]; x번 째 Row, y번 째 Column 호출
# .iloc[[x,y],[z,w]]; x,y번 째 Row에서 z,w번 째 Column 호출
# .iloc[x:y,z:w]; x~y-1번 째 Row에서 z~w-1번 째 Column 호출


# 09. 데이터 선택(조건); 조건에 해당하는 데이터 선택

# FILTER = (DataFrame[Key] >= Value); DataFrame[FILTER]; 선택된 Column에서 Value와의 크기 비교
# DataFrame[DataFrame[Key] >= Value]; 조건에 해당하는 Row만 호출

# FILTER = DataFrame[Key].str.startwith("str"); DataFrame[FILTER]; 선택된 Column의 값이 "str"로 시작하는 모든 row
# FILTER = DataFrame[Key].str.contains("str", na=False); DataFrame[FILTER]; 선택된 Column의 값이 "str"을 포함하는 모든 row / na=True; NaN을 False로 인식
# DataFrame[-FILTER]; FILTER 조건을 제외한 row
# FILTER = DataFrame[Key].isin(list); DataFrame[FILTER]; 선택된 Column의 값이 list의 값과 일치하는 모든 row
# FILTER = DataFrame[Key].str.lower().isin(list); DataFrame[FILTER]; 선택된 Column의 모든 값을 소문자로 변환한 뒤 list의 값과 일치하는지 비교


# 10. 결측치; 비어있는 데이터

# 데이터 채우기(filna)
# .fillna("str"); NaN Data를 "str"로 채움

# 데이터 제외하기(drop)
# .dropna(); NaN이 포함된 Row를 삭제
# .dropna(axis="index" or "columns", how="any" or "all"); axis = "index"는 row 삭제, "columns"은 column 삭제 // how = "any"는 하나라도 NaN이면 삭제, "all"은 전체가 NaN이면 삭제


# 11. 데이터 정렬

# .sort_values(Key, ascending=True or False); 해당하는 Column을 정렬
# .sort_values([Key1, Key2], ascending=False); 해당하는 Columns를 내림 차순으로 정렬하되, 앞쪽부터 우선 순위가 높음
# .sort_values([Key1, Key2], ascending=[True,False]); 해당하는 Columns를 해당하는 차순으로 정렬 // Key1은 오름차순, Key2는 내림차순 정렬됨


# 12. 데이터 수정

# Column 수정
# DataFrame[Key].replace({"Value1":"Value2","Value3":"Value4"}); 선택된 Column에서 Value1을 Value2로, Value3을 Value4로 바꿈
# DataFrame[Key] = DataFrame[Key].str.lower(); 선택된 Column을 소문자로 치환
# DataFrame[Key] = DataFrame[Key] + Value; 선택된 Column 전체에 Value를 더한 값을 입력

# Column 추가
# DataFrame[NewKey] = ~~~; 해당 식으로 계산하여 NewKey Column을 우측에 추가함
# .loc[DataFrame[Key1] > Value1, Key2] = Value2; Key1 Column의 값이 Value1보다 큰 Row를 가져온 후 Key2 Column에 Value2를 넣음

# Row 추가
# .loc[NewIndex] = ~~~; 해당 Index로 시작하는 Row를 하단에 추가함

# Column 삭제
# .drop(columns=[Keylist]); Keylist에 해당하는 Column을 삭제

# Row 삭제
# .drop(index=[Keylist]); Keylist에 해당하는 Row를 삭제
# .drop(index=DataFrame[FILTER].index); FILTER에 해당하는 index를 확인하여 해당 row를 삭제

# Cell 수정
# .loc[Index, Key] = Value; index row의 Key Column에 해당하는 값을 Value로 업데이트
# .loc[Index, [Key1, Key2]] = [Value1, Value2]; index row의 Key1 Column 값은 Value1로, Key2 Column 값은 Value2로 업데이트

# Column 위치 변경
# Columns = list(DataFrame.columns); DataFrame의 Key 값들을 List 형태로 저장
# DataFrame = DataFrame[[Columns[1]]+[Columns[-1]]+Columns[2:4]+.....]; Key값들을 재배열하여 List형태로 만든 뒤 다시 index로 지정

# Column 이름 변경
# .columns = [Keys]; 새로운 Key list로 Column의 이름을 바꿈


# 13. 함수 적용; int 형에 str 데이터를 추가하는 등의 작업을 할 때

# 데이터에 함수 적용(apply)
# def add_cm(height): # 키 뒤에 cm를 추가하는 함수
#     return str(height) + "cm"
# DataFrame[Key] = DataFrame[Key].apply(add_cm); 선택된 Column에 해당 함수를 적용

# def capitalize(lang):
#     if pandas.notnull(lang): # 데이터 값이 null인지 확인하는 구문
#         return lang.capitalize()
#     return lang
# DataFrame[Key] = DataFrame[Key].apply(capitalize)
# DataFrame[Key].str.capitalize()


# 14. 그룹화; 동일한 값을 가진 데이터끼리 통계값을 산출하기 위해 사용

# .groupby(Key); Key 값을 통해 묶음
# .groupby(Key).get_gruop(Value); 묶인 데이터 중 Value 값을 가진 데이터를 가져옴
# .groupby(Key).mean(); 묶음마다 데이터의 평균을 가져옴
# .groupby(Key).size(); 묶음마다 데이터의 사이즈를 가져옴
# .groupby(Key).size()[Value]; 묶인 데이터 중 Value 값을 가진 데이터의 사이즈를 가져옴
# .groupby(Key1)[Key2].mean(); 묶인 데이터 중 Key2의 평균을 가져옴
# .groupby(Key1)[[Key2,Key3,Key4]].mean(); 묶인 데이터 중 Key2, Key3, Key4의 평균을 가져옴
# .groupby([Key1, Key2]); Key1로 묶음을 나눈 뒤, Key2로 다시 묶음
# .groupby(Key1)[[Key2,Key3,Key4]].count(); 묶인 데이터 중 Key2, Key3, Key4의 데이터 개수를 가져옴. (NaN은 미포함)

# GroupData = DataFrame.groupby(Key1)
# GroupData[Key2].value_counts(); Key2의 데이터 개수를 Key1으로 그룹화하여 보여줌
# GroupData[Key2].value_counts().loc[value]; Key1 중 value 값을 가지는 그룹에서 Key2의 데이터 개수를 보여줌
# GroupData[Key2].value_counts(normalize=True).loc[value]; 위 데이터를 %로 전환하여 보여줌

school = csv_.groupby("학교")
print(school["SW특기"].value_counts(normalize=True).loc["북산고"])






