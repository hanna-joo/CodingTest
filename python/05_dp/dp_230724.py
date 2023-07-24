# 등굣길
# keyword : 다이나믹 프로그래밍
# return : (1, 1)에서 (m, n)까지 갈 수 잇는 최단 경로 개수

"""
1. 다이나믹 프로그래밍 해결 방법
- 어떤 값(=반복되는 부분 문제의 정답)을 저장할 것인지 정한다
- 저장한 값들 간의 점화식을 세우고, 초기 값을 설정한 뒤 계산한다
- 점화식을 세울 때는 미리 저장해둔 값을 언제, 어떻게 재사용할지를 반영한다

2. 문제 풀이
(1) 침수지역 표시
(2) 초기값 설정
- dp[1][1] = 1
(3) 점화식 구하기
- 현재 경로 수 = 위쪽 칸 경로 수 + 왼쪽 칸 경로 수
- dp[i][j] = dp[i-1][j] + dp[i][j-1]
- 현재/위쪽/왼쪽 칸이 침수지역인 경우 예외 처리
"""

def solution_1(m, n, puddles):
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    # (1) 침수지역 표시
    for y, x in puddles:
        dp[y][x] = -1
    # (2) 초기값 설정
    dp[1][1] = 1
    for i in range(1, m+1):
        for j in range(1, n+1):
            # (3) 점화식 + 예외 처리
            if (i == 1 and j == 1) or (dp[i][j] == -1):
                continue
            elif dp[i-1][j] == -1:
                dp[i][j] = dp[i][j-1]
            elif dp[i][j-1] == -1:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    answer = dp[m][n]
    return answer % 1000000007


def solution_2(m, n, puddles):
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    # (1) 침수지역 표시
    for y, x in puddles:
        dp[y][x] = -1
    for i in range(1, m+1):
        for j in range(1, n+1):
            # (2) 초기값 설정
            if (i == j == 1):
                dp[i][j] = 1
                continue
            # (3) 침수지역인 경우 다음 계산에 영향 미치지 않도록 0으로 변경
            if dp[i][j] == -1:
                dp[i][j] = 0
                continue
            # (3) 점화식
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    answer = dp[m][n]
    return answer % 1000000007


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [(4, 3, [[2, 2]])] # 4

    for case in test_cases:
        print(solution_1(case[0], case[1], case[2]))
        print(solution_2(case[0], case[1], case[2]))