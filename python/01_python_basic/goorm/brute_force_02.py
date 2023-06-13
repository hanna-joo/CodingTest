# 개미와 진딧물
# keyword : 구현, 완전 탐색, 맨해튼 거리
# return : 개미(1)와 진딧물(2)의 맨해튼 거리가 m 이하인 경우 수액 가능, 수액 받는 개미는 몇 마리인지 출력

"""
1. 인코딩
- 정해진 정보를 비트의 조합으로 표현하는 것

2. ASCII
- 문자를 인코딩하는 방식 중 하나
- 문자를 특정 비트의 집합으로 표현하는 것
- ord() : 특정 문자 > ASCII 값 (정수)
- chr() : ASCII 값 > 해당 문자
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
    ants_cnt = 0
    

    return ants_cnt


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [([[2, 0, 0, 0], [2, 0, 0, 1], [2, 0, 0, 0], [2, 0, 0, 1]], 2),
                  ([[0, 1, 0, 0],[0, 2, 0, 1],[0, 0, 0, 1],[2, 0, 1, 0]], 2)] # 0, 3

    for case in test_cases:
        print(ants_receiving_sap_2(case[0], case[1]))
        print(ants_receiving_sap_2(case[0], case[1]))