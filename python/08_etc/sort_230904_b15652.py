# N과 M(4) (s3, 78.893%)
# source : https://www.acmicpc.net/problem/15652
# keyword : 조합
# return : 문제의 조건을 만족하는 수열을 공백으로 구분하여 출력

"""
1. 문제
- 아래 조건을 만족하는 길이가 M인 수열 모두 출력
    - 1부터 N까지 자연수 중에서 M개
    - 같은 수 중복으로 골라도 됨
    - 고른 수열은 오름차순이어야 함 (A1<=A2<=...<=Ak)

2. 입력 및 제한
- N, M (1<=M<=N<=8)

3. 로직
- 재귀함수 사용
    - 종료 : arr 길이가 M이 되면 종료
    - 지속 : arr의 마지막 값과 같거나 큰 값을 arr에 추가
"""


import sys
N, M = map(int, sys.stdin.readline().split())

def rec(arr, cnt):
    if cnt == M:
        print(*arr[1:], end=' ')
        print()
        return
    for i in range(arr[-1], N+1):
        rec(arr+[i], cnt+1)

rec([1], 0)


"""
테스트케이스

3 1
---
1
2
3

4 2
---
1 1
1 2
1 3
1 4
2 2
2 3
2 4
3 3
3 4
4 4

3 3
---
1 1 1
1 1 2
1 1 3
1 2 2
1 2 3
1 3 3
2 2 2
2 2 3
2 3 3
3 3 3
"""