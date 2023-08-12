# 가장 긴 증가하는 부분 수열 (s2, 37.712%)
# source : https://www.acmicpc.net/problem/11053
# keyword : 다이나믹 프로그래밍
# return : 수열 A의 최장 부분 수열 길이 출력

"""
1. 문제
- A = {10, 20, 10, 30, 20, 50}
- 최장 증가 부분 수열 = {10, 20, 30, 50}

2. 입력
- 수열 A의 크기 N (1<=N<=1,000)
- 수열 A를 이루고 있는 Ai (1<=Ai<=1,000)

3. 점화식
- 첫 번째까지 왔을 때 최증부수 = 1
- 두 번째까지 왔을 때 최증부수
    - 첫 번째 < 두 번째 : 1+1
    - 첫 번째 >= 두 번째 : 1
- 세 번째까지 왔을 때 최증부수
    - 세 번째보다 앞에 있으면서 작은 값 중 최증부수 최댓값
- dp[i] = max(dp[1] ~ dp[i-1])
"""

def solution_1(num, arr):
    dp = [1 for _ in range(N)]

    for i in range(num):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] <= dp[j]:
                dp[i] = dp[j] + 1

    print(max(dp))


def solution_2(num, arr):
    stack = [arr[0]]

    for new in arr[1:]:
        if stack[-1] < new:
            stack.append(new)
        else:
            for i, pre in enumerate(stack):
                if new <= pre:
                    stack[i] = new
                    break
    
    print(len(stack))


if __name__ == "__main__":

    N = int(input())
    A = [*map(int, input().split())]

    solution_1(N, A) # 104ms
    solution_2(N, A) # 44ms



"""
테스트케이스 : 4 / 5 / 1 / 4 / 6

6
10 20 10 30 20 50

6
10 20 50 30 40 45

6
10 10 9 8 7 1

7
100 200 10 20 300 40 50

9
1 5 2 3 4 2 7 10 1
"""
