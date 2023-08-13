# 절댓값 힙 (s1, 56.384%)
# source : https://www.acmicpc.net/problem/11286
# keyword : 구현, 우선순위 큐
# return : 절댓값 힙 구현
"""
1. 문제
- 배열에 정수 x를 넣는다
- 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거
- 작은 값이 여러 개일 때는 가장 작은 수 출력 및 제거
- x가 0이면 배열에서 절댓값이 가장 작은 값 출력
- 배열이 비어있으면 0 출력

2. 입력
- 연산 개수 N (1<=N<=100,000)
- 연산에 대한 정보 x (-2^31<=x<=2^31)

3. 로직
- heapq 모듈 사용
- heapq에 입력된 값이 (val1, val2)면 
    - 정렬 기준은 val1, val2 순으로 적용
    - val1이 같을 때 val2 기준으로 정렬
"""


import heapq

N, *ops = map(int, open(0).read().split())
pq = []
for op in ops:
    if op == 0:
        print(heapq.heappop(pq)[1]) if pq else print(0)
    else:
        heapq.heappush(pq, (abs(op), op))


"""
테스트케이스

18
1
-1
0
0
0
1
1
-1
-1
2
-2
0
0
0
0
0
0
0
---결과 출력
-1
1
0
-1
-1
1
1
-2
2
0
"""
