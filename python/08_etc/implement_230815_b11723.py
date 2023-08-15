# 집합 (s5, 29.303%)
# source : https://www.acmicpc.net/problem/11723
# keyword : 구현
# return : 주어진 연산 수행하면서 check 연산 결과 출력
"""
1. 문제
- add(x) : S에 x 추가 (1<=x<=20), x가 이미 있으면 연산 무시
- remove(x) : S에서 x 제거, x가 없는 경우에는 연산 무시
- check(x) : S에 x가 있으면 1, 없으면 0 출력
- toggle(x) : S에 x가 있으면 x 제거, 없으면 x 추가
- all : S를 {1, 2, ..., 20} 으로 변경
- empty : S를 공집합으로 변경

2. 입력
- 수행해야 하는 연산의 수 M (1<=M<=3,000,000)
- 연산
"""

import sys
input = sys.stdin.readline
S = set()
all = set(str(i) for i in range(1, 21))
for _ in range(int(input())):
    op = input().rstrip().split()
    if op[0] == 'all':
        S = all.copy()
    elif op[0] == 'empty':
        S = set()
    elif op[0] == 'add':
        S.add(op[1])
    elif op[0] == 'remove':
        if op[1] in S:
            S.remove(op[1])
    elif op[0] == 'toggle':
        if op[1] in S:
            S.remove(op[1])
        else:
            S.add(op[1])
    else:
        print(1 if op[1] in S else 0)



"""
테스트케이스

26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1
---결과 출력
1
1
0
1
0
1
0
1
0
1
1
0
0
0
1
0
"""
