# 경로 찾기 (s1, 60.386%)
# source : https://www.acmicpc.net/problem/11403
# keyword : 구현, 해시
# return : N의 길이인 정사각형을 잘랐을 때 하얀색과 파란색 색종이 개수 출력

"""
1. 문제
- 가중치 없는 방향 그래프 G
- 모든 정점 (i,j)에 대해서 i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 구한다

2. 입력
- 정점의 개수 N (1<=N<=100)
- 그래프의 인접 행렬 N줄
    - 1이면 i->j 경로 있음
    - 0이면 i->j 경로 없음(i->i는 없음)

3. 로직 
- bfs
- 출발지에서 시작
- q를 비울 때까지 지속
    - 인접행렬에서 1인 것들만 q에 삽입 + 방문 기록
    - 도착지를 만나면 1로 변경
"""


import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
G = [[*map(int, input().split())] for _ in range(N)]

def bfs(s, e):
    visited = [0 for _ in range(N)]
    q = deque([s])
    while q: 
        cur = q.popleft()
        for i in range(N):
            if G[cur][i] == 1 and not visited[i]:
                if i == e:
                    G[s][e] = 1
                    break
                q.append(i)
                visited[i] = 1
# 경로가 없는 경우 경로 탐색
for i in range(N):
    for j in range(N):
        if not G[i][j]:
            bfs(i, j)
# 결과 출력
for r in range(N):
    print(*G[r], end=' ')
    print()


"""
테스트케이스

3
0 1 0
0 0 1
1 0 0

7
0 0 0 1 0 0 0
0 0 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 0 1 1 0
1 0 0 0 0 0 0
0 0 0 0 0 0 1
0 0 1 0 0 0 0
---결과 출력
1 1 1
1 1 1
1 1 1

1 0 1 1 1 1 1
0 0 1 0 0 0 1
0 0 0 0 0 0 0
1 0 1 1 1 1 1
1 0 1 1 1 1 1
0 0 1 0 0 0 1
0 0 1 0 0 0 0
"""