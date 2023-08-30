# 리모컨 (g5, 23.078%)
# source : https://www.acmicpc.net/problem/1107
# keyword : 고장난 버튼 제외하고 100번에서 N번으로 이동하기 위해 눌러야 하는 최소 버튼 수 출력

"""
1. 문제
- 버튼 종류 : 0-9, +-
    - + : 채널+1
    - - : 채널-1, 채널 0인 경우 변화 없음
- 100번에서 N번으로 채널 이동하기 위해 버튼을 최소 몇 번 눌러야하는지 출력

2. 입력
- 이동하려고 하는 채널 N (0<=N<=500,000)
- 고장난 버튼의 개수 M (0<=M<=10)
    - 고장난 버튼 번호

3. 로직
- N이 100번인지 확인
- 사용 가능한 버튼
- 모든 경우의 수 따지기
"""


import sys
sys.setrecursionlimit(100000)

N, *broken = map(int, open(0).read().split())
possible = set(range(0, 10)) - set(broken[1:])

def rec(s):
    global ret
    if len(s) > len(str(N))+1 or s == '0':
        return
    for i in possible:
        ns = s+str(i)
        tmp = abs(int(ns) - N) + len(ns)
        if tmp < ret:
            ret = tmp
        rec(ns)

if N == 100:
    exit(print(0))

ret = abs(N-100)
rec('')
print(ret)


"""
테스트케이스
- 반례 모음 : https://www.acmicpc.net/board/view/31853

5457
3
6 7 8
---6

100
5
0 1 2 3 4
---0

500000
8
0 2 3 4 6 7 8 9
---11117

100
3
1 0 5
---0

14124
0
---5

1
9
1 2 3 4 5 6 7 8 9
---2

80000
2
8 9
---2228

99
0
---1

322
1
2
---6

99999
1
9
---7

1555
8
0 1 3 4 5 6 7 9
---670 (888)
"""
