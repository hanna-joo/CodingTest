# 테트로미노 (g4, 36.059%)
# source : https://www.acmicpc.net/problem/14500
# keyword : brute force
# return : 종이에서 테트로미노가 놓인 칸에 쓰인 수들의 합 최대 출력

"""
1. 문제
- 테트로미노 : 정사각형 4개를 이어 붙인 폴리오미노
- 테트로미노 한 개를 종이 위에 적절히 놓았을 때,
- 테트로미노가 놓인 종이 칸에 쓰여 있는 수들의 합 최댓값

2. 입력
- 종이 크기 N, M (4 <= N,M <= 500)
- 종이에 쓰여있는 점수 (1 <= 점수 < 1000)

3. 로직
- bfs + 예외처리
- 모든 점에 대해 아래 반복
    - 상하좌우 이동 (4번까지)
    - 방문한 곳은 미 방문
    - 값 업데이트
- 반복하고나서 방문 리스트 초기화
- 예외 처리 : ㅗㅜㅏㅓ 모양은 dfs로 불가
"""

import sys

input = sys.stdin.readline

paper = []
N, M = map(int, input().split())
for _ in range(N):
    paper.append([*map(int, input().split())])

global ans, visited
visited = [[0 for _ in range(M)] for _ in range(N)]
ans = 0
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(point, depth, total):
    global ans, visited
    if depth == 4:
        if total > ans:
            ans = total
        return
    for i in range(4):
        ny, nx = point[0] + dy[i], point[1] + dx[i]
        if ny < 0 or nx < 0 or ny >= N or nx >= M:
            continue
        if visited[ny][nx]:
            continue
        visited[ny][nx] = 1
        dfs((ny, nx), depth + 1, total + paper[ny][nx])
        visited[ny][nx] = 0


def exception(point):
    global ans
    # 예외 처리
    y, x = point
    tmp = paper[y][x]
    lst = list()
    for k in range(4):
        ty, tx = y + dy[k], x + dx[k]
        if ty < 0 or tx < 0 or ty >= N or tx >= M:
            continue
        tmp += paper[ty][tx]
        lst.append(paper[ty][tx])
    if len(lst) == 3:
        ans = max(ans, tmp)
    if len(lst) == 4:
        for k in lst:
            ans = max(ans, tmp - k)


for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs((i, j), 1, paper[i][j])
        visited[i][j] = 0
        exception((i, j))


print(ans)

"""
테스트케이스 : 19 / 20 / 7

5 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1

4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

4 10
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1
"""
