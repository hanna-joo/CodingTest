# problem source : https://www.acmicpc.net/problem/1260
# return : 주어진 노드번호 V부터 방문된 점을 순서대로 출력 (DFS, BFS)

import sys
from collections import deque

sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 노드 개수, 엣지 개수, 시작점
node_cnt, edge_cnt, start_node = map(int, input().split())

# 인접 리스트 생성
graph = [[] for _ in range(node_cnt + 1)]
for _ in range(edge_cnt):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

# 작은 노드부터 탐색하기 위해 정렬
for node in graph:
    node.sort()

# DFS
def DFS(start):
    print(start, end=' ')
    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            DFS(node)

visited = [False] * (node_cnt + 1)
DFS(start_node)

print()

# BFS
def BFS(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

visited = [False] * (node_cnt + 1)
BFS(start_node)