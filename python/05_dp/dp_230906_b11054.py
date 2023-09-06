# 가장 긴 바이토닉 부분 수열 (g4, 50.657%)
# source : https://www.acmicpc.net/problem/11054
# keyword : 구현
# return : 주어진 수열의 부분 수열 중 가장 긴 바이토닉 수열의 길이 출력

"""
1. 문제
- 바이토닉 수열 : S1<S2<...<Sk>Sk+1>...>Sn-1>Sn
    - 10, 20, 30, 25, 20
    - 10, 20, 30, 40
    - 50, 40, 25, 10
- 바이토닉이 아닌 수열
    - 1, 2, 3, 2, 1, 2, 3, 2, 1
    - 10, 20, 30, 40, 20, 30
- 수열 A가 주어졌을 때, 그 수열의 부분 수열 중 가장 긴 바이토닉 수열의 길이 출력

2. 입력 및 제한
- 수열 A의 크기 N (1<=N<=1,000)
- 수열 A (1<=Ai<=1,000)

3. 로직 1 : 시간 초과
- 재귀 함수
    - 다음 값과 부호를 확인한다
    - 부호가 -인 경우, 더 이상 내려갈 곳이 없을 때까지 탐색한다
    - 종료 : 끝까지 탐색할 때 / 변화가 없을 때 / 감소하다가 증가할 때
- 만일 l_max가 남은 길이보다 길다면 종료한다

4. 로직 2
- 다이나믹 프로그래밍
- i번째를 기준으로 부분 수열 구하기
    - i번째 기준으로 앞,뒤는 A[i]보다 작아야 함
    - i가 끝점인 증가부분수열 + i가 시작점인 감소부분수열
"""


import sys
input = sys.stdin.readline


def solution_1(N, A):
    global l_max
    l_max = 1
    def rec(cur, idx, l, dec):
        global l_max
        if idx == N:
            l_max = max(l_max, l)
        for i in range(idx, N):
            tmp = cur - A[i]
            # 변화가 없거나 감소하다가 증가할 때 탐색 종료
            if tmp == 0 or (dec and tmp <= 0):
                l_max = max(l_max, l)
                continue
            # 계속 증가하거나 감소할 때 탐색 지속
            if tmp > 0:
                rec(A[i], i+1, l+1, 1)
            else:
                rec(A[i], i+1, l+1, 0)
            

    for i in range(N):
        if l_max >= N-i:
            break
        rec(A[i], i+1, 1, 0)

    print(l_max)


def solution_2(N, A):
    dp_asc, dp_desc = [1] * (N), [1] * (N)
    for i in range(N):
        for j in range(i):
            if A[j] < A[i]:
                dp_asc[i] = max(dp_asc[i], dp_asc[j] + 1)
            if A[::-1][j] < A[::-1][i]:
                dp_desc[i] = max(dp_desc[i], dp_desc[j]+1)
    
    total = [x+y for x, y in zip(dp_asc, dp_desc[::-1])]
    print(max(total) -1)


if __name__ == "__main__":

    N, A = int(input()), [*map(int, input().split())]
    solution_1(N, A)
    solution_2(N, A)


"""
테스트케이스 : 7 / 1 / 3

10
1 5 2 1 4 3 4 5 2 1

5
1 1 1 1 1

6
9 8 9 1 2 3
"""