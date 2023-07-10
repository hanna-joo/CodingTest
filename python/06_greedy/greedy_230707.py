# 구명보트
# source : https://school.programmers.co.kr/learn/courses/30/lessons/42885#
# keyword : 그리디 알고리즘
# return : 모든 사람 구출하기 위해 필요한 구명보트 개수 최솟값

"""
1. 그리디 알고리즘
- 탐욕법, 탐욕 알고리즘
- 최적해를 구하는 데에 사용되는 근사적인 방법
- 문제를 해결할 때 있어서 현재 경우만 고려해서 최적의 상황을 선택하는 방법

2. 그리디 적용 필수 조건
- 현재의 최적의 선택이 다음 선택에 영향을 미치지 않아야 함
- 현재의 선택이 최종 선택의 최적 해결 방법에 포함되어야 함

3. 대표 그리디 문제
- 동전 교환 문제
- 회의실 배정 문제
- Fractional Knapsack, 분할 가능한 배낭 채우기
- 다익스트라, 프림, 크루스칼 등의 비용 최적화하는 그래프 이론

4. 해결 방법
- 정렬 + 큐
- 구명 보트 1개에 최대 2명 탑승 가능
- 가장 가벼운 사람과 무거운 사람 무게가 limit 넘는지 확인
- 넘는다면 혼자만 탑승 가능  -> boat ++1
- 안 넘는다면 둘이 탑승 가능 -> boat ++1
"""


def solution(people, limit):
    from collections import deque
    people.sort()
    q = deque(people)
    boat = 0
    while len(q) >= 2:
        if q[0] + q[-1] > limit:
            q.pop()
            boat += 1
        else:
            q.pop()
            q.popleft()
            boat += 1
    if q:
        boat += 1
    return boat


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [[[70, 50, 80, 50], 100], 
                  [[70, 80, 50], 100],
                  [[20, 80, 20, 80], 100],
                  [[50, 20, 30, 60, 40], 100],
                  [[10, 10, 90, 80, 10, 60], 100],
                  [[20, 20, 90, 80, 20], 100]] # 3 / 3 / 2 / 3 / 3 / 3
    
    for case in test_cases:
        print(solution(case[0], case[1]))