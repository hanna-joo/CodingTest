# problem : https://www.acmicpc.net/problem/1012
# keyword : dfs/bfs
# return : 해충 방지를 위해 필요한 배추흰지렁이 마리 수

"""
1. 문제
- 1 : 배추 심은 땅
- 0 : 배추 안 심은 땅

2. 입력
- 테스트 케이스 개수
- 가로길이, 세로길이, 배추 위치 개수
- 배추 위치
"""

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

# 배추 구역 탐색
def bfs(x, y, ground):
    w, h = len(ground[0]), len(ground)
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = deque([(x, y)])
    ground[y][x] = 0
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if (0<=nx<w) and (0<=ny<h):
                if ground[ny][nx] == 1:
                    queue.append((nx, ny))
                    # 방문한 배추는 0으로 변경
                    ground[ny][nx] = 0

# 필요한 지렁이 개수
def need_worm():
    # 땅 만들기
    w, h, cabbage_cnt = map(int, input().split())
    ground = [[0 for _ in range(w)] for _ in range(h)]
    cabbage_loc = list()
    
    for _ in range(cabbage_cnt):
        x, y = map(int, input().split())
        # 양배추 심기
        ground[y][x] = 1
        # 양배추 위치 저장
        cabbage_loc.append((x, y))

    worm_cnt = 0
    for x, y in cabbage_loc:
        # 아직 방문 안한 배추만 탐색 시작
        if ground[y][x] == 1:
            bfs(x, y, ground)
            worm_cnt += 1

    return worm_cnt


test_cnt = int(input())
for _ in range(test_cnt):
    print(need_worm())