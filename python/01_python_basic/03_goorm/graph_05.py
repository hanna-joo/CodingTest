# 알파벳 트리 장난감
# keyword : 포화 이진 트리, DFS
# return : 공을 굴렸을 때 나올 수 있는 점수의 최솟값과 최댓값 출력

"""
1. 문제 분석
- 포화 이진 트리 형태의 알파벳 트리 장난감
- 각 노드에 알파벳이 있고, 루트 노드의 윗부분에 구멍이 있음
- 공을 넣으면 왼쪽 또는 오른쪽 자식 노드로 리프 노드에 도달할 때까지 굴러감
- 루트 노드 높이 = 1, 리프 노드 높이 = N
- 경로 점수 = 공이 지나간 경로에 포함된 알파벳들의 점수 합
- A는 1점, B는 2점, ... , Z는 26점

2. 트리
- N개의 정점과 N-1개의 양방향 간선으로 이루어져 있으며, 사이클이 존재하지 않는 그래프
- 임의의 두 정점을 연결하는 단순 경로가 유일한 그래프
- 임의의 간선을 제거하면 그래프가 여러 연결 컴포넌트로 나눠지는 그래프
- 트리의 경우, 탐색 가능한 경로의 수가 많지 않음
- 루트 정점과 리프 정점을 잇는 경로가 유일함

3. 포화 이진 트리
- 이진 트리 : 각 정점이 최대 2개의 자식을 가짐
- 리프 정점을 제외한 모든 정점이 2개의 자식을 가짐
- 모든 리프 정점의 높이가 동일함

4. DFS
- 방문할 수 있는 정점의 후보 관리 시 큐 대신 스택 사용
- 트리에서 탐색할 때, 백트래킹 구현할 때 사용
- BFS보다 구현이 편하고, 재귀적인 성질을 통해 쉽게 해결 가능
"""


def alphabet_tree_1(height, info):
    # 동적 프로그래밍 : 경로 누적 값 저장
    #import sys
    #input = sys.stdin.readline

    height = int(height)
    tree = []

    for i in range(height):
        tree.append(info[i].rstrip())

    # 각 노드까지의 경로 점수를 매긴 누적 트리
    tree_cum = [[] for _ in range(height)]
    for i in range(height):
        # i행 j열 노드의 부모 노드는 i-1행, j//2열
        for j in range(0, len(tree[i]), 2):
            # 루트 노드 값
            if i == 0:
                tree_cum[i].append(ord(tree[i][j]) - 64)
                continue
            # 현재 노드의 누적 값 = 부모 노드의 누적 값 + 현재 노드의 트리 값
            left = tree_cum[i-1][j//2] + ord(tree[i][j]) - 64
            right = tree_cum[i-1][j//2] + ord(tree[i][j+1]) - 64
            tree_cum[i].extend([left, right])
            #print(ord('A')-64)
            #print(ord('Z')-64)

    leaf = tree_cum[-1]

    return min(leaf), max(leaf)


def alphabet_tree_2(height, info):
    # DFS(h, n, score) : 현재 높이 h의 n번째 정점까지의 경로 점수 score
    height = int(height)
    tree = [[] for _ in range(height+1)]
    for i in range(1, height+1):
        tree[i] = info[i-1].rstrip()

    global ans1, ans2
    ans1, ans2 = 9**9, 0

    def dfs(h, n, score):
        # 현재 정점까지의 경로 점수
        score += ord(tree[h][n]) - ord('A') + 1
        # 리프 정점이 아닌 경우 : 탐색 계속 진행
        if h < height:
            dfs(h + 1, n * 2, score)
            dfs(h + 1, n * 2 + 1, score)
        # 리프 정점인 경우 : 답 갱신
        else:
            global ans1, ans2
            ans1 = min(ans1, score)
            ans2 = max(ans2, score)

    dfs(1, 0, 0)

    return ans1, ans2


def alphabet_tree_3(height, info):
    height = int(height)
    tree = [[] for _ in range(height+1)]
    for i in range(1, height+1):
        tree[i] = info[i-1].rstrip()

    global ans1, ans2
    ans1, ans2 = 9**9, 0

    def dfs(h, n, score):
        # 비효율적 재귀 함수
        score += ord(tree[h][n]) - ord('A') + 1
        if h < height:
            global ans1, ans2
            tmp1 = dfs(h + 1, n * 2, score)
            tmp2 = dfs(h + 1, n * 2 + 1, score)
            ans1, ans2 = min(ans1, tmp1, tmp2), max(ans2, tmp1, tmp2)
            return tmp2 # 리프 노드 점수
        else:
            return score
        
    dfs(1, 0, 0)

    return ans1, ans2

if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [('3', ['A', 'BC', 'DEFG']),
                  ('4', ['K', 'WL', 'TZAL', 'YYWBNRJT'])] # 7 11 / 38 83

    for case in test_cases:
        print(alphabet_tree_1(case[0], case[1]))
        print(alphabet_tree_2(case[0], case[1]))
        print(alphabet_tree_3(case[0], case[1]))
