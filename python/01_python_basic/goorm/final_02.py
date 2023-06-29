# K 공기업 변형 모의고사 2번
# keyword : 복잡한 구현문제
# return : 선입력 이동 명령을 시행하고 미로 탈출 성공 여부와 이동 횟수(명령 시행 횟수) 출력

"""
0200
3330
0100
0000

1. 문제 분석
- r번째 행, c번째 열에 해당하는 칸 = M(r,c) 
- (0 : 통과 가능 칸, 1 : 출발 위치, 2 : 탈출 위치, 3 : 통과 불가능 칸)
- 이동 명령은 U, D, L, R로 상하좌우 1칸만 이동
- 미로 줄 : 3 <= N <= 200
- 이동 명령 수 : 1 <= K <= 10,000
- 명령이 이미 주어져 있음!!! (탐색X, 시뮬레이션O)
- 이동에 있어서 제약 조건 정리 중요!!!

2. 제약 조건
- 이동하는 칸이 벽인 경우 명령 무시
- 탈출 위치에 도착하면 명령 종료
- 모든 명령 수행 후 탈출 위치에 도착하지 못하면 실패

3. 해결 방법
- 2차원 배열에서 데이터 핸들링
- 방향과 이동 구현 : dx, dy
- 효율적 탐색 <-- Simulation --> BruteForce

4. 데이터 핸들링
- 함수형에서는 X, 일반형에서는 O
- 함수형 프로그래밍 시, 2차원 배열을 한 번 탐색해야 함
- 입출력 직접 구현 시, 데이터를 입력 받을 때 필요한 자료 추출
- 시작 지점을 입력과 동시에 받음
"""


def miro_escape_1(size, commands, info):
    N, K = map(int, size.split())
    commands = list(commands.rstrip())
    Matrix = list()

    # 핸들링을 통해서 찾고 싶은 값을 저장할 변수
    start_Point = []

    for i in range(N):
        temp = list(map(int, info[i].split()))
        # 2차원 매트릭스 생성
        Matrix.append(temp)
        # 시작 지점 찾기
        if 1 in temp:
            start_Point = [i, temp.index(1)]
            
    #print(Matrix)
    #print(start_Point)

    # Dir 기법
    dir = {
        "U": [-1, 0],
        "D": [1, 0],
        "L": [0, -1],
        "R": [0, 1]
    }

    # 시작 지점
    x, y = start_Point
    # 경로 상 탈출 지점에 도착 => 바로 탈출하기 위한 변수
    flag = True
    # 실제로 이동한 횟수
    move_cnt = 0
    # 구현 / 시뮬레이션
    for command in commands:
        nx = x + dir[command][0]
        ny = y + dir[command][1]
        if (0<=nx<N) and (0<=ny<N):
            if Matrix[nx][ny] == 3:
                continue
            elif Matrix[nx][ny] == 2:
                flag = False
                move_cnt += 1
                break
            else:
                x = nx
                y = ny
                move_cnt += 1
                
    if flag:
        return 'FAIL'
    else:
        return 'SUCCESS %d'%(move_cnt)


def miro_escape_2(size, commands, info):
    #import  sys
    #input = sys.stdin.readline

    N, K = map(int, size.split())
    M = list()
    # c_point => 시작지점
    c_point = list()
    for i in range(N):
        tmp = list(map(int, info[i].split()))
        M.append(tmp)
        # 시작 지점 추출 Good
        if 1 in tmp:
            j = tmp.index(1)
            c_point = [i, j]

    # 이동 횟수를 센다.
    t_counter = 0
    exited = False
    cx, cy = c_point
    nx, ny = cx, cy
    for command in commands:
        # 다음 탐색 지점 갱신
        if command == "U":
            nx -= 1
        elif command == "D":
            nx += 1
        elif command == "L":
            ny -=1
        else:
            ny += 1
        # 범위 & 지나가지 못하는 벽 검사
        if nx < 0 or nx >= N or ny < 0 or ny >= N or M[nx][ny] == 3:
            nx, ny = cx, cy
            continue
        t_counter += 1
        cx, cy = nx, ny
        # 시뮬레이션 종료와 비종료 조건
        if M[nx][ny] == 2:
            exited = True
            break

    if not exited:
        return 'FAIL'
    else:
        return f'SUCCESS {t_counter}'
    

def miro_escape_3(size, commands, info):
    # 내가 작성한 코드 수정
    n, k = map(int, size.split())
    #commands = list(input().rstrip())
    miro = list()
    for i in range(n):
        miro.append(list(map(int, info[i].split())))
                
    # 출발점 구하기
    found = False
    for i in range(n):
        for j in range(n):
            if miro[i][j] == 1:
                start = (i, j)
                found = True
                break
        if found:
            break
            
    # 명령 시행
    command_dict = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }

    move_cnt = 0
    exited = False
    cy, cx = start[0], start[1]
    for command in commands:
        move = command_dict[command]
        ny, nx = cy + move[0], cx + move[1]
        if (0 <= ny < n) and (0 <= nx < n):
            if miro[ny][nx] == 3:
                continue
            cy, cx = ny, nx
            move_cnt += 1
            if miro[ny][nx] == 2:
                exited = True
                break
    
    if not exited:
        return 'FAIL'
    else:
        return f'SUCCESS {move_cnt}'


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [('4 6', 'ULRDUU', ['0 0 0 3', '0 2 3 0', '3 0 3 3', '0 1 0 0']),
                  ('4 6', 'LRRRDD', ['3 0 3 1', '2 0 0 0', '0 0 3 3', '0 0 3 0'])] # SUCCESS 4 / FAIL

    for case in test_cases:
        print(miro_escape_1(case[0], case[1], case[2]))
        print(miro_escape_2(case[0], case[1], case[2]))
        print(miro_escape_3(case[0], case[1], case[2]))
