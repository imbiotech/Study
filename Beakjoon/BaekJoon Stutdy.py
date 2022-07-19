# 2948 번
# 문제
# 2009년 날짜가 주어졌을 때, 무슨 요일인지 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 D와 M이 주어진다.
# M월 D일이다.
# 출력
# 2009년 M월 D일의 요일을 영어로 출력한다.
# 출력은 다음 중 하나이다.
# "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday".

from datetime import *
wd=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
y,d,m=map(int,("2009 "+input()).split())
print(wd[date(y,m,d).weekday()])


# 10992 번
# 문제
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 출력
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
# 예제 입력 1
# 1
# 예제 출력 1
# *
# 예제 입력 2
# 2
# 예제 출력 2
#  *
# ***
# 예제 입력 3
# 3
# 예제 출력 3
#   *
#  * *
# *****
# 예제 입력 4
# 4
# 예제 출력 4
#    *
#   * *
#  *   *
# *******

n=int(input())
for i in range(n):
    if i == 0:
        print(f"""{" "*(n-(i+1))}*""")
    elif i == n-1:
        print("*"*(2*n-1))
    else:
        print(f"""{" "*(n-(i+1))}*{" "*(2*i-1)}*""")


# 11944 번
# 문제
# 문제는 매우 간단하다. N을 N번 출력하는 프로그램을 작성하여라.
# 다만, 답이 길어지는 경우 답의 앞 M자리만 출력한다.
# 입력
# 첫 번째 줄에는 N, M이 주어진다. (1 ≤ N, M ≤ 2016)
# 출력
# N을 N번 출력한다. 만약 답이 길어지면 답의 앞 M자리를 출력한다.

N,M=input().split()
n=N*int(N)
print(n[:int(M)])


# 10845 번
# 문제
# 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# 명령은 총 여섯 가지이다.
# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# 입력
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다.
# 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
# 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다.
# 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
# 출력
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

# from sys import * # 안 쓰면 시간 초과.....
# input = stdin.readline
que = []
for _ in range(int(input())):
    f = input().strip()
    if "push" in f:
        n=int(f.split()[-1])
        que.append(n)
    elif f in ["pop", "front", "back"]:
        if len(que) == 0:
            print(-1)
        elif f == "pop":
            print(que.pop(0))
        elif f == "front":
            print(que[0])
        else: # back
            print(que[-1])
    elif "size" in f:
        print(len(que))
    else: # empty
        if len(que) == 0:
            print(1)
        else:
            print(0)


# 10866 번
# 문제
# 정수를 저장하는 덱(Deque)를 구현한 다음,
# 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# 명령은 총 여덟 가지이다.
# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# 입력
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다.
# 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
# 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다.
# 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
# 출력
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

# from sys import *
# input = stdin.readline
que = []
for _ in range(int(input())):
    f = input().strip()
    if "push" in f:
        n=int(f.split()[-1])
        if "front" in f:
            que=[n]+que
        else:
            que.append(n)
    elif "empty" in f:
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif "size" in f:
        print(len(que))
    else:
        if len(que) == 0:
            print(-1)
        elif "pop" in f:
            if "front" in f:
                print(que.pop(0))
            else:
                print(que.pop(len(que)-1))
        elif "front" in f:
            print(que[0])
        else:
            print(que[-1])


# 11656 번
# 문제
# 접미사 배열은 문자열 S의 모든 접미사를 사전순으로 정렬해 놓은 배열이다.
# baekjoon의 접미사는 baekjoon, aekjoon, ekjoon, kjoon, joon, oon, on, n 으로 총 8가지가 있고,
# 이를 사전순으로 정렬하면, aekjoon, baekjoon, ekjoon, joon, kjoon, n, on, oon이 된다.
# 문자열 S가 주어졌을 때, 모든 접미사를 사전순으로 정렬한 다음 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 문자열 S가 주어진다.
# S는 알파벳 소문자로만 이루어져 있고, 길이는 1,000보다 작거나 같다.
# 출력
# 첫째 줄부터 S의 접미사를 사전순으로 한 줄에 하나씩 출력한다.

S = input()
for i in sorted([S[i:].strip() for i in range(len(S))]):
    print(i)


# 10820 번
# 문제
# 문자열 N개가 주어진다.
# 이때, 문자열에 포함되어 있는 소문자, 대문자, 숫자, 공백의 개수를 구하는 프로그램을 작성하시오.
# 각 문자열은 알파벳 소문자, 대문자, 숫자, 공백으로만 이루어져 있다.
# 입력
# 첫째 줄부터 N번째 줄까지 문자열이 주어진다. (1 ≤ N ≤ 100)
# 문자열의 길이는 100을 넘지 않는다.
# 출력
# 첫째 줄부터 N번째 줄까지 각각의 문자열에 대해서 소문자, 대문자, 숫자, 공백의 개수를 공백으로 구분해 출력한다.

while True:
    try:
        S,s = list(input()),[0]*4
        # Low chr(97~122)
        s[0] = sum([S.count(chr(i)) for i in range(97, 123)])
        # Cap chr(65~96)
        s[1] = sum([S.count(chr(i)) for i in range(65,97)])
        # Num chr(48~57)
        s[2] = sum([S.count(chr(i)) for i in range(48, 58)])
        # Bln
        s[3]=S.count(" ")

        # for i in S:
        #     if i.islower():
        #         s[0]+=1
        #     elif i.isupper():
        #         s[1]+=1
        #     elif i.isnumeric():
        #         s[2]+=1
        #     else:
        #         s[3]+=1

        print(*s) # Cap, Low, Num, Bln
    except EOFError:
        break










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

# 2086 번 - 메모리 초과
# 문제
# 제 1항과 제 2항을 1이라 하고, 제 3항부터는 앞의 두 항의 합을 취하는 수열을 피보나치(fibonacci) 수열이라고 한다.
# 예를 들어 제 3항은 2이며, 제 4항은 3이다.
# 피보나치 수열의 a번째 항부터 b번째 항까지의 합을 구하는 프로그램을 작성하시오.
# 수가 매우 커질 수 있으므로 마지막 아홉 자리만을 구하도록 한다.
# 즉 1,000,000,000으로 나눈 나머지를 구하면 된다.
# 입력
# 첫째 줄에 a와 b이 주어진다.
# 출력
# 첫째 줄에 구한 합을 출력한다.

fib = [0,1,1]
getdata = list(map(int,input().split()))
a = min(getdata)
b = max(getdata)
while True:
    try:
        fib[b]
        break
    except:
        fib.append(fib[-1]+fib[-2])
print(sum(fib[a:b+1])%10**9)





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





print(n)

print(n)











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