# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 1 로만 갈 수 있음
# (1, 1) -> (n, m)
# return : case 1 - 목표값으로 가기 위해 지나야 하는 칸의 개수의 최솟값
# return : case 2 - 목표값으로 가는 것이 불가능할 경우 -1

# bfs 필수 요소 : 인접 리스트, 방문 기록, 큐

from collections import deque

# maps에 depth 저장
def solution1(maps, x, y):
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    # 큐에 시작 노드 삽입 후 방문 기록
    queue = deque([(x, y)])
    visited[x][y] = True
    # 큐 비우기
    while queue:
        x, y = queue.popleft()
        # 상하좌우 탐색
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if (nx, ny) == (n-1, m-1):
                return maps[x][y] + 1
            # 좌표 유효성 검사 (0,0) <= (x,y) <= (n,m)
            if 0<=nx<n and 0<=ny<m:
                # 방문X & 이동 가능한 칸(1)
                if not visited[nx][ny] and maps[nx][ny]:
                    # 방문 기록, maps에 depth 업데이트, 큐에 삽입
                    visited[nx][ny] = True
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
    return -1

# depth 별도 저장
def solution2(maps, x, y):
    n, m = len(maps), len(maps[0])
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    visited = [[False] * n for _ in range(m)]
    queue = deque()
    distance = {(x, y): 1}
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        if x == n-1 and y == m-1:
            return distance[(x, y)]
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    distance[(nx, ny)] = distance[(x, y)] + 1
                    queue.append((nx, ny))
    return -1



if __name__ == '__main__':
    test_cases = [[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]], [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]] # 11, -1
    start, end = 0, 0
    for case in test_cases:
        print(solution1(case, start, end))
        print(solution2(case, start, end))

'''
    bool_test
    if bool_test:
        print("숫자 0이면 if문에서 True")
    else:
        print("숫자 0이면 if문에서 False")
'''