# 최소 힙 (s2, 49.008%)
# source : https://www.acmicpc.net/problem/1927
# keyword : 
# return : 
"""
1. 문제
- x = 자연수 : 자연수 x를 넣는다
- x = 0 : 가장 작은 값을 출력 후 배열에서 제거한다

2. 입력
- 연산 개수 N (1<=N<=100,000)
- 연산 정보 x (0<=x<=2^31)
"""

import heapq
N, *nums = map(int, open(0).read().split())
pq = []
for i in nums:
    if i == 0:
        print(heapq.heappop(pq) if pq else 0)
    else:
        heapq.heappush(pq, i)



"""
테스트케이스

9
0
12345678
1
2
0
0
0
0
32
---결과 출력
0
1
2
12345678
0
"""
