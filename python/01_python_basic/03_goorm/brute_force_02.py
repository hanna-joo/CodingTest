# 개미와 진딧물
# keyword : 구현, 완전 탐색, 맨해튼 거리
# return : 개미(1)와 진딧물(2)의 맨해튼 거리가 m 이하에 위치한 개미는 몇 마리인지 출력

"""
1. 문제 분석
- 맨해튼 거리 상에서 진딧물로부터 거리 M 이하에 위치한 개미의 수
- 어떤 개미를 중심으로 마름모 형태 땅 안에 진딧물이 존재하는지 탐색
- 정사각형 땅 : 1 <= N <= 100
- 수액 가능 거리 : 1 <= M <= 10

2. 방법 1
- 진딧물과 개미가 위치한 좌표 별도로 저장
- 특정 개미와 모든 진딧물 사이의 맨해탄 거리 측정
- M 이하인 경우 cnt ++1
- 총 시간 복잡도 = O(N^4)

3. 방법 2
- 특정 개미를 중심으로 마름모 형태 땅에 진딧물 있는지 탐색
- 마름모 영역에 해당하는 땅 = O(M^2)개
- 총 시간 복잡도 = O(N^2*M^2)
"""

def ants_receiving_sap_1(square, dist):
    square_size = len(square)
    ants, aphids = list(), list()
    
    for m in range(square_size):
        row = square[m]
        for n in range(square_size):
            if row[n] == 1:
                ants.append((m, n))
            elif row[n] == 2:
                aphids.append((m, n))

    ants_cnt = 0
    for ant in ants:
        for aphid in aphids:
            new_dist = abs(ant[0]-aphid[0]) + abs(ant[1]-aphid[1])
            if new_dist <= dist:
                ants_cnt += 1
                break # 진딧물 1개만 필요 > 다음 개미로 넘어가기

    return ants_cnt


def ants_receiving_sap_2(square, dist):
    size = len(square)

    def search(y, x, dist):
        # 마름모 윗 부분 탐색
        for dy in range(-dist, 0):
            # x 방향으로 이동 가능한 범위(dist)가 y 방향으로 이동한 만큼 줄어듦
            for dx in range(-dist-dy, dist+dy+1):
                if y + dy < 0 or y + dy >= size or x + dx < 0 or x + dx >= size:
                    continue
                # 해당 지점에 진딧물이 있으면 return
                if square[y + dy][x + dx] == 2:
                    return True
        # 마름모 아랫 부분 탐색
        for dy in range(0, dist+1):
            for dx in range(-dist+dy, dist-dy+1):
                if y + dy < 0 or y + dy >= size or x + dx < 0 or x + dx >= size:
                    continue
                if square[y + dy][x + dx] == 2:
                    return True
        # 마름모 범위에서 진딧물 발견 못한 경우
        return False
    
    ants_cnt = 0
    for i in range(size):
        for j in range(size):
            # 개미 발견 시 주변 마름모 범위에서 진딧물 탐색
            if square[i][j] == 1:
                if search(i, j, dist):
                    ants_cnt += 1

    return ants_cnt


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [([[2, 0, 0, 0], [2, 0, 0, 1], [2, 0, 0, 0], [2, 0, 0, 1]], 2),
                  ([[0, 1, 0, 0],[0, 2, 0, 1],[0, 0, 0, 1],[2, 0, 1, 0]], 2)] # 0, 3

    for case in test_cases:
        print(ants_receiving_sap_2(case[0], case[1]))
        print(ants_receiving_sap_2(case[0], case[1]))