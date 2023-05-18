# problem source : https://www.acmicpc.net/problem/2747
# return : 피보나치 수열 결과 출력

import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 피보나치 수열 : f[n] = f[n-1] + f[n-2]

def fibo(dp, i):
    if dp[i] != -1:
        return dp[i]
    dp[i] = fibo(dp, i-2) + fibo(dp, i-1)
    return dp[i]

def top_down(n):
    # dp 테이블 생성
    dp = [-1] * (n+1)
    dp[0] = 0
    dp[1] = 1
    # 피보나치 수열 실행
    fibo(dp, n)
    print(dp[n])

def bottom_up(n):
    # dp 테이블 생성
    dp = [-1] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    print(dp[n])

# 피보나치 수열 수행
n = int(input())
top_down(n)
bottom_up(n)