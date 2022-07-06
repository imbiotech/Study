# 10162 번
# 문제
# 3개의 시간조절용 버튼 A B C가 달린 전자레인지가 있다.
# 각 버튼마다 일정한 시간이 지정되어 있어
# 해당 버튼을 한번 누를 때마다 그 시간이 동작시간에 더해진다.
# 버튼 A, B, C에 지정된 시간은 각각 5분, 1분, 10초이다.
# 냉동음식마다 전자레인지로 요리해야할 시간 T가 초단위로 표시되어 있다.
# 우리는 A, B, C 3개의 버튼을 적절히 눌러서
# 그 시간의 합이 정확히 T초가 되도록 해야 한다.
# 단 버튼 A, B, C를 누른 횟수의 합은 항상 최소가 되어야 한다.
# 이것을 최소버튼 조작이라고 한다.
# 만일 요리시간이 100초라고 하면(T=100) B를 1번, C는 4번 누르면 된다.
# 이와 다르게 C를 10번 눌러도 100초가 되지만
# 이 경우 10번은 최소 횟수가 아니기 때문이 답이 될 수 없다.
# 이 경우 B 1번, C 4번, 총 5번이 최소버튼 조작이다.
# 그리고 T=234와 같이 3개의 버튼으로 시간을 정확히 맞출 수 없는 경우도 있다.
# 여러분은 주어진 요리시간 T초를 맞추기 위한
# 최소버튼 조작 방법을 구하는 프로그램을 작성해야 한다.
# 입력
# 첫 번째 줄에는 요리시간 T(초)가 정수로 주어져 있으며
# 그 범위는 1 ≤ T ≤ 10,000 이다.
# 출력
# 여러분은 T초를 위한 최소버튼 조작의 A B C 횟수를 첫 줄에 차례대로 출력해야 한다.
# 각각의 횟수 사이에는 빈 칸을 둔다.
# 해당 버튼을 누르지 않는 경우에는 숫자 0을 출력해야한다.
# 만일 제시된 3개의 버튼으로 T초를 맞출 수 없으면 음수 -1을 첫 줄에 출력해야 한다.

A, B, C = 300, 60, 10
btn = []
btn_cnt = []
T = int(input())
if T%C != 0:
    print(-1)
else:
    btn.append(T//A)
    btn.append((T%A)//B)
    btn.append(((T%A)%B)//C)
    print(*btn)


# 10103 번
# 문제
# 창영이와 상덕이는 게임을 하고 있다.
# 게임을 시작하는 시점에서, 두 사람의 점수는 모두 100점이다.
# 게임은 여섯 면 주사위를 사용하며, 라운드로 진행된다.
# 매 라운드마다, 각 사람은 주사위를 던진다.
# 낮은 숫자가 나온 사람은 상대편 주사위에 나온 숫자만큼 점수를 잃게 된다.
# 두 사람의 주사위가 같은 숫자가 나온 경우에는 아무도 점수를 잃지 않는다.
# 게임이 끝난 이후에 두 사람의 점수를 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 라운드의 수 n (1 ≤ n ≤ 15)가 주어진다.
# 다음 n개 줄에는 두 정수가 주어진다.
# 첫 번째 정수는 그 라운드에서 창영이의 주사위에 나타난 숫자,
# 두 번째 정수는 상덕이의 주사위에 나타난 숫자이다.
# 두 정수는 항상 1보다 크거나 같고, 6보다 작거나 같다.
# 출력
# 첫째 줄에 게임이 끝난 이후에 창영이의 점수, 둘째 줄에는 상덕이의 점수를 출력한다.

C, S = 100, 100
for _ in range(int(input())):
    c, s = map(int,input().split())
    if c>s:
        S-=c
    elif c<s:
        C-=s
print(f"{C}\n{S}")


# 10214 번
# 문제
# 경근이는 수업 과제의 일환으로 연세대학교의 역사를 조사하고 있었다.
# 케케묵은 도서관 구석에서 경근이가 발견한 것은 역대 연고전의 야구경기 실황 기록문서였다.
# 하지만 문서를 가지고 있음에도 불구하고
# 한 눈에 당시의 경기 승패를 파악하기에는 어려움이 많았는데,
# 문서에는 회차별 양 팀 획득 점수만이 적혀져 있기 때문이었다.
# 경근이는 주어진 방대한 자료를 해석하는것이 귀찮았기 때문에
# 절친한 프로그래머 친구인 당신에게 도움을 요청했다.
# 주어진 실황 기록문서에서 어떤 팀이 이겼는지를 알아내 경근이를 도와주자!
# 입력
# 입력 파일의 첫 번째 줄에 테스트 케이스의 수를 의미하는 자연수 T가 주어진다.
# 그 다음에는 T개의 테스트 케이스가 주어진다.
# 각 테스트 케이스는 9줄에 걸쳐서 입력되며,
# 매 줄마다 해당 회의 연세대 득점 Y와 고려대 득점 K가 공백으로 구분되어 주어진다.
# 이 두 수는 0이상 9이하이다.
# 출력
# 각각의 케이스마다 한 줄에 연세대가 이겼을 경우 "Yonsei",
# 고려대가 이겼을 경우 "Korea",
# 비겼을 경우 "Draw"를 출력한다.

for _ in range(int(input())):
    Y = []
    K = []
    for __ in range(9):
        y, k = map(int,input().split())
        Y.append(y)
        K.append(k)
    Ys = sum(Y)
    Ks = sum(K)
    if Ys>Ks:
        print("Yonsei")
    elif Ys<Ks:
        print("Korea")
    else:
        print("Draw")


# 11557 번
# 문제
# 입학 OT때 누구보다도 남다르게 놀았던 당신은
# 자연스럽게 1학년 과대를 역임하게 되었다.
# 타교와의 조인트 엠티를 기획하려는 당신은
# 근처에 있는 학교 중 어느 학교가 술을 가장 많이 먹는지 궁금해졌다.
# 학교별로 한 해동안 술 소비량이 주어질 때,
# 가장 술 소비가 많은 학교 이름을 출력하여라.
# 입력
# 입력의 첫 줄에는 테스트 케이스의 숫자 T가 주어진다.
# 매 입력의 첫 줄에는 학교의 숫자 정수 N(1 ≤ N ≤ 100)이 주어진다.
# 이어서 N줄에 걸쳐 학교 이름 S(1 ≤ |S| ≤ 20, S는 공백없는 대소문자 알파벳 문자열)와
# 해당 학교가 지난 한 해동안 소비한 술의 양 L(0 ≤ L ≤ 10,000,000)이 공백으로 구분되어 정수로 주어진다.
# 같은 테스트 케이스 안에서 소비한 술의 양이 같은 학교는 없다고 가정한다.
# 출력
# 각 테스트 케이스마다 한 줄에 걸쳐 술 소비가 가장 많은 학교의 이름을 출력한다.

# List형을 쓰는 법
for _ in range(int(input())):
    Univ = []
    Alcohol = []
    for __ in range(int(input())):
        u, a = map(str,input().split())
        Univ.append(u)
        Alcohol.append(int(a))
    print(Univ[Alcohol.index(max(Alcohol))])

# Dict형을 쓰는 법
T=int(input())
for _ in range(T):
    A={}
    for _ in range(int(input())):
        a,b=input().split()
        A[a]=int(b)
    print(max(A, key=A.get))


# 1977 번
# 문제
# M과 N이 주어질 때 M이상 N이하의 자연수 중 완전제곱수인 것을 모두 골라 그 합을 구하고 그 중 최솟값을 찾는 프로그램을 작성하시오.
# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중
# 완전제곱수는 64, 81, 100 이렇게 총 3개가 있으므로 그 합은 245가 되고 이 중 최솟값은 64가 된다.
# 입력
# 첫째 줄에 M이, 둘째 줄에 N이 주어진다.
# M과 N은 10000이하의 자연수이며 M은 N보다 같거나 작다.
# 출력
# M이상 N이하의 자연수 중 완전제곱수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다.
# 단, M이상 N이하의 자연수 중 완전제곱수가 없을 경우는 첫째 줄에 -1을 출력한다.

M = int(input())
N = int(input())
perf = []
for i in range(M, N+1):
    if i**0.5 == int(i**0.5):
        perf.append(i)
if len(perf) == 0:
    print(-1)
else:
    print(f"{sum(perf)}\n{min(perf)}")


# 11098 번
# 문제
# 구단이 성적을 내지 못한다면 답은 새 선수 영입뿐이다.
# 이것은 오늘날 유럽 리그에서 가장 흔한 전략이고,
# 노르웨이의 로젠버그 팀은 이러한 전략이 성공한 대표적 예시다.
# 그들은 많은 스카우터들을 지구 곳곳에 파견해 가능성 있는 루키를 찾는다.
# 현재 첼시는 프리미어 리그에서 헤매고 있고, 결국 새로운 선수를 사기로 결정했다.
# 하지만 그들은 스카우터를 기다리기 지쳤고, 훨씬 더 효율적인 전략을 개발해냈다.
# "만약 무언가 팔리고 있다면, 그것에는 합당한 이유가 있다"는 배룸의 명언이 바로 그것이다.
# 축구에서 이 말은 곧 가장 비싼 선수가 가장 좋은 선수라는 이야기가 된다.
# 이에 따라 새로운 선수를 찾는 방법은 단순히 구단들에게 전화를 걸어 그들의 가장 비싼 선수를 사는게 되었다.
# 당신의 임무는 첼시가 리스트에서 가장 비싼 선수를 찾아낼 수 있도록 돕는 것이다.
# 입력
# 첫 번째 줄에는 테스트 케이스의 개수 n이 주어진다 (n≤100).
# 각 테스트 케이스의 첫 번째 줄 p는 고려해야될 선수의 수이다 (1≤p≤100).
# 그 아래 p개의 줄에는 선수의 정보가 표시된다.
# 각각의 줄은 선수의 가격 C 와 이름을 입력한다 (C<2*109).
# 모든 선수의 가격은 서로 다르다.
# 선수의 이름은 20자 이하여야 하며, 사이에 공백이 있어서는 안 된다.
# 출력
# 각각의 테스트 케이스에서 가장 비싼 선수의 이름을 출력해야한다.

for _ in range(int(input())):
    players = {}
    for __ in range(int(input())):
        salary, name = map(str,input().split())
        players[name] = int(salary)
    print(max(players, key=players.get))


# 5635 번
# 문제
# 어떤 반에 있는 학생들의 생일이 주어졌을 때,
# 가장 나이가 적은 사람과 가장 많은 사람을 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 반에 있는 학생의 수 n이 주어진다. (1 ≤ n ≤ 100)
# 다음 n개 줄에는 각 학생의 이름과 생일이 "이름 dd mm yyyy"와 같은 형식으로 주어진다.
# 이름은 그 학생의 이름이며, 최대 15글자로 이루어져 있다.
# dd mm yyyy는 생일 일, 월, 연도이다. (1990 ≤ yyyy ≤ 2010, 1 ≤ mm ≤ 12, 1 ≤ dd ≤ 31)
# 주어지는 생일은 올바른 날짜이며, 연, 월 일은 0으로 시작하지 않는다.
# 이름이 같거나, 생일이 같은 사람은 없다.
# 출력
# 첫째 줄에 가장 나이가 적은 사람의 이름, 둘째 줄에 가장 나이가 많은 사람 이름을 출력한다.

# 풀이 1; 코드 정리 전
n, d, m, y = [],[],[],[]
for _ in range(int(input())):
    N, D, M, Y = map(str,input().split())
    n.append(N);d.append(int(D));m.append(int(M));y.append(int(Y))
# d = [1, 30, 15, 18, 20]
# m = [10, 12, 8, 9, 9]
# n = ['M', 'A', 'T', 'J', 'G']
# y = [1991, 1990, 1993, 1990, 1990]
if y.count(max(y)) == 1:
    print(n[y.index(max(y))])
else:
    m2 = list(map(lambda x,z: x if z == max(y) else False, m, y))
    max_m2 = max(x for x in m2 if x is not False)
    if m2.count(max_m2) == 1:
        print(n[m2.index(max_m2)])
    else:
        d2 = list(map(lambda x,z: x if z == max(y) else False, d, y))
        max_d2 = max(x for x in d2 if x is not False)
        print(n[d2.index(max_d2)])

if y.count(min(y)) == 1:
    print(n[y.index(min(y))])
else:
    m2 = list(map(lambda x,z: x if z == min(y) else False, m, y))
    min_m2 = min(x for x in m2 if x is not False)
    if m2.count(min_m2) == 1:
        print(n[m2.index(min_m2)])
    else:
        d2 = list(map(lambda x,z: x if z == min(y) else False, d, y))
        min_d2 = min(x for x in d2 if x is not False)
        print(n[d2.index(min_d2)])

# 풀이 2; 코드 정리
def min_(a,b):
    min2 = list(map(lambda x,y: x if y == min(b) else False, a,b))
    min_min2 = min(x for x in min2 if x is not False)
    c = min2.count(min_min2)
    i = min2.index(min_min2)
    return c, i

def max_(a,b):
    max2 = list(map(lambda x, y: x if y == max(b) else False, a, b))
    max_max2 = max(x for x in max2 if x is not False)
    c = max2.count(max_max2)
    i = max2.index(max_max2)
    return c, i

n, d, m, y = [],[],[],[]
for _ in range(int(input())):
    N, D, M, Y = map(str,input().split())
    n.append(N);d.append(int(D));m.append(int(M));y.append(int(Y))
if y.count(max(y)) == 1:
    print(n[y.index(max(y))])
else:
    c, i = max_(m,y)
    if c == 1:
        print(n[i])
    else:
        c,i = max_(d,y)
        print(n[i])

if y.count(min(y)) == 1:
    print(n[y.index(min(y))])
else:
    c, i = min_(m,y)
    if c == 1:
        print(n[i])
    else:
        c, i = min_(d,y)
        print(n[i])


# 1408 번
# 문제
# 도현이는 Counter Terror Unit (CTU)에서 일하는 특수요원이다.
# 도현이는 모든 사건을 정확하게 24시간이 되는 순간 해결하는 것으로 유명하다.
# 도현이는 1시간 만에 범인을 잡을 수 있어도 잡지 않는다.
# 정확하게 24시간이 되는 순간이 아니면 잡지 않는 CTU 특수요원이다.
# 2008년 3월 3일 월요일, CTU는 새학기에 맞춰 핵폭탄을 날리겠다는 테러 정보를 입수했다.
# CTU에서는 특수요원 도현이에게 이 임무를 맡겼다.
# CTU의 프로그래머 준규는 이 사건의 배후가 김선영이란 것을 해킹을 통해 밝혀내었다.
# 도현이는 선영이를 임무를 시작한지 정확하게 24시간이 되는 순간에 잡으려고 한다.
# 만약 지금 시간이 13:52:30이고,
# 임무를 시작한 시간이 14:00:00 이라면 도현이에게 남은시간은 00:07:30 이다.
# 모든 시간은 00:00:00 ~ 23:59:59로 표현할 수 있다.
# 입력과 출력에 주어지는 모든 시간은 XX:XX:XX 형태이며,
# 숫자가 2자리가 아닐 경우에는 0으로 채운다.
# 도현이가 임무를 시작한 시간과, 현재 시간이 주어졌을 때,
# 도현이에게 남은 시간을 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에는 현재 시간이, 둘째 줄에는 도현이가 임무를 시작한 시간이 주어진다.
# 임무를 시작한 시간과 현재 시간이 같은 경우는 주어지지 않는다.
# 출력
# 첫째 줄에 도현이가 임무를 수행하는데 남은 시간을 문제에서 주어지는 시간의 형태 (XX:XX:XX)에 맞춰 출력한다.

from datetime import *
now = input().split(":")
start = input().split(":")
# now = "13:52:30".split(":")
# start = "14:00:00".split(":")
if now > start:
    now_t = datetime.combine(date(1,1,1),time(int(now[0]),int(now[1]),int(now[2])))
else:
    now_t = datetime.combine(date(1,1,2), time(int(now[0]),int(now[1]),int(now[2])))
end =  datetime.combine(date(1,1,2),time(int(start[0]),int(start[1]),int(start[2])))
left = str(end-now_t)
if len(left) == 7:
    print("0"+left)
else:
    print(left)


# 5565 번
# 문제
# 새 학기를 맞아 상근이는 책을 10권 구입했다.
# 상근이는 의욕이 너무 앞서서 가격을 조사하지 않고 책을 구입했다.
# 이제 각 책의 가격을 알아보려고 한다.
# 하지만, 영수증에는 얼룩이 묻어있었고, 상근이는 책 10권 중 9권의 가격만 읽을 수 있었다.
# 책 10권의 총 가격과 가격을 읽을 수 있는 9권 가격이 주어졌을 때,
# 가격을 읽을 수 없는 책의 가격을 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 10권의 총 가격이 주어진다.
# 둘째 줄부터 9개 줄에는 가격을 읽을 수 있는 책 9권의 가격이 주어진다.
# 책의 가격은 10,000이하인 양의 정수이다.
# 출력
# 첫째 줄에 가격을 읽을 수 없는 책의 가격을 출력한다.

books=[]
for _ in range(10):
    books.append(int(input()))
print(books[0]-sum(books[1:]))


# 2609 번
# 문제
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

def diviser(num):
    divs = []
    for i in range(1,num+1):
        if num%i==0:
            divs.append(i)
    return divs

a, b = map(int,input().split())
dis_a = diviser(a)
dis_b = diviser(b)
max_div = max([x for x in dis_a if x in dis_b])
min_mul = int(a * b / max_div)
print(f"{max_div}\n{min_mul}")


# 10984 번
# 문제
# 게으른 근우는 열심히 놀다가 문득, 자신의 학점 평균이 얼마일지 궁금해졌다.
# 학사시스템도 들어가기 귀찮아하는 근우를 위해 구해주도록 하자.
# 입력
# 첫 번째 줄에 학기의 수 T가 주어진다.
# 두 번째 줄부터 T개 학기에 대한 정보가 주어진다.
# 각 학기에 대한 정보는 다음과 같이 구성되어 있다.
# 첫 번째 줄에 들었던 과목의 수 N이 주어지고,
# 다음 N개 줄에 걸쳐서 N개 과목들의 학점 C와 성적 G가 주어진다. (1 ≤ N ≤ 10, 1 ≤ C ≤ 6, C는 정수)
# G는 {0, 0.7, 1, 1.3, 1.7, 2, 2.3, 2.7, 3, 3.3, 3.7, 4, 4.3} 중 하나이며 소수 부분은 최대 한 자리까지 주어진다.
# 출력
# 각 학기에 대해 근우의 총 학점과 평점(GPA)을 출력한다. 정답과의 절대 오차는 10-1까지 허용한다.

for _ in range(int(input())):
    Credit = 0
    Grade = 0
    for __ in range(int(input())):
        c, g = map(float,input().split())
        Credit += c
        Grade += c*g
    print(f"{int(Credit)} {round(Grade/Credit,1)}")


""" ######################################## 아래는 수정 필요 ######################################## """
""" ######################################## 아래는 수정 필요 ######################################## """
""" ######################################## 아래는 수정 필요 ######################################## """
""" ######################################## 아래는 수정 필요 ######################################## """
""" ######################################## 아래는 수정 필요 ######################################## """
""" ######################################## 아래는 수정 필요 ######################################## """
""" ######################################## 아래는 수정 필요 ######################################## """
""" ######################################## 아래는 수정 필요 ######################################## """
""" ######################################## 아래는 수정 필요 ######################################## """
""" ######################################## 아래는 수정 필요 ######################################## """

# 1934 번 - 통과는 했는데 시간 개선 필요
# 문제
# 두 자연수 A와 B에 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다.
# 이런 공배수 중에서 가장 작은 수를 최소공배수라고 한다.
# 예를 들어, 6과 15의 공배수는 30, 60, 90등이 있으며, 최소 공배수는 30이다.
# 두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다.
# 둘째 줄부터 T개의 줄에 걸쳐서 A와 B가 주어진다. (1 ≤ A, B ≤ 45,000)
# 출력
# 첫째 줄부터 T개의 줄에 A와 B의 최소공배수를 입력받은 순서대로 한 줄에 하나씩 출력한다.

# 풀이 1 - 시간 초과, 숫자 리스트를 받아서 1~작은수 로 나누기
for _ in range(int(input())):
    num = sorted(list(map(int,("1 "+input()).split()))) # 리스트 생성
    for i in range(num[1]):
        a=num[1]-i # 제수 = 작은수 ~ 1 사이의 수
        if a == 0: # 제수가 0 일 때 종료
            break
        elif num[1]%a == 0 and num[2]%a == 0: # 두 피제수에 대한 나머지가 0 일 때 값 업데이트
            num[1]/=a
            num[2]/=a
            num[0]*=a
    print(int(num[0]*num[1]*num[2]))

# 풀이 2 - 시간 초과, while을 하나 더 넣어서 값 업데이트 후 break 진행
for _ in range(int(input())):
    num = sorted(list(map(int,("1 "+input()).split()))) # 리스트 생성
    try:
        while True:
            for i in range(num[1]):
                a = num[1] - i  # 제수 = 작은수 ~ 1 사이의 수
                if a == 0:  # 제수가 0 일 때 종료
                    break
                elif num[1] % a == 0 and num[2] % a == 0:  # 두 피제수에 대한 나머지가 0 일 때 값 업데이트
                    num[1] /= a
                    num[2] /= a
                    num[0] *= a
                    break
    except TypeError:
        print(int(num[0]*num[1]*num[2]))

# 풀이 3 - 시간 초과, 역순 한게 문제인 것 같아서 다시 변경
for _ in range(int(input())):
    num = sorted(list(map(int,("1 "+input()).split()))) # 리스트 생성
    try:
        while True:
            x = num[0]
            for i in range(2, int(num[1])+1):
                if num[1] % i == 0 and num[2] % i == 0:  # 두 피제수에 대한 나머지가 0 일 때 값 업데이트
                    num[1] /= i
                    num[2] /= i
                    num[0] *= i
                    break
            if x == num[0]:
                x/0
    except:
        print(int(num[0]*num[1]*num[2]))

# 풀이 4 - 다른 문제에서...
def diviser(num):
    divs = []
    for i in range(1,num+1):
        if num%i==0:
            divs.append(i)
    return divs

for _ in range(int(input())):
    a, b = map(int,input().split())
    div = diviser(min([a,b]))
    max_div = max([x for x in div if max([a,b])%x==0])
    min_mul = int(a * b / max_div)
    print(min_mul)

# 풀이 5 - 라이브러리
from math import lcm
for _ in range(int(input())):
    a, b = map(int,input().split())
    print(lcm(a,b))




# 4948 번 - 시간 초과
# 문제
# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
# 이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
# 예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19)
# 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.
# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.
# 입력의 마지막에는 0이 주어진다.
# 출력
# 각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.
# 제한
# 1 ≤ n ≤ 123,456

# 풀이 1
def prime(n):
    if n == 1:
        return 0
    else:
        m = int(n**0.5+1)
        o = 1
        for i in range(2,m):
            if n % i == 0:
                o = 0
                break
        return o

while True:
    n=int(input())
    c=0
    if n==0:break
    if n==1:
        print(1)
        continue
    else:
        # 수정 전: number 의 원소가 범위 내의 모든 수
        # numbers = [i for i in range(n+1, 2*n+1)]
        # 수정 후: numbers 의 원소를 범위 내의 홀수로 제한
        numbers = [2 * i + 1 for i in range(int((n + 1) / 2), n)]
        # 수정 전: map 사용하여 list 생성
        # Prime = list(map(prime,numbers))
        # 수정 후: for 사용하여 list 생성
        Prime = []
        for i in numbers:
            Prime.append(prime(i))
    print(Prime.count(1))

# 2617 번
# 문제
# 모양은 같으나, 무게가 모두 다른 N개의 구슬이 있다. N은 홀수이며, 구슬에는 번호가 1,2,...,N으로 붙어 있다.
# 이 구슬 중에서 무게가 전체의 중간인 (무게 순서로 (N+1)/2번째) 구슬을 찾기 위해서 아래와 같은 일을 하려 한다.
# 우리에게 주어진 것은 양팔 저울이다. 한 쌍의 구슬을 골라서 양팔 저울의 양쪽에 하나씩 올려 보면 어느 쪽이 무거운가를 알 수 있다.
# 이렇게 M개의 쌍을 골라서 각각 양팔 저울에 올려서 어느 것이 무거운가를 모두 알아냈다.
# 이 결과를 이용하여 무게가 중간이 될 가능성이 전혀 없는 구슬들은 먼저 제외한다.
# 예를 들어, N=5이고, M=4 쌍의 구슬에 대해서 어느 쪽이 무거운가를 알아낸 결과가 아래에 있다.
# 구슬 2번이 구슬 1번보다 무겁다.
# 구슬 4번이 구슬 3번보다 무겁다.
# 구슬 5번이 구슬 1번보다 무겁다.
# 구슬 4번이 구슬 2번보다 무겁다.
# 위와 같이 네 개의 결과만을 알고 있으면, 무게가 중간인 구슬을 정확하게 찾을 수는 없지만,
# 1번 구슬과 4번 구슬은 무게가 중간인 구슬이 절대 될 수 없다는 것은 확실히 알 수 있다.
# 1번 구슬보다 무거운 것이 2, 4, 5번 구슬이고, 4번 보다 가벼운 것이 1, 2, 3번이다. 따라서 답은 2개이다.
# M 개의 쌍에 대한 결과를 보고 무게가 중간인 구슬이 될 수 없는 구슬의 개수를 구하는 프로그램을 작성하시오.
# 입력
# 첫 줄은 구슬의 개수를 나타내는 정수 N(1 ≤ N ≤ 99)과 저울에 올려 본 쌍의 개수 M(1 ≤ M ≤ N(N-1)/2)이 주어진다.
# 그 다음 M 개의 줄은 각 줄마다 두 개의 구슬 번호가 주어지는데, 앞 번호의 구슬이 뒤 번호의 구슬보다 무겁다는 것을 뜻한다.
# 출력
# 첫 줄에 무게가 중간이 절대로 될 수 없는 구슬의 수를 출력 한다.

N, M = map(int,input().split())
weight = [[0,0]] * N
for _ in range(M):
    a, b = map(int,input().split())
    i1 = weight[a-1][0] + 1
    i2 = weight[a-1][1]
    j1 = weight[b-1][0]
    j2 = weight[b-1][1] + 1
    weight[a-1] = [i1, i2]
    weight[b-1] = [j1, j2]
    print(f"[{i1}, {i2}], [{j1}, {j2}]")
    print(weight)
print(weight)


# 1759 번 - ?
# 문제
# 바로 어제 최백준 조교가 방 열쇠를 주머니에 넣은 채 깜빡하고 서울로 가 버리는 황당한 상황에 직면한 조교들은,
# 702호에 새로운 보안 시스템을 설치하기로 하였다.
# 이 보안 시스템은 열쇠가 아닌 암호로 동작하게 되어 있는 시스템이다.
# 암호는 서로 다른 L개의 알파벳 소문자들로 구성되며
# 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다.
# 또한 정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아
# 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다.
# 즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.
# 새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 C가지가 있다고 한다.
# 이 알파벳을 입수한 민식, 영식 형제는 조교들의 방에 침투하기 위해 암호를 추측해 보려고 한다.
# C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 두 정수 L, C가 주어진다. (3 ≤ L ≤ C ≤ 15)
# 다음 줄에는 C개의 문자들이 공백으로 구분되어 주어진다.
# 주어지는 문자들은 알파벳 소문자이며, 중복되는 것은 없다.
# 출력
# 각 줄에 하나씩, 사전식으로 가능성 있는 암호를 모두 출력한다.

L, C = map(int,input().split())
password = set(map(str,input().split()))
vowel = {"a", "e", "i", "o", "u"}
v_in_p = password.intersection(vowel)


# 25192 번 - 시간 초과
# 문제
# 알고리즘 입문방 오픈 채팅방에서는 새로운 분들이 입장을 할 때마다 곰곰티콘을 사용해 인사를 한다. 이를 본 문자열 킬러 임스는 채팅방의 기록을 수집해 그 중 곰곰티콘이 사용된 횟수를 구해 보기로 했다.
# ENTER는 새로운 사람이 채팅방에 입장했음을 나타낸다. 그 외는 채팅을 입력한 유저의 닉네임을 나타낸다. 닉네임은 숫자 또는 영문 대소문자로 구성되어 있다.
# 새로운 사람이 입장한 이후 처음 채팅을 입력하는 사람은 반드시 곰곰티콘으로 인사를 한다. 그 외의 기록은 곰곰티콘을 쓰지 않은 평범한 채팅 기록이다.
# 채팅 기록 중 곰곰티콘이 사용된 횟수를 구해보자!
# 입력
# 첫 번째 줄에는 채팅방의 기록 수를 나타내는 정수 N 이 주어진다. (1 <= N <= 100,000)
# 두 번째 줄부터 N 개의 줄에 걸쳐 새로운 사람의 입장을 나타내는 ENTER, 혹은 채팅을 입력한 유저의 닉네임이 문자열로 주어진다. (1 <= 문자열 길이 <= 20)
# 첫 번째 주어지는 문자열은 무조건 ENTER이다.
# 출력
# 채팅 기록 중 곰곰티콘이 사용된 횟수를 출력하시오.

# 풀이 1
count = 0 # 횟수 체크 변수 선언
for _ in range(int(input())):
    log = input()
    if log == "ENTER": # 채팅 로그가 "입장"이면 채팅 로그 리스트 초기화
        gomgom = []
    elif log not in gomgom: # 채팅 로그 리스트 내에 닉네임이 없을 경우 닉네임 삽입하고, 곰곰티콘 횟수 1회 증가
        gomgom.append(log)
        count += 1
print(count)


# 11653 번 - 시간 초과
# 문제
# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.
# 출력
# N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.

# 풀이 1 - 소수를 먼저 입력해 놓고 나누기, 시간 초과
primenumber = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
               101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
               211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
               307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
               401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
               503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
               601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
               701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
               809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887,
               907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
N = int(input())
while N>1:
    for i in primenumber:
        if N % i == 0:
            print(i)
            N /= i
            break

# 풀이 2 - N 이하의 소수를 구하고 소인수분해 하기, 시간 초과
def prime(n):
    if n == 1:
        return 0
    else:
        m = int(n**0.5+1)
        for i in range(2,m):
            if n % i == 0:
                n = 0
                break
        return n

N = int(input())
N_list = [i for i in range(N+1)]
M_list = list(set(map(prime,N_list)))
M_list.sort()
if 0 in M_list:
    M_list.remove(0)
while N>1:
    for i in M_list:
        if N % i == 0:
            print(i)
            N /= i
            break
        else:
            M_list.remove(i)

















# 10815 번 - 시간 초과
# 문제
# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다.
# 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 두 숫자 카드에 같은 수가 적혀있는 경우는 없다.
# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다.
# 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다.
# 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다
# 출력
# 첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다.

# 시간 초과
from sys import stdin
N = int(stdin.readline())
N_list=list(map(int,stdin.readline().split()))
M = int(stdin.readline())
M_list=list(map(int,stdin.readline().split()))
C_list=[]
for i in M_list:
    if i in N_list:
        C_list.append(1)
    else:
        C_list.append(0)
print(C_list)

# 런타임 에러, 외부 lib 없음
from sys import stdin
import pandas as pd
N = int(stdin.readline())
N_df=pd.DataFrame(map(int,stdin.readline().split()),columns=["N"])
M = int(stdin.readline())
M_df=pd.DataFrame(map(int,stdin.readline().split()),columns=["M"])
Filter = M_df["M"].isin(N_df["N"])
M_df.loc[Filter, "M"] = 1
M_df.loc[-Filter, "M"] = 0
print(" ".join(list(M_df["M"])))


# 2004 번 - 시간 초과
# 문제
# binom{n}{m}의 끝자리 $0$의 개수를 출력하는 프로그램을 작성하시오
# 입력
# 첫째 줄에 정수 n, m (0 ≤ m ≤ n ≤ 2,000,000,000, n != 0 )이 들어온다.
# 출력
# 첫째 줄에 binom{n}{m}의 끝자리 0의 개수를 출력한다.

# 시간 초과
from math import factorial
n, m = map(int,input().split())
n_m = int(factorial(n)//(factorial(m)*factorial(n-m)))
count = 0
while n_m%10==0:
    n_m//=10
    count+=1
print(count)

# 시간 초과
from math import factorial
n, m = map(int,input().split())
n_m = list(str(int(factorial(n)//(factorial(m)*factorial(n-m)))))
n_m.reverse()
count = 0
for i in n_m:
    if i=="0":
        count+=1
    else:
        break
print(count)

# 시간 초과
from sys import stdin
from math import factorial
n, m = map(int,stdin.readline().split())
n_m = list(str(int(factorial(n)//(factorial(m)*factorial(n-m)))))
n_m.reverse()
count = 0
for i in n_m:
    if i=="0":
        count+=1
    else:
        break
print(count)

# 시간 초과
from math import factorial
n, m = map(int,input().split())
n_m = list(str(int(factorial(n)//(factorial(m)*factorial(n-m)))))
n_m.reverse()
count = len(n_m)
for i in range(1,10):
    count=min(0, n_m.index(i))
print(count)


# 10757 번 - C 언어 문제
# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 A와 B가 주어진다. (0 < A,B < 10**10000)
# 출력
# 첫째 줄에 A+B를 출력한다.
import sys
a,b=map(int,sys.stdin.readline().split())
print(a+b)



"""
# 풀이 1 - 시간 초과
def fibonacci(n, listing):
    if n == 0:
        listing.append(n)
        return 0, listing
    elif n == 1:
        listing.append(n)
        return 1, listing
    else:
        return fibonacci(n-1, listing) + fibonacci(n-2, listing)

for i in range(int(input())):
    count = []
    fibonacci(int(input()),count)
    print(count.count(0), count.count(1))

# 풀이 2
def fibonacci(n):
    if n == 0:
        f_list.append(0)
        return 0
    elif n == 1:
        f_list.append(1)
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
global f_list
f_list = []
fibonacci(6)
print(f_list)
"""




"""
시간 측정 모델
from time import time
start = time()



print("#######end#######")
print(time()-start)
"""

"""
파이참 편집 기능
# 찾아서 바꾸기
편집할 부분을 블럭으로 씌운 다음에 Ctrl + R 로 특정 문자를 바꿈

# 위 아래 코드와 줄바꿈
해당 열에 커서를 놓고 Alt + Shift + 방향키

# 동일 위치 열 편집
Ctrl + Ctrl + 방향키

# 다중 커서 편집
Alt + 클릭
"""