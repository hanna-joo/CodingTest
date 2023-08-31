# 뱀 (g4, 40.117%)
# source : https://www.acmicpc.net/problem/3190
# keyword : 
# return : 

"""
1. 문제
- 

2. 입력 및 제한
- 

3. 로직
- X초 전까지 이동 및 사과 먹기
- X초 되면 
    - L -> dy, dx = move[i-1]
    - R -> dy, dx = move[i+1]
"""

import sys
input = sys.stdin.readline
N = int(input())
A, B = sorted(map(int, input().split())), sorted(map(int, input().split()), reverse=True)
s = 0
for a, b in zip(A, B):
    s += a * b

print(s)

"""
테스트케이스 : 18 / 80 / 528

5
1 1 1 6 0
2 7 8 3 1

3
1 1 3
10 30 20

9
5 15 100 31 39 0 0 3 26
11 12 13 2 3 4 5 9 1
"""