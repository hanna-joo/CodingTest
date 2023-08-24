# 2xn 타일링 2 (s3, 58.980%)
# source : https://www.acmicpc.net/problem/11727
# keyword : 
# return : 2xn 직사각형을 1x2, 2x1, 2x2 타일로 채우는 방법의 수 출력

"""
1. 문제
- 2xn 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지 출력

2. 입력
- n (1<=n<=1,000)

3. 로직 
"""


import sys
N = int(sys.stdin.readline())
dp = [0, 1, 3] + [0 for _ in range(N-2)]

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2] * 2

print(dp[N]%10007)

"""
테스트케이스 : 3 / 171 / 2731

2
8
12
"""