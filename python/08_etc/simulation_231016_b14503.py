# 로봇 청소기 (g5, 53.685%)
# source : https://www.acmicpc.net/problem/14503
# keyword : 구현
# return : 방의 상태가 주어졌을 때 청소하는 칸의 개수 출력

"""
1. 문제
- N * M 크기의 직사각형 방
    - 각각의 칸은 벽 또는 빈 칸
    - 처음 빈 칸은 모두 청소되지 않은 칸
- 청소기가 바라보는 방향은 동, 서, 남, 북 중 하나
    - 현재 칸이 청소되지 않은 경우 청소
    - 주변 4칸 중 청소되지 않은 칸이 없으면 -> 방향 유지 + 후진/작동 중지
    - 주변 4칸 중 청소되지 않은 칸이 있으면 -> 반시계 90도 회전 + 청소안된칸인 경우 전진
    
2. 입력 및 제한
- 방의 크기 N, M (3<=N,M<=50)
- 로봇 청소기 위치 (r,c)와 방향 d
    - 0(북), 1(동), 2(남), 3(서)
- 방의 상태 N줄
    - 0(빈 칸), 1(벽)
"""


import sys
input = sys.stdin.readline
N, M = map(int, input().split())
r, c, d = map(int, input().split())
move = [(-1, 0), (0, -1), (1, 0), (0, 1)]
room = [[*map(int, input().split())] for _ in range(N)]
cy, cx = r, c
cnt = 0
while True:
    if room[cy][cx] == 0:
        room[cy][cx] = 2
        cnt += 1
    unclean = False
    tmp = d
    for _ in range(4):
        ny, nx = cy+move[tmp][0], cx+move[tmp][1]
        if room[ny][nx] == 0:
            unclean = True
            break
        tmp = (tmp+1) % 4
    if unclean:
        cy, cx, d = ny, nx, tmp
    else:
        ny, nx = cy-move[d][0], cx-move[d][1]
        if room[ny][nx] == 1:
            break
        cy, cx = ny, nx

print(cnt)


"""
테스트케이스

3 3
1 1 0
1 1 1
1 0 1
1 1 1
---
1

11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
---
57
"""