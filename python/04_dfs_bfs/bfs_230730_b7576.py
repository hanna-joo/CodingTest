# 토마토
# source : https://www.acmicpc.net/problem/7576
# keyword : dfs/bfs
# return : 토마토가 모두 익게 되는 최소 일수 출력

"""
1. 문제
- 격자 모양 상자의 칸에 토마토 보관
- 하루 지나면 익은 토마토와 상하좌우로 인접해 있는 토마토가 익음
- 모든 토마토가 이미 익었다면 0, 모두 못 익으면 -1

2. 입력
- 상자의 가로M, 세로N (2<=M,N<=1,000)
- 상자에 저장된 토마토 정보 (1-익, 0-안익, -1-빈칸)
- 토마토는 최소 1개 이상

3. 로직
- 예외 처리
- 익은 토마토 위치 별도 저장
- bfs 활용

4. 주의
- UnboundLocalError
    - 반복문/조건문에서 선언한 변수를 반복문/조건문 밖에서 사용
        -> 반복문/조건문이 실행되지 않을 경우 에러 발생
    - 함수 안에서 전역변수에 대해 참조
        -> global로 전역 변수임을 명시하지 않아도 됨
    - 함수 안에서 전역변수에 값 할당(변경)
        -> global로 전역 변수임을 명시 / 매개변수로 전달
"""


import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int, input().split())

graph = []
not_ripe = 0
for _ in range(N):
    row = [*map(int, input().rstrip().split())]
    # 안 익은 토마토 세기
    not_ripe += sum(1 for i in row if i == 0)
    graph.append(row)


def go(graph, not_ripe):
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    # 익은 토마토 좌표 얻기
    ripe = deque()
    day = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                ripe.append((i, j, day))
    # BFS
    while ripe:
        cy, cx, day = ripe.popleft()
        for i in range(4):
            ny, nx = cy+dy[i], cx+dx[i]
            if ny>=N or ny<0 or nx>=M or nx<0:
                continue
            if graph[ny][nx] == 0:
                graph[ny][nx] = 1
                not_ripe -= 1
                ripe.append((ny, nx, day+1))

    return day, not_ripe

# 처음부터 모두 익었을 때
if not_ripe == 0:
    print(0)
else:
    # 창고에서 익히기
    day, not_ripe = go(graph, not_ripe)
    if not_ripe != 0:
        print(-1)
    else:
        print(day)


"""
테스트 케이스 : -1 / 8 / -1 / 6 / 14 / 0

2 2
0 0
0 0

6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

6 4
0 -1 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

6 4
1 -1 0 0 0 0
0 -1 0 0 0 0
0 0 0 0 -1 0
0 0 0 0 -1 1

5 5
-1 1 0 0 0
0 -1 -1 -1 0
0 -1 -1 -1 0
0 -1 -1 -1 0
0 0 0 0 0

2 2
1 -1
-1 1

5 5
0 0 0 0 0
0 -1 -1 -1 -1
0 -1 1 1 0
0 -1 1 1 0
0 -1 0 0 0
"""