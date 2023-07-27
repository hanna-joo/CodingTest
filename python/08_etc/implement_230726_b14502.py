# problem : https://www.acmicpc.net/problem/14502
# keyword : 구현, 완전 탐색, bfs
# return : 벽 3개를 세워서 얻을 수 있는 안전 영역의 최대 크기 출력

"""
1. 문제
- 바이러스 유출을 막기 위해 연구소에 벽 세우기
- 0 : 빈 칸 / 1 : 벽 / 2 : 바이러스
- 벽은 반드시 3개 세워야 함

2. 입력 및 제한
- 세로 N, 가로 M (3<=N,M<=8)
- 지도의 모양 (0, 1, 2)
- 2<=바이러스 개수(2)<=10
- 3<=빈 칸 개수(0)

3. 로직
- O(N^5) : 완전 탐색 + bfs
- 참고 풀이 : https://www.youtube.com/watch?v=DBXEWJx2mIw
(1) 벽을 3개 세운다
(2) 바이러스를 퍼트린다
(3) 안전 영역의 개수를 센다

4. 포인트
- 바이러스 퍼지기 전과 바이러스 퍼진 후를 나누기
- 둘 다 빈 칸인 경우 안전 영역
"""
import sys
input = sys.stdin.readline

def spread_virus(y, x):
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        # 다음 위치가 범위를 벗어나면 스킵
        if ny<0 or nx<0 or ny>=N or nx>=M: continue
        # 이미 바이러스가 방문했거나 벽이라면 스킵
        if visited[ny][nx] or lab[ny][nx]: continue
        visited[ny][nx] = 1
        spread_virus(ny, nx)

def find_safety(lab):
    global visited
    visited = [[0 for _ in range(M)] for _ in range(N)]
    # (2) 바이러스를 퍼트린다
    for y, x in vir:
        visited[y][x] = 1
        spread_virus(y, x)
    # (3) 안전 영역의 개수를 센다
    cnt = 0
    for i in range(N):
        for j in range(M):
            # 실제로 빈 칸이면서 바이러스가 오지 않았다면 안전영역
            if lab[i][j] == 0 and visited[i][j] == 0:
                cnt += 1
    return cnt

N, M = map(int, input().split())
lab = []
for i in range(N):
    lab.append(list(map(int, input().split())))

# 벽 세울 수 있는 위치 저장
wall = []
vir = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            wall.append([i, j])
        if lab[i][j] == 2:
            vir.append([i, j])

# (1) 벽을 3개 세운다 - wall 내에서 3개 조합(중복X)
ret = 0
for i in range(len(wall)):
    for j in range(i):
        for k in range(j):
            lab[wall[i][0]][wall[i][1]] = 1
            lab[wall[j][0]][wall[j][1]] = 1
            lab[wall[k][0]][wall[k][1]] = 1
            # (2)+(3) 바이러스를 퍼트리고 안전영역을 센다
            ret = max(ret, find_safety(lab))
            # 원상복구 : 세웠던 벽 3개 삭제
            lab[wall[i][0]][wall[i][1]] = 0
            lab[wall[j][0]][wall[j][1]] = 0
            lab[wall[k][0]][wall[k][1]] = 0

print(ret)

"""
테스트 케이스 : 27, 9, 3

7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
"""