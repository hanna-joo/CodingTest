# Z (s1, 40.442%)
# source : https://www.acmicpc.net/problem/1074
# keyword : 분할 정복, 재귀, 구현
# return : Z 방향 탐색 구현

"""
1. 문제
- Z모양으로 탐색 (왼-오-왼아래-오른아래)
- 2^N * 2^N
- N > 1인 경우, 4등분 후 재귀적으로 방문
- r행 c열까지 탐색 후 몇 번째로 방문했는지 출력

2. 입력 및 제한
- 정수 N, r, c (1<=N<=5, 0<=r,c<2^N)

3. 로직
- 이동 방향 : [(0, 0), (0, 1), (1, 0), (1, 1)]
- 시작점 구하기
- 4칸짜리인지 확인
    - 4칸짜리 O -> Z방향으로 1 변경
    - 4칸짜리 X -> 분할 -> 새 시작점 구하기
"""


def solution(N, r, c):
    move = [(0, 0), (0, 1), (1, 0), (1, 1)]
    arr = [[0 for _ in range(2**N)] for _ in range(2**N)]
    global cnt
    cnt = 0
    def rec(num, x, y):
        global cnt
        if num == 1:
            for dx, dy in move:
                nx, ny = x+dx, y+dy
                if (nx, ny) == (r, c):
                    return False
                arr[nx][ny] = 1
                cnt += 1
            for i in range(2**N):
                print(arr[i])
            print()  
          
            return True
        for dx, dy in move:
            nx, ny = x+(2**(num-1))*dx, y+(2**(num-1))*dy
            res = rec(num-1, nx, ny)
            if not res:
                return False
        return True
    rec(N, 0, 0)
    print(cnt)


if __name__ == "__main__":

    import sys
    input = sys.stdin.readline

    N, r, c = map(int, input().split())
    solution(N, r, c)


"""
테스트 케이스 : 11 / 63 / 0 / 41

2 3 1

3 7 7

1 0 0

3 6 1
"""