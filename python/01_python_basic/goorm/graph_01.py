# 구름이의 여행
# keyword : 그래프 탐색
# return : 구름이가 1번 섬에서 N번 섬까지 K개 이하의 다리를 사용해서 갈 수 있는지 여부 출력

"""
1. 문제 분석
- 뭉친 그룹 : 상하좌우 인접해있으면서 같은 값을 가지는 칸들의 집합
- 배열 크기 1 <= N <= 500
- 

"""


def travel_within_k(info, connections):
    from collections import defaultdict
    from collections import deque

    N, M, K = map(int, info.split())
    # 자료형 명시 필요
    graph = defaultdict(list)

    for conn in connections:
        start, end = map(int, conn.split())
        graph[start].append(end)
        graph[end].append(start)

    # 탐색 후보
    Q = deque()
    Q.append(1)

    # Visited[i] : 1번 노드에서 i번 노드까지의 최소 간선 개수
    Visited = [10e9 for _ in range(N+1)]
    Visited[1] = 0

    while Q:
        cur_Node = Q.popleft()
        for next_Node in graph[cur_Node]:
            if Visited[next_Node] <= Visited[cur_Node] + 1:
                continue
            Visited[next_Node] = Visited[cur_Node] + 1
            Q.append(next_Node)
            
    if Visited[N] <= K:
        return 'YES'
    else:
        return 'NO'


def fibonacci_2(num):

    return


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [('6, 6, 2', ['1 4', '4 2', '2 6', '4 3', '1 2', '3 1']),
                  ('6, 6, 2', ['1 2', '2 3', '3 4', '3 5', '5 6', '5 2']),
                  ('3 1 1', ['1 2'])] # YES, NO, NO

    for case in test_cases:
        print(travel_within_k(case[0], case[1]))