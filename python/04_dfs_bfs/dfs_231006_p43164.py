# problem : https://school.programmers.co.kr/learn/courses/30/lessons/43164
# keyword : dfs/bfs
# return : 방문하는 공항 경로 (2개 이상이면 알파벳 순서 앞서는 경로)
# 이전 풀이 : dfs_230719_p43164

"""
1. 문제
- 주어진 항공권 모두 사용하는 방법
- 경로가 2개이면 알파벳 순으로 첫번째 경로 출력
- 주어진 입력은 무조건 모든 도시를 방문 가능
- 시작 공항은 무조건 ICN, 중복 항공권 있음

2. 로직
- Graph는 딕셔너리로 구현(일방향)
- DFS로 경로 저장
    - 종료 조건 : 항공 티켓 모두 사용했을 때 종료
    - 경로 저장 : 종료 직전에 경로길이=티켓수+1면 경로 저장
    - 티켓 사용 : 티켓 사용했으면 ''으로 변경
"""

from collections import defaultdict

def dfs(cur, path, count):
    if len(path) == count+1:
        answer.append(path)
        return
    for nxt in graph[cur]:
        graph[cur].remove(nxt)
        dfs(nxt, path+[nxt], count)
        graph[cur].append(nxt)

def solution(tickets):
    global graph, answer
    answer = []
    count = len(tickets)
    graph = defaultdict(list)
    for u, v in tickets:
        graph[u].append(v)
    dfs("ICN", ["ICN"], count)
    answer.sort()
    print(graph)
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
