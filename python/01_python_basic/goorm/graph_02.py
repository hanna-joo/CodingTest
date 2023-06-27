# 뭉친 K
# keyword : 격자 형태의 그래프, 그래프 탐색
# return : 특정 좌표의 값이 k일 때, k로 이루어진 그룹 중 가장 큰 뭉친 그룹의 크기 출력

"""
1. 연결 요소
- 원래 그래프의 일부 정점과 간선만을 골라서 만든 부분 그래프 중에서
- 다른 부분 그래프에 포함되지 않은 가장 큰 부분 그래프를 연결 요소라고 함
- 한 번의 그래프 탐색으로 방문할 수 있는 모든 정점과 간선이 속한 부분 그래프
- 연결 요소에 속한 정점이 1개일 수도 있음

2. 문제 분석
- 뭉친 그룹 : 상하좌우 인접해있으면서 같은 값을 가지는 칸들의 집합
- 배열 크기 1 <= N <= 500

3. 첫번째 : BFS 탐색
- 인접 리스트 말고 matrix 로 구현
- 방문기록은 matrix에 -1로 기록
- 특정 조건 만족 시 방문 (인덱스 범위 내, 같은 숫자인 경우)
- 방문할 때마다 q에 삽입 + 방문기록 + 그룹 크기 (+1)

4. 두번째
- 배열의 각 칸이 정점
- 가로와 세로로 각각 인접한 칸이 간선
- 특정 값을 가지는 칸만 탐색
- 방문기록은 matrix와 동일한 형태로 따로 배열 생성해서 0과 1로 기록
- 방문할 때마다 q에 삽입 + 방문기록
- q에서 뺄 때마다 그룹 크기 (+1)
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
    y, x = map(int, input().split())
    matrix = [[0 for _ in range(size+1)] for _ in range(size+1)]
    visited = [[0 for _ in range(size+1)] for _ in range(size+1)]

    for i in range(1, size+1):
        matrix[i] = [0] + list(map(int, info[i].split()))
    
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
