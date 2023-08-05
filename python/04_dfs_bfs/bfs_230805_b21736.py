# 헌내기는 친구가 필요해
# source : https://www.acmicpc.net/problem/21736
# keyword : dfs/bfs
# return : 도연이가 만날 수 있는 사람 수 출력

"""
1. 문제
- 벽이 아닌 상하좌우로 이동해서 만날 수 있는 사람 수 출력
- 아무도 못 만나면 TT 출력

2. 입력
- 캠퍼스 크기 N, M (1 <= N,M <= 600)
- 캠퍼스 줄 (0-빈공간, X-벽, I-도연, P-사람)

3. 로직
- 상하좌우 확인
- 벽이 아니고, 방문하지 않았다면 큐에 삽입
- P만나면 cnt ++1
"""


import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
campus = []
for i in range(N):
    row = list(input().rstrip())
    # 도연이 위치 저장
    for j in range(M):
        if row[j] == 'I':
            start = (i, j)
    campus.append(row)

visited = [[0 for _ in range(M)] for i in range(N)]
visited[start[0]][start[1]] = 1
q = deque([start])
cnt = 0

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
while q:
    cy, cx = q.popleft()
    for i in range(4):
        ny, nx = cy+dy[i], cx+dx[i]
        if ny<0 or nx<0 or ny>=N or nx>=M:
            continue
        if visited[ny][nx] or campus[ny][nx] == 'X':
            continue
        if campus[ny][nx] == 'P':
            cnt += 1
        q.append((ny, nx))
        visited[ny][nx] = 1

if cnt:
    print(cnt)
else:
    print('TT')


"""
테스트 케이스 : 1 / TT

3 5
OOOPO
OIOOX
OOOXP

3 3
IOX
OXP
XPP
"""