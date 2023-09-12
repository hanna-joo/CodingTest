# 섬의 개수 (s2, 49.362%)
# source : https://www.acmicpc.net/problem/4963
# keyword : dfs/bfs
# return : 섬의 개수 출력

"""
1. 문제
- 같은 섬 = 가로, 세로, 대각선으로 걸어갈 수 있는 곳
- 1은 섬, 0은 바다

2. 입력 및 제한
- 테스트 케이스 여러 개
    - 지도 너비와 높이 w, h (1<=w,h<=50)
    - 지도 정보 (1, 0)
- 0 0 주어지면 종료

3. 로직
- bfs
"""

from sys import stdin


def bfs(y, x):
    global graph
    q = [(y, x)]
    graph[y][x] = '0'
    while q:
        cy, cx = q.pop(0)
        for i in range(8):
            ny, nx = cy+move[i][0], cx+move[i][1]
            if 0<=ny<h and 0<=nx<w and graph[ny][nx] == '1':
                graph[ny][nx] = '0'
                q.append((ny, nx))
    

move = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
while True:
    w, h = map(int, stdin.readline().split())
    if w == h == 0:
        break
    graph = [stdin.readline().split() for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '1':
                bfs(i, j)
                cnt += 1
            
    print(cnt)


"""
테스트케이스

1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
---
0
1
1
3
1
9
"""