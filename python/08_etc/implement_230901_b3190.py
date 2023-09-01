# 뱀 (g4, 40.117%)
# source : https://www.acmicpc.net/problem/3190
# keyword : 구현
# return : 사과를 먹으면 길어지는 뱀이 부딪혀서 종료될 때까지의 시간 출력

"""
1. 문제
- Dummy 도스게임
    - 시작 위치 (0,0), 시작 길이 1, 시작 방향 오른쪽
    - 머리를 먼저 다음 칸에 이동
    - 이동한 곳이 벽/자기자신이면 게임 종료
    - 이동한 칸에 사과 있으면, 사과 사라지고 꼬리 위치는 그대로
    - 이동한 칸에 사과 없으면, 꼬리도 이동
- 사과 위치, 뱀 이동경로 주어질 때 게임이 몇 초에 끝나는지 계산

2. 입력 및 제한
- 보드의 크기 N (2<=N<=100)
- 사과의 개수 K (0<=K<=100)
- 사과의 위치(행,열) K줄
- 뱀의 방향 변환 횟수 L (1<=L<=100)
- 뱀의 방향 변환 정보 게임 시작 X초 뒤에 왼/오른쪽 90도 방향 회전 (0<X<=10,000)

3. 로직
- X초 전까지 이동 및 사과 먹기
    - 이동한 좌표가 벽이거나 자기 자신이면 종료
    - 이동할 때마다 머리 좌표(hy, hx) 2로 변경 snake에 넣기
    - 사과가 없으면 snake 에서 하나 빼고 꼬리 좌표 0으로 돌려놓기
- X초 되면 방향 전환
    - L -> dy, dx = move[i-1]
    - D -> dy, dx = move[i+1]
"""


import sys
input = sys.stdin.readline

N, K = int(input()), int(input())
board = [[-1]*(N+2)] + [[-1]+[0 for _ in range(N)]+[-1] for _ in range(N)] + [[-1]*(N+2)]
# 사과 놓기
for _ in range(K):
    r, c = map(int, input().split())
    board[r][c] = 1
# 명령어 저장
ops = []
for _ in range(int(input())):
    x, c = input().rstrip().split()
    ops.append((int(x), c))
# 초깃값 설정
move = [(0, 1), (1, 0), (0, -1), (-1, 0)] # D -> +1, L -> -1
sec, hx, hy, i = 0, 1, 1, 0
snake = [(hy, hx)]
board[hy][hx] = 2
# 게임 시작
while True:
    sec += 1
    # 머리가 다음 좌표로 이동
    hy, hx = hy+move[i][0], hx+move[i][1]
    # 벽이나 자기 자신을 만나면 종료
    if board[hy][hx] in (-1, 2):
        break
    # 사과가 없으면 snake 길이 줄이기
    if board[hy][hx] == 0:
        ty, tx = snake.pop(0)
        board[ty][tx] = 0
    # 이동한 좌표 표시하고 snake에 추가하기
    snake.append((hy, hx))
    board[hy][hx] = 2
    # 방향 전환
    if ops and sec == ops[0][0]:
        if ops.pop(0)[1] == 'L':
            i = (i-1) % 4
        else:
            i = (i+1) % 4

print(sec)


"""
테스트케이스 : 9 / 21 / 13

6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L

10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
"""