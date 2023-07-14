# 단어 변환
# keyword : DFS
# return : 한 번에 한 글자만 변환 가능, words의 단어 중 하나여야 함, 최소 몇 단계의 과정을 거쳐야 하는지 출력

"""
1. 변환이 불가능한 경우
- (1) words에 target이 없는 경우
- (2) words에 target까지 가는 경로가 없는 경우

2. 변환이 가능한 경우
- 단어 길이는 모두 같음 -> 인덱스 활용
- 한 글자씩만 변환 가능 -> 차이가 1개만 나는 단어
- (1) target 에서 시작
- (2) 차이가 1개만 나는 단어 찾기 (words 인덱스)
    - (21) 이미 방문한 단어 패스
    - (22) 현재 단어와 나머지 단어 간 차이 비교
- (3) 있으면 해당 단어 이동
    - (31) depth += 1, visited[i] = 1
    - (32) if 이동한 단어 == begin -> 종료
- (4) (2)~(3) 반복
"""


def solution(begin, target, words):    
    def dfs(cur, depth, visited):
        # 가능 (31)
        visited[cur] = True
        # 가능 (32)
        if words[cur] == begin:
            global answer
            answer = min(answer, depth)
            return
        # 가능 (2) : 차이가 1개만 나는 단어 찾기
        for i in range(len(words)):
            # 가능 (21) : 이미 방문한 단어 패스
            if visited[i]:
                continue
            # 가능 (22) : 현재 단어와 나머지 단어 간 차이 비교
            diff = 0
            for j in range(len(words[0])):
                if words[i][j] != words[cur][j]:
                    diff += 1
            # 가능 (3) : 있으면 해당 단어 이동
            if diff == 1:
                dfs(i, depth+1, visited)
    
    # 불가 (1)
    if target not in words:
        return 0
    
    global answer
    answer = 99999
    words.append(begin)
    visited = [False for _ in range(len(words))]
    
    # 가능 (1) : target 에서 시작
    dfs(words.index(target), 0, visited)
    
    # 불가 (2)
    if answer == 99999:
        return 0
    
    return answer


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [('6 5', ['1 1 1 1 1',
                           '1 1 1 1 1',
                           '1 1 0 1 1',
                           '1 1 0 1 1',
                           '1 1 1 1 1',
                           '1 1 0 1 1']),
                  ('5 5', ['0 0 1 0 0',
                           '0 1 1 1 0',
                           '1 1 1 1 1',
                           '0 1 1 1 0',
                           '0 0 1 0 0'])] # 2, -1

    for case in test_cases:
        print(solution(case[0], case[1]))
