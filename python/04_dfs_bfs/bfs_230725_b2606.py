# problem : https://www.acmicpc.net/problem/2606
# keyword : dfs/bfs
# return : 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 바이러스에 걸리는 컴퓨터 수 출력

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

# 입력 값 받아서 그래프 구현
node_cnt = int(input().rstrip())
edge_cnt = int(input().rstrip())
graph = defaultdict(list)

for _ in range(edge_cnt):
    s, e = map(int, input().rstrip().split())
    graph[s].append(e)
    graph[e].append(s)

# 1번 먼저 방문 (큐 삽입 + 방문 기록)
visited = [False for _ in range(node_cnt+1)]
visited[1] = True
queue = deque([1])
infected_cnt = 0

# 1번과 연결된 곳 모두 감염
while queue:
    cur = queue.popleft()
    for i in graph[cur]:
        if visited[i]:
            continue
        visited[i] = True
        queue.append(i)
        infected_cnt += 1

print(infected_cnt)