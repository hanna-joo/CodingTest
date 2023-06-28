# 구름이의 여행
# keyword : 그래프, BFS
# return : 1번 섬에서 N번 섬까지 K개 이하의 다리를 사용해서 갈 수 있는지 여부 출력

"""
1. 그래프 표현 - 인접 행렬
- 직관적인 표현 방식
- N * N 크기의 2차원 배열 선언
- 배열의 초기값은 모두 0으로 설정
- a번 정점에서 b번 정점으로 가는 간선이 존재하는 경우 a행 b열 칸을 1로 표현
- 양방향인 경우 a행 b열, b행 a열 모두 1로 표시
- 장점 : 두 정점 간 연결을 O(1)에 파악 가능
- 단점 : 메모리 복잡도 큼, 하나의 정점에 연결된 정점 파악 시 N개 정점을 모두 탐색해야 함

2. 그래프 표현 - 인접 리스트
- 한 정점과 간선으로 연결된 정점만 관리
- python 에서는 list(동적 배열) 이용
- 장점 : 공간 복잡도 측면에서 효율적, 하나의 정점에 연결된 정점 파악 위해 모든 정점 확인 필요 없음
- 단점 : 두 정점 간 연결을 빠르게 파악 불가능
- 인접 행렬보다 장점이 더 강력하기 때문에 인접 리스트 활용

3. 그래프 탐색 - BFS
- 간선을 따라서 모든 정점을 방문하는 과정
- 시작 정점으로부터 가까이에 있는 정점부터 방문
- 탐색 후보(queue)에 먼저 들어간 순서대로 정점 방문
- 모든 간선의 가중치가 동일한 그래프에서 최단 거리 구할 때 사용

4. 문제 분석
- 1번 섬에서 N번 섬으로 이동하는 최단 경로에 포함된 다리의 개수가 K개 이하인지 판별
"""

def bfs(info, connections):
    from collections import deque

    n, m = map(int, info.split()[:2])

    dist = [9**9 for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]

    for conn in connections:
        a, b = map(int, conn.split())
        graph[a].append(b)
        graph[b].append(a)

    q = deque()

    dist[1] = 0
    q.append(1)

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            # 이미 방문한 정점이라면 거리가 초기값보다 작음
            # 또한 nxt 정점의 최단 거리는 현재 정점의 최단 거리와 최대 1 차이 남
            # 현재 정점의 최단 거리 + 1 보다 크면 nxt 정점의 최단 거리 수정
            if dist[nxt] <= dist[cur] + 1:
                continue
            dist[nxt] = dist[cur] + 1
            q.append(nxt)

        print(f"현재 정점: {cur}, 1번과 {cur}번과의 최단 거리는 {dist[cur]}")


def travel_within_k(info, connections):
    from collections import defaultdict
    from collections import deque

    N, M, K = map(int, info.split())
    # 자료형 명시 필요
    graph = defaultdict(list)

    for conn in connections:
        start, end = map(int, conn.split())
        graph[start].append(end)
        graph[end].append(start)

    # 탐색 후보
    Q = deque()
    Q.append(1)

    # Visited[i] : 1번 노드에서 i번 노드까지의 최소 간선 개수
    Visited = [10e9 for _ in range(N+1)]
    Visited[1] = 0

    while Q:
        cur_Node = Q.popleft()
        for next_Node in graph[cur_Node]:
            if Visited[next_Node] <= Visited[cur_Node] + 1:
                continue
            Visited[next_Node] = Visited[cur_Node] + 1
            Q.append(next_Node)
            
    if Visited[N] <= K:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [('6 6 2', ['1 4', '4 2', '2 6', '4 3', '1 2', '3 1']),
                  ('6 6 2', ['1 2', '2 3', '3 4', '3 5', '5 6', '5 2']),
                  ('3 1 1', ['1 2'])] # YES, NO, NO

    for case in test_cases:
        bfs(case[0], case[1])
        print(travel_within_k(case[0], case[1]))