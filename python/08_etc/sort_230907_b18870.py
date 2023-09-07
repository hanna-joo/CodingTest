# 좌표 압축 (s2, 39.721%)
# source : https://www.acmicpc.net/problem/18870
# keyword : 정렬
# return : 좌표 압축한 값 출력

"""
1. 문제
- 수직선 위에 N개의 좌표가 있을 때 좌표 압축
    - X'i의 값 = Xi보다 작은 값의 개수(중복 없음)
    - [4, 2, -9, -10] -> [3, 2, 1, 0]

2. 입력 및 제한
- N (1 <= N <= 1,000,000)
- X1 ~ Xi ~ Xn (-10^9 <= Xi <= 10^9)

3. 로직
- 파이썬의 sorted() : O(NlogN)
"""


import sys
#input = sys.stdin.readline
stdin = sys.stdin.buffer

stdin.readline()
X = list(map(int, stdin.read().split()))
rank = {x: i for i, x in enumerate(sorted(set(X)))}
print(' '.join(map(str, [rank[x] for x in X])))


"""
테스트케이스

5
2 4 -10 4 -9
---
2 3 0 3 1

6
1000 999 1000 999 1000 999
---
1 0 1 0 1 0
"""