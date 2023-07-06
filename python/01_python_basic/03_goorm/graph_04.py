# 구름이의 여행2
# keyword : BFS, BFS 활용해 사이클 찾기
# return : K번에서 1개 이상의 섬을 방문하고 K번으로 돌아오는 최단 거리 출력

"""
1. 문제 분석
- 두 정점을 잇는 간선은 최대 1개
- 각 간선은 단방향, 서로 다른 두 정점 이음
- K번에서 최소 하나 이상의 섬을 방문하고 K번으로 돌아옴 (최단 거리)
- 최소 몇 개의 다리를 거쳐서 돌아오는지 출력
- 다시 돌아올 수 없는 경우 -1 출력

2. 해결 방안
- 그래프 구현 + BFS
- K번 -> n1번 -> n2번 -> ... -> np번 -> K번
- (1) K번 -> np번 : 최단 거리
- (2) np번 -> K번 : K번과 인접한 정점들
- K번과 모든 정점 간의 최단 거리를 구한다
- K번에서 K번까지의 경로가 여러 개 있을 수 있으니 최단 거리 변수를 마련한다
- K번과 만나면 최단 거리를 기록한다
"""


def travel(size, info):
    #import sys
    from collections import deque
    #input = sys.stdin.readline

    island_cnt, bridge_cnt, target = map(int, size.split())
    graph = [[] for _ in range(island_cnt+1)]
    for i in range(bridge_cnt):
        s, e = map(int, info[i].split())
        graph[s].append(e)
        
    dist = [9**9 for _ in range(island_cnt+1)]
    dist[target] = 0
    q = deque()
    q.append(target)

    # K번에서 K번으로 이동하는 경로가 여러 개일 수 있음
    min_dist = 9**9
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            # 다음 섬이 목적지면 값 갱신
            # 다음 섬이 목적지여도 다른 경로가 있을 수 있기에 탐색 계속
            if nxt == target:
                min_dist = min(min_dist, dist[cur] + 1)
            # 다음 섬까지의 거리가 새로운 거리보다 크다면 새로 방문
            if dist[nxt] > dist[cur] + 1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)

    if min_dist == 9**9:
        return -1
    else:
        return min_dist


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [('5 6 4', ['1 2', '1 4', '3 1', '4 2', '4 5', '5 3']),
                  ('5 6 4', ['1 2', '1 3', '3 2', '4 2', '5 1', '5 4'])] # 4, -1

    for case in test_cases:
        print(travel(case[0], case[1]))
