# problem source : https://www.acmicpc.net/problem/1260
# return : 주어진 그래프를 탐색할 때 방문 순서대로 출력 (DFS, BFS)

import sys
from collections import deque

sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 노드 개수, 엣지 개수, 시작점
node_cnt, edge_cnt = map(int, input().split())

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
    # (1) 노드 방문하고 실행
    visited[start] = True
    print(start, end=' ')
    # (2) 방문한 노드와 연결된 노드 하나씩 검수
    for node in graph[start]:
        # (3) 검수 : 방문 여부 확인 후 미방문 노드 방문
        if not visited[node]:
            # (4) 방문 : 방문 기록하고 연결 노드 바로 검수
            DFS(node)

visited = [False] * (node_cnt + 1)
for i in range(1, node_cnt+1):
    if not visited[i]:
        print()
        print('New Connection Founded : ', end=' ')
        DFS(i)

print()

# BFS
def BFS(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        # (1) 맨 앞 노드 빼고 실행
        node = queue.popleft()
        print(node, end=' ')
        # (2) 맨 앞 노드와 연결된 노드 하나씩 검수
        for i in graph[node]:
            # (3) 검수 : 방문 여부 확인 후 미방문 노드 방문
            if not visited[i]:
                # (4) 방문 : 방문 기록하고 queue에 삽입
                visited[i] = True
                queue.append(i)
                # (5) 이후에 바로 (1)로 이동!

visited = [False] * (node_cnt + 1)
for i in range(1, node_cnt+1):
    if not visited[i]:
        print()
        print('New Connection Founded : ', end=' ')
        BFS(i)