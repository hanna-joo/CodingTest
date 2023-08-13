# 1, 2, 3 더하기 (s3, 64.232%)
# source : https://www.acmicpc.net/problem/9095
# keyword : 다이나믹 프로그래밍
# return : 1,2,3 의 합으로 n을 나타내는 방법의 수 출력
"""
1. 문제
- D : (n*2)%10000
- S : n-1, n=0이면 9999
- L : d2, d3, d4, d1
- R : d4, d1, d2, d3
- 정수 A에서 B로 바꾸는 최소한의 명령어 생성

2. 입력
- 테스트 케이스 개수 T
- 정수 n (1<=n<11)

3. 로직
dp[1] = 1
dp[2] = 1+1 = 2
dp[3] = 1+2+1 = 4
dp[4] = dp[1] + dp[2] + dp[3]
dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
"""


def solution_1(num):
    dp = [0 for _ in range(num+1)]
    dp[1:4] = [1, 2, 4]
    for i in range(4, num+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    print(dp[num])


if __name__ == "__main__":

    T = int(input())
    for _ in range(T):
        solution_1(int(input()))


"""
테스트케이스 : 7 44 274

3
4
7
10
"""
