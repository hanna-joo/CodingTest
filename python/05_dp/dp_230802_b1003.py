# 피보나치 함수 (s3, 32.543%)
# source : https://www.acmicpc.net/problem/1003
# keyword : 다이나믹 프로그래밍
# return : 피보나치 함수를 호출했을 때, 0과 1이 출력되는 횟수 출력

"""
1. 문제
- 피보나치 수를 구하는 함수 fibonacci(num)
- fibonacci(0) -> print(0)
- fibonacci(1) -> print(1)

2. 입력 및 제한
- 테스트 케이스 개수 T
- 정수 N (0<=N<=40)

3. 로직 1 - Top Down
- dp[i][0] = dp[i-1][0] + dp[i-2][0]
- dp[i][1] = dp[i-1][1] + dp[i-2][1]

4. 로직 2 - Bottom Up
- dp[i] = fibo(i)일 때 [0출현 횟수, 1출현 횟수]
    - dp[i][0]: 1, 0, 1, 1, 2, 3, 5, ...
    - dp[i][1] : 0, 1, 1, 2, 3, 5, ...
- dp[i][0] = dp[i-1][1]
- dp[i][1]
    - dp[i-1][1] + dp[i-2][1]
    - dp[i-1][1] + dp[i-1][0]
"""

def solution_1(num):
    sys.setrecursionlimit(100000)
    if dp1.get(num):
        return dp1[num]
    dp1[num] = [x+y for x, y in zip(solution_1(num-1), solution_1(num-2))]
    return dp1[num]


def solution_2(num):
    zero, one = 1, 0
    for _ in range(num):
        zero, one = one, zero+one
    return zero, one


def solution_3(num):
    for i in range(2, num+1):
        dp2[i] = [dp2[i-1][1], sum(dp2[i-1])]
    return dp2[num]


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        global dp1, dp2
        dp1 = {0: [1, 0], 1: [0, 1]}
        print(*solution_1(N), end=' ')

        dp2 = [[1, 0], [0, 1]] + [0] * 39
        print(*solution_2(N), end=' ')

        print(*solution_3(N), end=' ')


"""
테스트 케이스 : 1 0 0 1 1 2 / 5 8 10946 17711

3
0
1
3

2
6
22
"""