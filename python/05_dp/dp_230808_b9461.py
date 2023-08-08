# 파도반 수열 (s3, 42.991%)
# source : https://www.acmicpc.net/problem/9461
# keyword : 다이나믹 프로그래밍
# return : 나선 모양으로 놓여진 삼각형 중 N번째 정삼각형의 변의 길이 출력

"""
1. 문제
- 파도반 수열 P(N) : 나선에 있는 정삼각형의 변의 길이
- P(1) ~ P(10) : [1, 1, 1, 2, 2, 3, 4, 5, 7]

2. 입력 및 제한
- 테스트 케이스 개수 T
- 정수 N (1<=N<=100)
"""


def solution_1(num):
    dp = [0, 1, 1, 1, 2, 2]
    for i in range(6, num+1):
        dp.append(dp[i-1] + dp[i-5])
    print(dp[num])


def solution_2(num):
    dp = [0, 1, 1, 1, 2, 2] + [0 for _ in range(num-5)]
    dp[1], dp[2], dp[3], dp[4], dp[5] = 1, 1, 1, 2, 2
    for i in range(6, num+1):
        dp[i] = dp[i-1] + dp[i-5]
    print(dp[num])


if __name__ == "__main__":

    import sys
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        solution_1(int(input()))
        solution_2(int(input()))



"""
테스트 케이스 : 3 16

2
6
12
"""