# Z (s1, 40.442%)
# source : https://www.acmicpc.net/problem/1074
# keyword : 분할 정복, 재귀
# return : Z탐색으로 r행 c열을 몇 번째로 방문했는지 출력

"""
1. 문제
- Z모양으로 탐색 (왼-오-왼아래-오른아래)
- 2^N * 2^N
- N > 1인 경우, 4등분 후 재귀적으로 방문
- r행 c열을 몇 번째로 방문했는지 출력
- 정수 N, r, c (1<=N<=15, 0<=r,c<2^N)

2. 로직 1 : 4분할하면서 범위 시작점 갱신
- base는 현재 범위 길이
- 4분할 시 base = 기존 base의 절반
- (r,c)가 위치한 사분면 선택
    - (범위 시작점 + base)와 (r,c) 비교
- 해당하는 사분면의 범위 시작점 찾기
- 각 사분면 이전 칸 개수 한 번에 계산
    - 2사분면 : 현재 범위 크기의 칸 1개+
    - 3사분면 : 현재 범위 크기의 칸 2개+
    - 4사분면 : 현재 범위 크기의 칸 3개+
- 위 과정을 반복하는데 범위 시작점 넘겨주기
- base가 1칸이 되면 멈추기

3. 로직 2 : 4분할하면서 (r,c) 갱신
- 4분할 시 base = 기존 base의 절반
- (r,c)가 위치한 사분면 선택
    - base와 (r,c) 비교
- 각 사분면 이전 칸 개수 한 번에 계산
- (r,c) 좌표 이동
- 위 과정을 base > 1까지 반복
"""


def z_search_1(N, r, c):
    global cnt
    cnt = 0
    move = [(0, 0), (0, 1), (1, 0), (1, 1)]


    def rec(num, x, y):
        global cnt
        base = 2 ** (num-1)
        if r < (x+base):
            q = 0 if (y+base) > c else 1
        else:
            q = 2 if (y+base) > c else 3
        nx, ny = x+(move[q][0]*base), y+(move[q][1]*base)
        cnt += (q)*base*base
        if num >= 2:
            rec(num-1, nx, ny)


    rec(N, 0, 0)
    print(cnt)


def z_search_2(num, r, c):
    r += 1
    c += 1
    base = 2**num
    cnt = 0
    while base > 1:
        base *= 0.5
        q = (1 if r <= base else 3)+(0 if c <= base else 1)
        cnt += base**2*(q-1)
        r -= base if base < r else 0
        c -= base if base < c else 0
    print(int(cnt))


if __name__ == "__main__":

    import sys
    input = sys.stdin.readline

    N, r, c = map(int, input().split())
    z_search_1(N, r, c)
    z_search_2(N, r, c)




"""
테스트 케이스 : 11 / 63 / 0 / 41

2 3 1

3 7 7

1 0 0

3 6 1
"""