# Four Squares (s3, 43.902%)
# source : https://www.acmicpc.net/problem/17626
# keyword : 완전 탐색
# return : 합이 n이 되는 제곱수들의 최소 개수를 한 줄에 출력

"""
1. 문제
- 라그랑주 : 모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현할 수 있다
- 15663 = 125^2 + 6^2 + 1^2 + 1^2
- 자연수 n이 주어질 때, n을 최소 개수의 제곱수 합으로 표현하는 프로그램 작성

2. 입력 및 제한
- 자연수 n (1<=n<=50,000)

3. 로직 1
- 다이나믹 프로그래밍
- dp[i] = min([dp[i-1], dp[i-4], dp[i-9], ...]) + 1
    - i 미만의 제곱 수
    - 18 = min([dp[18-1], dp[18-4], dp[18-9], dp[18-16]])

4. 로직 2
- 정답은 최소 1 ~ 최대 4 (4개쯤 되면 다시 제곱수가 나옴)
- 1일 때 : n = 제곱수
- 2일 때 : n = 제곱수 + 제곱수
- 3일 때 : n = 제곱수 + 제곱수 + 제곱수
- 4일 때 : n % 8 = 7 (단, n을 4의 배수가 아닐 때까지 4로 나눔)
    - 7, 15, 23, 28, 31, 39, 47, 55, 60, 63, 71, 79, 87, 92, 95
"""


def solution_1(num):
    dp = [0 for _ in range(num+1)]
    divisor = []
    for i in range(1, num+1):
        if (i ** 0.5).is_integer():
            divisor.append(i)
        dp[i] = min(dp[i-j] for j in divisor) + 1
    return dp[num]


def solution_2(num):
    if (num ** 0.5).is_integer():
        return 1
    
    squares = {i**2 for i in range(int(num**0.5), 0, -1)}
    for i in squares:
        if num - i in squares:
            return 2
    
    while num % 4 == 0:
        num //= 4
    return 4 if num % 8 == 7 else 3


if __name__ == "__main__":
    import sys
    n = int(sys.stdin.readline())

    print(solution_1(n))
    print(solution_2(n))


"""
테스트케이스 : 1 / 2 / 3 / 4

25
26
11339
34567
"""