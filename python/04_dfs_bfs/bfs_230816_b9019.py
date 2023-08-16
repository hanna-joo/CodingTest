# DSLR (g4, 20.912%)
# source : https://www.acmicpc.net/problem/9019
# keyword : 
# return : 
"""
1. 문제
- D : (n*2)%10000
- S : n-1, n=0이면 9999
- L : d2, d3, d4, d1
- R : d4, d1, d2, d3
- 정수 A에서 B로 바꾸는 최소한의 명령어 생성

2. 입력
- 테스트 케이스 개수 T
- 정수 A, B (0<=A!=B<10,000)

3. 로직 수정 전
- BFS + 우선순위 큐
- 변경 후 명령어 길이가 우선순위 점수
- string 기반으로 데이터 저장

4. 로직 수정 후
- 시간 초과 원인
    - str(int) 시간 많이 소요 -> int로 통일
    - 우선순위큐 정렬 -> 삭제
"""

import sys, heapq
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = map(int, input().rstrip().split())
    q = deque([(A, '')])
    visited = [0 for _ in range(10000)]
    visited[A] = 1

    while q:
        cur, op = q.popleft()
        if cur == B:
            print(op)
            break
        for c in 'DSLR':
            if c == 'D': new = cur * 2 % 10000
            elif c == 'S': new = (cur-1) % 10000
            elif c == 'L': new = (cur//1000) + (cur%1000)*10
            else: new = (cur//10) + (cur%10)*1000
            if not visited[new]:
                visited[new] = 1
                q.append((new, op+c))


"""
테스트케이스

4
1234 3412
1000 1
1 16
0 9999
---결과 출력
LL
L
DDDD
S
"""
