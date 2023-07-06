# K 공기업 변형 모의고사 1번
# keyword : 자료형(defaultdict), 정렬
# return : 가장 많이 실행한 이벤트 출력, 여러 개라면 번호가 큰 순서에서 작은 순서로 출력

"""
1. 문제 분석
- 이벤트 개수 : 1 <= N <= 100,000
- 사용자 수 : 1 <= M <= 1,000
- 명령 수와 이벤트 번호 동시에 주어짐

- 자주 실행하는 이벤트 = 이벤트 정렬
- m개의 테스트마다 주어지는 k개의 숫자 중에서 최다 등장한 정수를 찾는 문제
- 최다 등장한 정수가 같다면, 큰 정수에서 작은 정수로 출력

2. 해결 방안
- 많은 카테고리화된 자료 저장 시 딕셔너리 자료형 (쓸모없는 데이터는 저장하지 않음)
- 자료를 여러 가지 기준에 따라 정렬 시 lambda 정렬
- 정렬된 자료 중, 조건에 맞는 결과 출력 시 반복문 / filter

3. defaultdict
- 새로운 Key 값이 들어올 때 값 초기화를 하지 않고 바로 연산 수행 가능
- 연산 수행할 때 일일이 Key 값이 딕셔너리에 존재하는지 체크하지 않아도 됨
- 배열을 이용할 경우 : 100,000 크기의 배열을 만들어야 하는데 이벤트 종류가 많지 않을 경우 효율적이지 않음

4. 정렬
- dict.items() 는 (key, value) 쌍을 반환
- 정렬 기본은 오름차순
- sorted(dic.items(), key=lambda x: (x[1], x[0]), reverse=True)
"""


def frequent_events_1(size, info):
    from collections import defaultdict

    N, M = map(int, size.split())
    cnt = defaultdict(int)

    for i in range(M):
        events = list(map(int, info[i].split()))
        for e in events[1:]:
            cnt[e] += 1

    res = sorted(cnt.items(), key=lambda x: (x[1], x[0]), reverse=True)
    res = list(filter(lambda x: x[1]==res[0][1], res))

    for i in res:
        print(i[0], end=' ')
    print()


def frequent_events_2(size, info):
    from collections import defaultdict

    N, M = map(int, size.split())
    cnt = defaultdict(int)

    for i in range(M):
        events = list(map(int, info[i].split()))
        for e in events[1:]:
            cnt[e] += 1

    # print(cnt.items())
    res = sorted(cnt.items(), key = lambda x:(x[1], x[0]), reverse=True)
    ans = list()
    ans.append(res[0][0])
    for i in range(1, len(res)):
        if res[i-1][1] != res[i][1]:
            break
        ans.append(res[i][0])

    print(*ans)


def frequent_events_3(size, info):
    # 이벤트 번호가 10, 1000, 100000 과 같이 주어지면 비효율적
    # import sys
    # input = sys.stdin.readline
    n, m = map(int, size.split())

    event_cnt = [0 for _ in range(100001)]

    for i in range(m):
        event = list(map(int, info[i].split()))
        for e in event[1:]:
            event_cnt[e] += 1
            
    event_max = max(event_cnt)
    popular = list()
    for i in range(100000, 0, -1):
        if event_cnt[i] == event_max:
            popular.append(i)

    for i in popular:
        print(i, end = ' ')
    print()


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [('4 4', ['4 1 2 3 4', '4 1 2 3 4', '4 1 2 3 4', '4 1 2 3 4']),
                  ('4 4', ['4 1 2 3 4', '4 1 2 3 4', '4 1 2 3 4', '4 1 2 3 3']),
                  ('5 4', ['5 10 2 3 1000 1000', '5 2 1000 1000 10 2', '5 10 3 10 1000 10', '5 1000 1000 2 2 2'])] # 4 3 2 1 / 3

    for case in test_cases:
        frequent_events_1(case[0], case[1])
        frequent_events_2(case[0], case[1])
        frequent_events_3(case[0], case[1])