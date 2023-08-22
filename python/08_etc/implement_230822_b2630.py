# 색종이 만들기 (s4, 69.35%)
# source : https://www.acmicpc.net/problem/2630
# keyword : 구현, 해시
# return : N의 길이인 정사각형을 잘랐을 때 하얀색과 파란색 색종이 개수 출력

"""
1. 문제
- 정사각형이 모두 하나의 색으로 칠해질 때까지 4등분
- 하얀색 색종이와 파란색 색종이 개수 구하기

2. 입력
- 전체 종이의 한 변의 길이 N (N=[2, 4, 8, 16, 32, 64, 128])
- 색종이의 색 정보 (0=하얀색, 1=파란색)

3. 로직 
- 재귀 함수
- 한 줄씩 탐색한다 (w=False, b=False)
    - 하얀색을 만나면 w=True, 파란색을 만나면 b=True
- 탐색 완료 후 w, b 둘 다 True면 나눈다
- 탐색 완료 후 w, b 둘 중에 하나만 True면 카운트 하고 종료한다
"""


import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N = int(input())

global b_cnt, w_cnt
b_cnt, w_cnt = 0, 0
paper = [[*map(int, input().split())] for _ in range(N)]

move = [(0, 0), (0, 1), (1, 0), (1, 1)]
def cut(y, x, l):
    global w_cnt, b_cnt
    w, b = False, False
    for r in paper[y:y+l]:
        for c in r[x:x+l]:
            if c == 0: w = True
            else: b = True
        if w and b:
            for i in range(4):
                ny, nx = y+(move[i][0]*l//2), x+(move[i][1]*l//2)
                cut(ny, nx, l//2)
            break
    if not (w and b):
        if w: w_cnt += 1
        else: b_cnt += 1

cut(0, 0, N)
print(w_cnt)
print(b_cnt)


"""
테스트케이스

8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1
---결과 출력
9
7
"""