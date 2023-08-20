# 주사위 굴리기 (g4, 44.457%)
# source : https://www.acmicpc.net/problem/14499
# keyword : 구현
# return : 주사위가 이동할 때마다 상단에 쓰여 있는 값 출력


"""
1. 문제
- N*M 지도
- 주사위 전개도
- 이동한 칸에 쓰여 있는 수 
    - 0인 경우 -> 칸=바닥면
    - 0이 아닌 경우 -> 바닥면=칸, 칸=0
- 주사위를 놓은 곳의 좌표와 이동시키는 명령
    - 지도 바깥으로 이동시키려는 경우 명령, 출력 무시

2. 입력
- 첫째 줄
    - 지도 크기 세로N과 가로M (1<=N,M<=20)
    - 주사위를 놓은 곳의 좌표 x, y (0<=x<=N-1, 0<=y<=M-1)
    - 명령의 개수 K(1<=K<=1,000)
- 둘째 줄 ~ N째 줄
    - 지도에 쓰여 있는 수가 북쪽부터 남쪽으로 각 줄은 서쪽, 동쪽 형태로 주어짐
    - 주사위를 놓은 칸에 쓰여 있는 수는 항상 0
    - 지도의 각 칸에 쓰여 있는 수 x (0<=x<10)
- 마지막 줄 : 이동하는 명령
    - 1-동쪽 / 2-서쪽 / 3-북쪽 / 4-남쪽

3. 로직 
"""


import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
ops = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0] # 위,아래,좌,우,앞,뒤
move = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
for op in ops:
    nx, ny = x+move[op][0], y+move[op][1]
    if nx<0 or ny<0 or nx>=N or ny>=M:
        continue
    
    if op == 1:
        dice = [dice[2], dice[3], dice[1], dice[0], dice[4], dice[5]]
    elif op == 2:
        dice = [dice[3], dice[2], dice[0], dice[1], dice[4], dice[5]]
    elif op == 3:
        dice = [dice[4], dice[5], dice[2], dice[3], dice[1], dice[0]]
    else:
        dice = [dice[5], dice[4], dice[2], dice[3], dice[0], dice[1]]
    x, y = nx, ny
    if ground[x][y] == 0:
        ground[x][y] = dice[1]
    else:
        dice[1], ground[x][y] = ground[x][y], 0

    print(dice[0])




"""
테스트케이스

4 2 0 0 8
0 2
3 4
5 6
7 8
4 4 4 1 3 3 3 2

3 3 1 1 9
1 2 3
4 0 5
6 7 8
1 3 2 2 4 4 1 1 3

2 2 0 0 16
0 2
3 4
4 4 4 4 1 1 1 1 3 3 3 3 2 2 2 2

3 3 0 0 16
0 1 2
3 4 5
6 7 8
4 4 1 1 3 3 2 2 4 4 1 1 3 3 2 2
---결과 출력
0
0
3
0
0
8
6
3

0
0
0
3
0
1
0
6
0

0
0
0
0

0
0
0
6
0
8
0
2
0
8
0
2
0
8
0
2
"""