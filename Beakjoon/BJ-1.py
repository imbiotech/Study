#2557번 Hello World!를 출력하시오.
import time

print("Hello World!")

array = ['H','e','l','l','o',' ','W','o','r','l','d','!']
for i in array:
    print(i,end='') #배열로 지정하여 원소를 출력, 끝에 줄바꿈 삭제를 위해서 end='' 삽입


# 10718번 두 줄에 걸쳐 "강한친구 대한육군"을 한 줄에 한 번씩 출력한다.

print("강한친구 대한육군\n강한친구 대한육군")
print("강한친구 대한육군\n"*2) #\n 줄바꿈, 전체 str에 *2 하면 두 번 출력
for i in range(2):
    print("강한친구 대한육군") #동일 구문을 for문으로 두 번 출력


# 10171번 고양이를 출력한다.
# \    /\
#  )  ( ')
# (  /  )
#  \(__)|

# \가 들어가 있으므로 \\으로 이중 처리
print("""\    /\\ 
 )  ( ')
(  /  )
 \(__)|""")
print("""\    /\\\n )  ( ')\n(  /  )\n \(__)|""")


# 10172번 개를 출력한다.
# |\_/|
# |q p|   /}
# ( 0 )"""\
# |"^"`    |
# ||_/=\\__|

#"""이 들어가 있으므로 구문 출력 시 ''' 으로 묶기, \가 들어가 있으므로 \\으로 이중 처리
print('''|\_/|
|q p|   /}
( 0 )"""\\
|"^"`    |
||_/=\\\\__|''')
print('''|\_/|\n|q p|   /}\n( 0 )"""\\\n|"^"`    |\n||_/=\\\\__|''')


# 1000번 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10), 첫째 줄에 A+B를 출력한다.

a = input().split() #입력한 데이터를 split하여 list 형으로 저장
b = 0 #b 초기화
for i in a: #a의 원소에 대해서 합산 진행
    b=b+int(i) #i는 str형으로 저장되므로 int형으로 전환하여 합산 진행
print(b)

a, b = map(int,input().split()) #int형으로 데이터를 split하여 저장
print(a+b)


# 1001번 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10), 첫째 줄에 A-B를 출력한다.

a = input().split() #입력한 데이터를 split하여 list 형으로 저장
b = int(a[0])-int(a[1]) #0번 원소와 1번 원소를 각각 int 형으로 불러와서 계산
print(b)

a, b = map(int,input().split()) #int형으로 데이터를 split하여 저장
print(a-b)


# 10998번 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10), 첫째 줄에 A×B를 출력한다.

a = input().split() #입력한 데이터를 split하여 list 형으로 저장
print(int(a[0])*int(a[1])) #0번 원소와 1번 원소를 각각 int 형으로 불러와서 계산

a, b = map(int,input().split()) #int형으로 데이터를 split하여 저장
print(a*b)


# 1008번 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10), 첫째 줄에 A/B를 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 10-9 이하이면 정답이다.

a = input().split()
print(int(a[0])/int(a[1]))

a,b=map(int,input().split())
print(a/b)


# 10869번 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000), 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

a = input().split()
b, c = int(a[0]), int(a[1])
print(f"""{b+c}\n{b-c}\n{b*c}\n{b//c}\n{b%c}""") #print(f"""""")로 한 번에 출력


# 10926번 첫째 줄에 준하가 가입하려고 하는 사이트에 이미 존재하는 아이디가 주어진다. 아이디는 알파벳 소문자로만 이루어져 있으며, 길이는 50자를 넘지 않는다.,첫째 줄에 준하의 놀람을 출력한다. 놀람은 아이디 뒤에 ??!를 붙여서 나타낸다.

print(input()+"??!") #print 문에 바로 input을 넣어서 출력


# 18108번
# 서기 연도를 알아보고 싶은 불기 연도 y가 주어진다. (1000 ≤ y ≤ 3000), 불기 연도를 서기 연도로 변환한 결과를 출력한다.

print(int(input())-543)


# 10430번
# 첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000), 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.

a=input().split() #list 형 저장
A,B,C=int(a[0]),int(a[1]),int(a[2])
print(f"""{(A+B)%C}\n{(A%C+B%C)%C}\n{(A*B)%C}\n{((A%C)*(B%C))%C}""")

a,b,c=input().split() #각각에 저장
A,B,C=int(a),int(b),int(c)
print(f"""{(A+B)%C}\n{(A%C+B%C)%C}\n{(A*B)%C}\n{((A%C)*(B%C))%C}""")


# 2588번
# (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.

a=int(input())
b=int(input())
c,d,e=a*(b%10),a*(b//10%10),a*(b//100%10)
print(f"""{c}\n{d}\n{e}\n{a*b}""")

a=int(input())
b=int(input())
for i in range(3): #똑같은 형식이므로 for 문 사용해서 수식화
    print(a*(b//10**i%10))
print(a*b)


# 1330번
# 첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.
# 첫째 줄에 다음 세 가지 중 하나를 출력한다.
# A가 B보다 큰 경우에는 '>'를 출력한다.
# # A가 B보다 작은 경우에는 '<'를 출력한다.
# # A와 B가 같은 경우에는 '=='를 출력한다.
#
a,b=input().split()
a,b=int(a),int(b)
if a>b:
    print(">")
elif a<b:
    print("<")
else:
    print("==")

sqrt=lambda x:x**0.5
print(sqrt(25))


# 9498번
# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

a=int(input())
if a>= 90:
    print("A")
elif a>=80:
    print("B")
elif a>=70:
    print("C")
elif a>=60:
    print("D")
else:
    print("F")

print('FFFFFFDCBAA'[int(input())//10]) #문자열 형태로 저장하고 점수에 따라서 숫자를 나눠서 출력


# 2753번 첫째 줄에 연도가 주어진다. 연도는 1보다 크거나 같고, 4000보다 작거나 같은 자연수이다. 첫째 줄에 윤년이면 1, 아니면 0을 출력한다.
# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.

a=int(input())
if a%400==0 or (a%4==0 and a%100!=0):
    print(1)
else:
    print(0)

a=int(input())
print((a%100or a//100)%4<1)

# True or False
print(1 or True) #==1
print(True or 1) #==True
print(1 and True) #==True
print(True and 1) #==1
print(1 or False) #==1
print(False or 1) #==1
print(1 and False) #==False
print(False and 1) #==False


# 14681번
# 첫 줄에는 정수 x가 주어진다. (−1000 ≤ x ≤ 1000; x ≠ 0) 다음 줄에는 정수 y가 주어진다. (−1000 ≤ y ≤ 1000; y ≠ 0)
# 점 (x, y)의 사분면 번호(1, 2, 3, 4 중 하나)를 출력한다.

x=int(input())
y=int(input())
if x*y>0:
    if x>0:
        print(1)
    else:
        print(3)
else:
    if x<0:
        print(2)
    else:
        print(4)


# 2884번
# 첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 그리고 이것은 현재 상근이가 설정한 놓은 알람 시간 H시 M분을 의미한다.
# 입력 시간은 24시간 표현을 사용한다. 24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다. 시간을 나타낼 때, 불필요한 0은 사용하지 않는다.
# 첫째 줄에 상근이가 창영이의 방법을 사용할 때, 설정해야 하는 알람 시간을 출력한다. (입력과 같은 형태로 출력하면 된다.)
# eg.1 10 10 -> 9 25
# eg.2 0 30 -> 23 45

a,b=input().split()
a,b=int(a),int(b)
if b>=45:
    print(a,b-45)
else:
    print((a-1)%24,b+15)

a,b=map(int,input().split())
print((a-(b<45))%24,(b-45)%60) #-1 % 10 == 9


# 2525번
# 첫째 줄에는 현재 시각이 나온다. 현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다. 두 번째 줄에는 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위로 주어진다.
# 첫째 줄에 종료되는 시각의 시와 분을 공백을 사이에 두고 출력한다. (단, 시는 0부터 23까지의 정수, 분은 0부터 59까지의 정수이다. 디지털 시계는 23시 59분에서 1분이 지나면 0시 0분이 된다.)

a,b = input().split()
a,b = int(a), int(b)
c = int(input())
if c+b<60:
    print(a,b+c)
else:
    print((a+(b+c)//60)%24,(b+c)%60)


# 2480번
# 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.
# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
# 예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3×100으로 계산되어 1,300원을 받게 된다. 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2×1,000 으로 계산되어 12,000원을 받게 된다.
# 3개의 눈이 6, 2, 5로 주어지면 그중 가장 큰 값이 6이므로 6×100으로 계산되어 600원을 상금으로 받게 된다.
# 3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.

a,b,c=input().split()
if a==b and b==c:
    print(10000+int(a)*1000)
elif a!=b and b!=c and c!=a:
    print(100*int(max(a,b,c)))
else:
    if a==b or b==c:
        print(1000+int(b)*100)
    else:
        print(1000+int(a)*100)

a,b,c=sorted(input().split()) # 3개 숫자를 순서대로 집어넣음, b를 카운트 하면 같은 숫자 개수를 모두 파악할 수 있음(총 3개여서 가능)
print([c,10+b,10+b+100][[a,b,c].count(b)-1]*100) #b가 1개면 c가 제일 큼, 나머지는 b의 개수에 따라 분류


# 2739번
# 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.
# 출력형식과 같게 N*1부터 N*9까지 출력한다.

a=int(input())
for i in range(9):
    print(f"""{a} * {i+1} = {a*(i+1)}""")
    # print("{} * {} = {}".format(a,i+1,a*(i+1)))


# 10950번
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 각 테스트 케이스마다 A+B를 출력한다.

for i in range(int(input())):
    a,b=map(int,input().split()) # map(자료형,input().split())은 편리함
    print(a+b)


# 8393번
# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다. 1부터 n까지 합을 출력한다.

a=0
for i in range(int(input())+1):
    a+=i
print(a)


# 15552번
# Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다.
# 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.
# 첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다.
# 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.
# 각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.

import sys

for i in range(int(sys.stdin.readline())):
    a,b=map(int,sys.stdin.readline().split())
    print(a+b)
    # print(sum(map(int,sys.stdin.readline().split())))


# 2741번
# 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
# 첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다. 첫째 줄부터 N번째 줄 까지 차례대로 출력한다.

for i in range(int(input())):
    print(i+1)


# 2742번
# 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
# 첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다. 첫째 줄부터 N번째 줄 까지 차례대로 출력한다.

a=int(input())
for i in range(a):
    print(a-i)

while a>0:
    print(a)
    a-=1


# 11021번
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.

case=int(input())
case_list=[]
for i in range(case):
    case_list.append(map(int,input().split()))
for i in range(case):
    print(f"""Case #{i+1}: {sum(case_list[i])}""")

for i in range(int(input())):
    print(f"""Case #{i+1}: {sum(map(int,input().split()))}""")


# 11022번
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다.
# x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.

for i in range(int(input())):
    a,b=map(int,input().split())
    print(f"""Case #{i+1}: {a} + {b} = {a+b}""")


# 2438번
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

for i in range(int(input())):
    print('*'*(i+1))


# 2439번
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# 하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

case=int(input())
for i in range(case):
    print(' '*(case-i-1)+'*'*(i+1)) #,로 구분하면 앞쪽에 공백란이 하나 생김


# 10871번
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다.
# 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
# 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
# 둘째 줄에 수열 A를 이루는 정수 N개가 주어진다.
# 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.
# X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.

l,x=map(int,input().split())
A,B=map(int,input().split()),[]
for i in A:
    if i<x:
        B.append(i)
for i in B:
    print(i,end=' ')


# 10952번
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 입력의 마지막에는 0 두 개가 들어온다.
# 각 테스트 케이스마다 A+B를 출력한다.

while True:
    a,b=map(int,input().split())
    if a==b==0:
        break
    print(a+b)


#10951번
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 각 테스트 케이스마다 A+B를 출력한다.

while True:
    try:
        a,b=map(int,input().split())
        print(a+b)
    except:
        break


# 1110번
# 0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다.
# 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다.
# 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.
# 다음 예를 보자.
# 26부터 시작한다. 2+6 = 8이다.
# 새로운 수는 68이다. 6+8 = 14이다.
# 새로운 수는 84이다. 8+4 = 12이다.
# 새로운 수는 42이다. 4+2 = 6이다.
# 새로운 수는 26이다.
# 위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.
# N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

a=int(input())
b,i=a,0
while True:
    i+=1
    c=b%10*10+(b//10+b%10)%10
    if a==c:
        break
    b=c
print(i)


# 10818
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다.
# 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.
# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

N=int(input())

n=map(int,input().split())
m=list(n)
print(min(m),max(m))

n=list(map(int,input().split()))
print(min(n),max(m))

m=[]
for i in n:
    m.append(int(i))
print(min(m),max(m))


# 2562번
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
# 예를 들어, 서로 다른 9개의 자연수 3, 29, 38, 12, 57, 74, 40, 85, 61
# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.
# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

a=[]
for i in range(9):
    a.append(int(input()))
print(max(a))
print(a.index(max(a))+1)


# 2577번
# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에
# 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
# 예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300
# 이 되고, 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.
# 첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다.
# A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수이다.
# 첫째 줄에는 A × B × C의 결과에 0 이 몇 번 쓰였는지 출력한다.
# 마찬가지로 둘째 줄부터 열 번째 줄까지 A × B × C의 결과에
# 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.

A=1
for i in range(3):
    A*=int(input())
a=[]
while A>=1:
    a.append(A%10)
    A=int(A/10)
for i in range(10):
    print(a.count(i))

A=str(A)
for i in range(10):
    print(A.count(str(i)))


# 3052번
# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다.
# 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다.
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다.
# 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.
# 첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다.
# 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.
# 첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.

a=[]
for i in range(10):
    a.append(int(input())%42)
# a=[int(input())%42 for i in range(10)]

print(len(set(a)))


# 1546번
# 세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로 했다.
# 일단 세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다.
# 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
# 예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.
# 세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.
# 첫째 줄에 시험 본 과목의 개수 N이 주어진다. 이 값은 1000보다 작거나 같다.
# 둘째 줄에 세준이의 현재 성적이 주어진다.
# 이 값은 100보다 작거나 같은 음이 아닌 정수이고, 적어도 하나의 값은 0보다 크다.
# 첫째 줄에 새로운 평균을 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 10-2 이하이면 정답이다.

n=int(input())
s=list(map(int,input().split()))
print(sum(s)/len(s)/max(s)*100)


# 8958번
# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다.
# O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다.
# 예를 들어, 10번 문제의 점수는 3이 된다.
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 테스트 케이스의 개수가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다.
# 문자열은 O와 X만으로 이루어져 있다.
# 각 테스트 케이스마다 점수를 출력한다.

for i in range(int(input())):
    s,c=0,0
    r=input()
    for i in r:
        if i=='X':
            c=0
        else:
            s+=1+c
            c+=1
    print(s)


# 4344번
# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다.
# 당신은 그들에게 슬픈 진실을 알려줘야 한다.
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
# 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

for i in range(int(input())):
    s=list(map(int,input().split()))
    c=s.pop(0)
    aver=sum(s)/c
    n=0
    for i in s:
        if i>aver:
            n+=1
    print(f"{n/c*100:.3f}%") #:.3f -> 셋째 자리까지 나타내시오.


# 15596번
# 정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.
# 작성해야 하는 함수는 다음과 같다.
# def solve(a: list) -> int
# a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
# 리턴값: a에 포함되어 있는 정수 n개의 합 (정수)

def solve(a: list):
    return sum(a)


# 4673번
# 셀프 넘버는 1949년 인도 수학자 D.R. Kaprekar가 이름 붙였다.
# 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자.
# 예를 들어, d(75) = 75+7+5 = 87이다.
# 양의 정수 n이 주어졌을 때, 이 수를 시작해서 n, d(n), d(d(n)), d(d(d(n))),
# ...과 같은 무한 수열을 만들 수 있다.
# 예를 들어, 33으로 시작한다면 다음 수는 33 + 3 + 3 = 39이고,
# 그 다음 수는 39 + 3 + 9 = 51, 다음 수는 51 + 5 + 1 = 57이다.
# 이런식으로 다음과 같은 수열을 만들 수 있다.
# 33, 39, 51, 57, 69, 84, 96, 111, 114, 120, 123, 129, 141, ...
# n을 d(n)의 생성자라고 한다. 위의 수열에서 33은 39의 생성자이고,
# 39는 51의 생성자, 51은 57의 생성자이다. 생성자가 한 개보다 많은 경우도 있다.
# 예를 들어, 101은 생성자가 2개(91과 100) 있다.
# 생성자가 없는 숫자를 셀프 넘버라고 한다.
# 100보다 작은 셀프 넘버는 총 13개가 있다. 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97
# 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
# 10,000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력한다.

def sn(a):
    rt=[]
    for i in str(a):
        rt.append(int(i))
    rt.append(a)
    return sum(rt)
n=1
SNL=[i for i in range(1,10001)]
while n<10001:
    if sn(n) in SNL:
        SNL.remove(sn(n))
    n+=1
# NSN=[sn(i) for i in range(1,10001)]
# SN=[i for i in range(1,10001) if i not in NSN]
for i in SNL:
    print(i)


# Class & Instance
def plus(*arg): # *arg = 비지정변수, **kwarg = 지정변수
    result=0
    for number in arg:
        result+=number
    return result


# 1316 번
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다.
# 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.
# 첫째 줄에 그룹 단어의 개수를 출력한다.

count=0
for i in range(int(input())):
    bools = True
    a=input()
    for i in a:
        if i*a.count(i) not in a:
            bools*=False
    if bools == True:
        count+=1
print(count)


# 2941 번
# 예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.
# č:c=, ć:c-, dž:dz=, đ:d-, li:li, ni:ni, š:s=, ž:z=
# 예를 들어, lies=niak은 크로아티아 알파벳 6개(li, e, š, ni, a, k)로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
# dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. li와 ni도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.
# 첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.
# 단어는 크로아티아 알파벳으로 이루어져 있다. 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.
# 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

c_alphbet = {"c=":"č", "c-":"ć", "dz=":"ž", "d-":"đ", "li":"L", "ni":"N", "s=":"š", "z=":"ž"}
a=input()
for i in c_alphbet:
    if i in a:
        a=a.replace(i, c_alphbet[i])
print(len(a))


# 10872 번
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.
# 출력
# 첫째 줄에 N!을 출력한다.

def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(int(input())))


# 10870 번
# 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
# 이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.
# n=17일때 까지 피보나치 수를 써보면 다음과 같다.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다.
# 출력
# 첫째 줄에 n번째 피보나치 수를 출력한다.

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(int(input())))


# 17478 번
# 평소에 질문을 잘 받아주기로 유명한 중앙대학교의 JH 교수님은 학생들로부터 재귀함수가 무엇인지에 대하여 많은 질문을 받아왔다.
# 매번 질문을 잘 받아주셨던 JH 교수님이지만 그는 중앙대학교가 자신과 맞는가에 대한 고민을 항상 해왔다.
# 중앙대학교와 자신의 길이 맞지 않다고 생각한 JH 교수님은 결국 중앙대학교를 떠나기로 결정하였다.
# 떠나기 전까지도 제자들을 생각하셨던 JH 교수님은 재귀함수가 무엇인지 물어보는 학생들을 위한 작은 선물로 자동 응답 챗봇을 준비하기로 했다.
# JH 교수님이 만들 챗봇의 응답을 출력하는 프로그램을 만들어보자.
# 입력
# 교수님이 출력을 원하는 재귀 횟수 N(1 ≤ N ≤ 50)이 주어진다.
# 출력
# 출력 예시를 보고 재귀 횟수에 따른 챗봇의 응답을 출력한다.

def Recursion(a,n):
    print(f'{"____"*a}"재귀함수가 뭔가요?"')
    if n==a:
        print(f'{"____"*a}"재귀함수는 자기 자신을 호출하는 함수라네"')
    else:
        print(f'''{"____"*a}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
{"____"*a}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
{"____"*a}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."''')
        a += 1
        Recursion(a, n)
        print(f'{"____"*a}라고 답변하였지.')
n = int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
Recursion(0, n)
print("라고 답변하였지.")


# 25083 번
# 문제
# 아래 예제와 같이 새싹을 출력하시오.
# 입력
# 입력은 없다.
# 출력
# 새싹을 출력한다.

print(f"""         ,r'"7
r`-_   ,'  ,/
 \. ". L_r'
   `~\/
      |
      |""")


# 1193 번
# 무한히 큰 배열에 다음과 같이 분수들이 적혀있다.
# 1/1	1/2	1/3	1/4	1/5	…
# 2/1	2/2	2/3	2/4	…	…
# 3/1	3/2	3/3	…	…	…
# 4/1	4/2	…	…	…	…
# 5/1	…	…	…	…	…
# …	…	…	…	…	…
# 이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.
# 출력
# 첫째 줄에 분수를 출력한다.

# 1/1
# 1/2 2/1
# 1/3 2/2 3/1
# 4/1 3/2 2/3 1/4
# 1/5 2/4 3/3 4/2 5/1
# n 번째 집합까지 원소 개수 -> n(n+1)/2

n=1
a=int(input())
while True:
    if n*(n+1)/2>=a:
        a-=n*(n-1)/2
        break
    n+=1
if n%2==0:
    print(f"{int(a)}/{int(n+1-a)}")
else:
    print(f"{int(n+1-a)}/{int(a)}")


# 2839 번
# 문제
# 상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
# 상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.
# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)
# 출력
# 상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.

number=0
weight=int(input())
a=weight//5
b=weight//3
num=[]
for i in range(a+1):
    for i in range(b+1):
        if weight>5*i+3*i:
            continue
        elif weight==5*i+3*i:
            num.append((i+i))
if len(num) == 0:
    print(-1)
else:
    print(min(num))


# 2292 번
# 문제
# 그림과 같이 육각형으로 이루어진 벌집이 있다. 그림에서 보는 바와 같이 중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매길 수 있다. 숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 계산하는 프로그램을 작성하시오. 예를 들면, 13까지는 3개, 58까지는 5개를 지난다.
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 1,000,000,000)이 주어진다.
# 출력
# 입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력한다.

def bees(n):
    for i in range(n):
        if 3*i**2+3*i+1>=n:
            return i+1
print(bees(int(input())))


# 10250 번
# 문제
# ACM 호텔 매니저 지우는 손님이 도착하는 대로 빈 방을 배정하고 있다.
# 고객 설문조사에 따르면 손님들은 호텔 정문으로부터 걸어서 가장 짧은 거리에 있는 방을 선호한다고 한다.
# 여러분은 지우를 도와 줄 프로그램을 작성하고자 한다.
# 즉 설문조사 결과 대로 호텔 정문으로부터 걷는 거리가 가장 짧도록 방을 배정하는 프로그램을 작성하고자 한다.
# 문제를 단순화하기 위해서 호텔은 직사각형 모양이라고 가정하자.
# 각 층에 W 개의 방이 있는 H 층 건물이라고 가정하자 (1 ≤ H, W ≤ 99). 그리고 엘리베이터는 가장 왼쪽에 있다고 가정하자(그림 1 참고).
# 이런 형태의 호텔을 H × W 형태 호텔이라고 부른다. 호텔 정문은 일층 엘리베이터 바로 앞에 있는데, 정문에서 엘리베이터까지의 거리는 무시한다.
# 또 모든 인접한 두 방 사이의 거리는 같은 거리(거리 1)라고 가정하고 호텔의 정면 쪽에만 방이 있다고 가정한다.
# 방 번호는 YXX 나 YYXX 형태인데 여기서 Y 나 YY 는 층 수를 나타내고 XX 는 엘리베이터에서부터 세었을 때의 번호를 나타낸다.
# 즉, 그림 1 에서 빗금으로 표시한 방은 305 호가 된다.
# 손님은 엘리베이터를 타고 이동하는 거리는 신경 쓰지 않는다. 다만 걷는 거리가 같을 때에는 아래층의 방을 더 선호한다.
# 예를 들면 102 호 방보다는 301 호 방을 더 선호하는데, 102 호는 거리 2 만큼 걸어야 하지만 301 호는 거리 1 만큼만 걸으면 되기 때문이다.
# 같은 이유로 102 호보다 2101 호를 더 선호한다.
# 여러분이 작성할 프로그램은 초기에 모든 방이 비어있다고 가정하에 이 정책에 따라 N 번째로 도착한 손님에게 배정될 방 번호를 계산하는 프로그램이다.
# 첫 번째 손님은 101 호, 두 번째 손님은 201 호 등과 같이 배정한다. 그림 1 의 경우를 예로 들면, H = 6이므로 10 번째 손님은 402 호에 배정해야 한다.
# 입력
# 프로그램은 표준 입력에서 입력 데이터를 받는다. 프로그램의 입력은 T 개의 테스트 데이터로 이루어져 있는데 T 는 입력의 맨 첫 줄에 주어진다.
# 각 테스트 데이터는 한 행으로서 H, W, N, 세 정수를 포함하고 있으며 각각 호텔의 층 수, 각 층의 방 수, 몇 번째 손님인지를 나타낸다
# (1 ≤ H, W ≤ 99, 1 ≤ N ≤ H × W).
# 출력
# 프로그램은 표준 출력에 출력한다. 각 테스트 데이터마다 정확히 한 행을 출력하는데, 내용은 N 번째 손님에게 배정되어야 하는 방 번호를 출력한다.

for i in range(int(input())):
    H, W, N = map(int,input().split()) # H = 층, W = 호
    if N%H==0:
        RN=str(N//H)
    else:
        RN=str(N//H+1)
    if len(RN) == 1:
        RN="0"+RN
    # print(RN)
    # print(f"{str(N%H)+RN}={str(N%H)}+{RN}")
    if N%H!=0:
        RN=str(N%H)+RN
    else:
        RN=str(H)+RN
    print(RN)


# 2750 번
# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 전체 리스트 입력 후 정렬
lst=[]
for i in range(int(input())):
    lst.append(int(input()))
lst.sort()
for i in lst:
    print(i)

# 삽입 정렬
lst=[]
for i in range(int(input())):
    if len(lst) == 0:
        lst.append(int(input()))
    else:
        n = int(input())
        if n>lst[-1]:
            lst.append(n)
        else:
            for j in lst:
                if n < j:
                    index = lst.index(j)
                    break
            lst.insert(index, n)
for i in lst:
    print(i)

# 거품 정렬
lst=[]
for i in range(int(input())):
    lst.append(int(input()))
while True:
    bools=True
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            bools*=False
    if bools==True:
        break
print(lst)


# 2477 번
# 문제
# 시골에 있는 태양이의 삼촌 댁에는 커다란 참외밭이 있다.
# 문득 태양이는 이 밭에서 자라는 참외가 도대체 몇 개나 되는지 궁금해졌다.
# 어떻게 알아낼 수 있는지 골똘히 생각하다가 드디어 좋은 아이디어가 떠올랐다.
# 유레카! 1m2의 넓이에 자라는 참외 개수를 헤아린 다음, 참외밭의 넓이를 구하면 비례식을 이용하여 참외의 총개수를 구할 수 있다.
# 1m2의 넓이에 자라는 참외의 개수는 헤아렸고, 이제 참외밭의 넓이만 구하면 된다.
# 참외밭은 ㄱ-자 모양이거나 ㄱ-자를 90도, 180도, 270도 회전한 모양(┏, ┗, ┛ 모양)의 육각형이다.
# 다행히도 밭의 경계(육각형의 변)는 모두 동서 방향이거나 남북 방향이었다.
# 밭의 한 모퉁이에서 출발하여 밭의 둘레를 돌면서 밭경계 길이를 모두 측정하였다.
# 예를 들어 참외밭 면적은 6800m2이다.
# 만약 1m2의 넓이에 자라는 참외의 개수가 7이라면, 이 밭에서 자라는 참외의 개수는 47600으로 계산된다.
# 1m2의 넓이에 자라는 참외의 개수와, 참외밭을 이루는 육각형의 임의의 한 꼭짓점에서 출발하여 반시계방향으로 둘레를 돌면서 지나는 변의 방향과 길이가 순서대로 주어진다.
# 이 참외밭에서 자라는 참외의 수를 구하는 프로그램을 작성하시오.
# 입력
# 첫 번째 줄에 1m2의 넓이에 자라는 참외의 개수를 나타내는 양의 정수 K (1 ≤ K ≤ 20)가 주어진다. 참외밭을 나타내는 육각형의 임의의 한 꼭짓점에서 출발하여 반시계방향으로 둘레를 돌면서 지나는 변의 방향과 길이 (1 이상 500 이하의 정수) 가 둘째 줄부터 일곱 번째 줄까지 한 줄에 하나씩 순서대로 주어진다. 변의 방향에서 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4로 나타낸다.
# 출력
# 첫째 줄에 입력으로 주어진 밭에서 자라는 참외의 수를 출력한다.

melon = int(input())
length = []
for i in range(6):
    direction, leng = map(int,input().split())
    length.append(leng)
width = max([length[0], length[2], length[4]])
height = max([length[1], length[3], length[5]])
a,b = length.index(width)+3, length.index(height)+3
if a>5:
    a-=6
if b>5:
    b-=6
area = width * height - length[a] * length[b]
print(area*melon)


# 3009 번
# 문제
# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
# 입력
# 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.
# 출력
# 직사각형의 네 번째 점의 좌표를 출력한다.

a,b=[],[]
for i in range(3):
    A, B=map(int,input().split())
    a.append(A)
    b.append(B)
for i in a:
    if a.count(i) == 1:
        x = i
        break
for i in b:
    if b.count(i) == 1:
        y = i
        break
print(x,y)


# 3034 번
# 문제
# 창영이는 화가나서 성냥을 바닥에 던졌다.
# 상근이는 바닥이 더러워진 것을 보고 창영이를 매우 혼냈다.
# 강산이는 근처에서 박스를 발견했다.
# 상덕이는 강산이가 발견한 박스를 상근이에게 주었다.
# 상근이는 박스에 던진 성냥을 모두 담아오라고 시켰다.
# 하지만, 박스에 들어가지 않는 성냥도 있다.
# 이런 성냥은 박스에 담지 않고 희원이에게 줄 것이다.
# 성냥이 박스에 들어가려면, 박스의 밑면에 성냥이 모두 닿아야 한다.
# 박스의 크기와 성냥의 길이가 주어졌을 때, 성냥이 박스에 들어갈 수 있는지 없는지를 구하는 프로그램을 작성하시오. 창영이는 성냥을 하나씩 검사한다.
# 입력
# 첫째 줄에 던진 성냥의 개수 N과 박스의 가로 크기 W와 세로 크기 H가 주어진다. (1 ≤ N ≤ 50, 1 ≤ W, H ≤ 100)
# 다음 N개 줄에는 성냥의 길이가 주어진다. 길이는 1보다 크거나 같고 1000보다 작거나 같은 자연수이다.
# 출력
# 입력으로 주어지는 각각의 성냥에 대해서, 박스안에 들어갈 수 있으면 "DA" 없으면 "NE"를 출력한다.

N, W, H = map(int,input().split())
for i in range(N):
    if int(input()) <= (W**2 + H**2)**0.5:
        print("DA")
    else:
        print("NE")