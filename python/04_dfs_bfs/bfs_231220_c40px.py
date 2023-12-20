# SK 기출유형 : 가중치가 동일한 그래프에서의 BFS / 나이트
# source : https://www.codetree.ai/cote/18/problems/knight-movements/description
# keyword : bfs
# return : 시작점에서 도착점까지 도달하는데 필요한 이동 횟수 최솟값

"""
1. 문제 : 나이트가 시작 위치에서 도착 위치까지 도달하는 데 필요한 최소 이동 횟수 출력
2. 제한 : 1<=n<=100
"""

from collections import deque

n = int(input())
points = [i-1 for i in map(int, input().split())]
s, e = points[:2], points[2:]
graph = [[0 for _ in range(n)] for _ in range(n)]
steps = [[0 for _ in range(n)] for _ in range(n)]
dy, dx = [-2, -2, -1, -1, 1, 1, 2, 2], [-1, 1, -2, 2, -2, 2, -1, 1]
q = deque([s])
graph[s[0]][s[1]] = 1

while q:
    cy, cx = q.popleft()
    for i in range(8):
        ny, nx = cy+dy[i], cx+dx[i]
        if ny == e[0] and nx == e[1]:
            print(steps[cy][cx]+1)
            exit()
        if 0<=ny<n and 0<=nx<n and not graph[ny][nx]:
            graph[ny][nx] = 1
            steps[ny][nx] = steps[cy][cx] + 1
            q.append([ny, nx])

print(-1)