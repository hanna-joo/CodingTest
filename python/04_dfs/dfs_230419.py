# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/43162

# 컴퓨터가 직접적, 간접적으로 연결되어 있다면 같은 네트워크 상
# 컴퓨터 개수 : n개 (0 ~ n-1)
# return : 네트워크 개수

def dfs(computers, visited, node):
    global connections
    visited[node] = True
    for i in range(len(computers)):
        # 방문X, 연결O 노드일 경우 연결 개수 +1
        if not visited[i] and computers[node][i]:
            connections += 1
            dfs(computers, visited, i)
    return visited

def solution(n, computers):
    global connections
    connections = 0
    visited = [False] * n
    # 모든 노드 방문할 때까지 연결 수 탐색
        # 노드가 2개씩 연결되어 있는 경우(a-b-c d-e f-g)
    while True:
        if False in visited:
            node = visited.index(False)
            visited = dfs(computers, visited, node)
        else:
            break
    # 네트워크 수 = 서버 수 - 연결 수
    answer = n - connections
    return answer

if __name__ == '__main__':
    test_cases = [(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]), (3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])] # 2, 1
    
    for n, computers in test_cases:
        print(solution(n, computers))