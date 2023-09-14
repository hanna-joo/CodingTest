# 계단 오르기 (s3, 33.723%)
# source : https://www.acmicpc.net/problem/2579
# keyword : 다이나믹 프로그래밍
# return : 계단 오르기 게임에서 얻을 수 있는 점수 최댓값 출력

"""
1. 문제
- 계단 오르기 게임 : 아래 시작점에서 꼭대기 도착점까지 가는 게임
    - 한 번에 1-2개 계단 오를 수 있음
    - 연속된 3개의 계단을 모두 밟으면 안 됨
    - 마지막 도착 계단은 반드시 밟아야 함
- 각 계단에 쓰여 있는 점수가 주어질 때 얻을 수 있는 점수 최댓값 출력

2. 입력 및 제한
- 계단의 개수 N (1<=N<=300)
- 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰인 점수 N줄 (1<=점수<=10,000)

3. 로직1
- dp[i] = (한칸전, 두칸전) = (한칸전의 두칸전, 두칸전의 최댓값)
    - dp[0] = (0, 0)
    - dp[1] = (0, 0) + 10 = (10, 10)
    - dp[2] = (10, 0) + 20 = (30, 20)
    - dp[3] = (20, 10) + 15 = (35, 25)
    - dp[4] = (25, 30) + 25 = (50, 55)
    - dp[5] = (55, 35) + 10 = (65, 45)
    - dp[6] = (35, 55) + 20 = (55, 75)

4. 로직2 -> 로직1을 간단히 변경
- dp[i] = max(세칸전+한칸전, 두칸전)
    - dp[1] = 10
    - dp[2] = 30
    - dp[3] = max(20, 10) + 15 = 35
    - dp[4] = max(10, 30) + 25 = 55
"""


def solution_1(N, stairs):
    dp = [[0, 0] for _ in range(N+1)]
    dp[1] = [stairs[0], stairs[0]]
    for i in range(2, N+1):
        dp[i] = [dp[i-1][1]+stairs[i-1], max(dp[i-2])+stairs[i-1]]
    print(max(dp[N]))


def solution_2(N, stairs):
    dp = [0] * 301
    scores = [0] + stairs + [0] * (300-N)
    dp[1] = scores[1]
    dp[2] = dp[1] + scores[2]
    for i in range(3, N+1):
        dp[i] = max(dp[i-3]+scores[i-1], dp[i-2]) + scores[i]
    print(dp[N])


if __name__ == "__main__":
    N, *stairs = map(int, open(0).read().split())
    solution_1(N, stairs)
    solution_2(N, stairs)


"""
테스트케이스

6
10
20
15
25
10
20
---
75
"""