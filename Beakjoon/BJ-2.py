# 3053 번
# 문제
# 19세기 독일 수학자 헤르만 민코프스키는 비유클리드 기하학 중 택시 기하학을 고안했다.
# 택시 기하학에서 두 점 T1(x1,y1), T2(x2,y2) 사이의 거리는 다음과 같이 구할 수 있다.
# D(T1,T2) = |x1-x2| + |y1-y2|
# 두 점 사이의 거리를 제외한 나머지 정의는 유클리드 기하학에서의 정의와 같다.
# 따라서 택시 기하학에서 원의 정의는 유클리드 기하학에서 원의 정의와 같다.
# 원: 평면 상의 어떤 점에서 거리가 일정한 점들의 집합
# 반지름 R이 주어졌을 때, 유클리드 기하학에서 원의 넓이와, 택시 기하학에서 원의 넓이를 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 반지름 R이 주어진다. R은 10,000보다 작거나 같은 자연수이다.
# 출력
# 첫째 줄에는 유클리드 기하학에서 반지름이 R인 원의 넓이를, 둘째 줄에는 택시 기하학에서 반지름이 R인 원의 넓이를 출력한다. 정답과의 오차는 0.0001까지 허용한다

import math
r = int(input())
print(math.pi*(r**2))
print(((2*r)**2)/2)


# 5086 번
# 문제
# 4 × 3 = 12이다.
# 이 식을 통해 다음과 같은 사실을 알 수 있다.
# 3은 12의 약수이고, 12는 3의 배수이다.
# 4도 12의 약수이고, 12는 4의 배수이다.
# 두 수가 주어졌을 때, 다음 3가지 중 어떤 관계인지 구하는 프로그램을 작성하시오.
# 1. 첫 번째 숫자가 두 번째 숫자의 약수이다.
# 2. 첫 번째 숫자가 두 번째 숫자의 배수이다.
# 3. 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.
# 입력
# 입력은 여러 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 10,000이 넘지않는 두 자연수로 이루어져 있다. 마지막 줄에는 0이 2개 주어진다. 두 수가 같은 경우는 없다.
# 출력
# 각 테스트 케이스마다 첫 번째 숫자가 두 번째 숫자의 약수라면 factor를, 배수라면 multiple을, 둘 다 아니라면 neither를 출력한다.

while True:
    a, b = map(int,input().split())
    if a == b == 0:
        break
    if b%a == 0:
        print("factor")
    elif a%b == 0:
        print("multiple")
    else:
        print("neither")


# 1010 번
# 문제
# 재원이는 한 도시의 시장이 되었다. 이 도시에는 도시를 동쪽과 서쪽으로 나누는 큰 일직선 모양의 강이 흐르고 있다.
# 하지만 재원이는 다리가 없어서 시민들이 강을 건너는데 큰 불편을 겪고 있음을 알고 다리를 짓기로 결심하였다.
# 강 주변에서 다리를 짓기에 적합한 곳을 사이트라고 한다.
# 재원이는 강 주변을 면밀히 조사해 본 결과 강의 서쪽에는 N개의 사이트가 있고 동쪽에는 M개의 사이트가 있다는 것을 알았다. (N ≤ M)
# 재원이는 서쪽의 사이트와 동쪽의 사이트를 다리로 연결하려고 한다.
# (이때 한 사이트에는 최대 한 개의 다리만 연결될 수 있다.)
# 재원이는 다리를 최대한 많이 지으려고 하기 때문에 서쪽의 사이트 개수만큼 (N개) 다리를 지으려고 한다.
# 다리끼리는 서로 겹쳐질 수 없다고 할 때 다리를 지을 수 있는 경우의 수를 구하는 프로그램을 작성하라.
# 입력
# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다.
# 그 다음 줄부터 각각의 테스트케이스에 대해 강의 서쪽과 동쪽에 있는 사이트의 개수 정수 N, M (0 < N ≤ M < 30)이 주어진다.
# 출력
# 각 테스트 케이스에 대해 주어진 조건하에 다리를 지을 수 있는 경우의 수를 출력한다.

from math import factorial
for i in range(int(input())):
    a, b = map(int,input().split())
    print(int(factorial(b)/(factorial(a)*factorial(b-a))))


# 11050 번
# 문제
# 자연수 N과 정수 K가 주어졌을 때 이항계수 binom{N}{K}를 구하는 프로그램을 작성하시오.
#입력
# 첫째 줄에 N과 정수 K가 주어진다.(1 ≤ N ≤ 10, 0 ≤ K ≤ N)
# 출력
# binom{N}{K}를 출력한다.

from math import factorial
N, K = map(int,input().split())
print(int(factorial(N)/(factorial(K)*factorial(N-K))))


# 11051 번
# 문제
# 자연수 N과 정수 K가 주어졌을 때 이항계수 binom{N}{K}를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.
#입력
# 첫째 줄에 N과 정수 K가 주어진다.(1 ≤ N ≤ 10, 0 ≤ K ≤ N)
# 출력
# binom{N}{K}를 10,007로 나눈 나머지를 출력한다.

# 부동 소수점에 관한 문제, N_K 계산 시 / 가 아닌 // 를 사용
from math import factorial
N, K = map(int,input().split())
N_K = int(factorial(N)//(factorial(K)*factorial(N-K)))
print(int(N_K%10007))


# 1037 번
# 문제
# 양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다.
# 어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 N의 진짜 약수의 개수가 주어진다. 이 개수는 50보다 작거나 같은 자연수이다.
# 둘째 줄에는 N의 진짜 약수가 주어진다. 1,000,000보다 작거나 같고, 2보다 크거나 같은 자연수이고, 중복되지 않는다.
# 출력
# 첫째 줄에 N을 출력한다. N은 항상 32비트 부호있는 정수로 표현할 수 있다.

count = int(input())
divisor = list(map(int,input().split()))
divisor.sort()
print(divisor[0]*divisor[-1])
# 또는 .sort() 없이 max(divisor)*min(divisor)


# 1676 번
# 문제
# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)
# 출력
# 첫째 줄에 구한 0의 개수를 출력한다.

# 10으로 나누면서 확인
from math import factorial
a = factorial(int(input()))
count = 0
while a%10==0:
    a//=10
    count+=1
print(count)

# 역순 리스트 만들어서 [0]부터 확인
from math import factorial
a = list(str(factorial(int(input()))))
a.reverse()
count = 0
for i in a:
    if i=="0":
        count+=1
    else:
        break
print(count)

# 역순 리스트 만들어서 index 확인
from math import factorial
a = list(str(factorial(int(input()))))
a.reverse()
count = len(a)
for i in range(1,10):
    if i in a:
        count=min(0, a.index(i))
print(count)

# 충분히 많은 2의 개수를 고려하여 5의 배수 = 0이 1개, 5*5의 배수 = 0이 2개, 5*5*5의 배수 = 0이 3개 로 계산
a = int(input())
print(a//5+a//25+a//125)


# 1065 번
# 문제
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
# 출력
# 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

N = int(input())
if N < 100:
    print(N)
else:
    count=99
    for i in range(100,N+1):
        A = i // 100
        B = i % 100 // 10
        C = i % 10
        if 2 * B == A + C:
            count+=1
    print(count)


# 2775 번
# 문제
# 평소 반상회에 참석하는 것을 좋아하는 주희는 이번 기회에 부녀회장이 되고 싶어
# 각 층의 사람들을 불러 모아 반상회를 주최하려고 한다.
# 이 아파트에 거주를 하려면 조건이 있는데,
# “a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다”
# 는 계약 조항을 꼭 지키고 들어와야 한다.
# 아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때,
# 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라.
# 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
# 입력
# 첫 번째 줄에 Test case의 수 T가 주어진다. 그리고 각각의 케이스마다 입력으로 첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어진다
# 출력
# 각각의 Test case에 대해서 해당 집에 거주민 수를 출력하라.

# 풀이 1 - 시간 초과
def nk(k,n):
    if k==0:
        return n # 0층 i호는 i
    else:
        sum = 0
        for i in range(1,n+1): # k층 n호는 k-1층의 1~n호 합
            sum+=nk(k-1,i)
        return sum

for i in range(int(input())):
    k = int(input())
    n = int(input())
    print(nk(k,n))

# 풀이 2 - 시간 초과
def nk(k,n):
    if k==0:
        return n
    elif n==1:
        return 1
    else:
        return nk(k,n-1)+nk(k-1,n) # k층 n호는 k층 n-1호와 k-1층 n호의 합과 같음

for i in range(int(input())):
    k = int(input())
    n = int(input())
    print(nk(k,n))

# 풀이 3 - 파스칼의 삼각형 문제였음......
from math import factorial

for i in range(int(input())):
    k = int(input())
    n = int(input())
    print(int(factorial(k+n)/(factorial(n-1)*factorial(k+1))))


# 1978 번
# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

# 풀이 1
cnt=0
N = int(input()) # 숫자 개수 입력
n_list=list(map(int,input().split())) # 주어진 수
if max(n_list) == 1:
    print(0)
else:
    m_list = [i for i in range(2, max(n_list)+1)] # 2 ~ n_list의 최대값까지 리스트 생성
    # m_list의 각 원소의 배수를 m_list에서 제외함
    for i in m_list:
        print(f"#####{i}#####")
        for k in range(2, max(m_list)):
            if i*k in m_list:
                m_list.remove(i*k)
                print(f"{i} * {k} = {i*k} is removed")
print(m_list)
for i in n_list:
    if i in m_list:
        cnt+=1
print(cnt)

# 풀이? - prime number list를 다 만들고 있는지만 체크
N = int(input()) # 숫자 개수 입력
n_list=list(map(int,input().split())) # 주어진 수
cnt=0
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
for i in n_list:
    if i in primenumber:
        cnt+=1
print(cnt)

# 풀이 2 - 입력된 list를 나눠서 맞는지만 먼저 체크
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

N = int(input())
n_list = list(map(int,input().split()))
m_list = []
for i in n_list:
    m_list.append(prime(i))
print(sum(m_list))


# 2581 번
# 문제
# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.
# 입력
# 입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.
# M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.
# 출력
# M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다.
# 단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.

# 풀이 1 - 시간 초과
n=int(input())
m=int(input())
num_list=[i for i in range(1,m+1)]
for i in num_list:
    if i == 1:
        continue
    else:
        for k in range(2, m+1):
            if i*k in num_list:
                num_list.remove(i*k)
for i in range(1,n):
    try:
        num_list.remove(i)
    except:
        continue
print(sum(num_list))
print(min(num_list))

# 풀이 2 - 시간 초과
min_ = int(input())
max_ = int(input())
m_list = [i for i in range(min_, max_+1)] # min ~ max까지 리스트 생성
# m_list의 각 원소의 배수를 m_list에서 제외함
for i in range(2, int(max(m_list)**0.5+1)):
    for k in range(2, max(m_list)+1):
        if i*k in m_list:
            m_list.remove(i*k)
print(sum(m_list))
print(min(m_list))

# 풀이 3 - 소수 판별 함수 사용
def prime(n):
    if n == 1:
        return 0
    else:
        for i in range(2, int(n**0.5 + 1)):
            if n % i == 0:
                n = 0
                break
    return n
min_ = int(input())
max_ = int(input())
m_list = [i for i in range(min_, max_+1)] # min ~ max까지 리스트 생성
M_LIST = list(set(map(prime,m_list))) # map을 이용해서 m_list 원소에 prime 을 적용하고 M_LIST에 반환
if 0 in M_LIST:
    M_LIST.remove(0)
if len(M_LIST) == 0:
    print(-1)
else:
    print(sum(M_LIST))
    print(min(M_LIST))


# 1929 번 - 개선 필요
# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
def prime(n):
    if n == 1:
        return 0
    else:
        for i in range(2, int(n**0.5 + 1)):
            if n % i == 0:
                n = 0
                break
    return n
M, N = map(int,input().split())
M_N = [i for i in range(M, N+1)] # min ~ max까지 리스트 생성
prlist = list(set(map(prime,M_N))) # map을 이용해서 prlist 원소에 prime 을 적용하고 prlist에 반환
if 0 in prlist:
    prlist.remove(0)
prlist.sort()
for i in prlist:
    print(i)


# 25191 번
# 문제
# 치킨 댄스를 추고 있는 곰곰이를 본 임스는 치킨을 먹고 싶어졌다. 임스는 치킨 1마리를 먹을 때 반드시 집에 있는 콜라 2개나 맥주 1개와 같이 먹어야 한다.
# 또한, 치킨집에 있는 치킨의 개수보다 치킨을 많이 시켜먹을 수는 없다.
# 치킨집에 있는 치킨의 개수와 임스의 집에 있는 콜라, 맥주의 개수가 주어졌을 때, 임스가 시켜먹을 수 있는 치킨의 총 개수를 출력하시오.
# 입력
# 첫 번째 줄에는 치킨집에 있는 치킨의 총 개수를 나타내는 정수 N이 주어진다. (1 <= N <= 1000)
# 두 번째 줄에는 임스의 집에 있는 콜라의 개수 A와 맥주의 개수 B가 공백을 사이에 두고 주어진다. (1 <= A, B <= 1000, A, B는 정수)
# 출력
# 임스가 시켜먹을 수 있는 치킨의 총 개수를 출력하시오.

Chicken = int(input())
Cola, Beer = map(int,input().split())
print(min([Chicken, Cola//2 + Beer]))


# 25193 번
# 문제
# 곰곰이는 치킨을 좋아한다. 그러다 보니 매 끼니에 치킨을 먹고 있다. 당신은 곰곰이의 트레이너로서 곰곰이의 식단을 관리해주기로 했다.
# 곰곰이가 N일간 먹어야 할 음식들의 리스트가 주어졌을 때, 리스트의 순서를 원하는 대로 조정하여 곰곰이가 연속으로 치킨을 먹는 날의 최댓값을 가장 작게 만들려고 한다.
# 곰곰이의 건강을 위해 위와 같은 프로그램을 작성해 보자.
# 입력
# 첫 번째 줄에 식단을 정할 일수 N (1 <= N <= 100,000)이 주어진다.
# 두 번째 줄에 음식의 리스트인 길이 N의 문자열 S가 주어진다. 문자열은 영어 대문자로만 이루어져 있다. S_i가 C인 경우, i번째 음식이 치킨이며, 그 외의 경우에는 다른 음식이다.
# 출력
# 곰곰이가 연속으로 치킨을 먹는 날의 최댓값의 최솟값을 구하여라.

N = int(input())
diet_list = list(map(list,input().split()))[0]
C = diet_list.count("C")
O = len(diet_list) - C
if O == 0: # 다른 음식이 없을 때
    print(C)
elif C == 0: # 치킨이 없을 때
    print(0)
else: # 치킨과 다른 음식이 섞여 있을 때
    make = []
    for i in range(1, C//O+1):
        for j in range(i+1):
            if C == i * O + j: # 나눗셈 식을 활용해서 피제수 = 제수 * 몫 + 나머지 방식으로 풀이. 단 나머지가 몫과 같을 수 있음
                make.append(i)
    print(min(make))



# 1003 번
# 문제
# fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.
# fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
# fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
# 두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
# fibonacci(0)은 0을 출력하고, 0을 리턴한다.
# fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
# 첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
# fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
# 1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.
# 각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.

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

# 풀이 2 - 시간 초과
def fibonacci(n):
    if n == 0:
        f_list.append(0) # f_list 0 반환
        return 0
    elif n == 1:
        f_list.append(1) # f_list 1 반환
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(int(input())):
    global f_list # global f_list 선언
    f_list = []
    fibonacci(int(input()))
    print(f_list.count(0), f_list.count(1)) # f_list 내 0, 1 카운트

# 풀이?
fib = [ # 강제로 fibonacci list 를 만들고 뽑아오는 법
    [1, 0],[0, 1],[1, 1],[1, 2],
    [2, 3],[3, 5],[5, 8],[8, 13],
    [13, 21],[21, 34],[34, 55],[55, 89],
    [89, 144],[144, 233],[233, 377],[377, 610],
    [610, 987],[987, 1597],[1597, 2584],[2584, 4181],
    [4181, 6765],[6765, 10946],[10946, 17711],[17711, 28657],
    [28657, 46368],[46368, 75025],[75025, 121393],[121393, 196418],
    [196418, 317811],[317811, 514229],[514229, 832040],[832040, 1346269],
    [1346269, 2178309],[2178309, 3524578],[3524578, 5702887],[5702887, 9227465],
    [9227465, 14930352],[14930352, 24157817],[24157817, 39088169],[39088169, 63245986],
    [63245986, 102334155],[102334155, 165580141]
]

for i in range(int(input())):
    a = fib[int(input())]
    print(a[0], a[1])

# 풀이 3
global fib
fib = [[0,0]] * 101 # 리스트 내에 자리를 먼저 만들어야 대입 가능
fib[0] = [1,0]
fib[1] = [0,1]

def fibonacci(n):
    for i in range(2,n+1):
        a = fib[i-1][0] + fib[i-2][0]
        b = fib[i-1][1] + fib[i-2][1]
        fib[i] = [a,b]
    return fib[n]

for i in range(int(input())):
    result = fibonacci(int(input()))
    print(result[0], result[1])


# 24900 번
# 문제
# 한별이를 출력하는 프로그램을 작성하시오.
# 출력
# 한별이를 아래 예제 출력과 같이 출력한다
print(f"""                                                           :8DDDDDDDDDDDDDD$.                                           
                                                      DDDNNN8~~~~~~~~~~=~7DNNDNDDDNNI                                   
                                                  ?NNDD=~=~~~~~~~~~~~~~~~~~=~~==~=INNDNN7                               
                                               +NDDI~~~~~~~~~~~~~~~~~~~~~~~=~~========~ODND+                            
                                            :NND~~~~~~~~~~~~~~~~~~~~~~~~~~~=~~============7NDN                          
                                          $DD$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=~~==============~DNN                        
                                        $DD=~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=~~=================NND                      
                                       ND7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=~~===================DD7                    
                                     ~DD=~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=======================8DN.                  
                                    8DO~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=========================DD                  
                                   8N~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=~~=======================DN                 
                                  NN::::::::~~~~~~~~~~~=~~~~~~~~~~~~~~~~~~~=~~========================DDO               
                                 $D$:::::::::::::::~~~~DD~~~~~~~~~~~~~~~~~~=~~=========================DN.              
                                 D8:::::::::::::::::::DN=::~~~~~~~~~~~~~~~~=~~======================~~:~DN              
                                DN:::::::::::::::::::ONO::::::::::::::::::::~~~~~~~~~~~~:::::::::::::::::DN             
                               DN::::::::::::::::::::NN.:::::::::::::::::::::::::::DN::::::::::::::::::::$DO            
                               DD:::::::::::::::::::DNI:::::::::::::::::::::::::::::D=::::::::::::::::::::NN            
                              NN~~~~:::::$N?:::::::.NN::::::::::::::::::::::::::::::ND.:::::::::::::::::::+N8           
                              N7~~~~~~~~OD7::::::::~DD::::::::::::::::::::::::::::::~D$::::::::::::::::::::DN           
                             NN~~~~~~~~IDZ~~~~~::::DN~:::::::::::::::::::::::::::::::DN::::::::::::::::::::=N~          
                             DD~~~~~~~~NN~~~~~~~~~=NN::::::::::::::::::::::::::::::::DN:::::::::::::::~~====NN          
                            8D~~~~~~~~ND~~~~~~~~~~~ND~~~~~~~~:::::::::::::::::::::::::N7:::~~===============NN          
                            DD~~~~~~~ON+~~~~~~~~~~~ND~~~~~~~~~~~~~~~~~~~=+NZ==========NN====================~ND         
               :DD7   DNDD. N8~~~~~~~NN~~~~~~~~~~DDND~~~~~~~~~~~~~~~~~~~~ND~~=========DD=====================ND         
               N~:DDNNN .8NDN~~~~~~~$D=~~~~~~~~+ND.DD~~~~~~~~~~~~~~~~~~~=DD~~=========~D+====================DN         
              :D     .  ..~ND~~~~~~~NN~~~~~~~+NN$..ND~~~~~~~~~~~~~~~~~~~7N=~~=========~ND=======~============ON         
              NN       ...:N?~~~~~~~N=~~~~~NNNI.. .7D+~~~~~~~~~~~~~~~~~=8NN~~==========NN=======N============$N         
         N  ODN       ....DN~~~~~~~DD=8NNND$..     .DD~~~=~~~~~~~~~~~~~=NNDD=~=========8D~======NN===========~N$        
    N? =NN  ND      .....NND~~~~~~~DDNN:...        .ND=~DNN~~~~~~~~~~~~=DN.DN~=========?N+======NN============ND        
   $D? DN    DZ    ....ND8NN~~~~~~$D                .DD~NNDD~~~~~~~~~~~~D8..DN=========~DN======NN============DN        
   DN ~N~   NN    ..:~NN..NZ~~~~~~DN                  NNN8.ND~~~~NDN?~~~DZ...7DD=======~NN======NN============DN        
   ND DD    :DN.  ..ND$  .N?~~~~~=NNN                   . ..DDD$~N8OND8=N+   ..DDDZ~====NN======+D+===========ND        
   NO         DD  ZDN    8NO~~~~~~NNN..DDDNN7               ...NND...:DDD:     .:.NDND=~DD======~DO===========DN        
              DNDDN:.    DN~~~~~~=NNNN.ODNNNNDDNNO              ...     .         ...DNNNN=======ND===========DD        
       INDN7    DD.     .DD~~~~~=IDND:.:~.....?DNDNN.                        ...... ....$D=======ND===========ND        
       NN        ND.    8N=~~~~$ND::.:=~:.~=......=ND~                 .NNNNNNNNNNNNNNN.~N+======NN===========DN        
       $DD        DN:   DD~~~~7NO...~==.:~~:.....                      NNNND? ..::..7NZ.:N?======8D~==========ZN        
       DN?     ~D: DND.?D~~~~~DD....~:.~=~.......                            ....~=:.:~..ND======~N$==========~DO       
       ND    ..DD.  .DNDN=~~~~DI.......:.........                           ....=~..~~~..DN======~DD===========NN       
       DDD  :.:DD.  . DDI~~~~~ND................        .DNNNNNNNNNN7      ....=~:.:~~...NN=======ND===========?D~      
       8D. ...OD..    DD~~~~~~+ND ............          NN:~::::~~~8N      ........~~...:ND=======DN============NN      
       DDI:...ND     .D7~~~~~~~7NN ..........           ID8::::::::8D      .............:DN=======ON============NN      
        ~NNND.N=.   .NN~~~~~~~~~NDN8                       ~::::::~N8       .............DN========D=============NI     
               DDNNN.ND~~~~~~~~DD =DND                                       ............DN========N+~===========NN     
                   ~:N=~~~~~~~~DD   .DDDD                                       ........ NN========DD============8D     
                    8N~~~~~~~~~ND    . .7NDDD? .                                      .8DDN========NN=============D:    
                    DD~~~~~~~~~DND:         IDNNND$.                           .+DNNNNDNIDN========DD=============DD    
                    ND~~~~~~~~ZN 7DD .. .:DDNDDNNDNNNNDDNDND8$?===+$8DDNNNDDDDDN8I~DN====8N========NN=============NN    
                    DD~~~~~~~~8N   DD.  .NN~~~~.~~=DNDNO.:7ODDDDNNDD8DDDND=~~~ =~~~ON====8N========DN=============DN    
                    ND~~~~~~~~DN    ZDD  DN~~~ ~~~~~=.7DDD+.......8NNN==~~~~~ ~~~~~ONN$==DN========8N=============ON    
                    ND~8N~=~~~ZN      DDODN=~.~~~~~=.~~~~INDNNNNDNN~~~~~~~~:~~~~~~~DN~ND=DN========DD=========~ND=8N    
                    IN=NDDI~~~~D8       DNN::~~~~~.~~~~~=.~~ND~~ND~~~~~~~~.~~~~~~~~NN  NDNN====ND==ND~D?======DNN=ND    
                     DNNI8ND=~~DN:       ZN=~~~~~ ~~~~~.~~~~DD~=DD~~~~~~~ ~~~~~~~=.ND. . ND===DNDD=NDDNN=====8NZDDDN    
                      NND  IDNDNNN+       D+~~~:~~~~~~ ~~~~~DDNNN+~~~~~~~~~~~~~~:=?N7   .ND=~ND  DNNN~ID====ND7 NNN     
                       ID                 ND~~ ~~~~~:.~~~7DDN7IDNN==~~ ~~~~~~~~ ~~DN   .:N?DDDDD NND  8N~=DDD  ZNN      
                                          NN~:~~~~~ =7DDDD+8N  :N8DDZ.~~~~~~~~.~~~DD.   NDD+ . DN=     OND+             
                                          DND~~~=8DNDDZ=~~ ND   NN~INND~~~~~.~~~~ND .    .    ..IDD                     
                                         DDNNNDNNN+~~~~~~.7N.    ND~~~NDDI~ ~~~~=NNN             .DDI                   
                                        DN=~~~~.=~~~~~~ ~~DN     +N+~~~~+DNDD~~~NNNND.            ..ND                  
                                         DDI~~ ~~~~~~~ ~~~ND..  ..ND~~~~:~~~DNDNNNN+            ..7O8ND+                
                                          .DND=~~~~=::~~=NN.   . . 8D~~.~~~~~~=DN$ODNDNDNNNDNNNNND8+~..                 
                                             8DNNI=.~~~~=NDDNNNNDDNDNN.~~~~~IDDNDND7:.                                  
                                                ?DNNDD?~DD          ~NN~~=NDD$                                          
                                                     :DDD.            NNNN=                                           """)


# 24901 번
# 문제
# 이진수 게임은 술자리 게임으로, 순서대로 돌아가면서 이진수의 각 자리수를 말하는 게임이다.
# 첫 번째 사람이 0의 이진수 표현인 0을 말하고, 다음 사람은 1의 이진수 표현인 1을 말한다.
# 그 다음 사람은 2의 이진수 표현인 10의 첫 번째 자리를 말하고, 그 다음 사람이 두 번째 자리인 0을 말하는 식이다.
# 즉, 순서대로 말하는 숫자를 나열하면 0-1-1-0-1-1-1-0-0-... 이다.
# 정수가 입력되면 그 값까지의 이진수 게임 수열을 출력하는 프로그램을 작성하시오.
# 입력
# 정수 n이 입력된다. 이때 0 ≤ n ≤ 10이다.
# 출력
# 0부터 n까지의 이진수 게임 수열을 출력한다.
n = int(input())+1
binary_all = []
for i in range(n):
    binary=["0"]*4
    if i == 0:
        binary_all.append("0")
    else:
        if i//8 == 1:
            binary[0] = "1"
            i%=8
        if i//4 == 1:
            binary[1] = "1"
            i%=4
        if i//2 == 1:
            binary[2] = "1"
            i%=2
        binary[3] = str(i)
        while binary[0] == "0":
            binary.remove("0")
        binary_all.append("".join(binary))
print("".join(binary_all))




# 2558 번
# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 A, 둘째 줄에 B가 주어진다. (0 < A, B < 10)
# 출력
# 첫째 줄에 A+B를 출력한다.

A = int(input())
B = int(input())
print(A+B)


# 10039 번
# 문제
# 상현이가 가르치는 아이폰 앱 개발 수업의 수강생은 원섭, 세희, 상근, 숭, 강수이다.
# 어제 이 수업의 기말고사가 있었고, 상현이는 지금 학생들의 기말고사 시험지를 채점하고 있다.
# 기말고사 점수가 40점 이상인 학생들은 그 점수 그대로 자신의 성적이 된다.
# 하지만, 40점 미만인 학생들은 보충학습을 듣는 조건을 수락하면 40점을 받게 된다.
# 보충학습은 거부할 수 없기 때문에, 40점 미만인 학생들은 항상 40점을 받게 된다.
# 학생 5명의 점수가 주어졌을 때, 평균 점수를 구하는 프로그램을 작성하시오.
# 입력
# 입력은 총 5줄로 이루어져 있고, 원섭이의 점수, 세희의 점수, 상근이의 점수, 숭이의 점수, 강수의 점수가 순서대로 주어진다.
# 점수는 모두 0점 이상, 100점 이하인 5의 배수이다. 따라서, 평균 점수는 항상 정수이다.
# 출력
# 첫째 줄에 학생 5명의 평균 점수를 출력한다.

score = [0]*5
for _ in range(5):
    n = int(input())
    if n<40:
        n = 40
    score[_] = n
print(int(sum(score)/5))


# 2748 번
# 문제
# 피보나치 수는 0과 1로 시작한다.
# 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다.
# 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
# 이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.
# n=17일때 까지 피보나치 수를 써보면 다음과 같다.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 n이 주어진다. n은 90보다 작거나 같은 자연수이다.
# 출력
# 첫째 줄에 n번째 피보나치 수를 출력한다.

n = int(input())
if n in [0, 1]:
    print(n)
else:
    fib = [0]*(n+1)
    fib[0], fib[1] = 0, 1
    for i in range(2,n+1):
        fib[i] = fib[i-1] + fib[i-2]
    print(fib[i])


# 2475 번
# 문제
# 컴퓨터를 제조하는 회사인 KOI 전자에서는 제조하는 컴퓨터마다 6자리의 고유번호를 매긴다.
# 고유번호의 처음 5자리에는 00000부터 99999까지의 수 중 하나가 주어지며 6번째 자리에는 검증수가 들어간다.
# 검증수는 고유번호의 처음 5자리에 들어가는 5개의 숫자를 각각 제곱한 수의 합을 10으로 나눈 나머지이다.
# 예를 들어 고유번호의 처음 5자리의 숫자들이 04256이면,
# 각 숫자를 제곱한 수들의 합 0+16+4+25+36 = 81 을 10으로 나눈 나머지인 1이 검증수이다.
# 입력
# 첫째 줄에 고유번호의 처음 5자리의 숫자들이 빈칸을 사이에 두고 하나씩 주어진다.
# 출력
# 첫째 줄에 검증수를 출력한다.
a = list(map(int,input().split()))
sum = 0
for i in a:
    sum+=i**2
print(sum%10)


# 9461 번
# 문제
# 오른쪽 그림과 같이 삼각형이 나선 모양으로 놓여져 있다.
# 첫 삼각형은 정삼각형으로 변의 길이는 1이다.
# 그 다음에는 다음과 같은 과정으로 정삼각형을 계속 추가한다.
# 나선에서 가장 긴 변의 길이를 k라 했을 때, 그 변에 길이가 k인 정삼각형을 추가한다.
# 파도반 수열 P(N)은 나선에 있는 정삼각형의 변의 길이이다.
# P(1)부터 P(10)까지 첫 10개 숫자는 1, 1, 1, 2, 2, 3, 4, 5, 7, 9이다.
# N이 주어졌을 때, P(N)을 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. (1 ≤ N ≤ 100)
# 출력
# 각 테스트 케이스마다 P(N)을 출력한다.

for _ in range(int(input())):
    wave=[0]*100
    wave[0:2]=[1,1,1]
    n = int(input())
    if n in [1, 2, 3]:
        print(1)
    else:
        for i in range(4,n+1):
            wave[i-1] = wave[i-3]+wave[i-4]
        print(wave[n-1])


# 10953 번
# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다.
# A와 B는 콤마(,)로 구분되어 있다. (0 < A, B < 10)
# 출력
# 각 테스트 케이스마다 A+B를 출력한다.

for _ in range(int(input())):
    a, b = map(int,input().split(","))
    print(a+b)


# 2163 번
# 문제
# 정화는 N×M 크기의 초콜릿을 하나 가지고 있다.
# 초콜릿은 금이 가 있는 모양을 하고 있으며, 그 금에 의해 N×M개의 조각으로 나눠질 수 있다.
# 초콜릿의 크기가 너무 크다고 생각한 그녀는 초콜릿을 친구들과 나눠 먹기로 했다.
# 이를 위해서 정화는 초콜릿을 계속 쪼개서 총 N×M개의 조각으로 쪼개려고 한다.
# 초콜릿을 쪼갤 때에는 초콜릿 조각을 하나 들고, 적당한 위치에서 초콜릿을 쪼갠다.
# 초콜릿을 쪼갤 때에는 금이 가 있는 위치에서만 쪼갤 수 있다.
# 이와 같이 초콜릿을 쪼개면 초콜릿은 두 개의 조각으로 나눠지게 된다.
# 이제 다시 이 중에서 초콜릿 조각을 하나 들고, 쪼개는 과정을 반복하면 된다.
# 초콜릿을 쪼개다보면 초콜릿이 녹을 수 있기 때문에, 정화는 가급적이면 초콜릿을 쪼개는 횟수를 최소로 하려 한다.
# 초콜릿의 크기가 주어졌을 때, 이를 1×1 크기의 초콜릿으로 쪼개기 위한 최소 쪼개기 횟수를 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 두 정수 N, M(1 ≤ N, M ≤ 300)이 주어진다.
# 출력
# 첫째 줄에 답을 출력한다.

a, b = map(int,input().split())
print(a*b-1)


# 2217 번
# 문제
# N(1 ≤ N ≤ 100,000)개의 로프가 있다.
# 이 로프를 이용하여 이런 저런 물체를 들어올릴 수 있다.
# 각각의 로프는 그 굵기나 길이가 다르기 때문에 들 수 있는 물체의 중량이 서로 다를 수도 있다.
# 하지만 여러 개의 로프를 병렬로 연결하면 각각의 로프에 걸리는 중량을 나눌 수 있다.
# k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.
# 각 로프들에 대한 정보가 주어졌을 때,
# 이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구해내는 프로그램을 작성하시오.
# 모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다.
# 입력
# 첫째 줄에 정수 N이 주어진다. 다
# 음 N개의 줄에는 각 로프가 버틸 수 있는 최대 중량이 주어진다.
# 이 값은 10,000을 넘지 않는 자연수이다.
# 출력
# 첫째 줄에 답을 출력한다.

# 풀이 1 - 시간초과, 각 로프의 데이터를 받고, 버틸 수 있는 하중 * 로프 개수 의 리스트에서 최대값 출력
from sys import stdin
# input = stdin.readline
n = int(input())
rope = [0] * n
weight = [0] * n
for _ in range(n):
    rope[_] = int(input())
for i in range(n):
    weight[i] = len(rope)*min(rope)
    rope.remove(min(rope))
print(max(weight))

# 풀이 2 - 각 로프의 데이터를 받고 역순으로 나열. 하중 최대값을 비교하여 마지막 값 출력
from sys import stdin
# input = stdin.readline
n = int(input())
rope = [0] * n
for _ in range(n):
    rope[_] = int(input())
rope.sort()
rope.reverse()
a = rope[0]
for i in range(1,n):
    a = max(a, (i + 1) * rope[i])
print(a)


# 9987 번
# 문제
# 입력으로 포켓몬의 번호가 주어졌을 때, 그 포켓몬의 이름과 타입을 출력하는 프로그램을 작성하시오.
# 입력
# 입력으로 포켓몬의 번호가 주어진다. 포켓몬의 번호는 718을 넘지 않는 자연수이다.
# 출력
# 첫째 줄에 포켓몬의 이름을 출력한다. 둘째 줄에는 포켓몬의 타입을 공백으로 구분하여 출력한다.
# http://web.archive.org/web/20140301191716/http://pokemondb.net/pokedex/national

# pokemon index 만들기
import requests
from bs4 import BeautifulSoup as bs

url = "http://web.archive.org/web/20140301191716/http://pokemondb.net/pokedex/national"
result =requests.get(url)
soup = bs(result.text, 'html.parser')
pokemons = soup.find_all("span", {"class":"infocard-tall"})
pokemon = []
for i in pokemons:
    number = i.find("small")
    number = number.text
    name = i.find("a", {"class": "ent-name"})
    name = name.text
    type_ = i.find_all("a", {"class": "itype"})
    type__ = []
    for j in type_:
        type__.append(j.text)
    type__
    type = " ".join(type__)
    poke = {
        "number": number,
        "name": name,
        "type": type
    }
    pokemon.append(poke)
print(pokemon)

# 실행 코드
pokemon = [
    {'number': '#001', 'name': 'Bulbasaur', 'type': 'Grass Poison'},
    {'number': '#002', 'name': 'Ivysaur', 'type': 'Grass Poison'},
    {'number': '#003', 'name': 'Venusaur', 'type': 'Grass Poison'},
    {'number': '#004', 'name': 'Charmander', 'type': 'Fire'},
    {'number': '#005', 'name': 'Charmeleon', 'type': 'Fire'},
    {'number': '#006', 'name': 'Charizard', 'type': 'Fire Flying'},
    {'number': '#007', 'name': 'Squirtle', 'type': 'Water'},
    {'number': '#008', 'name': 'Wartortle', 'type': 'Water'},
    {'number': '#009', 'name': 'Blastoise', 'type': 'Water'},
    {'number': '#010', 'name': 'Caterpie', 'type': 'Bug'},
    {'number': '#011', 'name': 'Metapod', 'type': 'Bug'},
    {'number': '#012', 'name': 'Butterfree', 'type': 'Bug Flying'},
    {'number': '#013', 'name': 'Weedle', 'type': 'Bug Poison'},
    {'number': '#014', 'name': 'Kakuna', 'type': 'Bug Poison'},
    {'number': '#015', 'name': 'Beedrill', 'type': 'Bug Poison'},
    {'number': '#016', 'name': 'Pidgey', 'type': 'Normal Flying'},
    {'number': '#017', 'name': 'Pidgeotto', 'type': 'Normal Flying'},
    {'number': '#018', 'name': 'Pidgeot', 'type': 'Normal Flying'},
    {'number': '#019', 'name': 'Rattata', 'type': 'Normal'},
    {'number': '#020', 'name': 'Raticate', 'type': 'Normal'},
    {'number': '#021', 'name': 'Spearow', 'type': 'Normal Flying'},
    {'number': '#022', 'name': 'Fearow', 'type': 'Normal Flying'},
    {'number': '#023', 'name': 'Ekans', 'type': 'Poison'},
    {'number': '#024', 'name': 'Arbok', 'type': 'Poison'},
    {'number': '#025', 'name': 'Pikachu', 'type': 'Electric'},
    {'number': '#026', 'name': 'Raichu', 'type': 'Electric'},
    {'number': '#027', 'name': 'Sandshrew', 'type': 'Ground'},
    {'number': '#028', 'name': 'Sandslash', 'type': 'Ground'},
    {'number': '#029', 'name': 'Nidoran♀', 'type': 'Poison'},
    {'number': '#030', 'name': 'Nidorina', 'type': 'Poison'},
    {'number': '#031', 'name': 'Nidoqueen', 'type': 'Poison Ground'},
    {'number': '#032', 'name': 'Nidoran♂', 'type': 'Poison'},
    {'number': '#033', 'name': 'Nidorino', 'type': 'Poison'},
    {'number': '#034', 'name': 'Nidoking', 'type': 'Poison Ground'},
    {'number': '#035', 'name': 'Clefairy', 'type': 'Fairy'},
    {'number': '#036', 'name': 'Clefable', 'type': 'Fairy'},
    {'number': '#037', 'name': 'Vulpix', 'type': 'Fire'},
    {'number': '#038', 'name': 'Ninetales', 'type': 'Fire'},
    {'number': '#039', 'name': 'Jigglypuff', 'type': 'Normal Fairy'},
    {'number': '#040', 'name': 'Wigglytuff', 'type': 'Normal Fairy'},
    {'number': '#041', 'name': 'Zubat', 'type': 'Poison Flying'},
    {'number': '#042', 'name': 'Golbat', 'type': 'Poison Flying'},
    {'number': '#043', 'name': 'Oddish', 'type': 'Grass Poison'},
    {'number': '#044', 'name': 'Gloom', 'type': 'Grass Poison'},
    {'number': '#045', 'name': 'Vileplume', 'type': 'Grass Poison'},
    {'number': '#046', 'name': 'Paras', 'type': 'Bug Grass'},
    {'number': '#047', 'name': 'Parasect', 'type': 'Bug Grass'},
    {'number': '#048', 'name': 'Venonat', 'type': 'Bug Poison'},
    {'number': '#049', 'name': 'Venomoth', 'type': 'Bug Poison'},
    {'number': '#050', 'name': 'Diglett', 'type': 'Ground'},
    {'number': '#051', 'name': 'Dugtrio', 'type': 'Ground'},
    {'number': '#052', 'name': 'Meowth', 'type': 'Normal'},
    {'number': '#053', 'name': 'Persian', 'type': 'Normal'},
    {'number': '#054', 'name': 'Psyduck', 'type': 'Water'},
    {'number': '#055', 'name': 'Golduck', 'type': 'Water'},
    {'number': '#056', 'name': 'Mankey', 'type': 'Fighting'},
    {'number': '#057', 'name': 'Primeape', 'type': 'Fighting'},
    {'number': '#058', 'name': 'Growlithe', 'type': 'Fire'},
    {'number': '#059', 'name': 'Arcanine', 'type': 'Fire'},
    {'number': '#060', 'name': 'Poliwag', 'type': 'Water'},
    {'number': '#061', 'name': 'Poliwhirl', 'type': 'Water'},
    {'number': '#062', 'name': 'Poliwrath', 'type': 'Water Fighting'},
    {'number': '#063', 'name': 'Abra', 'type': 'Psychic'},
    {'number': '#064', 'name': 'Kadabra', 'type': 'Psychic'},
    {'number': '#065', 'name': 'Alakazam', 'type': 'Psychic'},
    {'number': '#066', 'name': 'Machop', 'type': 'Fighting'},
    {'number': '#067', 'name': 'Machoke', 'type': 'Fighting'},
    {'number': '#068', 'name': 'Machamp', 'type': 'Fighting'},
    {'number': '#069', 'name': 'Bellsprout', 'type': 'Grass Poison'},
    {'number': '#070', 'name': 'Weepinbell', 'type': 'Grass Poison'},
    {'number': '#071', 'name': 'Victreebel', 'type': 'Grass Poison'},
    {'number': '#072', 'name': 'Tentacool', 'type': 'Water Poison'},
    {'number': '#073', 'name': 'Tentacruel', 'type': 'Water Poison'},
    {'number': '#074', 'name': 'Geodude', 'type': 'Rock Ground'},
    {'number': '#075', 'name': 'Graveler', 'type': 'Rock Ground'},
    {'number': '#076', 'name': 'Golem', 'type': 'Rock Ground'},
    {'number': '#077', 'name': 'Ponyta', 'type': 'Fire'},
    {'number': '#078', 'name': 'Rapidash', 'type': 'Fire'},
    {'number': '#079', 'name': 'Slowpoke', 'type': 'Water Psychic'},
    {'number': '#080', 'name': 'Slowbro', 'type': 'Water Psychic'},
    {'number': '#081', 'name': 'Magnemite', 'type': 'Electric Steel'},
    {'number': '#082', 'name': 'Magneton', 'type': 'Electric Steel'},
    {'number': '#083', 'name': "Farfetch'd", 'type': 'Normal Flying'},
    {'number': '#084', 'name': 'Doduo', 'type': 'Normal Flying'},
    {'number': '#085', 'name': 'Dodrio', 'type': 'Normal Flying'},
    {'number': '#086', 'name': 'Seel', 'type': 'Water'},
    {'number': '#087', 'name': 'Dewgong', 'type': 'Water Ice'},
    {'number': '#088', 'name': 'Grimer', 'type': 'Poison'},
    {'number': '#089', 'name': 'Muk', 'type': 'Poison'},
    {'number': '#090', 'name': 'Shellder', 'type': 'Water'},
    {'number': '#091', 'name': 'Cloyster', 'type': 'Water Ice'},
    {'number': '#092', 'name': 'Gastly', 'type': 'Ghost Poison'},
    {'number': '#093', 'name': 'Haunter', 'type': 'Ghost Poison'},
    {'number': '#094', 'name': 'Gengar', 'type': 'Ghost Poison'},
    {'number': '#095', 'name': 'Onix', 'type': 'Rock Ground'},
    {'number': '#096', 'name': 'Drowzee', 'type': 'Psychic'},
    {'number': '#097', 'name': 'Hypno', 'type': 'Psychic'},
    {'number': '#098', 'name': 'Krabby', 'type': 'Water'},
    {'number': '#099', 'name': 'Kingler', 'type': 'Water'},
    {'number': '#100', 'name': 'Voltorb', 'type': 'Electric'},
    {'number': '#101', 'name': 'Electrode', 'type': 'Electric'},
    {'number': '#102', 'name': 'Exeggcute', 'type': 'Grass Psychic'},
    {'number': '#103', 'name': 'Exeggutor', 'type': 'Grass Psychic'},
    {'number': '#104', 'name': 'Cubone', 'type': 'Ground'},
    {'number': '#105', 'name': 'Marowak', 'type': 'Ground'},
    {'number': '#106', 'name': 'Hitmonlee', 'type': 'Fighting'},
    {'number': '#107', 'name': 'Hitmonchan', 'type': 'Fighting'},
    {'number': '#108', 'name': 'Lickitung', 'type': 'Normal'},
    {'number': '#109', 'name': 'Koffing', 'type': 'Poison'},
    {'number': '#110', 'name': 'Weezing', 'type': 'Poison'},
    {'number': '#111', 'name': 'Rhyhorn', 'type': 'Ground Rock'},
    {'number': '#112', 'name': 'Rhydon', 'type': 'Ground Rock'},
    {'number': '#113', 'name': 'Chansey', 'type': 'Normal'},
    {'number': '#114', 'name': 'Tangela', 'type': 'Grass'},
    {'number': '#115', 'name': 'Kangaskhan', 'type': 'Normal'},
    {'number': '#116', 'name': 'Horsea', 'type': 'Water'},
    {'number': '#117', 'name': 'Seadra', 'type': 'Water'},
    {'number': '#118', 'name': 'Goldeen', 'type': 'Water'},
    {'number': '#119', 'name': 'Seaking', 'type': 'Water'},
    {'number': '#120', 'name': 'Staryu', 'type': 'Water'},
    {'number': '#121', 'name': 'Starmie', 'type': 'Water Psychic'},
    {'number': '#122', 'name': 'Mr. Mime', 'type': 'Psychic Fairy'},
    {'number': '#123', 'name': 'Scyther', 'type': 'Bug Flying'},
    {'number': '#124', 'name': 'Jynx', 'type': 'Ice Psychic'},
    {'number': '#125', 'name': 'Electabuzz', 'type': 'Electric'},
    {'number': '#126', 'name': 'Magmar', 'type': 'Fire'},
    {'number': '#127', 'name': 'Pinsir', 'type': 'Bug'},
    {'number': '#128', 'name': 'Tauros', 'type': 'Normal'},
    {'number': '#129', 'name': 'Magikarp', 'type': 'Water'},
    {'number': '#130', 'name': 'Gyarados', 'type': 'Water Flying'},
    {'number': '#131', 'name': 'Lapras', 'type': 'Water Ice'},
    {'number': '#132', 'name': 'Ditto', 'type': 'Normal'},
    {'number': '#133', 'name': 'Eevee', 'type': 'Normal'},
    {'number': '#134', 'name': 'Vaporeon', 'type': 'Water'},
    {'number': '#135', 'name': 'Jolteon', 'type': 'Electric'},
    {'number': '#136', 'name': 'Flareon', 'type': 'Fire'},
    {'number': '#137', 'name': 'Porygon', 'type': 'Normal'},
    {'number': '#138', 'name': 'Omanyte', 'type': 'Rock Water'},
    {'number': '#139', 'name': 'Omastar', 'type': 'Rock Water'},
    {'number': '#140', 'name': 'Kabuto', 'type': 'Rock Water'},
    {'number': '#141', 'name': 'Kabutops', 'type': 'Rock Water'},
    {'number': '#142', 'name': 'Aerodactyl', 'type': 'Rock Flying'},
    {'number': '#143', 'name': 'Snorlax', 'type': 'Normal'},
    {'number': '#144', 'name': 'Articuno', 'type': 'Ice Flying'},
    {'number': '#145', 'name': 'Zapdos', 'type': 'Electric Flying'},
    {'number': '#146', 'name': 'Moltres', 'type': 'Fire Flying'},
    {'number': '#147', 'name': 'Dratini', 'type': 'Dragon'},
    {'number': '#148', 'name': 'Dragonair', 'type': 'Dragon'},
    {'number': '#149', 'name': 'Dragonite', 'type': 'Dragon Flying'},
    {'number': '#150', 'name': 'Mewtwo', 'type': 'Psychic'},
    {'number': '#151', 'name': 'Mew', 'type': 'Psychic'},
    {'number': '#152', 'name': 'Chikorita', 'type': 'Grass'},
    {'number': '#153', 'name': 'Bayleef', 'type': 'Grass'},
    {'number': '#154', 'name': 'Meganium', 'type': 'Grass'},
    {'number': '#155', 'name': 'Cyndaquil', 'type': 'Fire'},
    {'number': '#156', 'name': 'Quilava', 'type': 'Fire'},
    {'number': '#157', 'name': 'Typhlosion', 'type': 'Fire'},
    {'number': '#158', 'name': 'Totodile', 'type': 'Water'},
    {'number': '#159', 'name': 'Croconaw', 'type': 'Water'},
    {'number': '#160', 'name': 'Feraligatr', 'type': 'Water'},
    {'number': '#161', 'name': 'Sentret', 'type': 'Normal'},
    {'number': '#162', 'name': 'Furret', 'type': 'Normal'},
    {'number': '#163', 'name': 'Hoothoot', 'type': 'Normal Flying'},
    {'number': '#164', 'name': 'Noctowl', 'type': 'Normal Flying'},
    {'number': '#165', 'name': 'Ledyba', 'type': 'Bug Flying'},
    {'number': '#166', 'name': 'Ledian', 'type': 'Bug Flying'},
    {'number': '#167', 'name': 'Spinarak', 'type': 'Bug Poison'},
    {'number': '#168', 'name': 'Ariados', 'type': 'Bug Poison'},
    {'number': '#169', 'name': 'Crobat', 'type': 'Poison Flying'},
    {'number': '#170', 'name': 'Chinchou', 'type': 'Water Electric'},
    {'number': '#171', 'name': 'Lanturn', 'type': 'Water Electric'},
    {'number': '#172', 'name': 'Pichu', 'type': 'Electric'},
    {'number': '#173', 'name': 'Cleffa', 'type': 'Fairy'},
    {'number': '#174', 'name': 'Igglybuff', 'type': 'Normal Fairy'},
    {'number': '#175', 'name': 'Togepi', 'type': 'Fairy'},
    {'number': '#176', 'name': 'Togetic', 'type': 'Fairy Flying'},
    {'number': '#177', 'name': 'Natu', 'type': 'Psychic Flying'},
    {'number': '#178', 'name': 'Xatu', 'type': 'Psychic Flying'},
    {'number': '#179', 'name': 'Mareep', 'type': 'Electric'},
    {'number': '#180', 'name': 'Flaaffy', 'type': 'Electric'},
    {'number': '#181', 'name': 'Ampharos', 'type': 'Electric'},
    {'number': '#182', 'name': 'Bellossom', 'type': 'Grass'},
    {'number': '#183', 'name': 'Marill', 'type': 'Water Fairy'},
    {'number': '#184', 'name': 'Azumarill', 'type': 'Water Fairy'},
    {'number': '#185', 'name': 'Sudowoodo', 'type': 'Rock'},
    {'number': '#186', 'name': 'Politoed', 'type': 'Water'},
    {'number': '#187', 'name': 'Hoppip', 'type': 'Grass Flying'},
    {'number': '#188', 'name': 'Skiploom', 'type': 'Grass Flying'},
    {'number': '#189', 'name': 'Jumpluff', 'type': 'Grass Flying'},
    {'number': '#190', 'name': 'Aipom', 'type': 'Normal'},
    {'number': '#191', 'name': 'Sunkern', 'type': 'Grass'},
    {'number': '#192', 'name': 'Sunflora', 'type': 'Grass'},
    {'number': '#193', 'name': 'Yanma', 'type': 'Bug Flying'},
    {'number': '#194', 'name': 'Wooper', 'type': 'Water Ground'},
    {'number': '#195', 'name': 'Quagsire', 'type': 'Water Ground'},
    {'number': '#196', 'name': 'Espeon', 'type': 'Psychic'},
    {'number': '#197', 'name': 'Umbreon', 'type': 'Dark'},
    {'number': '#198', 'name': 'Murkrow', 'type': 'Dark Flying'},
    {'number': '#199', 'name': 'Slowking', 'type': 'Water Psychic'},
    {'number': '#200', 'name': 'Misdreavus', 'type': 'Ghost'},
    {'number': '#201', 'name': 'Unown', 'type': 'Psychic'},
    {'number': '#202', 'name': 'Wobbuffet', 'type': 'Psychic'},
    {'number': '#203', 'name': 'Girafarig', 'type': 'Normal Psychic'},
    {'number': '#204', 'name': 'Pineco', 'type': 'Bug'},
    {'number': '#205', 'name': 'Forretress', 'type': 'Bug Steel'},
    {'number': '#206', 'name': 'Dunsparce', 'type': 'Normal'},
    {'number': '#207', 'name': 'Gligar', 'type': 'Ground Flying'},
    {'number': '#208', 'name': 'Steelix', 'type': 'Steel Ground'},
    {'number': '#209', 'name': 'Snubbull', 'type': 'Fairy'},
    {'number': '#210', 'name': 'Granbull', 'type': 'Fairy'},
    {'number': '#211', 'name': 'Qwilfish', 'type': 'Water Poison'},
    {'number': '#212', 'name': 'Scizor', 'type': 'Bug Steel'},
    {'number': '#213', 'name': 'Shuckle', 'type': 'Bug Rock'},
    {'number': '#214', 'name': 'Heracross', 'type': 'Bug Fighting'},
    {'number': '#215', 'name': 'Sneasel', 'type': 'Dark Ice'},
    {'number': '#216', 'name': 'Teddiursa', 'type': 'Normal'},
    {'number': '#217', 'name': 'Ursaring', 'type': 'Normal'},
    {'number': '#218', 'name': 'Slugma', 'type': 'Fire'},
    {'number': '#219', 'name': 'Magcargo', 'type': 'Fire Rock'},
    {'number': '#220', 'name': 'Swinub', 'type': 'Ice Ground'},
    {'number': '#221', 'name': 'Piloswine', 'type': 'Ice Ground'},
    {'number': '#222', 'name': 'Corsola', 'type': 'Water Rock'},
    {'number': '#223', 'name': 'Remoraid', 'type': 'Water'},
    {'number': '#224', 'name': 'Octillery', 'type': 'Water'},
    {'number': '#225', 'name': 'Delibird', 'type': 'Ice Flying'},
    {'number': '#226', 'name': 'Mantine', 'type': 'Water Flying'},
    {'number': '#227', 'name': 'Skarmory', 'type': 'Steel Flying'},
    {'number': '#228', 'name': 'Houndour', 'type': 'Dark Fire'},
    {'number': '#229', 'name': 'Houndoom', 'type': 'Dark Fire'},
    {'number': '#230', 'name': 'Kingdra', 'type': 'Water Dragon'},
    {'number': '#231', 'name': 'Phanpy', 'type': 'Ground'},
{'number': '#232', 'name': 'Donphan', 'type': 'Ground'},
    {'number': '#233', 'name': 'Porygon2', 'type': 'Normal'},
{'number': '#234', 'name': 'Stantler', 'type': 'Normal'},
    {'number': '#235', 'name': 'Smeargle', 'type': 'Normal'},
{'number': '#236', 'name': 'Tyrogue', 'type': 'Fighting'},
    {'number': '#237', 'name': 'Hitmontop', 'type': 'Fighting'},
    {'number': '#238', 'name': 'Smoochum', 'type': 'Ice Psychic'},
    {'number': '#239', 'name': 'Elekid', 'type': 'Electric'},
{'number': '#240', 'name': 'Magby', 'type': 'Fire'},
    {'number': '#241', 'name': 'Miltank', 'type': 'Normal'},
{'number': '#242', 'name': 'Blissey', 'type': 'Normal'},
    {'number': '#243', 'name': 'Raikou', 'type': 'Electric'},
{'number': '#244', 'name': 'Entei', 'type': 'Fire'},
    {'number': '#245', 'name': 'Suicune', 'type': 'Water'},
    {'number': '#246', 'name': 'Larvitar', 'type': 'Rock Ground'},
    {'number': '#247', 'name': 'Pupitar', 'type': 'Rock Ground'},
    {'number': '#248', 'name': 'Tyranitar', 'type': 'Rock Dark'},
    {'number': '#249', 'name': 'Lugia', 'type': 'Psychic Flying'},
    {'number': '#250', 'name': 'Ho-oh', 'type': 'Fire Flying'},
    {'number': '#251', 'name': 'Celebi', 'type': 'Psychic Grass'},
    {'number': '#252', 'name': 'Treecko', 'type': 'Grass'},
{'number': '#253', 'name': 'Grovyle', 'type': 'Grass'},
    {'number': '#254', 'name': 'Sceptile', 'type': 'Grass'},
{'number': '#255', 'name': 'Torchic', 'type': 'Fire'},
    {'number': '#256', 'name': 'Combusken', 'type': 'Fire Fighting'},
    {'number': '#257', 'name': 'Blaziken', 'type': 'Fire Fighting'},
    {'number': '#258', 'name': 'Mudkip', 'type': 'Water'},
    {'number': '#259', 'name': 'Marshtomp', 'type': 'Water Ground'},
    {'number': '#260', 'name': 'Swampert', 'type': 'Water Ground'},
    {'number': '#261', 'name': 'Poochyena', 'type': 'Dark'},
{'number': '#262', 'name': 'Mightyena', 'type': 'Dark'},
    {'number': '#263', 'name': 'Zigzagoon', 'type': 'Normal'},
{'number': '#264', 'name': 'Linoone', 'type': 'Normal'},
    {'number': '#265', 'name': 'Wurmple', 'type': 'Bug'},
{'number': '#266', 'name': 'Silcoon', 'type': 'Bug'},
    {'number': '#267', 'name': 'Beautifly', 'type': 'Bug Flying'},
{'number': '#268', 'name': 'Cascoon', 'type': 'Bug'},
    {'number': '#269', 'name': 'Dustox', 'type': 'Bug Poison'},
    {'number': '#270', 'name': 'Lotad', 'type': 'Water Grass'},
    {'number': '#271', 'name': 'Lombre', 'type': 'Water Grass'},
    {'number': '#272', 'name': 'Ludicolo', 'type': 'Water Grass'},
    {'number': '#273', 'name': 'Seedot', 'type': 'Grass'},
{'number': '#274', 'name': 'Nuzleaf', 'type': 'Grass Dark'},
    {'number': '#275', 'name': 'Shiftry', 'type': 'Grass Dark'},
    {'number': '#276', 'name': 'Taillow', 'type': 'Normal Flying'},
    {'number': '#277', 'name': 'Swellow', 'type': 'Normal Flying'},
    {'number': '#278', 'name': 'Wingull', 'type': 'Water Flying'},
    {'number': '#279', 'name': 'Pelipper', 'type': 'Water Flying'},
    {'number': '#280', 'name': 'Ralts', 'type': 'Psychic Fairy'},
    {'number': '#281', 'name': 'Kirlia', 'type': 'Psychic Fairy'},
    {'number': '#282', 'name': 'Gardevoir', 'type': 'Psychic Fairy'},
    {'number': '#283', 'name': 'Surskit', 'type': 'Bug Water'},
    {'number': '#284', 'name': 'Masquerain', 'type': 'Bug Flying'},
    {'number': '#285', 'name': 'Shroomish', 'type': 'Grass'},
    {'number': '#286', 'name': 'Breloom', 'type': 'Grass Fighting'},
    {'number': '#287', 'name': 'Slakoth', 'type': 'Normal'},
{'number': '#288', 'name': 'Vigoroth', 'type': 'Normal'},
    {'number': '#289', 'name': 'Slaking', 'type': 'Normal'},
    {'number': '#290', 'name': 'Nincada', 'type': 'Bug Ground'},
    {'number': '#291', 'name': 'Ninjask', 'type': 'Bug Flying'},
    {'number': '#292', 'name': 'Shedinja', 'type': 'Bug Ghost'},
    {'number': '#293', 'name': 'Whismur', 'type': 'Normal'},
{'number': '#294', 'name': 'Loudred', 'type': 'Normal'},
    {'number': '#295', 'name': 'Exploud', 'type': 'Normal'},
{'number': '#296', 'name': 'Makuhita', 'type': 'Fighting'},
    {'number': '#297', 'name': 'Hariyama', 'type': 'Fighting'},
    {'number': '#298', 'name': 'Azurill', 'type': 'Normal Fairy'},
    {'number': '#299', 'name': 'Nosepass', 'type': 'Rock'},
{'number': '#300', 'name': 'Skitty', 'type': 'Normal'},
    {'number': '#301', 'name': 'Delcatty', 'type': 'Normal'},
    {'number': '#302', 'name': 'Sableye', 'type': 'Dark Ghost'},
    {'number': '#303', 'name': 'Mawile', 'type': 'Steel Fairy'},
    {'number': '#304', 'name': 'Aron', 'type': 'Steel Rock'},
    {'number': '#305', 'name': 'Lairon', 'type': 'Steel Rock'},
    {'number': '#306', 'name': 'Aggron', 'type': 'Steel Rock'},
    {'number': '#307', 'name': 'Meditite', 'type': 'Fighting Psychic'},
    {'number': '#308', 'name': 'Medicham', 'type': 'Fighting Psychic'},
    {'number': '#309', 'name': 'Electrike', 'type': 'Electric'},
    {'number': '#310', 'name': 'Manectric', 'type': 'Electric'},
    {'number': '#311', 'name': 'Plusle', 'type': 'Electric'},
{'number': '#312', 'name': 'Minun', 'type': 'Electric'},
    {'number': '#313', 'name': 'Volbeat', 'type': 'Bug'},
{'number': '#314', 'name': 'Illumise', 'type': 'Bug'},
    {'number': '#315', 'name': 'Roselia', 'type': 'Grass Poison'},
    {'number': '#316', 'name': 'Gulpin', 'type': 'Poison'},
{'number': '#317', 'name': 'Swalot', 'type': 'Poison'},
    {'number': '#318', 'name': 'Carvanha', 'type': 'Water Dark'},
    {'number': '#319', 'name': 'Sharpedo', 'type': 'Water Dark'},
    {'number': '#320', 'name': 'Wailmer', 'type': 'Water'},
{'number': '#321', 'name': 'Wailord', 'type': 'Water'},
    {'number': '#322', 'name': 'Numel', 'type': 'Fire Ground'},
    {'number': '#323', 'name': 'Camerupt', 'type': 'Fire Ground'},
    {'number': '#324', 'name': 'Torkoal', 'type': 'Fire'},
{'number': '#325', 'name': 'Spoink', 'type': 'Psychic'},
    {'number': '#326', 'name': 'Grumpig', 'type': 'Psychic'},
{'number': '#327', 'name': 'Spinda', 'type': 'Normal'},
    {'number': '#328', 'name': 'Trapinch', 'type': 'Ground'},
    {'number': '#329', 'name': 'Vibrava', 'type': 'Ground Dragon'},
    {'number': '#330', 'name': 'Flygon', 'type': 'Ground Dragon'},
    {'number': '#331', 'name': 'Cacnea', 'type': 'Grass'},
{'number': '#332', 'name': 'Cacturne', 'type': 'Grass Dark'},
    {'number': '#333', 'name': 'Swablu', 'type': 'Normal Flying'},
    {'number': '#334', 'name': 'Altaria', 'type': 'Dragon Flying'},
    {'number': '#335', 'name': 'Zangoose', 'type': 'Normal'},
{'number': '#336', 'name': 'Seviper', 'type': 'Poison'},
    {'number': '#337', 'name': 'Lunatone', 'type': 'Rock Psychic'},
    {'number': '#338', 'name': 'Solrock', 'type': 'Rock Psychic'},
    {'number': '#339', 'name': 'Barboach', 'type': 'Water Ground'},
    {'number': '#340', 'name': 'Whiscash', 'type': 'Water Ground'},
    {'number': '#341', 'name': 'Corphish', 'type': 'Water'},
    {'number': '#342', 'name': 'Crawdaunt', 'type': 'Water Dark'},
    {'number': '#343', 'name': 'Baltoy', 'type': 'Ground Psychic'},
    {'number': '#344', 'name': 'Claydol', 'type': 'Ground Psychic'},
    {'number': '#345', 'name': 'Lileep', 'type': 'Rock Grass'},
    {'number': '#346', 'name': 'Cradily', 'type': 'Rock Grass'},
    {'number': '#347', 'name': 'Anorith', 'type': 'Rock Bug'},
    {'number': '#348', 'name': 'Armaldo', 'type': 'Rock Bug'},
{'number': '#349', 'name': 'Feebas', 'type': 'Water'},
    {'number': '#350', 'name': 'Milotic', 'type': 'Water'},
{'number': '#351', 'name': 'Castform', 'type': 'Normal'},
    {'number': '#352', 'name': 'Kecleon', 'type': 'Normal'},
{'number': '#353', 'name': 'Shuppet', 'type': 'Ghost'},
    {'number': '#354', 'name': 'Banette', 'type': 'Ghost'},
{'number': '#355', 'name': 'Duskull', 'type': 'Ghost'},
    {'number': '#356', 'name': 'Dusclops', 'type': 'Ghost'},
    {'number': '#357', 'name': 'Tropius', 'type': 'Grass Flying'},
    {'number': '#358', 'name': 'Chimecho', 'type': 'Psychic'},
{'number': '#359', 'name': 'Absol', 'type': 'Dark'},
    {'number': '#360', 'name': 'Wynaut', 'type': 'Psychic'},
{'number': '#361', 'name': 'Snorunt', 'type': 'Ice'},
    {'number': '#362', 'name': 'Glalie', 'type': 'Ice'},
{'number': '#363', 'name': 'Spheal', 'type': 'Ice Water'},
    {'number': '#364', 'name': 'Sealeo', 'type': 'Ice Water'},
    {'number': '#365', 'name': 'Walrein', 'type': 'Ice Water'},
{'number': '#366', 'name': 'Clamperl', 'type': 'Water'},
    {'number': '#367', 'name': 'Huntail', 'type': 'Water'},
{'number': '#368', 'name': 'Gorebyss', 'type': 'Water'},
    {'number': '#369', 'name': 'Relicanth', 'type': 'Water Rock'},
    {'number': '#370', 'name': 'Luvdisc', 'type': 'Water'},
{'number': '#371', 'name': 'Bagon', 'type': 'Dragon'},
    {'number': '#372', 'name': 'Shelgon', 'type': 'Dragon'},
    {'number': '#373', 'name': 'Salamence', 'type': 'Dragon Flying'},
    {'number': '#374', 'name': 'Beldum', 'type': 'Steel Psychic'},
    {'number': '#375', 'name': 'Metang', 'type': 'Steel Psychic'},
    {'number': '#376', 'name': 'Metagross', 'type': 'Steel Psychic'},
    {'number': '#377', 'name': 'Regirock', 'type': 'Rock'},
{'number': '#378', 'name': 'Regice', 'type': 'Ice'},
    {'number': '#379', 'name': 'Registeel', 'type': 'Steel'},
    {'number': '#380', 'name': 'Latias', 'type': 'Dragon Psychic'},
    {'number': '#381', 'name': 'Latios', 'type': 'Dragon Psychic'},
    {'number': '#382', 'name': 'Kyogre', 'type': 'Water'},
{'number': '#383', 'name': 'Groudon', 'type': 'Ground'},
    {'number': '#384', 'name': 'Rayquaza', 'type': 'Dragon Flying'},
    {'number': '#385', 'name': 'Jirachi', 'type': 'Steel Psychic'},
    {'number': '#386', 'name': 'Deoxys', 'type': 'Psychic'},
{'number': '#387', 'name': 'Turtwig', 'type': 'Grass'},
    {'number': '#388', 'name': 'Grotle', 'type': 'Grass'},
    {'number': '#389', 'name': 'Torterra', 'type': 'Grass Ground'},
    {'number': '#390', 'name': 'Chimchar', 'type': 'Fire'},
    {'number': '#391', 'name': 'Monferno', 'type': 'Fire Fighting'},
    {'number': '#392', 'name': 'Infernape', 'type': 'Fire Fighting'},
    {'number': '#393', 'name': 'Piplup', 'type': 'Water'},
{'number': '#394', 'name': 'Prinplup', 'type': 'Water'},
    {'number': '#395', 'name': 'Empoleon', 'type': 'Water Steel'},
    {'number': '#396', 'name': 'Starly', 'type': 'Normal Flying'},
    {'number': '#397', 'name': 'Staravia', 'type': 'Normal Flying'},
    {'number': '#398', 'name': 'Staraptor', 'type': 'Normal Flying'},
    {'number': '#399', 'name': 'Bidoof', 'type': 'Normal'},
    {'number': '#400', 'name': 'Bibarel', 'type': 'Normal Water'},
    {'number': '#401', 'name': 'Kricketot', 'type': 'Bug'},
{'number': '#402', 'name': 'Kricketune', 'type': 'Bug'},
    {'number': '#403', 'name': 'Shinx', 'type': 'Electric'},
{'number': '#404', 'name': 'Luxio', 'type': 'Electric'},
    {'number': '#405', 'name': 'Luxray', 'type': 'Electric'},
    {'number': '#406', 'name': 'Budew', 'type': 'Grass Poison'},
    {'number': '#407', 'name': 'Roserade', 'type': 'Grass Poison'},
    {'number': '#408', 'name': 'Cranidos', 'type': 'Rock'},
{'number': '#409', 'name': 'Rampardos', 'type': 'Rock'},
    {'number': '#410', 'name': 'Shieldon', 'type': 'Rock Steel'},
    {'number': '#411', 'name': 'Bastiodon', 'type': 'Rock Steel'},
{'number': '#412', 'name': 'Burmy', 'type': 'Bug'},
    {'number': '#413', 'name': 'Wormadam', 'type': 'Bug Grass'},
    {'number': '#414', 'name': 'Mothim', 'type': 'Bug Flying'},
    {'number': '#415', 'name': 'Combee', 'type': 'Bug Flying'},
    {'number': '#416', 'name': 'Vespiquen', 'type': 'Bug Flying'},
    {'number': '#417', 'name': 'Pachirisu', 'type': 'Electric'},
{'number': '#418', 'name': 'Buizel', 'type': 'Water'},
    {'number': '#419', 'name': 'Floatzel', 'type': 'Water'},
{'number': '#420', 'name': 'Cherubi', 'type': 'Grass'},
    {'number': '#421', 'name': 'Cherrim', 'type': 'Grass'},
{'number': '#422', 'name': 'Shellos', 'type': 'Water'},
    {'number': '#423', 'name': 'Gastrodon', 'type': 'Water Ground'},
    {'number': '#424', 'name': 'Ambipom', 'type': 'Normal'},
    {'number': '#425', 'name': 'Drifloon', 'type': 'Ghost Flying'},
    {'number': '#426', 'name': 'Drifblim', 'type': 'Ghost Flying'},
    {'number': '#427', 'name': 'Buneary', 'type': 'Normal'},
{'number': '#428', 'name': 'Lopunny', 'type': 'Normal'},
    {'number': '#429', 'name': 'Mismagius', 'type': 'Ghost'},
    {'number': '#430', 'name': 'Honchkrow', 'type': 'Dark Flying'},
    {'number': '#431', 'name': 'Glameow', 'type': 'Normal'},
{'number': '#432', 'name': 'Purugly', 'type': 'Normal'},
    {'number': '#433', 'name': 'Chingling', 'type': 'Psychic'},
    {'number': '#434', 'name': 'Stunky', 'type': 'Poison Dark'},
    {'number': '#435', 'name': 'Skuntank', 'type': 'Poison Dark'},
    {'number': '#436', 'name': 'Bronzor', 'type': 'Steel Psychic'},
    {'number': '#437', 'name': 'Bronzong', 'type': 'Steel Psychic'},
    {'number': '#438', 'name': 'Bonsly', 'type': 'Rock'},
    {'number': '#439', 'name': 'Mime Jr.', 'type': 'Psychic Fairy'},
    {'number': '#440', 'name': 'Happiny', 'type': 'Normal'},
    {'number': '#441', 'name': 'Chatot', 'type': 'Normal Flying'},
    {'number': '#442', 'name': 'Spiritomb', 'type': 'Ghost Dark'},
    {'number': '#443', 'name': 'Gible', 'type': 'Dragon Ground'},
    {'number': '#444', 'name': 'Gabite', 'type': 'Dragon Ground'},
    {'number': '#445', 'name': 'Garchomp', 'type': 'Dragon Ground'},
    {'number': '#446', 'name': 'Munchlax', 'type': 'Normal'},
{'number': '#447', 'name': 'Riolu', 'type': 'Fighting'},
    {'number': '#448', 'name': 'Lucario', 'type': 'Fighting Steel'},
    {'number': '#449', 'name': 'Hippopotas', 'type': 'Ground'},
    {'number': '#450', 'name': 'Hippowdon', 'type': 'Ground'},
    {'number': '#451', 'name': 'Skorupi', 'type': 'Poison Bug'},
    {'number': '#452', 'name': 'Drapion', 'type': 'Poison Dark'},
    {'number': '#453', 'name': 'Croagunk', 'type': 'Poison Fighting'},
    {'number': '#454', 'name': 'Toxicroak', 'type': 'Poison Fighting'},
    {'number': '#455', 'name': 'Carnivine', 'type': 'Grass'},
{'number': '#456', 'name': 'Finneon', 'type': 'Water'},
    {'number': '#457', 'name': 'Lumineon', 'type': 'Water'},
    {'number': '#458', 'name': 'Mantyke', 'type': 'Water Flying'},
    {'number': '#459', 'name': 'Snover', 'type': 'Grass Ice'},
    {'number': '#460', 'name': 'Abomasnow', 'type': 'Grass Ice'},
    {'number': '#461', 'name': 'Weavile', 'type': 'Dark Ice'},
    {'number': '#462', 'name': 'Magnezone', 'type': 'Electric Steel'},
    {'number': '#463', 'name': 'Lickilicky', 'type': 'Normal'},
    {'number': '#464', 'name': 'Rhyperior', 'type': 'Ground Rock'},
    {'number': '#465', 'name': 'Tangrowth', 'type': 'Grass'},
    {'number': '#466', 'name': 'Electivire', 'type': 'Electric'},
    {'number': '#467', 'name': 'Magmortar', 'type': 'Fire'},
    {'number': '#468', 'name': 'Togekiss', 'type': 'Fairy Flying'},
    {'number': '#469', 'name': 'Yanmega', 'type': 'Bug Flying'},
{'number': '#470', 'name': 'Leafeon', 'type': 'Grass'},
    {'number': '#471', 'name': 'Glaceon', 'type': 'Ice'},
    {'number': '#472', 'name': 'Gliscor', 'type': 'Ground Flying'},
    {'number': '#473', 'name': 'Mamoswine', 'type': 'Ice Ground'},
    {'number': '#474', 'name': 'Porygon-Z', 'type': 'Normal'},
    {'number': '#475', 'name': 'Gallade', 'type': 'Psychic Fighting'},
    {'number': '#476', 'name': 'Probopass', 'type': 'Rock Steel'},
    {'number': '#477', 'name': 'Dusknoir', 'type': 'Ghost'},
    {'number': '#478', 'name': 'Froslass', 'type': 'Ice Ghost'},
    {'number': '#479', 'name': 'Rotom', 'type': 'Electric Ghost'},
    {'number': '#480', 'name': 'Uxie', 'type': 'Psychic'},
{'number': '#481', 'name': 'Mesprit', 'type': 'Psychic'},
    {'number': '#482', 'name': 'Azelf', 'type': 'Psychic'},
    {'number': '#483', 'name': 'Dialga', 'type': 'Steel Dragon'},
    {'number': '#484', 'name': 'Palkia', 'type': 'Water Dragon'},
    {'number': '#485', 'name': 'Heatran', 'type': 'Fire Steel'},
    {'number': '#486', 'name': 'Regigigas', 'type': 'Normal'},
    {'number': '#487', 'name': 'Giratina', 'type': 'Ghost Dragon'},
    {'number': '#488', 'name': 'Cresselia', 'type': 'Psychic'},
{'number': '#489', 'name': 'Phione', 'type': 'Water'},
    {'number': '#490', 'name': 'Manaphy', 'type': 'Water'},
{'number': '#491', 'name': 'Darkrai', 'type': 'Dark'},
    {'number': '#492', 'name': 'Shaymin', 'type': 'Grass'},
{'number': '#493', 'name': 'Arceus', 'type': 'Normal'},
    {'number': '#494', 'name': 'Victini', 'type': 'Psychic Fire'},
{'number': '#495', 'name': 'Snivy', 'type': 'Grass'},
    {'number': '#496', 'name': 'Servine', 'type': 'Grass'},
{'number': '#497', 'name': 'Serperior', 'type': 'Grass'},
    {'number': '#498', 'name': 'Tepig', 'type': 'Fire'},
{'number': '#499', 'name': 'Pignite', 'type': 'Fire Fighting'},
    {'number': '#500', 'name': 'Emboar', 'type': 'Fire Fighting'},
    {'number': '#501', 'name': 'Oshawott', 'type': 'Water'},
{'number': '#502', 'name': 'Dewott', 'type': 'Water'},
    {'number': '#503', 'name': 'Samurott', 'type': 'Water'},
{'number': '#504', 'name': 'Patrat', 'type': 'Normal'},
    {'number': '#505', 'name': 'Watchog', 'type': 'Normal'},
{'number': '#506', 'name': 'Lillipup', 'type': 'Normal'},
    {'number': '#507', 'name': 'Herdier', 'type': 'Normal'},
{'number': '#508', 'name': 'Stoutland', 'type': 'Normal'},
    {'number': '#509', 'name': 'Purrloin', 'type': 'Dark'},
{'number': '#510', 'name': 'Liepard', 'type': 'Dark'},
    {'number': '#511', 'name': 'Pansage', 'type': 'Grass'},
{'number': '#512', 'name': 'Simisage', 'type': 'Grass'},
    {'number': '#513', 'name': 'Pansear', 'type': 'Fire'},
{'number': '#514', 'name': 'Simisear', 'type': 'Fire'},
    {'number': '#515', 'name': 'Panpour', 'type': 'Water'},
{'number': '#516', 'name': 'Simipour', 'type': 'Water'},
    {'number': '#517', 'name': 'Munna', 'type': 'Psychic'},
{'number': '#518', 'name': 'Musharna', 'type': 'Psychic'},
    {'number': '#519', 'name': 'Pidove', 'type': 'Normal Flying'},
    {'number': '#520', 'name': 'Tranquill', 'type': 'Normal Flying'},
    {'number': '#521', 'name': 'Unfezant', 'type': 'Normal Flying'},
    {'number': '#522', 'name': 'Blitzle', 'type': 'Electric'},
    {'number': '#523', 'name': 'Zebstrika', 'type': 'Electric'},
    {'number': '#524', 'name': 'Roggenrola', 'type': 'Rock'},
{'number': '#525', 'name': 'Boldore', 'type': 'Rock'},
    {'number': '#526', 'name': 'Gigalith', 'type': 'Rock'},
    {'number': '#527', 'name': 'Woobat', 'type': 'Psychic Flying'},
    {'number': '#528', 'name': 'Swoobat', 'type': 'Psychic Flying'},
    {'number': '#529', 'name': 'Drilbur', 'type': 'Ground'},
    {'number': '#530', 'name': 'Excadrill', 'type': 'Ground Steel'},
    {'number': '#531', 'name': 'Audino', 'type': 'Normal'},
{'number': '#532', 'name': 'Timburr', 'type': 'Fighting'},
    {'number': '#533', 'name': 'Gurdurr', 'type': 'Fighting'},
    {'number': '#534', 'name': 'Conkeldurr', 'type': 'Fighting'},
    {'number': '#535', 'name': 'Tympole', 'type': 'Water'},
    {'number': '#536', 'name': 'Palpitoad', 'type': 'Water Ground'},
    {'number': '#537', 'name': 'Seismitoad', 'type': 'Water Ground'},
    {'number': '#538', 'name': 'Throh', 'type': 'Fighting'},
{'number': '#539', 'name': 'Sawk', 'type': 'Fighting'},
    {'number': '#540', 'name': 'Sewaddle', 'type': 'Bug Grass'},
    {'number': '#541', 'name': 'Swadloon', 'type': 'Bug Grass'},
    {'number': '#542', 'name': 'Leavanny', 'type': 'Bug Grass'},
    {'number': '#543', 'name': 'Venipede', 'type': 'Bug Poison'},
    {'number': '#544', 'name': 'Whirlipede', 'type': 'Bug Poison'},
    {'number': '#545', 'name': 'Scolipede', 'type': 'Bug Poison'},
    {'number': '#546', 'name': 'Cottonee', 'type': 'Grass Fairy'},
    {'number': '#547', 'name': 'Whimsicott', 'type': 'Grass Fairy'},
    {'number': '#548', 'name': 'Petilil', 'type': 'Grass'},
{'number': '#549', 'name': 'Lilligant', 'type': 'Grass'},
    {'number': '#550', 'name': 'Basculin', 'type': 'Water'},
    {'number': '#551', 'name': 'Sandile', 'type': 'Ground Dark'},
    {'number': '#552', 'name': 'Krokorok', 'type': 'Ground Dark'},
    {'number': '#553', 'name': 'Krookodile', 'type': 'Ground Dark'},
    {'number': '#554', 'name': 'Darumaka', 'type': 'Fire'},
{'number': '#555', 'name': 'Darmanitan', 'type': 'Fire'},
    {'number': '#556', 'name': 'Maractus', 'type': 'Grass'},
{'number': '#557', 'name': 'Dwebble', 'type': 'Bug Rock'},
    {'number': '#558', 'name': 'Crustle', 'type': 'Bug Rock'},
    {'number': '#559', 'name': 'Scraggy', 'type': 'Dark Fighting'},
    {'number': '#560', 'name': 'Scrafty', 'type': 'Dark Fighting'},
    {'number': '#561', 'name': 'Sigilyph', 'type': 'Psychic Flying'},
    {'number': '#562', 'name': 'Yamask', 'type': 'Ghost'},
{'number': '#563', 'name': 'Cofagrigus', 'type': 'Ghost'},
    {'number': '#564', 'name': 'Tirtouga', 'type': 'Water Rock'},
    {'number': '#565', 'name': 'Carracosta', 'type': 'Water Rock'},
    {'number': '#566', 'name': 'Archen', 'type': 'Rock Flying'},
    {'number': '#567', 'name': 'Archeops', 'type': 'Rock Flying'},
    {'number': '#568', 'name': 'Trubbish', 'type': 'Poison'},
{'number': '#569', 'name': 'Garbodor', 'type': 'Poison'},
    {'number': '#570', 'name': 'Zorua', 'type': 'Dark'},
{'number': '#571', 'name': 'Zoroark', 'type': 'Dark'},
    {'number': '#572', 'name': 'Minccino', 'type': 'Normal'},
{'number': '#573', 'name': 'Cinccino', 'type': 'Normal'},
    {'number': '#574', 'name': 'Gothita', 'type': 'Psychic'},
    {'number': '#575', 'name': 'Gothorita', 'type': 'Psychic'},
    {'number': '#576', 'name': 'Gothitelle', 'type': 'Psychic'},
    {'number': '#577', 'name': 'Solosis', 'type': 'Psychic'},
{'number': '#578', 'name': 'Duosion', 'type': 'Psychic'},
    {'number': '#579', 'name': 'Reuniclus', 'type': 'Psychic'},
    {'number': '#580', 'name': 'Ducklett', 'type': 'Water Flying'},
    {'number': '#581', 'name': 'Swanna', 'type': 'Water Flying'},
    {'number': '#582', 'name': 'Vanillite', 'type': 'Ice'},
{'number': '#583', 'name': 'Vanillish', 'type': 'Ice'},
    {'number': '#584', 'name': 'Vanilluxe', 'type': 'Ice'},
    {'number': '#585', 'name': 'Deerling', 'type': 'Normal Grass'},
    {'number': '#586', 'name': 'Sawsbuck', 'type': 'Normal Grass'},
    {'number': '#587', 'name': 'Emolga', 'type': 'Electric Flying'},
    {'number': '#588', 'name': 'Karrablast', 'type': 'Bug'},
    {'number': '#589', 'name': 'Escavalier', 'type': 'Bug Steel'},
    {'number': '#590', 'name': 'Foongus', 'type': 'Grass Poison'},
    {'number': '#591', 'name': 'Amoonguss', 'type': 'Grass Poison'},
    {'number': '#592', 'name': 'Frillish', 'type': 'Water Ghost'},
    {'number': '#593', 'name': 'Jellicent', 'type': 'Water Ghost'},
    {'number': '#594', 'name': 'Alomomola', 'type': 'Water'},
    {'number': '#595', 'name': 'Joltik', 'type': 'Bug Electric'},
    {'number': '#596', 'name': 'Galvantula', 'type': 'Bug Electric'},
    {'number': '#597', 'name': 'Ferroseed', 'type': 'Grass Steel'},
    {'number': '#598', 'name': 'Ferrothorn', 'type': 'Grass Steel'},
    {'number': '#599', 'name': 'Klink', 'type': 'Steel'},
{'number': '#600', 'name': 'Klang', 'type': 'Steel'},
    {'number': '#601', 'name': 'Klinklang', 'type': 'Steel'},
{'number': '#602', 'name': 'Tynamo', 'type': 'Electric'},
    {'number': '#603', 'name': 'Eelektrik', 'type': 'Electric'},
    {'number': '#604', 'name': 'Eelektross', 'type': 'Electric'},
    {'number': '#605', 'name': 'Elgyem', 'type': 'Psychic'},
{'number': '#606', 'name': 'Beheeyem', 'type': 'Psychic'},
    {'number': '#607', 'name': 'Litwick', 'type': 'Ghost Fire'},
    {'number': '#608', 'name': 'Lampent', 'type': 'Ghost Fire'},
    {'number': '#609', 'name': 'Chandelure', 'type': 'Ghost Fire'},
    {'number': '#610', 'name': 'Axew', 'type': 'Dragon'},
{'number': '#611', 'name': 'Fraxure', 'type': 'Dragon'},
    {'number': '#612', 'name': 'Haxorus', 'type': 'Dragon'},
{'number': '#613', 'name': 'Cubchoo', 'type': 'Ice'},
    {'number': '#614', 'name': 'Beartic', 'type': 'Ice'},
{'number': '#615', 'name': 'Cryogonal', 'type': 'Ice'},
    {'number': '#616', 'name': 'Shelmet', 'type': 'Bug'},
{'number': '#617', 'name': 'Accelgor', 'type': 'Bug'},
    {'number': '#618', 'name': 'Stunfisk', 'type': 'Electric Ground'},
    {'number': '#619', 'name': 'Mienfoo', 'type': 'Fighting'},
    {'number': '#620', 'name': 'Mienshao', 'type': 'Fighting'},
    {'number': '#621', 'name': 'Druddigon', 'type': 'Dragon'},
    {'number': '#622', 'name': 'Golett', 'type': 'Ground Ghost'},
    {'number': '#623', 'name': 'Golurk', 'type': 'Ground Ghost'},
    {'number': '#624', 'name': 'Pawniard', 'type': 'Dark Steel'},
    {'number': '#625', 'name': 'Bisharp', 'type': 'Dark Steel'},
    {'number': '#626', 'name': 'Bouffalant', 'type': 'Normal'},
    {'number': '#627', 'name': 'Rufflet', 'type': 'Normal Flying'},
    {'number': '#628', 'name': 'Braviary', 'type': 'Normal Flying'},
    {'number': '#629', 'name': 'Vullaby', 'type': 'Dark Flying'},
    {'number': '#630', 'name': 'Mandibuzz', 'type': 'Dark Flying'},
    {'number': '#631', 'name': 'Heatmor', 'type': 'Fire'},
{'number': '#632', 'name': 'Durant', 'type': 'Bug Steel'},
    {'number': '#633', 'name': 'Deino', 'type': 'Dark Dragon'},
    {'number': '#634', 'name': 'Zweilous', 'type': 'Dark Dragon'},
    {'number': '#635', 'name': 'Hydreigon', 'type': 'Dark Dragon'},
    {'number': '#636', 'name': 'Larvesta', 'type': 'Bug Fire'},
    {'number': '#637', 'name': 'Volcarona', 'type': 'Bug Fire'},
    {'number': '#638', 'name': 'Cobalion', 'type': 'Steel Fighting'},
    {'number': '#639', 'name': 'Terrakion', 'type': 'Rock Fighting'},
    {'number': '#640', 'name': 'Virizion', 'type': 'Grass Fighting'},
    {'number': '#641', 'name': 'Tornadus', 'type': 'Flying'},
    {'number': '#642', 'name': 'Thundurus', 'type': 'Electric Flying'},
    {'number': '#643', 'name': 'Reshiram', 'type': 'Dragon Fire'},
    {'number': '#644', 'name': 'Zekrom', 'type': 'Dragon Electric'},
    {'number': '#645', 'name': 'Landorus', 'type': 'Ground Flying'},
    {'number': '#646', 'name': 'Kyurem', 'type': 'Dragon Ice'},
    {'number': '#647', 'name': 'Keldeo', 'type': 'Water Fighting'},
    {'number': '#648', 'name': 'Meloetta', 'type': 'Normal Psychic'},
    {'number': '#649', 'name': 'Genesect', 'type': 'Bug Steel'},
{'number': '#650', 'name': 'Chespin', 'type': 'Grass'},
    {'number': '#651', 'name': 'Quilladin', 'type': 'Grass'},
    {'number': '#652', 'name': 'Chesnaught', 'type': 'Grass Fighting'},
    {'number': '#653', 'name': 'Fennekin', 'type': 'Fire'},
{'number': '#654', 'name': 'Braixen', 'type': 'Fire'},
    {'number': '#655', 'name': 'Delphox', 'type': 'Fire Psychic'},
    {'number': '#656', 'name': 'Froakie', 'type': 'Water'},
{'number': '#657', 'name': 'Frogadier', 'type': 'Water'},
    {'number': '#658', 'name': 'Greninja', 'type': 'Water Dark'},
    {'number': '#659', 'name': 'Bunnelby', 'type': 'Normal'},
    {'number': '#660', 'name': 'Diggersby', 'type': 'Normal Ground'},
    {'number': '#661', 'name': 'Fletchling', 'type': 'Normal Flying'},
    {'number': '#662', 'name': 'Fletchinder', 'type': 'Fire Flying'},
    {'number': '#663', 'name': 'Talonflame', 'type': 'Fire Flying'},
    {'number': '#664', 'name': 'Scatterbug', 'type': 'Bug'},
{'number': '#665', 'name': 'Spewpa', 'type': 'Bug'},
    {'number': '#666', 'name': 'Vivillon', 'type': 'Bug Flying'},
    {'number': '#667', 'name': 'Litleo', 'type': 'Fire Normal'},
    {'number': '#668', 'name': 'Pyroar', 'type': 'Fire Normal'},
{'number': '#669', 'name': 'Flabébé', 'type': 'Fairy'},
    {'number': '#670', 'name': 'Floette', 'type': 'Fairy'},
{'number': '#671', 'name': 'Florges', 'type': 'Fairy'},
    {'number': '#672', 'name': 'Skiddo', 'type': 'Grass'},
{'number': '#673', 'name': 'Gogoat', 'type': 'Grass'},
    {'number': '#674', 'name': 'Pancham', 'type': 'Fighting'},
    {'number': '#675', 'name': 'Pangoro', 'type': 'Fighting Dark'},
    {'number': '#676', 'name': 'Furfrou', 'type': 'Normal'},
{'number': '#677', 'name': 'Espurr', 'type': 'Psychic'},
    {'number': '#678', 'name': 'Meowstic', 'type': 'Psychic'},
    {'number': '#679', 'name': 'Honedge', 'type': 'Steel Ghost'},
    {'number': '#680', 'name': 'Doublade', 'type': 'Steel Ghost'},
    {'number': '#681', 'name': 'Aegislash', 'type': 'Steel Ghost'},
    {'number': '#682', 'name': 'Spritzee', 'type': 'Fairy'},
{'number': '#683', 'name': 'Aromatisse', 'type': 'Fairy'},
    {'number': '#684', 'name': 'Swirlix', 'type': 'Fairy'},
{'number': '#685', 'name': 'Slurpuff', 'type': 'Fairy'},
    {'number': '#686', 'name': 'Inkay', 'type': 'Dark Psychic'},
    {'number': '#687', 'name': 'Malamar', 'type': 'Dark Psychic'},
    {'number': '#688', 'name': 'Binacle', 'type': 'Rock Water'},
    {'number': '#689', 'name': 'Barbaracle', 'type': 'Rock Water'},
    {'number': '#690', 'name': 'Skrelp', 'type': 'Poison Water'},
    {'number': '#691', 'name': 'Dragalge', 'type': 'Poison Dragon'},
    {'number': '#692', 'name': 'Clauncher', 'type': 'Water'},
{'number': '#693', 'name': 'Clawitzer', 'type': 'Water'},
    {'number': '#694', 'name': 'Helioptile', 'type': 'Electric Normal'},
    {'number': '#695', 'name': 'Heliolisk', 'type': 'Electric Normal'},
    {'number': '#696', 'name': 'Tyrunt', 'type': 'Rock Dragon'},
    {'number': '#697', 'name': 'Tyrantrum', 'type': 'Rock Dragon'},
    {'number': '#698', 'name': 'Amaura', 'type': 'Rock Ice'},
{'number': '#699', 'name': 'Aurorus', 'type': 'Rock Ice'},
    {'number': '#700', 'name': 'Sylveon', 'type': 'Fairy'},
    {'number': '#701', 'name': 'Hawlucha', 'type': 'Fighting Flying'},
    {'number': '#702', 'name': 'Dedenne', 'type': 'Electric Fairy'},
    {'number': '#703', 'name': 'Carbink', 'type': 'Rock Fairy'},
{'number': '#704', 'name': 'Goomy', 'type': 'Dragon'},
    {'number': '#705', 'name': 'Sliggoo', 'type': 'Dragon'},
{'number': '#706', 'name': 'Goodra', 'type': 'Dragon'},
    {'number': '#707', 'name': 'Klefki', 'type': 'Steel Fairy'},
    {'number': '#708', 'name': 'Phantump', 'type': 'Ghost Grass'},
    {'number': '#709', 'name': 'Trevenant', 'type': 'Ghost Grass'},
    {'number': '#710', 'name': 'Pumpkaboo', 'type': 'Ghost Grass'},
    {'number': '#711', 'name': 'Gourgeist', 'type': 'Ghost Grass'},
    {'number': '#712', 'name': 'Bergmite', 'type': 'Ice'},
{'number': '#713', 'name': 'Avalugg', 'type': 'Ice'},
    {'number': '#714', 'name': 'Noibat', 'type': 'Flying Dragon'},
    {'number': '#715', 'name': 'Noivern', 'type': 'Flying Dragon'},
    {'number': '#716', 'name': 'Xerneas', 'type': 'Fairy'},
    {'number': '#717', 'name': 'Yveltal', 'type': 'Dark Flying'},
    {'number': '#718', 'name': 'Zygarde', 'type': 'Dragon Ground'}]
numb = int(input())-1
print(pokemon[numb]["name"])
print(pokemon[numb]["type"])
