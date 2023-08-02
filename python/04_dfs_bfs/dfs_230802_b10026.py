# 적록색약 (g5, 56.556%)
# source : https://www.acmicpc.net/problem/10026
# keyword : dfs/bfs
# return : 적록색약이 아닌 사람과 맞는 사람이 봤을 때 구역의 수 출력

"""
1. 문제
- 같은구역 = 상하좌우로 같은 색
- 적록색약 X : R / G / B
- 적록색약 O : RG / B

2. 입력 및 제한
- N (1<=N<=100)
- 그림 색 정보

3. 로직
- 상하좌우 탐색 (DFS)
- 색이 다르면 탐색 중지
"""

# 같은 구역인지 탐색
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
def dfs(cx, cy):
    visited[cx][cy] = 1
    for i in range(4):
        nx, ny = cx+dx[i], cy+dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=N:
            continue
        if visited[nx][ny]:
            continue
        if graph[cx][cy] == graph[nx][ny]:
            dfs(nx, ny)

# 적록색약 사람이 보는 그림
def red_to_green(graph):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'R':
                graph[i][j] = 'G'
    return graph

# 그림에서 구역 수 구하기
def search(graph, rgw=False):
    global visited
    visited = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0
    if rgw:
        # 적록색약이라면 해당 그림으로 변경
        graph = red_to_green(graph)
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                dfs(i, j)
                cnt += 1
    return cnt


if __name__ == "__main__":
    
    import sys
    sys.setrecursionlimit(100000)
    input = sys.stdin.readline
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(input().rstrip()))

    cnt1 = search(graph, rgw=False)
    cnt2 = search(graph, rgw=True)

    print(cnt1, cnt2)


"""
테스트 케이스 : 4 3

5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
"""