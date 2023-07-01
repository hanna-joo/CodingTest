# 순환하는 수로
# keyword : BFS/DFS, 정점과 간선의 수가 같은 특수 그래프
# return : 순환 수로에 포함된 물탱크 수 출력, 순환 수로를 구성하는 물탱크 번호 오름차순 출력
"""
1. 문제 분석
- N개의 물탱크와 N개의 수로(양방향)
- 모든 물탱크는 수로로 연결됨
- 수로는 서로 다른 물탱크 연결, 한 물탱크 쌍 연결 수로는 최대 1개
- 사이클에 포함되는 물탱크 번호 오름차순 출력
- 수로 수 : 1 <= N <= 1000
- 물탱크 번호 : 1 <= ui, vi <= N / ui != vi

2. 정확히 하나의 사이클을 가지는 그래프
- 조건 1. 정점과 간선의 개수가 같은 그래프
- 조건 2. 자기 자신을 잇는 간선이 존재하지 않음
- 조건 3. 모든 노드가 연결되어 있다
- N개의 정점과 N-1개의 간선을 가진 트리에 간선 추가한 것과 동일

3. 해결 방안
- 어떤 정점에서 DFS를 시작하던 간에 사이클이 포함되는 경로를 만나게 된다
- 이미 방문한 정점에 도달할 수 있다
- 현재 방문한 정점들을 스택에 저장 후, 사이클의 시작점이 나올 때까지 원소 빼줌
- DFS 1번 수행으로 O(N + M)
"""


def circulate_road(cnt, info):
    #import sys
    #input = sys.stdin.readline

    N = int(cnt)
    G = [[] for _ in range(N + 1)]
    V = [0 for _ in range(N + 1)]
    for i in range(N):
        u, v = map(int, info[i].split())
        G[u].append(v)
        G[v].append(u)

    # 현재 방문한 정점을 기록하는 스택입니다.
    ST = []
    # 사이클의 시작점을 의미하는 변수입니다.
    global start
    start = -1

    def DFS(cur, prev):
        global start
        ST.append(cur)
        for next in G[cur]:
            if start != -1:
                return
            # 바로 직전 정점과는 사이클을 이룰 수 없으므로, 예외처리를 해줘야 합니다.
            if next == prev:
                continue
            # 다음 정점이 이미 방문한 정점인 경우, 해당 정점을 사이클의 시작점으로 설정하고 DFS를 탈출합니다.
            if V[next]:
                start = next
                return
            V[next] = 1
            DFS(next, cur)
        # 사이클의 시작 정점을 찾은 경우, 방문한 정점 목록을 보존해야 하므로 DFS를 더 수행하면 안 됩니다.
        if start != -1:
            return
        # 해당 노드에서 더 갈 곳이 없는 경우!!!!! (여기서는 그런 경우가 없음)
        #print(ST[-1])
        ST.pop()

    V[4] = 1
    DFS(4, 0)

    # 현재 스택에는 사이클을 이루는 경로가 역순으로 저장되어 있습니다.
    # 사이클의 시작 정점이 보일 때까지 스택에서 원소들을 뽑아줍니다.
    ans = []
    while 1:
        ans.append(ST[-1])
        ST.pop()
        if ans[-1] == start:
            break
        
    ans.sort()
    print(len(ans))
    print(*ans)


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [('6', ['4 1', '2 1', '6 2', '3 6', '4 5', '3 2']),
                  ('6', ['2 5', '4 6', '3 5', '3 1', '2 3', '5 6'])] # 2 3 6 / 2 3 5

    for case in test_cases:
        circulate_road(case[0], case[1])
