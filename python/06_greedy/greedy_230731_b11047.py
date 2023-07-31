# 동전 0
# source : https://www.acmicpc.net/problem/11047
# keyword : 그리디(배수)
# return : 합을 K로 만드는 동전 개수의 최솟값 출력


"""
1. 문제
- 봉지 용량은 3, 5킬로그램 2가지
- 정확히 N킬로그램 만들 수 없으면 -1 출력

2. 입력
- 동전 종류 개수 N, 구하려는 합 K (1<=N<=10, 1<=K<=100,000,000)
- 동전 종류 별 액수 (1<=Ai<=1,000,000, Ai는 Ai-1의 배수)

3. 로직
- 동전 금액이 큰 순서대로 실행한다
    - 현재 K가 금액보다 큰지 확인한다
    - K에 나눈 나머지를 넣는다
"""
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

cnt = 0
for coin in coins[::-1]:
    if K >= coin:
        cnt += K // coin
        K %= coin
print(cnt)

"""
테스트 케이스 : 6 / 12

10 4200
1
5
10
50
100
500
1000
5000
10000
50000

10 4790
1
5
10
50
100
500
1000
5000
10000
50000
"""