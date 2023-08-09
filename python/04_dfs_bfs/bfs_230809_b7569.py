# 토마토 (g5, 41.706%)
# source : https://www.acmicpc.net/problem/7569
# keyword : dfs/bfs
# return : 토마토가 모두 익게 되는 최소 일수 출력

"""
1. 문제
- 격자 모양 상자의 칸에 토마토 보관하고 상자를 위, 아래로 겹쳐 놓음
- 하루 지나면 익은 토마토와 위, 아래, 왼쪽, 오른쪽, 앞, 뒤로 인접해 있는 토마토가 익음
- 모든 토마토가 이미 익었다면 0, 모두 못 익으면 -1

2. 입력
- 상자의 가로M, 세로N, 상자수H (2<=M,N<=100 / 1<=H<=100)
- 밑에 있는 상자부터 저장된 토마토 정보 (1-익, 0-안익, -1-빈칸)
- 토마토는 최소 1개 이상

3. 로직
- 익은 토마토 위치 별도 저장 -> 익은 토마토부터 dfs 탐색
- 안 익은 토마토 개수 저장 -> 처음과 마지막에 활용
- 6개 방향 이동 -> 범위내, 안익은 토마토 -> 익히기(day+1, not_ripe-1)
- 아예 안 익은 토마토만 주어졌을 경우 고려
"""


import sys
from collections import deque
input = sys.stdin.readline
M, N, H = map(int, input().split())

not_ripe = 0
ripe = deque()
day = 0

graph = []
for h in range(H):
    box = []
    for r in range(N):
        row = list(map(int, input().split()))
        for c in range(M):
            if row[c] == 0:
                not_ripe += 1
                continue
            if row[c] == 1:
                ripe.append([day, (h, r, c)])
        box.append(row)
    graph.append(box)

dh, dx, dy = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]
if not not_ripe:
    print(0)
else:
    while ripe:
        day, loc = ripe.popleft()
        for i in range(6):
            nh, ny, nx = loc[0]+dh[i], loc[1]+dy[i], loc[2]+dx[i]
            if nh<0 or ny<0 or nx<0 or nh>=H or ny>=N or nx>=M:
                continue
            if graph[nh][ny][nx] == 0:
                graph[nh][ny][nx] = 1
                ripe.append([day+1, (nh, ny, nx)])
                not_ripe -= 1
                
    if not_ripe:
        print(-1)
    else:
        print(day)


"""
테스트 케이스 : -1 / 4 / -1 / 0

5 3 1
0 -1 0 0 0
-1 -1 0 1 1
0 0 0 1 1

5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0

5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0

4 3 2
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
-1 -1 -1 -1
1 1 1 -1
"""