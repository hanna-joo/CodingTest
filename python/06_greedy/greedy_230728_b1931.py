# 회의실 배정
# source : https://www.acmicpc.net/problem/1931
# keyword : 그리디
# return : 한 개의 회의실을 사용할 수 있는 회의의 최대 개수 출력


"""
1. 문제
- 가장 빨리 끝나는 회의를 찾는다

2. 입력
- 회의의 수 N개(1<=N<=100,000)
- 회의 시작 시간, 끝나는 시간

3. 로직 1
- 우선순위 큐 사용한다

4. 로직 2
- open(0) : 읽기 모드에서 표준 입력(stdin)을 연다
- open(0).read() : 전체 입력을 단일 문자열로 읽는다
- 표준 입력을 닫으려면 ctrl+D(macOS), ctrl+Z(windows)
- *l, : 확장된 반복
- 종료시간
    - l[2::2] : 인덱스 2부터 끝까지 2개씩 증가 = range(2, N, 2)
- 시작시간
    - l[1::2] : 인덱스 1부터 끝까지 2개씩 증가 = range(1, N, 2)
- 종료시간 기준 정렬
    - sorted(zip(l[2::2], l[1::2]))
- 변수 := 표현식
    - 표현식의 결과를 변수에 할당과 동시에 return
    - 선언과 동시에 바로 사용 가능
"""


def solution_1():
    import sys
    import heapq
    input = sys.stdin.readline

    N = int(input().rstrip())
    meetings = list()
    for _ in range(N):
        s, e = map(int, input().rstrip().split())
        heapq.heappush(meetings, (e, s))

    # 맨 처음 시작하는 회의 뽑기
    cur_e, cur_s = heapq.heappop(meetings)
    cnt = 1
    while meetings:
        # 가장 빨리 끝나는 회의 뽑기
        next_e, next_s = heapq.heappop(meetings)
        # 뽑은 회의 시작 시간이 현재 회의 이후인지 확인 
        if next_s >= cur_e:
            # 현재 회의를 뽑은 회의로 변경
            cur_e, cur_s = next_e, next_e
            cnt += 1
    print(cnt)


def solution_2():
    *l, =map(int,open(0).read().split())
    e = 0
    print(sum((e:=i) and 1 for i,j in sorted(zip(l[2::2],l[1::2]))if e<=j))


"""
테스트 케이스 : 4

11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
"""