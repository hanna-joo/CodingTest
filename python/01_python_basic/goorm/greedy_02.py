# 구름 스퀘어
# keyword : 그리디 알고리즘, 회의실 배정 문제
# return : N개의 행사 시작 시간과 종료 시간이 주어질 때, 구름 스퀘어에서 열릴 수 있는 행사의 최대 개수 출력

"""
1. 회의실 배정 문제
- 시간이 겹치지 않게 최대한 많은 행사 개최
- 완전 탐색 : 2의 N승 개의 경우의 수가 있기 때문에 시간 초과
- 완전 탐색이 아닌 다른 접근 필요

2. 행사를 선택하는 기준 세우기
- 시작 시간이 빠른 순으로 행사 선택
- 행사 시간이 짧은 순으로 행사 선택
- 종료 시각이 빠른 순으로 행사 선택

3. 각 기준의 반례가 있는지 확인
- 해당 기준이 독립성을 보장하는 지도 확인(다음 선택에 영향 없는지)
- 1개의 회의실에 대해서 종료 시간 순으로 회의 선택 시 가장 많은 회의를 개최할 수 있는 최적해 보장
"""

def events_max_1(event_tm):
    import heapq
    # 모든 행사 시작 및 끝 시간 저장
    events = list()
    for tm in event_tm:
        s, e = map(int, tm.split())
        heapq.heappush(events, (e, s))

    # 가장 빨리 끝나는 것부터 선별
    count, now = 0, 0
    while events:
        # 가장 빨리 끝나는 행사 뽑기
        event = heapq.heappop(events)
        if event[1] > now:
            # 행사 진행
            count += 1
            # 다음 행사가 가능한 시간
            now = event[0]
                
    return count


def events_max_2(event_tm):
    events = list()
    for tm in event_tm:
        s, e = map(int, tm.split())
        events.append([s, e])
    
    events.sort(key=lambda x: (x[1], x[0]))
    count = now = 0
    for s, e in events:
        if s > now:
            count += 1
            now = e

    return count

if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [['1 2', '2 3', '3 6', '4 5', '1 10', '11 13'], 
                  ['1 2', '3 3', '3 5', '4 10', '5 6', '7 9', '10 11']] # 3, 5

    for case in test_cases:
        print(events_max_1(case))
        print(events_max_2(case))