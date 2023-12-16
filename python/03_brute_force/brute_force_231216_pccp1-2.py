# source : https://school.programmers.co.kr/learn/courses/15008/lessons/121684
# keyword : 완전 탐색
# return : 선발된 대표들의 해당 종목에 대한 능력치의 합 최대값

"""
1. 문제
- 체육 대회 한 종목당 1명의 대표 출전
- 선발된 대표들의 해당 종목에 대한 능력치의 합 최대값

2. 입력 및 제한
- 1 <= ability 행의 길이 = 학생 수 <= 10
- 1 <= ability 열의 길이 = 종목 수 <= ability 행의 길이
- 0 <= ability[i][j] = i+1번 학생의 j+1번 종목 능력치 <= 10,000

3. 로직
- 종목 개수 만큼 학생 뽑기
    - 순서를 고려하여 출전할 학생들 조합 = permutations(학생목록, 종목수)
- ex. 종목 3개에 출전하는 선수들 (a,b,c)
    - 1번 종목에 a학생, 2번 종목에 b학생, 3번 종목에 c학생
"""


from itertools import permutations

def solution(ability):
    answer = 0
    for players in permutations(range(len(ability)), len(ability[0])):
        tmp = sum(ability[i][j] for j, i in enumerate(players))
        if tmp > answer:
            answer = tmp
    return answer


def check(func, inputs, outputs):
    print(f"Check {func.__name__}", end= ' : ')
    result = func(inputs)
    print(result, "->", "Right" if result == outputs else "Wrong")
        

if __name__ == '__main__':
    test_cases = [([[40, 10, 10], 
                    [20, 5, 0], 
                    [30, 30, 30], 
                    [70, 0, 70], 
                    [100, 100, 100]], 210),
                  ([[20, 30], 
                    [30, 20], 
                    [20, 30]], 60)]
    for i, o in test_cases:
        check(solution, i, o)