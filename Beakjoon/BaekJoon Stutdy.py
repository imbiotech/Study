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


# 2857 번
# 문제
# 5명의 요원 중 FBI 요원을 찾는 프로그램을 작성하시오.
# FBI요원은 요원의 첩보원명에 FBI가 들어있다.
# 입력
# 5개 줄에 요원의 첩보원명이 주어진다.
# 첩보원명은 알파벳 대문자, 숫자 0~9, 대시 (-)로만 이루어져 있으며, 최대 10글자이다.
# 출력
# 첫째 줄에 FBI 요원을 출력한다.
# 이때, 해당하는 요원이 몇 번째 입력인지를 공백으로 구분하여 출력해야 하며, 오름차순으로 출력해야 한다.
# 만약 FBI 요원이 없다면 "HE GOT AWAY!"를 출력한다.

Code = [input() for i in range(5)]
Index = []
for i in range(5):
    if "FBI" in Code[i]:
        Index.append(i+1)
if len(Index) == 0:
    print("HE GOT AWAY!")
else:
    print(*Index)


# 10173 번
# 문제
# 영어 문장속 숨어있는 니모(Nemo)를 찾아보자.
# 니모를 찾는데 있어서 대소문자는 중요하지 않다.
# 입력
# 여러 문장이 각 줄로 입력되며, 입력의 마지막에는 "EOI" 입력된다.
# 한 줄은 최대 80개의 글자로 이루어져 있다.
# 출력
# 숨겨진 니모를 찾으면 “Found”, 못찾으면 “Missing”를 각 줄에 맞게 출력하면 된다.

while True:
    S = input()
    if S == "EOI":
        break
    if "NEMO" in S.upper():
        print("Found")
    else:
        print("Missing")


# 5598 번
# 문제
# 가이우스 율리우스 카이사르(Gaius Julius Caesar)는 고대 로마 군인이자 정치가였다.
# 카이사르는 비밀스럽게 편지를 쓸 때, 'A'를 'D로', 'B'를 'E'로, 'C'를 'F'로...
# 이런 식으로 알파벳 문자를 3개씩 건너뛰어 적었다고 한다.
# 26개의 대문자 알파벳으로 이루어진 단어를 카이사르 암호 형식으로 3문자를 옮겨 겹치지 않게 나열하여 얻은 카이사르 단어가 있다.
# 이 카이사르 단어를 원래 단어로 돌려놓는 프로그램을 작성하시오.
# 각 문자별로 변환 전과 변환 후를 나타낸 건 아래와 같다.
# 변환전    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# 변환후    D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
# 예를 들어서, 이 방법대로 단어 'JOI'를 카이사르 단어 형식으로 변환한다면 'MRL'을 얻을 수 있고,
# 앞의 예와 같은 방법으로 얻은 카이사르 단어 'FURDWLD'를 원래 단어로 고치면 'CROATIA'가 된다.
# 입력
# 입력은 한 줄로 이루어져 있으며, 그 한 줄에는 대문자 알파벳으로 구성된 단어가 1개 있다.
# 단어는 최대 1000자 이하이다.
# 출력
# 입력받은 카이사르 단어를 원래 단어로 고친 걸 출력하시면 된다.

S = list(input())
for i in range(len(S)):
    o = ord(S[i])
    if 64<o<68:
        S[i] = chr(o+23)
    else:
        S[i] = chr(o-3)
print("".join(S))


# 5597 번
# 문제
# X대학 M교수님은 프로그래밍 수업을 맡고 있다.
# 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.
# 교수님이 내준 특별과제를 28명이 제출했는데,
# 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.
# 입력
# 입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다.
# 출석번호에 중복은 없다.
# 출력
# 출력은 2줄이다.
# 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고,
# 2번째 줄에선 그 다음 출석번호를 출력한다.

std = [i+1 for i in range(30)]
for _ in range(28):
    std.remove(int(input()))
for i in sorted(std):
    print(i)


# 5596 번
# 문제
# 대한고등학교에 재학 중인 민국이와 만세는 4과목(정보, 수학, 과학, 영어)에 대한 시험을 봤다.
# 민국이와 만세가 본 4과목의 점수를 입력하면, 민국이의 총점 S와 만세의 총점 T 중에서 큰 점수를 출력하는 프로그램을 작성하시오.
# 단, 서로 동점일 때는 민국이의 총점 S를 출력한다.
# 입력
# 입력은 2줄로 이루어져 있다.
# 1번째 줄에는 순서대로 민국이의 정보, 수학, 과학, 영어 점수(정수형)가 있으며, 공백으로 구분되어 있다.
# 2번째 줄에는 1번째 줄과 마찬가지로 순서대로 만세의 정보, 수학, 과학, 영어 점수(정수형)가 있고, 공백으로 구분되어 있다.
# 출력
# 문제에서 요구하는 정답을 출력한다.

print(max(sum(list(map(int,input().split()))),sum(list(map(int,input().split())))))


# 2920 번
# 문제
# 다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다.
# 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다.
# c는 1로, d는 2로, ..., C를 8로 바꾼다.
# 1부터 8까지 차례대로 연주한다면 ascending,
# 8부터 1까지 차례대로 연주한다면 descending,
# 둘 다 아니라면 mixed 이다.
# 연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 8개 숫자가 주어진다.
# 이 숫자는 문제 설명에서 설명한 음이며, 1부터 8까지 숫자가 한 번씩 등장한다.
# 출력
# 첫째 줄에 ascending, descending, mixed 중 하나를 출력한다.

s=list(map(int,input().split()))
if s==sorted(s):
    print("ascending")
elif s==sorted(s,reverse=True):
    print("descending")
else:
    print("mixed")


# 9243 번
# 문제
# 어느 날, 상근이의 여자친구는 상근이에게 매우 긴급한 목소리로 전화했다.
# "상근아, 나 급하게 지워야 될 파일이 있어! 이 파일은 절대 복구되면 안돼."
# 파일을 완전 삭제하려면 하드드라이브에서 그 구간을 새로운 데이터로 반복해서 덮어써야 한다.
# 상근이는 여자친구를 위해 파일 완전 삭제 프로그램을 만들려고 한다. 파일 완전 삭제 프로그램은 매우 간단하다.
# 사용자는 삭제할 파일을 하나 고르고, 몇 번 덮어씌울지 n을 입력한다.
# n은 1부터 20까지 숫자 중 하나를 골라야 한다.
# 상근이의 프로그램은 파일을 비트단위로 덮어씌운다.
# 한 번 덮어씌울 때, 0인 비트는 1로, 1인 비트는 0으로 덮어씌운다.
# 상근이는 프로그램을 완성했고 테스트해보려고 한다.
# 파일을 삭제하기 전에 파일이 있었던 곳의 비트와 파일을 삭제한 후에 파일이 있었던 곳의 비트가 주어졌을 때,
# 프로그램을 올바르게 작성했는지 출력한다.
# 이 문제에서 파일이 실제로 삭제되었는지는 중요한 것은 아니다.
# 따라서, 문제에서 설명한대로 상근이가 프로그램을 작성했으면 삭제가 성공한 것으로, 그 외의 경우는 모두 실패한 것이다.
# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N ≤ 20)
# 둘째 줄에는 파일을 삭제하기 전에 파일이 있었던 곳의 비트가 주어지고,
# 셋째 줄에는 삭제한 후에 비트가 주어진다.
# 비트는 0과 1로만 이루어져 있고, 두 문자열의 길이는 같다.
# 비트는 최대 1000개의 문자로 이루어져 있다.
# 출력
# 첫째 줄에 삭제가 성공했으면 "Deletion succeeded"을, 실패했으면 "Deletion failed"을 출력한다.

n = int(input())
f = list(input())
f_ = list(map(lambda x: "1" if x == "0" else "0", f))
r = list(input())
if (n%2==1 and r==f_) or (n%2==0 and r==f):
    print("Deletion succeeded")
else:
    print("Deletion failed")


# 1871 번
# 문제
# 앨버타의 자동차 번호판은 ABC-0123 (세 글자, 네 숫자)와 같이 두 부분으로 나누어져 있다.
# 좋은 번호판은 첫 번째 부분의 가치와 두 번째 부분의 가치의 차이가 100을 넘지 않는 번호판이다.
# 글자로 이루어진 첫 번째 부분의 가치는 글자를 26진법 수처럼 계산한다. (각 자리가 [A..Z])
# 예를 들어, "ABC"의 가치는 28 (0×26**2 + 1×26**1 + 2×26**0)이 된다.
# "ABC-0123"은  |28 - 123| ≤ 100 이기 때문에, 좋은 번호판이다.
# 자동차 번호판이 주어졌을 때, 좋은 번호판인지 아닌지를 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 번호판의 수 N (1 ≤ N ≤ 100)이 주어진다.
# 다음 N개 줄에는 자동차 번호판이 LLL-DDDD 형식으로 주어진다.
# 출력
# 각각의 자동차 번호판에 대해서, 좋은 번호판이면 "nice"를, 아니면 "not nice"를 출력한다.

# from sys import *
# input = stdin.readline
for _ in range(int(input())):
    al,nu=input().strip().split("-")
    al_v, nu_v = 0, int(nu)
    for i in range(3):
        al_v+=(ord(al[i])-65)*26**(2-i)
    if abs(al_v-nu_v)<101:
        print("nice")
    else:
        print("not nice")


# 1032 번
# 문제
# 시작 -> 실행 -> cmd를 쳐보자. 검정 화면이 눈에 보인다.
# 여기서 dir이라고 치면 그 디렉토리에 있는 서브디렉토리와 파일이 모두 나온다.
# 이때 원하는 파일을 찾으려면 다음과 같이 하면 된다.
# dir *.exe라고 치면 확장자가 exe인 파일이 다 나온다.
# "dir 패턴"과 같이 치면 그 패턴에 맞는 파일만 검색 결과로 나온다
# . 예를 들어, dir a?b.exe라고 검색하면
# 파일명의 첫 번째 글자가 a이고, 세 번째 글자가 b이고, 확장자가 exe인 것이 모두 나온다.
# 이때 두 번째 문자는 아무거나 나와도 된다.
# 예를 들어, acb.exe, aab.exe, apb.exe가 나온다.
# 이 문제는 검색 결과가 먼저 주어졌을 때, 패턴으로 뭘 쳐야 그 결과가 나오는지를 출력하는 문제이다.
# 패턴에는 알파벳과 "." 그리고 "?"만 넣을 수 있다.
# 가능하면 ?을 적게 써야 한다.
# 그 디렉토리에는 검색 결과에 나온 파일만 있다고 가정하고, 파일 이름의 길이는 모두 같다.
# 입력
# 첫째 줄에 파일 이름의 개수 N이 주어진다.
# 둘째 줄부터 N개의 줄에는 파일 이름이 주어진다.
# N은 50보다 작거나 같은 자연수이고 파일 이름의 길이는 모두 같고 길이는 최대 50이다.
# 파일이름은 알파벳 소문자와 '.' 로만 이루어져 있다.
# 출력
# 첫째 줄에 패턴을 출력하면 된다.

# from sys import stdin
# input=stdin.readline
n=int(input())
comp=[]
for _ in range(n):
    if len(comp)==0:
        comp=list(input())
    else:
        f=input()
        for i in range(len(comp)):
            if comp[i]!=f[i]:
                comp[i]="?"
print("".join(comp))


# 2004 번
# 문제
# binom{n}{m}의 끝자리 0의 개수를 출력하는 프로그램을 작성하시오
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

# 시간 초과
from math import factorial
n, m = map(int,input().split())
n_m=str(int(factorial(n)//(factorial(m)*factorial(n-m))))
print(len(n_m)-len(n_m.rstrip("0")))

# 성공, fac(n)에 포함된 2와 5의 제곱수를 토대로 0의 개수를 계산
from math import log
def loog(n,k):
    if n==0:
        return 0
    return sum([n//k**i for i in range(1,int(log(n,k))+1)])

n,m = map(int,input().split())
print(max(0,min(loog(n,5)-loog(m,5)-loog(n-m,5),loog(n,2)-loog(m,2)-loog(n-m,2))))


# 3003 번
# 문제
# 동혁이는 오래된 창고를 뒤지다가 낡은 체스판과 피스를 발견했다.
# 체스판의 먼지를 털어내고 걸레로 닦으니 그럭저럭 쓸만한 체스판이 되었다.
# 하지만, 검정색 피스는 모두 있었으나, 흰색 피스는 개수가 올바르지 않았다.
# 체스는 총 16개의 피스를 사용하며,
# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성되어 있다.
# 동혁이가 발견한 흰색 피스의 개수가 주어졌을 때,
# 몇 개를 더하거나 빼야 올바른 세트가 되는지 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 동혁이가 찾은 흰색 킹, 퀸, 룩, 비숍, 나이트, 폰의 개수가 주어진다.
# 이 값은 0보다 크거나 같고 10보다 작거나 같은 정수이다.
# 출력
# 첫째 줄에 입력에서 주어진 순서대로 몇 개의 피스를 더하거나 빼야 되는지를 출력한다.
# 만약 수가 양수라면 동혁이는 그 개수 만큼 피스를 더해야 하는 것이고, 음수라면 제거해야 하는 것이다.

chess = [1,1,2,2,2,8]
white = list(map(int,input().split()))
chess = [chess[i]-white[i] for i in range(len(white))]
print(*chess)


# 4999 번
# 문제
# 재환이는 저스틴 비버 콘서트에서 소리를 너무 많이 질러서 인후염에 걸렸다.
# 의사는 재환이에게 "aaah"를 말해보라고 시켰다.
# 안타깝게도 재환이는 의사가 원하는만큼 소리를 길게 낼 수 없는 경우가 있었다.
# 각각의 의사는 재환이에게 특정한 길이의 "aah"를 말해보라고 요청한다.
# 어떤 의사는 "aaaaaah"를 요구하기도 하고, "h"만 요구하는 의사도 있다.
# 모든 의사는 자신이 원하는 길이의 "aah"를 듣지 못하면 진단을 내릴 수 없다.
# 따라서, 재환이는 집에서 자신이 얼마나 길게 "aah"를 낼 수 있는지 알아냈고,
# 자기가 소리낼 수 있는 길이의 "aah"를 요구하는 의사를 방문하려고 한다.
# 재환이가 낼 수 있는 "aah"의 길이와 의사가 요구하는 길이가 주어진다.
# 이때, 그 병원에 가야하는지 말아야하는지를 알아내는 프로그램을 작성하시오.
# 입력
# 입력은 두 줄로 이루어져 있다.
# 첫째 줄은 재환이가 가장 길게 낼 수 있는 "aaah"이다.
# 둘째 줄은 의사가 듣기를 원하는 "aah"이다.
# 두 문자열은 모두 a와 h로만 이루어져 있다.
# a의 개수는 0보다 크거나 같고, 999보다 작거나 같으며, 항상 h는 마지막에 하나만 주어진다.
# 출력
# 재환이가 그 병원에 가야하면 "go"를, 아니면 "no"를 출력한다.

if len(input())>=len(input()):
    print("go")
else:
    print("no")


# 2845 번
# 문제
# 파티가 끝나고 나면, 사람들은 누가 파티에 왔는지와 얼마나 많은 사람들이 왔는지를 궁금해한다.
# 보통 파티는 매우 크게 열리기 때문에, 정확하게 몇 명이 참가했는지 알 수가 없다.
# 지난주 토요일에 상근이는 자신의 3학년 진학을 기념하면서 매우 성대한 파티를 열었다.
# 그리고, 상근이는 1m2당 몇 명의 사람이 있었는지 알고있다.
# 상근이의 파티는 정말 엄청난 규모였기 때문에, 대부분의 신문에도 기사가 실렸다.
# 상근이는 서로 다른 5개의 신문을 보면서 그 기사에 적혀져있는 참가자의 수를 적었다.
# 상근이는 자신이 알고있는 참가자의 수가 정확하다고 생각한다.
# 각 신문 기사에 실려있는 참가자의 수가 몇 명 만큼 잘못되어있는지 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 1m2당 사람의 수 L (1 ≤ L ≤ 10)과 파티가 열렸던 곳의 넓이 P (1 ≤ P ≤ 1000)가 주어진다.
# 둘째 줄에는 각 기사에 실려있는 참가자의 수가 주어진다.
# 106보다 작은 양의 정수 5개가 주어진다.
# 출력
# 출력은 첫째 줄에 다섯 개의 숫자를 출력해야 한다.
# 이 숫자는 상근이가 계산한 참가자의 수와  각 기사에 적혀있는 참가자의 수의 차이이다.

L, P = map(int,input().split())
news = list(map(int,input().split()))
print(*[news[i]-L*P for i in range(5)])


# 4504 번
# 문제
# 정수 n(0 < n < 1000)과 수의 목록이 주어졌을 때,
# 목록에 들어있는 수가 n의 배수인지 아닌지를 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 n이 주어진다.
# 다음 줄부터 한 줄에 한 개씩 목록에 들어있는 수가 주어진다.
# 이 수는 0보다 크고, 10,000보다 작다. 목록은 0으로 끝난다.
# 출력
# 목록에 있는 수가 n의 배수인지 아닌지를 구한 뒤 예제 출력처럼 출력한다.
# 예제 입력 1
# 3
# 1
# 7
# 99
# 321
# 777
# 0
# 예제 출력 1
# 1 is NOT a multiple of 3.
# 7 is NOT a multiple of 3.
# 99 is a multiple of 3.
# 321 is a multiple of 3.
# 777 is a multiple of 3.

n=int(input())
l=[]
while True:
    m=int(input())
    if m==0:
        break
    l.append(m)
for i in l:
    if i%n==0:
        print(f"{i} is a multiple of {n}.")
    else:
        print(f"{i} is NOT a multiple of {n}.")


# 11575 번
# 문제
# 서쪽나라에서 특수훈련을 받은 정은이는 동쪽나라로 침투를 하게 되었다.
# 뛰어난 스파이였던 정은이는 동쪽나라의 정보를 입수하게 되었고
# 정보를 안전하게 서쪽나라로 전달하기 위해 아핀 암호(Affine Cipher)를 이용하기로 하였다.
# 아핀 암호는 다음과 같은 식을 통해 구할 수 있다.
# E(X) = (aX + b) mod 26
# A부터 Z까지의 알파벳을 차례대로 0, 1, 2, ... , 25 라고 하자.
# a = 3이고, b = 1인 경우에 알파벳 A를 아핀 암호식에 대입하면
# E(0) = (3 × 0 + 1) mod 26 이 되어 암호화된 결과는 B가 된다.
# a와 b, 그리고 알파벳 대문자로만 구성된 평문이 주어졌을 때,
# 이를 암호문으로 치환하는 프로그램을 작성하라.
# 입력
# 입력의 첫 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 50) 가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 두 정수 a와 b(0 < a, b ≤ 1,000,000)의 값이 주어진다.
# a는 26과 서로소이다.
# 각 테스트케이스의 두 번째 줄에는 평문 s가 주어진다.
# 평문의 길이 |s|는 0보다 크고 1,000,000보다 작다.
# 출력
# 각 테스트 케이스마다 한 줄에 한 개씩 평문 s를 암호문으로 치환한 결과를 출력한다.
# 예제 입력 1
# 2
# 3 1
# IAMSPY
# 5 3
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 예제 출력 1
# ZBLDUV
# DINSXCHMRWBGLQVAFKPUZEJOTY

for _ in range(int(input())):
    a,b = map(int,input().split())
    s=input()
    t=""
    for i in s:
        # E(X) = (aX + b) mod 26
        t+=chr((a*(ord(i)-65)+b)%26+65)
    print(t)


# 2774 번
# 문제
# 윤정이는 뭐든지 아름다운 것이 좋다고 생각한다.
# 그래서 윤정이는 사물을 볼 때 자신이 정한 방법으로 아름다운 정도를 평가한다.
# 윤정이는 수를 볼 때도 이런 아름다운 수의 정도를 따지는데,
# 윤정이에게 있어서 아름다운 수의 정도는 그 수를 이루고 있는 10진수의 서로 다른 숫자의 개수를 의미한다.
# 예를 들어 122이라는 수는 1과 2 라는 2개의 숫자로 이루어져 있으므로 아름다운 정도가 2가 된다.
# 윤정이의 방법으로 여러 수들의 아름다운 정도를 알아보자.
# 입력
# 첫째 줄에는 테스트 케이스의 개수 T가 주어진다.
# 다음 줄부터는 아름다운 정도를 알고 싶은 수 X(1 ≤ X ≤ 1000000000)가 주어진다.
# 출력
# 각각의 테스트 케이스마다 X의 아름다운 정도를 한 줄에 하나씩 입력으로 주어진 순서대로 출력한다.

for _ in range(int(input())):
    print(len(set(input())))


# 1453 번
# 문제
# 세준이는 피시방에서 아르바이트를 한다.
# 세준이의 피시방에는 1번부터 100번까지 컴퓨터가 있다.
# 들어오는 손님은 모두 자기가 앉고 싶은 자리에만 앉고싶어한다.
# 따라서 들어오면서 번호를 말한다.
# 만약에 그 자리에 사람이 없으면 그 손님은 그 자리에 앉아서 컴퓨터를 할 수 있고,
# 사람이 있다면 거절당한다.
# 거절당하는 사람의 수를 출력하는 프로그램을 작성하시오.
# 자리는 맨 처음에 모두 비어있고,
# 어떤 사람이 자리에 앉으면 자리를 비우는 일은 없다.
# 입력
# 첫째 줄에 손님의 수 N이 주어진다.
# N은 100보다 작거나 같다.
# 둘째 줄에 손님이 들어오는 순서대로 각 손님이 앉고 싶어하는 자리가 입력으로 주어진다.
# 출력
# 첫째 줄에 거절당하는 사람의 수를 출력한다.

int(input())
c=list(map(int,input().split()))
print(len(c)-len(set(c)))


# 5586 번
# 문제
# 입력으로 주어지는 문자열에서 연속으로 3개의 문자가 JOI 또는 IOI인 곳이 각각 몇 개 있는지 구하는 프로그램을 작성하시오.
# 문자열은 알파벳 대문자로만 이루어져 있다.
# 예를 들어, 아래와 같이 "JOIOIOI"에는 JOI가 1개, IOI가 2개 있다.
# 입력
# 첫째 줄에 알파벳 10000자 이내의 문자열이 주어진다.
# 출력
# 첫째 줄에 문자열에 포함되어 있는 JOI의 개수, 둘째 줄에 IOI의 개수를 출력한다.

j,i=0,0 # 정규 표현식은 나중에 공부...
S=input()
for x in range(len(S)):
    if x==len(S)-2:
        break
    if S[x:x+3]=="JOI":
        j+=1
    elif S[x:x+3]=="IOI":
        i+=1
print(f"{j}\n{i}")


# 2702 번

# 문제
# 두 정수 a와 b 최소공배수는 두 수의 공통된 배수 중 가장 작은 수이고,
# 최대공약수는 두 수의 공통된 약수중 가장 큰 수이다.
# a와 b가 주어졌을 때, 최소공배수와 최대공약수를 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1<=T<=1,000)가 주어진다.
# 각 테스트 케이스는 두 정수 a와 b로 이루어져 있고, 공백으로 구분되어 있다. (1 <= a,b <= 1,000)
# 출력
# 각 테스트 케이스에 대해 최소공배수와 최대공약수를 차례대로 출력한다.

# 풀이 1
def diviser(num):
    divs = []
    for i in range(1, num + 1):
        if num % i == 0:
            divs.append(i)
    return divs

for _ in range(int(input())):
    a, b = map(int, input().split())
    dis_a = diviser(a)
    dis_b = diviser(b)
    max_div = max([x for x in dis_a if x in dis_b])
    min_mul = int(a * b / max_div)
    print(f"{min_mul} {max_div}")

# 풀이 2
from math import lcm, gcd
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(f"{lcm(a,b)} {gcd(a,b)}")


# 5656 번
# 문제
# C언어의 비교 연산자는 아래 표에 나와있다.
# 연산자	뜻
# >   	크다
# >=	    크거나 같다
# <	    작다
# <=	    작거나 같다
# ==  	같다
# !=	    같지 않다
# 이 연산자는 두 피연산자를 비교하고, (왼쪽 값과 오른쪽 값) true또는 false (1 또는 0)을 리턴한다.
# 예를 들어, 2 > 3은 "false"를 리턴하고 (2는 3보다 작기 때문),
# 3 != 4는 "true", 3 >= 3은 "true"를 리턴한다.
# C언어의 비교 연산식이 주어졌을 때, 결과를 구하는 프로그램을 작성하시오.
# 입력
# 입력은 최대 12000줄로 이루어져 있다.
# 각 줄은 두 정수 a, b가 주어지며,
# 정수 사이에는 연산자 ">", ">=", "<", "<=", "==", "!="중 하나가 주어진다.
# 연산자와 피연산자 사이에는 공백이 하나 있으며,
# 연산자로 "E"가 주어진 경우에는 프로그램을 끝낸다. (-10000 ≤ a,b ≤ 10000)
# 출력
# 입력의 각 줄 마다 입력으로 주어진 식의 결과가 "true"인지 "false"인지 출력한다.

cnt=0
while True:
    a = input().split()
    b,c,d=int(a[0]),a[1],int(a[2])
    cnt+=1
    if c == "E":
        break
    if c == ">":
        bol=b > d
    elif c == ">=":
        bol=b >= d
    elif c == "<":
        bol=b < d
    elif c == "<=":
        bol=b <= d
    elif c == "==":
        bol=b == d
    else:
        bol=b != d
    print(f"Case {cnt}: {str(bol).lower()}")


# 2720 번
# 문제
# 미국으로 유학간 동혁이는 세탁소를 운영하고 있다.
# 동혁이는 최근에 아르바이트로 고등학생 리암을 채용했다.
# 동혁이는 리암에게 실망했다.
# 리암은 거스름돈을 주는 것을 자꾸 실수한다.
# 심지어 $0.5달러를 줘야하는 경우에 거스름돈으로 $5달러를 주는것이다!
# 어쩔수 없이 뛰어난 코딩 실력을 발휘해 리암을 도와주는 프로그램을 작성하려고 하지만,
# 디아블로를 하느라 코딩할 시간이 없어서 이 문제를 읽고 있는 여러분이 대신 해주어야 한다.
# 거스름돈의 액수가 주어지면 리암이 줘야할
# 쿼터(Quarter, $0.25)의 개수,
# 다임(Dime, $0.10)의 개수,
# 니켈(Nickel, $0.05)의 개수,
# 페니(Penny, $0.01)의 개수를 구하는 프로그램을 작성하시오.
# 거스름돈은 항상 $5.00 이하이고, 손님이 받는 동전의 개수를 최소로 하려고 한다.
# 예를 들어, $1.24를 거슬러 주어야 한다면, 손님은 4쿼터, 2다임, 0니켈, 4페니를 받게 된다.
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 거스름돈 C를 나타내는 정수 하나로 이루어져 있다.
# C의 단위는 센트이다. (1달러 = 100센트) (1<=C<=500)
# 출력
# 각 테스트케이스에 대해 필요한 쿼터의 개수, 다임의 개수, 니켈의 개수, 페니의 개수를 공백으로 구분하여 출력한다.
# 예제 입력 1
# 3
# 124
# 25
# 194
# 예제 출력 1
# 4 2 0 4
# 1 0 0 0
# 7 1 1 4

coin=[25,10,5,1]
for _ in range(int(input())): # T
    c=int(input())
    b=[0]*4
    for i in range(4):
        b[i]=int(c//coin[i])
        c%=coin[i]
    # b[0]=int(c//25)
    # c%=25
    # b[1]=int(c//10)
    # c%=10
    # b[2]=int(c//5)
    # c%=5
    # b[3]=int(c//1)
    print(*b)


# 2495 번
# 문제
# 여덟 자리의 양의 정수가 주어질 때,
# 그 안에서 연속하여 같은 숫자가 나오는 것이 없으면 1을 출력하고,
# 있으면 같은 숫자가 연속해서 나오는 구간 중 가장 긴 것의 길이를 출력하는 프로그램을 작성하라.
# 예를 들어 세 개의 숫자 12345123, 17772345, 22233331이 주어졌다고 하자.
# 12345123은 연속하여 같은 숫자가 나오는 것이 없으므로 1을 출력하고,
# 17772345는 7이 세 개 연속하여 나오므로 3을 출력하며,
# 22233331의 경우에는 2가 세 개, 3이 네 개 연속해서 나오므로 그 중 큰 값인 4를 출력하여야 한다.
# 입력
# 첫째 줄부터 셋째 줄까지 각 줄에 하나씩 세 개의 여덟 자리 양의 정수가 주어진다.
# 출력
# 첫째 줄에서 셋째 줄까지 한 줄에 하나씩 각 입력된 수 내에서 같은 숫자가 연속하여 나오는 가장 긴 길이를 입력 순서대로 출력한다.
# 예제 입력 1
# 12345123
# 17772345
# 22233331
# 예제 출력 1
# 1
# 3
# 4

for _ in range(3):
    b=[]
    num=input()
    for i in range(0,10):
        a=[str(i)*j for j in range(1,9)]
        b.append(max(list(map(lambda x:a.index(x)+1 if x in num else 0 ,a))))
    print(max(b))


# 2420 번
# 문제
# 사파리월드는 인터넷으로만 존재하는 미스테리한 나라이다.
# 사파리월드에는 2개의 서브도메인이 seunghwan.royal.gov.sw와 kyuhyun.royal.gov.sw 이 있는데,
# 이것이 couple.royal.gov.sw으로 합쳐질 것이다.
# 그러나 도메인 관리 센터 SWNIC(센터장: 김동규)에는 엄격한 룰이 있다.
# 두 서브도메인을 합칠 때, 유명도의 차이가 너무 차이나지 않을 경우에만 두 서브도메인을 결혼시키는 것이다. 서브도메인의 유명도는 정수이다. 두 서브도메인의 유명도가 주어졌을 때, 그 차이를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 두 도메인의 유명도 N과 M이 주어진다. (-2,000,000,000 ≤ N, M ≤ 2,000,000,000)
#
# 출력
# 첫째 줄에 두 유명도의 차이 (|N-M|)을 출력한다.
















# 1251 번
# 문제
# 알파벳 소문자로 이루어진 단어를 가지고 아래와 같은 과정을 해 보려고 한다.
# 먼저 단어에서 임의의 두 부분을 골라서 단어를 쪼갠다.
# 즉, 주어진 단어를 세 개의 더 작은 단어로 나누는 것이다.
# 각각은 적어도 길이가 1 이상인 단어여야 한다.
# 이제 이렇게 나눈 세 개의 작은 단어들을 앞뒤를 뒤집고, 이를 다시 원래의 순서대로 합친다.
# 예를 들어,
# 단어 : arrested
# 세 단어로 나누기 : ar / rest / ed
# 각각 뒤집기 : ra / tser / de
# 합치기 : ratserde
# 단어가 주어지면, 이렇게 만들 수 있는 단어 중에서
# 사전순으로 가장 앞서는 단어를 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 영어 소문자로 된 단어가 주어진다.
# 길이는 3 이상 50 이하이다.
# 출력
# 첫째 줄에 구하고자 하는 단어를 출력하면 된다.


# 예제 입력 1
# mobitel
# 예제 출력 1
# bometil



n=len("aba")
lam = lambda n: [[[x,y,n-x-y] for x in range(n) for y in range(x+1, n-1)] for _ in range(n)]
print(lam(n))

print(list(map(lambda x: [x,n-x-y],range(1,n-2))))





from itertools import combinations
for i in combinations(range(10),3):
    print(i)


list(map(lambda x,y: [x,y], [x for x in range(5)]), [y for y in range(5,10)])




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


# 2086 번 - 시간 초과
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

# 풀이 1 - 메모리 초과
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

# 풀이 2 - 시간 초과
# from sys import *
# input=stdin.readline
fib = [0,1,1]
getdata = list(map(int,input().split()))
a = min(getdata)
b = max(getdata)
if a==b==1:
    print(1)
else:
    while True:
        if b>2:
            b-=1
            fib.append((fib[-1]+fib[-2])%10**9)
        if a>0:
            a-=1
            fib.pop(0)
        if a==0 and b<3:
            break
    print(sum(fib)%10**9)


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

# 풀이 2
from time import *
while True:
    N=int(input())
    stt = time()
    if N==0:
        break
    elif N<4:
        print(1)
        continue
    n=[i for i in range(2,2*N+1) if i%2!=0 and i%3!=0]
    for i in n:
        if i not in n:
            continue
        n=[j for j in n if j%i!=0]
        if i>N:
            n+=[i]
            break
    print(f"""N={N} ~ {n} ~ 2N={2*N}""")
    print(len(n))
    print(time() - stt)


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
# from sys import *
# input = stdin.readline
count = 0 # 횟수 체크 변수 선언
gomgom=[]
for _ in range(int(input())):
    log = input()
    if log == "ENTER": # 채팅 로그가 "입장"이면 채팅 로그 리스트 초기화
        gomgom = []
    elif log not in gomgom: # 채팅 로그 리스트 내에 닉네임이 없을 경우 닉네임 삽입하고, 곰곰티콘 횟수 1회 증가
        gomgom.append(log)
        count += 1
print(count)

# 풀이 2
# from sys import *
# input = stdin.readline
count = 0 # 횟수 체크 변수 선언
n = int(input())
gomgom = [input() for _ in range(n)]

gom = []
for i in gomgom:
    if i == "ENTER": # 채팅 로그가 "입장"이면 채팅 로그 리스트 초기화
        gom = []
    elif i not in gom: # 채팅 로그 리스트 내에 닉네임이 없을 경우 닉네임 삽입하고, 곰곰티콘 횟수 1회 증가
        gom.append(i)
        count += 1
print(count)


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


# 1033 번
# 문제
# august14는 세상에서 가장 맛있는 칵테일이다.
# 이 칵테일을 만드는 정확한 방법은 아직 세상에 공개되지 않았지만, 들어가는 재료 N개는 공개되어 있다.
# 경근이는 인터넷 검색을 통해서 재료 쌍 N-1개의 비율을 알아냈고,
# 이 비율을 이용해서 칵테일에 들어가는 전체 재료의 비율을 알아낼 수 있다.
# 총 재료 쌍 N-1개의 비율이 입력으로 주어진다.
# 이때, 칵테일을 만드는데 필요한 각 재료의 양을 구하는 프로그램을 작성하시오.
# 이때, 필요한 재료의 질량을 모두 더한 값이 최소가 되어야 한다.
# 칵테일을 만드는 재료의 양은 정수이고, 총 질량은 0보다 커야한다.
# 비율은 "a b p q"와 같은 형식이고, a번 재료의 질량을 b번 재료의 질량으로 나눈 값이 p/q라는 뜻이다.
#
# 입력
# 첫째 줄에 august14를 만드는데 필요한 재료의 개수 N이 주어지며,
# N은 10보다 작거나 같은 자연수이다.
# 둘째 줄부터 N-1개의 줄에는 재료 쌍의 비율이 한 줄에 하나씩 주어지는데,
# 문제 설명에 나온 형식인 "a b p q"로 주어진다.
# 재료는 0번부터 N-1까지이며, a와 b는 모두 N-1보다 작거나 같은 음이 아닌 정수이다.
# p와 q는 9보다 작거나 같은 자연수이다.
#
# 출력
# 첫째 줄에 칵테일을 만드는데 필요한 각 재료의 질량을 0번 재료부터 순서대로 공백으로 구분해 출력한다.

N = int(input())
ingrd = [0] * N
for i in range(N-1):
  a, b, c, d = map(int,input().split())
  if ingrd[a] == 0 and ingrd[b] == 0:
    ingrd[a] = c
    ingrd[b] = d


# 1016 번번
# 문제
#어떤 정수 X가 1보다 큰 제곱수로 나누어 떨어지지 않을 때, 그 수를 제곱ㄴㄴ수라고 한다. 제곱수는 정수의 제곱이다. min과 max가 주어지면, min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수가 몇 개 있는지 출력한다.
# 입력
# 첫째 줄에 두 정수 min과 max가 주어진다.
# 출력
# 첫째 줄에 min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수의 개수를 출력한다.
# 제한
# 1 ≤ min ≤ 1,000,000,000,000
# min ≤ max ≤ min + 1,000,000

from time import time
# min, max 배분
min_, max_ = map(int,input().split())
start = time()

# sqrt(max)까지 제곱수 리스트 만들기
max_sqrt = int((max_**0.5+1))
power = [i**2 for i in range(2, max_sqrt)]

# min~max 사이의 숫자에 대해서 리스트 만들기
numbers = [i for i in range(min_, max_+1)]
count = 0

# numbers의 element인 i를 power의 element인 j로 나눠서 나머지가 0일 때 i는 제곱ㄴㄴ수가 아님
count = list(map(lambda i,j: (i,j), numbers, power))
# for i in numbers:
#   for j in power:
#     if i%j == 0:
#       count += 1
#       break
print(count)

# print(len(numbers) - count)

print(f"time spend = {round(time() - start, 5)}")


# 10944번
# 문제
# 1부터 10,000까지 정수 중에서 하나를 출력한다.
# 이 수가 채점 프로그램이 랜덤으로 얻은 수와 같으면 이 문제를 맞힐 수 있다.
# 채점 프로그램은 채점을 할 때마다 랜덤을 수행한다.
# 입력
# 이 문제는 입력이 없다.
# 출력
# 첫째 줄에 1부터 10,000까지 정수 중에서 하나를 출력한다.

from random import random
print(int(random()*10000))


# 문제
# 666은 종말을 나타내는 숫자라고 한다.
# 따라서, 많은 블록버스터 영화에서는 666이 들어간 제목을 많이 사용한다.
# 영화감독 숌은 세상의 종말 이라는 시리즈 영화의 감독이다.
# 조지 루카스는 스타워즈를 만들 때,
# 스타워즈 1, 스타워즈 2, 스타워즈 3, 스타워즈 4, 스타워즈 5, 스타워즈 6과 같이 이름을 지었고,
# 피터 잭슨은 반지의 제왕을 만들 때,
# 반지의 제왕 1, 반지의 제왕 2, 반지의 제왕 3과 같이 영화 제목을 지었다.
# 하지만 숌은 자신이 조지 루카스와 피터 잭슨을 뛰어넘는다는 것을 보여주기 위해서
# 영화 제목을 좀 다르게 만들기로 했다.
# 종말의 숫자란 어떤 수에 6이 적어도 3개이상 연속으로 들어가는 수를 말한다.
# 제일 작은 종말의 숫자는 666이고, 그 다음으로 큰 수는 1666, 2666, 3666, .... 과 같다.
# 따라서, 숌은 첫 번째 영화의 제목은 세상의 종말 666,
# 두 번째 영화의 제목은 세상의 종말 1666 이렇게 이름을 지을 것이다.
# 일반화해서 생각하면, N번째 영화의 제목은 세상의 종말 (N번째로 작은 종말의 숫자) 와 같다.
# 숌이 만든 N번째 영화의 제목에 들어간 숫자를 출력하는 프로그램을 작성하시오.
# 숌은 이 시리즈를 항상 차례대로 만들고, 다른 영화는 만들지 않는다.
# 입력
# 첫째 줄에 숫자 N이 주어진다. N은 10,000보다 작거나 같은 자연수이다.
# 출력
# 첫째 줄에 N번째 영화의 제목에 들어간 수를 출력한다.

def six(n):
  if "666" in str(n):
    return n
  else:
    return

sixes = list(set(map(six, range(1,4000000))))
sixes.remove(None)
sixes.sort()
N=int(input())
print(sixes[N-1])




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