# 모래섬
# keyword : 
# return : 모래섬 개수가 2개 이상이 되려면 최소 며칠 후인지 출력 (-1)

"""
1. 문제 분석
- 모래사장 크기 : 3 <= N, M <= 100
- s[i][j] = 0 : 물에 가라앉은 칸
- s[i][j] = 1 : 모래 칸
- 매일 상하좌우로 인접한 칸 중 물에 가라앉은 칸이 있으면 동시에 물에 가라앉음
- 모래섬 개수가 2개 이상이 되려면 최소 며칠 후인지 출력
- 2개 이상의 모래섬으로 나누어지지 않는 경우 -1 출력

2. 첫 번째
- 0이 들어간 칸의 상하좌우 칸 모두 0으로 변경 > day += 1
- 모래섬 개수가 2개 이상인 경우 멈추고 day 출력
- 모든 칸이 0이 된 경우 멈추고 -1 출력
"""


def biggest_group_1(size, point, info):
    def search(x, y):
        from collections import deque

        q = deque()
        q.append((x, y))
        matrix[x][y] = -1
        group = 1
        
        # 이동 범위 : 상하좌우
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        while q:
            cur = q.popleft()
            for i in range(4):
                nx, ny = cur[0]+dx[i], cur[1]+dy[i]
                if (0 <= nx < size) and (0 <= ny < size):
                    if matrix[nx][ny] == k:
                        q.append((nx, ny))
                        matrix[nx][ny] = -1
                        group += 1
                        
        return group
    
    matrix = list()
    for i in range(size):
        matrix.append(list(map(int, info[i].split())))

    x, y = map(int, point.split())
    k = matrix[x-1][y-1]
    group_max = 0

    for i in range(size):
        for j in range(size):
            if matrix[i][j] == k:
                group_max = max(group_max, search(i, j))

    return group_max


def biggest_group_2(size, point, info):
    from collections import deque
    y, x = map(int, point.split())
    matrix = [[0 for _ in range(size+1)] for _ in range(size+1)]
    visited = [[0 for _ in range(size+1)] for _ in range(size+1)]

    for i in range(1, size+1):
        matrix[i] = [0] + list(map(int, info[i-1].split()))
    
    k = matrix[y][x]

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    group_max = 0

    for i in range(1, size+1):
        for j in range(1, size+1):
            # 이미 방문했거나 k값이 아니라면 스킵
            if visited[i][j] or matrix[i][j] != k:
                continue
            # 방문하지 않았고, k값이라면 탐색 시작
            q = deque()
            visited[i][j] = 1
            # 현재 연결 요소에 있는 정점의 개수 세기
            cnt = 0
            q.append([i, j])
            while q:
                cy, cx = q.popleft()
                # 실제 방문했을 때 정점 개수 +1
                cnt += 1
                for k in range(4):
                    ny, nx = cy + dy[k], cx + dx[k]
                    # 이동할 좌표가 범위를 초과하면 스킵
                    if ny < 1 or nx < 1 or ny > size or nx > size:
                        continue
                    # 이동할 좌표가 방문했거나 k값이 아니라면 스킵
                    if visited[ny][nx] or matrix[ny][nx] != matrix[cy][cx]:
                        continue
                    # 이동할 좌표가 확정되었으면 방문 기록
                    visited[ny][nx] = 1
                    q.append([ny, nx])
            group_max = max(group_max, cnt)

    return group_max


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [(4, '1 2', ['0 0 1 1', '0 1 1 0', '0 0 0 1', '1 1 1 1']),
                  (4, '1 2', ['0 0 1 2', '2 1 1 2', '2 0 0 2', '1 1 1 2'])] # 6, 2

    for case in test_cases:
        print(biggest_group_1(case[0], case[1], case[2]))
        print(biggest_group_2(case[0], case[1], case[2]))
