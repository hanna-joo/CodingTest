# N과 M(9) (s2, 49.335%)
# source : https://www.acmicpc.net/problem/15663
# keyword : 순열, 정렬
# return : 문제의 조건을 만족하는 수열을 공백으로 구분하여 출력

"""
1. 문제
- 아래 조건을 만족하는 길이가 M인 수열 모두 출력
    - 주어진 N개의 자연수 중에서 M개

2. 입력 및 제한
- N, M (1<=M<=N<=8)
- X1 ~ Xi ~ Xn (1<=Xi<=10,000)

3. 로직
- 순열
"""


import sys
from itertools import permutations
input = sys.stdin.readline
N, M = map(int, input().split())
print('\n'.join(' '.join(map(str, combi)) for combi in sorted(set(permutations(map(int, input().split()), M)))))
#dict.fromkeys(permutations(arr, int(M)))


"""
테스트케이스

3 1
4 4 2
---
2
4

4 2
9 7 9 1
---
1 7
1 9
7 1
7 9
9 1
9 7
9 9

4 4
1 1 1 1
---
1 1 1 1
"""