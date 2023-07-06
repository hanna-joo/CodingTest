# 거리두기
# keyword : 다이나믹 프로그래밍, Bottom-Up DP
# return : 1줄 당 3개의 테이블이 있는 N줄의 테이블에서 거리두기 스티커를 붙일 수 있는 경우의 수 출력

"""
1. 다이나믹 프로그래밍 문제 해결 방식
- Top-down : 큰 문제를 작은 문제로 쪼개서 해결
- Bottom-up : 작은 문제들의 값들을 잘 조합해서 큰 문제 해결
- 저장한 값들을 활용해서 문제를 어떻게 해결할 수 있는지 그림 그려보면서 풀기

2. Bottom-up 으로 해결
- 점화식 세우기
- 작은 문제의 답을 먼저 구한 뒤, 해당 답을 이용해 큰 문제의 답을 계산
- 현재 상태가 되기 위해 이전 상태를 파악해야 함

3. Top-down 으로 해결
- 점화식 세우기
- 큰 문제의 답을 먼저 구하려고 시도
- 그를 계산하기 위해 조금 더 작은 문제를 해결하고
- 그 문제를 해결하기 위해 더 더 작은 문제를 해결하는 식

3. 점화식
- 0번   : [0, 0, 0]
- 1-3번 : [1, 0, 0], [0, 1, 0], [0, 0, 1]
- 4번   : [1, 0, 1]
- dp[i][j] : i번째 줄의 책상에 j번 상태로 스티커 배치하는 경우의 수
- dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3] + dp[i-1][4]
- dp[i][1] = dp[i-1][0] + dp[i-1][2] + dp[i-1][3]
- dp[i][2] = dp[i-1][0] + dp[i-1][1] + dp[i-1][3] + dp[i-1][4]
- dp[i][3] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
- dp[i][4] = dp[i-1][0] + dp[i-1][2]
- 최종 식 = dp[N][0] + dp[N][1] + dp[N][2] + dp[N][3] + dp[N][4]
- 총 시간 복잡도 : O(N)
"""

# Bottom-Up
def distancing_1(line):
    mod = 10 ** 8 + 7

    pre = [1, 1, 1, 1, 1]
    for i in range(1, line):
        cur0 = (pre[0] + pre[1] + pre[2] + pre[3] + pre[4]) % mod
        cur1 = (pre[0] + pre[2] + pre[3]) % mod
        cur2 = (pre[0] + pre[1] + pre[3] + pre[4]) % mod
        cur3 = (pre[0] + pre[1] + pre[2]) % mod
        cur4 = (pre[0] + pre[2]) % mod
        pre = [cur0, cur1, cur2, cur3, cur4]

    case_cnt = sum(pre) % mod

    return case_cnt

# Bottom-Up
def distancing_2(line):
    dp = [[0 for _ in range(5)] for _ in range(line+1)]
    dp[0][0] = 1
    mod = 100000007

    for i in range(1, line+1):
        dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3] + dp[i-1][4]) % mod
        dp[i][1] = (dp[i-1][0] + dp[i-1][2] + dp[i-1][3]) % mod
        dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][3] + dp[i-1][4]) % mod
        dp[i][3] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % mod
        dp[i][4] = (dp[i-1][0] + dp[i-1][2]) % mod

    return sum(dp[line]) % mod

# Top-Down
def distancing_3(line):
    import sys
    sys.setrecursionlimit(150000)
    
    # 해당 코드는 스택 메모리 제한으로 일부 테스트 케이스 통과 불가
    # 스택 메모리 제한을 일시적으로 조금 늘려서 문제 해결
    # 단, 시스템에 직접 접근하는 코드로, 일반 코테에서는 사용 금지
    # import resource
    # resource.setrlimit(resource.RLIMIT_STACK, (64 * 1024 * 1024, -1))

    mod = 10 ** 8 + 7
    dp = dict()
    for n in range(5):
        dp[(0, n)] = 1 if n == 0 else 0

    # i = i번째 줄, n = 상태
    def get(i, n):
        if (i, n) in dp:
            return dp[(i, n)]
        ret = 0
        if n == 0:
            ret += get(i-1, 0) + get(i-1, 1) + get(i-1, 2) + get(i-1, 3) + get(i-1, 4)
        elif n == 1:
            ret += get(i-1, 0) + get(i-1, 2) + get(i-1, 3)
        elif n == 2:
            ret += get(i-1, 0) + get(i-1, 1) + get(i-1, 3) + get(i-1, 4)
        elif n == 3:
            ret += get(i-1, 0) + get(i-1, 1) + get(i-1, 2)
        elif n == 4:
            ret += get(i-1, 0) + get(i-1, 2)
        ret %= mod
        dp[(i, n)] = ret
        return ret
    
    case_cnt = 0
    for n in range(5):
        case_cnt += get(line, n)

    return case_cnt % mod


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [1, 2, 3] # 5, 17, 63
    test_cases.append(int(input().rstrip()))

    for case in test_cases:
        print(distancing_1(case))
        print(distancing_2(case))
        print(distancing_3(case))