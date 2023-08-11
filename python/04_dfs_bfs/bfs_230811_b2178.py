# 미로 탐색 (s1, 43.230%)
# source : https://www.acmicpc.net/problem/2178
# keyword : dfs/bfs
# return : (1,1)에서 (N,M)으로 이동할 때 지나야 하는 최소의 칸 수 출력

"""
1. 문제
- 시작 위치와 도착 위치 칸도 세야 함
- 방향은 상하좌우
- 1은 이동 가능한 칸, 0은 이동 불가능한 칸

2. 입력
- 두 정수 N, M (2<=N, M<=100)
- 미로 정보 붙어서 입력
"""


import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
miro = [[0 for _ in range(M+1)]]
for _ in range(N):
    miro.append([0]+[*map(int, list(input().rstrip()))])

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
q = deque([(1, 1)])
while q:
    cy, cx = q.popleft()
    for i in range(4):
        ny, nx = dy[i]+cy, dx[i]+cx
        if ny<=0 or nx<=0 or ny>N or nx>M:
            continue
        if miro[ny][nx] == 1:    
            miro[ny][nx] = miro[cy][cx] + 1
            q.append((ny, nx))

print(miro[N][M])


"""
테스트케이스 : 15 / 9 / 38 / 13

4 6
101111
101010
101011
111011

4 6
110110
110110
111111
111101

2 25
1011101110111011101110111
1110111011101110111011101

7 7
1011111
1110001
1000001
1000001
1000001
1000001
1111111
"""
