# 이중 우선순위 큐 (g4, 21.893%)
# source : https://www.acmicpc.net/problem/7662
# keyword : 자료 구조, 우선순위 큐, 트리 사용한 집합과 맵
# return : 연산을 모두 처리한 후 Q의 최댓값과 최솟값 출력

"""
1. 문제
- 이중 우선순위 큐
    - 데이터 삽입
    - 데이터 삭제 : 우선순위 높은 것 삭제 & 낮은 것 삭제
- 모든 연산 처리 후 Q의 최댓값과 최솟값 출력(EMPTY)

2. 입력 및 제한
- 테스트 케이스 수 T (정수)
- 연산의 개수 k (k<=1,000,000)
- 연산
    - I n : 정수 n을 Q에 삽입하는 연산 (-2^31<=n<2^31)
    - D 1 : 최댓값 삭제
    - D -1 : 최솟값 삭제

3. 로직 1 -> 틀림
- 최소 힙 우선순위 큐에서 heappop(), pop(-1)
- 최소 힙 우선순위 큐는 최솟값은 정확히 찾지만, 자식들 간의 우열은 구분하지 않는다
- 예) 최소 힙 우선순위 큐 = [-6416, 9097, 5585]
    - -6416을 뺐을 때 [5585, 9097]이 된다

4. 로직 2
- 최소 힙 + 최대 힙 + 딕셔너리
"""


from heapq import heappop, heappush
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    Q_min, Q_max, valid = [], [], [0] * k
    for i in range(k):
        op = input().split()
        if op[0] == 'I':
            op[1] = int(op[1])
            heappush(Q_min, (op[1], i))
            heappush(Q_max, (-op[1], i))
            valid[i] = 1
        else:
            if op[1] == '-1':
                while Q_min and not valid[Q_min[0][1]]:
                    heappop(Q_min)
                if Q_min:
                    valid[Q_min[0][1]] = 0
                    heappop(Q_min)
            else:
                while Q_max and not valid[Q_max[0][1]]:
                    heappop(Q_max)
                if Q_max:
                    valid[Q_max[0][1]] = 0
                    heappop(Q_max)
    
    if 1 not in valid:
        print('EMPTY')
    else:
        while Q_min and not valid[Q_min[0][1]]:
            heappop(Q_min)
        while Q_max and not valid[Q_max[0][1]]:
            heappop(Q_max)
        print(-Q_max[0][0], Q_min[0][0])


"""
테스트케이스

2
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1
9
I -45
I 653
D 1
I -642
I 45
I 97
D 1
D -1
I 333
---
EMPTY
333 -45

1
9
D -1
D -1
I 8088
D 1
I 5585
I 9097
I -6416
D 1
D -1
---
5585 5585
"""