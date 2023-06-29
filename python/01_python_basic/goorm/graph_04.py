# 모래섬
# keyword : 시뮬레이션, 그래프 탐색
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
- 0이 들어간 칸의 상하좌우 칸 위치 기록
- 기록한 칸 모두 0으로 변경 > day += 1
- 모래섬 개수가 2개 이상인 경우 멈추고 day 출력
- 모든 칸이 0이 된 경우 멈추고 -1 출력

3. 두 번째
- 최악의 경우 : 모래로 거의 가득 찬 케이스
- 어떤 모래 칸이 물에 가라 앉는데 걸리는 시간 
    = 가라 앉은 칸과의 맨해튼 거리 중 최솟값
    = 최대 모래섬의 가로 길이 + 세로 길이
    = 200
- 한 번 모래섬의 개수를 세는 데 O(NM)
"""


def sand_island_1(size, info):
    from collections import deque

    def flooding(y, x):		
        dy = [-1, 0, 1, 0]
        dx = [0, -1, 0, 1]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0<=ny<n) and (0<=nx<m):
                ground[ny][nx] = 0
                  
    def island(y, x):		
        dy = [-1, 0, 1, 0]
        dx = [0, -1, 0, 1]
        q = deque()
        q.append([y, x])
        while q:
            cy, cx = q.popleft()
            visited[cy][cx] = 1
            for i in range(4):
                ny = cy + dy[i]
                nx = cx + dx[i]
                if (0<=ny<n) and (0<=nx<m):
                    # 모래 땅이면서 방문하지 않은 경우
                    if ground[ny][nx] and not visited[ny][nx]:
                        q.append([ny, nx])
        
    n, m = map(int, size.split())
    ground = list()
    day = 0

    for row in info:
        ground.append(list(map(int, row.split())))

    bridge = False
    while True:
        # 모든 칸이 0인 경우 break
        chk = 0
        for i in range(n):
            chk += sum(ground[i])
        if chk == 0:
            break
        
        points = list()
        for i in range(n):
            for j in range(m):
                if ground[i][j] == 0:
                    points.append([i, j])			
        for y, x in points:
            flooding(y, x)
        day += 1

        cnt = 2
        visited = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if (ground[i][j] == 1) and not visited[i][j]:
                    island(i, j)
                    cnt -= 1
                    if not cnt:
                        bridge = True
            if bridge:
                break
        if bridge:
            break
	
    if bridge:
        return day
    else:
        return -1


def sand_island_2(size, info):
    # 1번에서 시간 초과해서 수정 코드
    """
    1) 모든 칸이 0인 경우 일일이 합해서 구함 -> island=0인 경우로 변경
    2) 0 주변을 1로 변경 -> 주변에 0이 있으면 0으로 변경 (전자가 많이 빠름)
    3) 리스트에 침수 포인트 저장 -> update[i][j]와 같이 2차원 배열에 포인트 저장 (후자가 조금 빠름)
    4) BFS 알고리즘 -> DFS 알고리즘 (시간 초과 해결 직접적 원인)
    """
    import sys
    sys.setrecursionlimit(12345)
    from collections import deque
                
    def flooding(y, x):		
        for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if (0<=ny<n) and (0<=nx<m):
                        ground[ny][nx] = 0

    def bfs(y, x):		
        q = deque()
        q.append([y, x])
        while q:
            cy, cx = q.popleft()
            visited[cy][cx] = 1
            for i in range(4):
                ny = cy + dy[i]
                nx = cx + dx[i]
                if (0<=ny<n) and (0<=nx<m):
                    # 모래 땅이면서 방문하지 않은 경우
                    if ground[ny][nx] and not visited[ny][nx]:
                        q.append([ny, nx])
                        
    def dfs(y, x):
        for k in range(4):
                ny, nx = y + dy[k], x + dx[k]
                if ny < 0 or nx < 0 or ny >= n or nx >= m:
                        continue
                if visited[ny][nx] or not ground[ny][nx]:
                        continue
                visited[ny][nx] = 1
                dfs(ny, nx)
        
    n, m = map(int, size.split())
    ground = list()
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    for row in info:
        ground.append(list(map(int, row.split())))

    day = 0
    while True:	
        points = list()
        for i in range(n):
            for j in range(m):
                if not ground[i][j]:
                    points.append([i, j])
        for y, x in points:
                flooding(y, x)
        day += 1
        
        island = 0
        visited = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if ground[i][j] and not visited[i][j]:
                    dfs(i, j)
                    island += 1
                    
        if island >= 2:
            return day
            #exit(0)
            
        if island == 0:
            return -1
            #exit(0)


def sand_island_3(size, info):
    import sys
    sys.setrecursionlimit(12345)

    N, M = map(int, size.split())
    sand = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        row = list(map(int, info[i].split()))
        for j in range(M):
            sand[i][j] = row[j]
            
    checked = [[0 for _ in range(M)] for _ in range(N)]
    update = [[0 for _ in range(M)] for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def DFS(cur):
        cy, cx = cur
        for k in range(4):
            ny, nx = cy + dy[k], cx + dx[k]
            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue
            if checked[ny][nx] or not sand[ny][nx]:
                continue
            checked[ny][nx] = 1
            DFS([ny, nx])

    day = 0
    while 1:
        island = 0
        for i in range(N):
            for j in range(M):
                if checked[i][j] or not sand[i][j]:
                    continue
                checked[i][j] = 1
                island += 1
                DFS([i, j])
        
        if island > 1:
            return day
            #exit(0)
            
        if island == 0:
            return -1
            #exit(0)
            
        for i in range(N):
            for j in range(M):
                for k in range(4):
                    ny, nx = i + dy[k], j + dx[k]
                    if ny < 0 or nx < 0 or ny >= N or nx >= M:
                        continue
                    if not sand[ny][nx]:
                        update[i][j] = 1
                        
        for i in range(N):
            for j in range(M):
                if update[i][j]:
                    sand[i][j] = 0
        
        for i in range(N):
            for j in range(M):
                update[i][j] = checked[i][j] = 0
        day += 1


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [('6 5', ['1 1 1 1 1',
                           '1 1 1 1 1',
                           '1 1 0 1 1',
                           '1 1 0 1 1',
                           '1 1 1 1 1',
                           '1 1 0 1 1']),
                  ('5 5', ['0 0 1 0 0',
                           '0 1 1 1 0',
                           '1 1 1 1 1',
                           '0 1 1 1 0',
                           '0 0 1 0 0'])] # 2, -1

    for case in test_cases:
        print(sand_island_1(case[0], case[1]))
        print(sand_island_2(case[0], case[1]))
        print(sand_island_3(case[0], case[1]))
