# N과 M (2) (s3, 74.104%)
# source : https://www.acmicpc.net/problem/15650
# keyword : 구현
# return : 조건을 만족하는 길이가 M인 수열 모두 출력

"""
1. 문제
- 아래 조건을 만족하는 길이가 M인 수열 모두 출력
    - 1부터 N까지 자연수 중에서 중복 없이 M개 오름차순으로 출력

2. 입력 및 제한
- 자연수 N과 M (1<=M<=N<=8)
"""


from itertools import combinations

N, M = map(int, input().split())
for combi in combinations(range(1, N+1), M):
    print(*combi)


"""
테스트케이스

3 1
---
1
2
3

4 2
---
1 2
1 3
1 4
2 3
2 4
3 4

4 4
---
1 2 3 4
"""