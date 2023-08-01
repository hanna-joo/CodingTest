# 치킨 거리
# source : https://www.acmicpc.net/problem/15686
# keyword : 구현
# return : 폐업시키지 않을 치킨집을 M개 골랐을 때, 도시의 치킨 거리의 최솟값 출력

"""
1. 문제
- 치킨 거리 : 집과 가장 가까운 치킨집 사이의 거리
- 도시 치킨 거리 : 모든 집의 치킨 거리 합
- 치킨 거리를 최소화하면서 치킨집을 M개로 만드는 방법(폐업)

2. 입력 및 제한
- N(2<=N<=50), M(1<=M<=13)
- 도시 정보
    - 0 : 빈 칸
    - 1 : 집 (1개 이상 2N개 미만)
    - 2 : 치킨집 (M개 이상 13개 이하)

3. 로직
- 폐업하지 않아도 되는 경우
    - 바로 치킨 거리 계산 (집과 치킨집 그대로)
- 폐업해야 하는 경우
    - 치킨집 조합 구하기
    - 해당 치킨집 조합으로 치킨 거리 계산
    - 최솟값 업데이트
"""


import sys, itertools
input = sys.stdin.readline

# 치킨 거리 구하기
def dist(home, chicken):
    total = 0
    for r1, c1 in home:
        tmp = sys.maxsize
        for r2, c2 in chicken:
            tmp = min(tmp, abs(r1-r2) + abs(c1-c2))
        total += tmp
    return total

# 치킨 집과 집 위치 저장
N, M = map(int, input().split())
home, chicken = [], []
for i in range(N):
    row = [*map(int, input().split())]
    for j in range(N):
        if row[j] == 1:
            home.append((i, j))
        elif row[j] == 2:
            chicken.append((i, j))

# 폐업하지 않아도 되는 경우
if len(chicken) <= M:
    ans = dist(home, chicken)
# 폐업해야 하는 경우
else:
    # 오픈 가능한 치킨집 조합
    nCr = itertools.combinations(chicken, M)
    ans = sys.maxsize
    for comb in nCr:
        ans = min(ans, dist(home, comb))
    
print(ans)


"""
테스트 케이스 : 5 / 10 / 11 / 32

5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2

5 1
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0

5 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
"""