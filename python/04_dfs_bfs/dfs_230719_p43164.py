# problem : https://school.programmers.co.kr/learn/courses/30/lessons/43164
# keyword : dfs/bfs
# return : 방문하는 공항 경로 (2개 이상이면 알파벳 순서 앞서는 경로)

"""
1. 시작은 ICN, 중복 항공권 있음
2. Graph는 딕셔너리로 구현(일방향)
3. 항공권 사용 여부는 노드 0으로 변경
4. 경로 길이가 항공권 개수+1 인 경우 경로 반환
"""

from collections import defaultdict

def dfs(cur, path):
    if len(path) == count+1:
        answer.append(path)
        return
    for i, nxt in enumerate(graph[cur]):
        if graph[cur][i] == '':
            continue
        graph[cur][i] = ''
        dfs(nxt, path+[nxt])
        graph[cur][i] = nxt

def solution(tickets):
    global graph, answer, count
    answer = []
    count = len(tickets)
    graph = defaultdict(list)
    for u, v in tickets:
        graph[u].append(v)
    for k in graph.keys():
        graph[k].sort()
    dfs("ICN", ["ICN"])
    answer.sort()
    return answer[0]


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]],
                  [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]],
                  [["ICN", "AAA"], ["ICN", "CCC"], ["CCC", "DDD"], ["AAA", "BBB"], ["AAA", "BBB"], ["DDD", "ICN"], ["BBB", "AAA"]]]
                # ["ICN", "JFK", "HND", "IAD"]
                # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
                # ["ICN", "CCC", "DDD", "ICN", "AAA", "BBB", "AAA", "BBB"]
    for case in test_cases:
        print(solution(case))
