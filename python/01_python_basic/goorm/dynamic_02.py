# 보드 게임
# keyword : 다이나믹 프로그래밍
# return : 플레이어가 0번 칸에서 출발해서 N번 칸으로 이동할 수 있는 방법의 개수 출력

"""
1. 다이나믹 프로그래밍
- 같은 부분 문제가 여러 번 반복해서 등장할 때 해당 값을 저장해서 효율적으로 처리하는 기법

2. 다이나믹 프로그래밍 해결 방법
- 어떤 값(=반복되는 부분 문제의 정답)을 저장할 것인지 정한다
- 저장한 값들 간의 점화식을 세우고, 초기 값을 설정한 뒤 계산한다
- 점화식을 세울 때는 미리 저장해둔 값을 언제, 어떻게 재사용할지를 반영한다

3. 문제 해결 사고
- i번까지 가기 위해서는 직전에 i-1번 또는 i-3번에 위치해 있어야 한다
- i-1번 또는 i-3번에서 i번으로 가는 경우의 수는 1가지이다
- 즉, i번까지의 경우의 수 = (i-1번까지의 경우의 수) + (i-3번까지의 경우의 수)

4. 점화식 구하기
- dp[i] : 0번에서 i번까지 가는 경우의 수
- dp[0] = dp[1] = dp[2] = 1
- dp[3] = dp[3-1] + dp[3-3] = dp[2] + dp[0]
- dp[4] = dp[4-1] + dp[4-3] = dp[3] + dp[1]
- dp[5] = dp[5-1] + dp[5-3] = dp[4] + dp[2]
- dp[n] = dp[n-1] + dp[n-3]
"""

# Bottom-Up
def board(size):
    board = [0 for _ in range(size+1)]
    mod = 1000000007

    for i in range(size+1):
        # 초기값 세팅
        if i <= 2:
            board[i] = 1
        else:
            board[i] = (board[i-3] + board[i-1]) % mod
        
    answer = board[size]

    return answer


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [6, 7, 49584] # 6, 9, 871579385
    test_cases.append(int(input().rstrip()))

    for case in test_cases:
        print(board(case))