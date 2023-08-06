# 테트로미노 (s2, 48.123%)
# source : https://www.acmicpc.net/problem/11279
# keyword : 구현
# return : 0이 주어진 회수만큼 답 출력

"""
1. 문제
- 최대 힙을 이용하여 연산
    - 자연수 > 배열에 자연수 넣는다
    - 0 > 가장 큰 값 출력하고 배열에서 제거한다
- 비어있는데 출력해야 하면 0 출력

2. 입력
- 연산 개수 N(1<=N<=100,000)
- 연산 정보 x(0<=x<=2^31)
"""


import sys, heapq
input = sys.stdin.readline

max_heap = list()
for i in [*map(int, open(0).read().split())][1:]:
    if i == 0:
        print(-heapq.heappop(max_heap) if max_heap else 0)
    else:
        heapq.heappush(max_heap, -i)


"""
테스트케이스

13
0
1
2
0
0
3
2
1
0
0
0
0
0
"""
