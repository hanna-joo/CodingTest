# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/43165

# return : numbers 안의 숫자 조합으로 target 값을 만드는 경우의 수

def dfs(numbers, target, depth, total):
    global answer
    if depth == len(numbers) and total == target:
        answer += 1
    elif depth < len(numbers):
        dfs(numbers, target, depth+1, total-numbers[depth])
        dfs(numbers, target, depth+1, total+numbers[depth])
    return answer
    
def solution(numbers, target):
    global answer
    answer = 0
    return dfs(numbers, target, 0, 0)

if __name__ == '__main__':
    test_cases = [([1, 1, 1, 1, 1], 3), ([4, 1, 2, 1], 4)] # 5, 2
    
    for numbers, target in test_cases:
        print(solution(numbers, target))