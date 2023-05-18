# problem source : https://www.acmicpc.net/problem/9252
# return : 주어진 두 문자열의 LCS 길이, LCS 출력
    # LCS 가 여러가지일 경우에는 아무거나 출력
    # LCS 의 길이가 0일 때는 LCS 출력하지 않음

import sys
input = sys.stdin.readline

'''

LCS : 최장 공통 부분 수열
- 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾아라
- 2차원 배열에 공통 부분 수열 개수 저장
- 문자열 하나 하나 서로 비교
- 같다 : 공통 부분 수열 개수 1개 증가
    LCS[i][j] = LCS[i-1][j-1] + 1
- 다르다 : 이전 공통 부분 수열 개수만 저장
    LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
- 수열 추출
    1) LCS[i][j]에서 출발
    2) LCS[i-1][j]와 LCS[i][j-1]와 비교
    3) 같다면 해당 위치로 이동
    4) 다르다면 result에 해당 문자 추가하고 LCS[i-1][j-1]로 이동

'''

# 두 문자열 입력 받기
str_i = ' ' + input()
str_j = ' ' + input()
n, m = len(str_i)-1, len(str_j)-1
lcs = ''

# n행 m열의 2차원 배열 생성
dp = [[0 for i in range(m+1)] for j in range(n+1)]

# 비교해서 공통 부분 수열 정보 입력
for i in range(1, n+1):
    for j in range(1, m+1):
        if str_i[i] == str_j[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# 공통 부분 수열 추출
i, j = n, m
while (i > 0) and (j > 0):
    now = dp[i][j]
    # 현재까지의 공통 부분 수열 개수가 이전 문자열들과 동일하다면
    # 정보 업데이트가 일어난 것이 아니기 때문에
    # 해당 문자는 공통 부분이 아니다
    if (now == dp[i-1][j]):
        i = i-1
    elif (now == dp[i][j-1]):
        j = j-1
    # 현재까지의 공통 부분 수열 개수가 이전 문자열들보다 크다면
    # 정보 업데이트가 발생했다는 뜻이고
    # 해당 문자는 새로 추가된 공통 부분이다
    else:
        lcs += str_i[i]
        i, j = i-1, j-1

lcs = lcs[::-1]
print(lcs)
print(len(lcs))