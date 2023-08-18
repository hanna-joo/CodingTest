# 단지번호붙이기 (s1, 42.060%)
# source : https://www.acmicpc.net/problem/2667
# keyword : 
# return : 단지수를 출력하고 각 단지에 속하는 집의 수를 오름차순으로 출력

"""
1. 문제
- 상하좌우로 연결된 집은 같은 단지
- 1은 집이 있는 곳, 0은 집이 없는 곳

2. 입력
- 지도의 크기 N (5<=N<=25)
- N개의 자료

3. 로직
- bfs
- visited 대신 graph=0으로 변경
"""


import sys
input = sys.stdin.readline

N = int(input())
graph = [[*map(int, input().rstrip())] for _ in range(N)]

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs(y, x):
    q, cnt = [(y, x)], 1
    graph[y][x] = 0
    while q:
        cy, cx = q.pop(0)
        for k in range(4):
            ny, nx = cy+dy[k], cx+dx[k]
            if ny<0 or nx<0 or ny>=N or nx>=N:
                continue
            if graph[ny][nx]:
                q.append((ny, nx))
                graph[ny][nx] = 0
                cnt += 1
    return cnt

complex = []
for i in range(N):
    for j in range(N):
        if graph[i][j]:
            complex.append(bfs(i, j))

complex.sort()
print(len(complex))
for num in complex:
    print(num)
        

"""
테스트케이스

7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

3
001
100
001
---결과 출력
3
7
8
9

3
1
1
1
"""