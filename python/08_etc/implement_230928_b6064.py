# 카잉 달력 (s1, 26.366%)
# source : https://www.acmicpc.net/problem/6064
# keyword : 중국인의 나머지 정리, 정수론
# return : <x:y>가 <M:N> 중에서 몇 번째 해인지 출력

"""
1. 문제
- 카잉제국의 달력에서 <M:N>은 마지막 해
- 예시 : M=10, N=12
    - <1:1>, <2:2>, ... , <1:11>, <2:12>, <3:1>, ... , <10:12>
- M, N, x, y가 주어졌을 때 <x:y>는 몇 번째 해인지 출력
    - <x:y>로 표현되는 해가 없다면 -1 출력
    
2. 입력 및 제한
- 테스트 케이스 T
- M, N, x, y (1<=M,N<=40,000, 1<=x<=M, 1<=y<=N)

3. 로직
- k번째 해 = <k%10:k%12>
- <3:9> 찾으려면 다음 값들 중 공통 k값 찾기
    - k%10=3인 값 [3, 13, 23, 33, 43, ... , 53]
    - k%12=9인 값 [9, 21, 33, ... , 57]
- k값은 (10*12)+1 이전까지만 찾기
"""


import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())

    k_x = set(i+x for i in range(0, M*N+1, M))
    k_y = set(i+y for i in range(0, M*N+1, N))
    k = k_x & k_y

    if k:
        print(min(k))
    else:
        print(-1)


"""
테스트케이스

3
10 12 3 9
10 12 7 2
13 11 5 6
---
33
-1
83
"""