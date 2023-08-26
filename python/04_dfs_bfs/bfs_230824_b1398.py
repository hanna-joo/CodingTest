# 케빈 베이컨의 6단계 법칙 (s1, 55.972%)
# source : https://www.acmicpc.net/problem/1398
# keyword : dfs/bfs
# return : BOJ 유저 중에 케빈 베이컨의 수가 가장 작은 사람 출력

"""
1. 문제
- 케빈 베이컨의 6단계 법칙 : 지구의 모든 사람들은 최대 6단계 이내에서 서로 아는 사람으로 연결될 수 있음
- 케빈 베이컨 게임 : 임의의 두 사람이 최소 몇 단계 만에 이어질 수 있는지 계산하는 게임
- 케빈 베이컨 수 : A가 각 구성원과 몇 단계 만에 이어지는지 총합

2. 입력 및 제한
- 유저의 수 N, 친구 관계의 수 M (2<=N<=100) (1<=M<=5000)
- 친구 관계 M줄 (중복될 수 있음)
- 모든 사람은 친구가 있고 1~N번으로 구성됨

3. 로직
- bfs
- 중복되는 친구 관계 처리 (set)
"""

import sys
from collections import defaultdict, deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = defaultdict(set)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

def bfs(start):
    q = deque([start])
    d = [-1 for _ in range(N+1)]
    d[start] = 0
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if d[i] == -1:
                d[i] = d[cur] + 1
                q.append(i)
    return sum(d[1:])

ans = [1, bfs(1)]
for i in range(2, N+1):
    new = [i, bfs(i)]
    if new[1] < ans[1]:
        ans = new
        
print(ans[0])


"""
테스트케이스 : 3

5 5
1 3
1 4
4 5
4 3
3 2
"""