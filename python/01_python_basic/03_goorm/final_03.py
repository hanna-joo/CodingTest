# K 공기업 변형 모의고사 3번
# keyword : 완전 탐색 개선, 다이나믹 프로그래밍, 3차원 DP
# return : N * N 크기의 정사각형 모양 타일에서 각 타일마다 가장 가까운 1타일과의 거리 출력

"""
1. 문제 분석
- 타일 크기 : 3 <= N <= 1000
- 타일 거리는 맨해튼 거리

2. DP의 필요성
- N 1000개 이상 -> for문 3개 이상 -> O(N^3) -> Python에서는 틀림
- 1억 번 계산 -> Python에서는 틀림
- 동적 프로그래밍 -> for문 줄이기
- 사방에서 탐색 -> 4방향 각각 관리 -> 3차원 DP

3. 해결 방안
- 데이터 핸들링으로 값 넣기
- 각 점에서 시작해서 1 찾기 -> 1에서 시작해서 각 점과의 거리 찾기
- 왼쪽만 관리하는 Matrix
- 오른쪽만 관리하는 Matrix
- 위쪽만 관리하는 Matrix
- 아래쪽만 관리하는 Matrix
"""


def closest_dist_1(size, info):
    # 완전 탐색 (시간 초과)
    """
    - 모든 지점을 매 번 탐색하는 것은 비효율적
    - N=1000, 모든 요소가 0인 경우 Timeout 발생
    - 매 타일 마다 N^2 탐색 * 탐색할 타일 N^2 = O(N^4)
    """
    # 1. 데이터 입력 받기
    INF = 1004
    N = int(size)
    Matrix = [[0]*(N+2) for _ in range(N+2)] # 넉넉하게 자리 만들기
    for i in range(1, N+1):
        line = info[i-1].strip()
        for j in range(1, N+1):
            if line[j-1] == '1':
                Matrix[i][j] = 1
    # 2. 모든 좌표 탐색
    for x in range(1, N+1):
        for y in range(1, N+1):
            distance = INF
            # 2.1. 상하탐색 (맨 위에서부터 x,y와 가까운 1 찾기)
            for i in range(1, N+1):
                if Matrix[i][y] == 1:
                    if distance > abs(i-x):
                        distance = abs(i-x)
            # 2.2. 좌우탐색 (맨 왼쪽에서부터 x,y와 가까운 1 찾기)
            for j in range(1, N+1):
                if Matrix[x][j] == 1:
                    if distance > abs(j-y):
                        distance = abs(j-y)
            if distance == INF:
                distance = -1
            print(distance, end = ' ')
        print()


def closest_dist_2(size, info):
    # 동적 프로그래밍
    """
    - 1에서 거리 퍼져나가기
    - 탐색 타일이 1이라면 거리 = 0
    - 탐색 타일이 0이라면 거리 = 전 타일의 거리 + 1
    - 탐색 방향도 주의해서 range() 설정
    - matrix[i][j] = 1, dp[i][j] = 0
    - 좌 : dp[0][i][j] = 0 / dp[0][i][j-1] + 1 <- 왼쪽부터
    - 우 : dp[1][i][j] = 0 / dp[1][i][j+1] + 1 <- 오른쪽부터
    - 상 : dp[2][i][j] = 0 / dp[2][i-1][j] + 1 <- 위에서부터
    - 하 : dp[3][i][j] = 0 / dp[3][i+1][j] + 1 <- 밑에서부터
    """
    # 1. 데이터 입력 받기
    INF = 1004
    N = int(size)
    matrix = [[0]*(N+2) for _ in range(N+2)] # 넉넉하게 자리 만들기
    dp = [[[INF]*(N+2) for _ in range(N+2)] for _ in range(4)]
    for i in range(1, N+1):
        line = info[i-1].strip()
        for j in range(1, N+1):
            if line[j-1] == '1':
                matrix[i][j] = 1
    
    # 2. 1과의 거리 저장
    # 2.1. 좌우 탐색 - 행(i)은 순서대로, 열(j)은 좌에서 순서/우에서 역순
    for i in range(1, N+1):
        for j in range(1, N+1):
            dp[0][i][j] = 0 if matrix[i][j] else dp[0][i][j-1] + 1
        for j in range(N, 0, -1):
            dp[1][i][j] = 0 if matrix[i][j] else dp[1][i][j+1] + 1
    # 2.2. 상하 탐색 - 열(j)은 순서대로, 행(i)은 상에서 순서/하에서 역순
    for j in range(1, N+1):
        for i in range(1, N+1):
            dp[2][i][j] = 0 if matrix[i][j] else dp[2][i-1][j] + 1
        for i in range(N, 0, -1):
            dp[3][i][j] = 0 if matrix[i][j] else dp[3][i+1][j] + 1

    # 3. 결과 출력
    for i in range(1, N+1):
        for j in range(1, N+1):
            ans = min(dp[k][i][j] for k in range(4))
            if ans >= INF:
                ans = -1
            print(ans, end=' ')
        print()


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [('4', ['0100', '0001', '0000', '0010'])]
    '''
    1 0 1 1
    3 1 1 0
    -1 2 1 1
    2 1 0 1
    '''

    for case in test_cases:
        closest_dist_1(case[0], case[1])
        closest_dist_2(case[0], case[1])
