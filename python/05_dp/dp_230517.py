# problem source : https://www.acmicpc.net/problem/2193
# return : N자리의 이친수 개수 출력

import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

'''
이친수 : 1로 시작하고, 1이 연속 2번 이상 나타나지 않는 이진수

- dp[1][0] : 1자리 수 중 0으로 끝나는 이친수의 개수
- dp[1][1] : 1자리 수 중 1으로 끝나는 이친수의 개수
- dp[2][0] : 1자리 이친수 끝에 0 붙인 경우의 수
- dp[2][1] : 1자리 & 0으로 끝나는 이친수 끝에 1 붙인 경우의 수

dp[2][0] = dp[1][0] + dp[1][1]
dp[2][1] = dp[1][0]

dp[i][0] = dp[i-1][0] + dp[i-1][1]
dp[i][1] = dp[i-1][0]
'''

n = int(input())
dp = [[0, 0] for _ in range(n+1)]
i = 1

# 1자릿수에서 이친수는 1뿐
dp[i][1] = 1

# 자릿수(i)가 n이 될 때까지 반복
while i < n:
    dp[i+1][0] = dp[i][0] + dp[i][1]
    dp[i+1][1] = dp[i][0]
    i += 1

print(dp[5][0] + dp[5][1])