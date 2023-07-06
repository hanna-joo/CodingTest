# 폭탄 구현하기
# keyword : 시뮬레이션, 수학
# return : N*N 크기의 정사각형 모양에서 폭탄(y,x)들을 떨어트렸을 때 모든 땅들의 폭탄 값 출력

"""
1. 문제 설명
- 폭탄이 떨어지면, 떨어진 위치 기준으로 십자가 영역 폭탄 값 증가
- K개의 폭탄이 떨어졌을 때 모든 땅의 폭탄 값 합 구하기

2. 영향 범위 표현
- dy = [-1, 0, 0, 1]
- dx = [0, -1, 1, 0]
- ny = y + dy
- nx = x + dx
- 주의 : 영향 범위가 땅 밖일 경우 예외 처리
"""

def bomb_sum_1(info, bombs):
    ground_len, bomb_cnt = map(int, info.split())
    ground = [[0] * (ground_len+1) for _ in range(ground_len+1)]
    effect = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

    for bomb in bombs:
        y, x = map(int, bomb.split())
        for m, n in effect:
            m, n = y+m, x+n
            if (0<m<=ground_len) and (0<n<=ground_len):
                ground[m][n] += 1

    bomb_sum = 0
    for i in range(1, ground_len+1):
        bomb_sum += sum(ground[i])
        
    return bomb_sum


def bomb_sum_2(info, bombs):
    ground_len, bomb_cnt = map(int, info.split())
    ground = [[0 for _ in range(ground_len+1)] for _ in range(ground_len+1)]
    dy = [-1, 0, 0, 1]
    dx = [0, -1, 1, 0]

    for bomb in bombs:
        y, x = map(int, bomb.split())
        ground[y][x] += 1
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 1 or nx < 1 or ny > ground_len or nx > ground_len:
                continue
            ground[ny][nx] += 1
    
    bomb_sum = 0
    for i in range(1, ground_len+1):
        for j in range(1, ground_len+1):
            bomb_sum += ground[i][j]
            
    return bomb_sum


def bomb_sum_3(info, bombs):
    # 폭탄 값의 합이기 때문에 몇 개의 영역이 영향을 받는지만 파악하면 됨
    # 5칸에서 경계 선에 떨어졌을 때만큼 빼기
    ground_len, bomb_cnt = map(int, info.split())

    bomb_sum = 0
    for bomb in bombs:
        y, x = map(int, bomb.split())
        bomb_sum += 5 - (y==1) - (y==ground_len) - (x==1) - (x==ground_len)

    return bomb_sum


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [('3 3', ['3 3', '3 3', '1 1']), 
                  ('4 4', ['1 1', '4 4', '3 3', '2 4'])] # 9, 15
    info = input().rstrip()
    test_cases.append((info, list(input().rstrip() for _ in range(int(info[-1])))))

    for case in test_cases:
        print(bomb_sum_1(case[0], case[1]))
        print(bomb_sum_2(case[0], case[1]))
        print(bomb_sum_3(case[0], case[1]))