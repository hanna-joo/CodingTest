# 숨바꼭질 (s1, 25.699%)
# source : https://www.acmicpc.net/problem/1697
# keyword : bfs
# return : 수빈이가 동생을 찾는 가장 빠른 시간(초) 출력

"""
1. 문제
- 수빈이가 N에서 동생이 위치한 K까지 가는 방법
    - 걷기 : 1초 후에 X-1, X+1
    - 순간이동 : 1초 후에 2X

2. 입력 및 제한
- N, K (0<=N,K<=100,000)

3. 로직
- N = K -> 0초
- N > K -> X-1 -> (N-K)초
- N < K -> X-1, X+1, 2X
    - nxt = K -> 탐색 종료
    - 0 < nxt < K -> q 삽입 제외
    - nxt가 이미 방문한 적 있음 -> q 삽입 제외
"""

import heapq

N, K = map(int, input().split())
ans = (N-K)

if N >= K:
    print(ans)
    exit()

q = [(0, N)]
visited = [0 for _ in range(K+2)]
flag = False
while q:
    sec, cur = heapq.heappop(q)
    for i in [-1, 1, cur]:
        nxt = cur + i
        if nxt == K:
            flag = True
            break
        if nxt < 0 or nxt > K+1:
            continue
        if not visited[nxt]:
            visited[nxt] = 1
            heapq.heappush(q, (sec+1, nxt))
    if flag:
        ans = sec + 1
        break

print(ans)