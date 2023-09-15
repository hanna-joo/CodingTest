# 숨바꼭질 (s1, 25.473%)
# source : https://www.acmicpc.net/problem/1697
# keyword : 
# return : 수빈이가 동생을 찾는 가장 빠른 시간(초) 출력

"""
1. 문제
- 수빈이가 N에서 동생이 위치한 K까지 가는 방법
    - 걷기 : 1초 후에 X-1, X+1
    - 순간이동 : 1초 후에 2X

2. 입력 및 제한
- N, K (0<=N,K<=100,000)

3. 로직
- N = K : 0초
- N > K : (N-K)초    <- (X-1)
- N < K : 너비우선탐색  <- (X-1, X+1, 2*X)
"""
from heapq import heappop, heappush

def bfs(num):
    q = [(0, num)]
    visited = [0 for _ in range(K+2)]
    while q:
        sec, cur = heappop(q)
        for nxt in (cur-1, cur+1, cur*2):
            if nxt < 0 or nxt > K+1:
                continue
            if nxt == K:
                return sec+1
            if not visited[nxt]:
                visited[nxt] = 1
                heappush(q, (sec+1, nxt))
    

N, K = map(int, input().split())
if N >= K:
    print(N-K)
else:
    print(bfs(N))


"""
테스트케이스

5 17
---
4

6 1
---
5

6 11
---
2
"""