# 1로 만들기 (s3, 32.636%)
# source : https://www.acmicpc.net/problem/1463
# keyword : 다이나믹 프로그래밍
# return : 정수 N을 1로 만들기 위해 사용하는 연산 횟수 최솟값 출력

"""
1. 문제
- 가능한 연산
    - 3으로 나누어 떨어지면, 3으로 나눈다
    - 2로 나누어 떨어지면, 2로 나눈다
    - 1을 뺀다

2. 입력 및 제한
- 정수 N (1<=N<=10^6)

3. 로직 1 - Bottom Up (496ms)
- 점화식
    - dp[i] = min(dp[i-1], dp[i//2], dp[i//3])
    - 단, dp[i//2]와 dp[i//3]은 나누어 떨어질 때에만 적용
- 초깃값
    - dp[1] = 0
    - dp[2] = 1
    - dp[3] = 1
- 예시
    - dp[4] = min(dp[3], dp[2]) + 1 = 2
    - dp[5] = min(dp[4]) + 1 = 3
    - dp[6] = min(dp[5], dp[3], dp[2]) + 1 = 2

4. 로직 2 - Bottom Up (672ms)
- dp = {1: 0, 2: 1}
- dp[i] = 1 + min(dp[i//3]+n%3, dp[i//2]+n%2)

5. 로직 3 - Top Down (44ms)
- dp = {1: 0, 2: 1}
- dp[i] = 1 + min(dp[i//3]+n%3, dp[i//2]+n%2)
"""


import sys
def solution_1(num):
    dp = [sys.maxsize for _ in range(num+1)]
    dp[1] = 0
    for i in range(2, N+1):
        if i % 6 == 0:
            dp[i] = min(dp[i-1], dp[i//2], dp[i//3]) + 1
        elif i % 2 == 0:
            dp[i] = min(dp[i-1], dp[i//2]) + 1
        elif i % 3 == 0:
            dp[i] = min(dp[i-1], dp[i//3]) + 1
        else:
            dp[i] = dp[i-1] + 1

    print(dp[num])


def solution_2(num):
    dp = {1: 0, 2: 1}
    for i in range(3, num+1):
        dp[i] = min(dp[i//2]+i%2, dp[i//3]+i%3) + 1
    print(dp[num])


def solution_3(num):
    dp = {1: 0, 2: 1}
    def s(n):
        if n in dp:
            return dp[n]
        tmp = min(s(n//3)+n%3, s(n//2)+n%2) + 1
        dp[n] = tmp
        return tmp
    print(s(num))


if __name__ == "__main__":

    N = int(input())

    solution_1(N)
    solution_2(N)
    solution_3(N)


"""
테스트 케이스 : 1 / 3

2
10
"""