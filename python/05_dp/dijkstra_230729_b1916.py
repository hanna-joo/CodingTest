# 최소비용 구하기
# source : https://www.acmicpc.net/problem/1916
# keyword : 다익스트라, 다이나믹 프로그래밍
# return : A번 도시에서 B번 도시까지 가는 데 드는 최소 비용 출력

"""
1. 문제
- A도시에서 B도시까지 가는 데 드는 최소 비용 출력

2. 입력
- 도시 개수 N(1<=N<=1,000)
- 버스 개수 M(1<=M<=100,000)
- 버스 정보 : 출발 도시, 도착 도시, 버스 비용(0<=비용<=100,000)
- 실제 출발 도시, 도착 도시

3. 로직
- 우선순위 큐 사용
- 방문리스트, 거리리스트 
- 거리리스트로 방문여부 확인(244ms) : dist[c_node] < c_cost
- 방문리스트를 별도로 사용(240ms) : visited[c_node] == 1

4. 주의 사항
- 비용이 0일 수 있다
- 동일한 u, v에 대한 비용을 여러 번 입력할 수 있다
- u == v일 수 있다
- a도시와 b도시가 같을 수 있다 (1번에서 1번으로 갈 때 비용 != 0)
"""


import sys, heapq

input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

start, end = map(int, input().split())
#visited = [0 for _ in range(N+1)]
dist = [sys.maxsize for _ in range(N+1)]

# 출발 도시에서 시작
q = [(0, start)]

while q:
    # 거리 가까운 도시부터 뽑기
    cost, node = heapq.heappop(q)
    # 이미 방문했다면 다시 뽑기
    #if visited[node]:
    #    continue
    if dist[node] < cost:
        continue
    # 도착 도시면 종료
    if node == end:
        break
    # 방문 안했다면 방문 기록
    #visited[node] = 1
    # 연결된 도시(e), 비용(next_w)
    for n_cost, n_node in graph[node]:
        # 새로운 비용 : s까지 온 비용 + s에서 e까지 가는 비용
        n_cost += cost
        # 기존 비용보다 새로운 비용이 적으면 갱신
        if dist[n_node] > n_cost:
            dist[n_node] = n_cost
            # 더 작은 비용이 나왔으니 q에 넣기
            heapq.heappush(q, (n_cost, n_node))

print(dist[end])
print(dist)


"""
테스트 케이스 : 4 / 0 / 3 / 2 / 5

5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5

1
1
1 1 1
1 1

2
3
1 2 5
1 2 10
1 2 3
1 2

2
3
1 1 3
1 1 2
1 2 5
1 1

2
3
1 1 3
1 1 2
1 2 5
1 2
"""