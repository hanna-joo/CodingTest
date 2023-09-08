# N과 M(12) (s3, 80.998%)
# source : https://www.acmicpc.net/problem/15666
# keyword : 조합
# return : 문제의 조건을 만족하는 수열을 공백으로 구분하여 출력

"""
1. 문제
- 아래 조건을 만족하는 길이가 M인 수열 모두 출력
    - 주어진 N개의 자연수 중에서 M개
    - 같은 수 중복으로 골라도 됨
    - 고른 수열은 오름차순이어야 함 (A1<=A2<=...<=Ak)

2. 입력 및 제한
- N, M (1<=M<=N<=8)
- X1 ~ Xi ~ Xn (1<=Xi<=10,000)

3. 로직
- 순열 : 서로 다른 n개에서 r개를 택하여 일렬로 나열하는 경우의 수
    - nPr = n! / (n-r)!
    - permutations(iterable, 3)
- 조합 : 서로 다른 n개에서 순서 생각하지 않고 r개를 택하는 경우의 수
    - nCr = n! / (n-r)!r!
    - combinations(iterable, 3)
- 중복 순열 : 중복 가능한 n개에서 r개 나열하는 경우의 수
    - nㅠr = n^r
    - product(iterable, repeat=3)
- 중복 조합 : 중복 가능한 n개에서 순서 생각하지 않고 r개 택하는 경우의 수
    - nHr = n+r-1Cr
    - combinations_with_replacement(iterable, 3)
"""


import sys
from itertools import combinations_with_replacement as cwr
input = sys.stdin.readline
N, M = map(int, input().split())
nums = sorted(set(map(int, input().split())))

print('\n'.join(' '.join(map(str, combi)) for combi in cwr(nums, M)))


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
1 1
1 7
1 9
7 7
7 9
9 9

4 4
1 1 2 2
---
1 1 1 1
1 1 1 2
1 1 2 2
1 2 2 2
2 2 2 2
"""