# PCCP 모의고서 #1 - 3. 유전 법칙
# source : https://school.programmers.co.kr/learn/courses/15008/lessons/121685
# keyword : 완전 탐색
# return : n세대의 p번째 완두콩 형질 출력

"""
1. 문제
- 완두콩 교배
    - RR + RR = RR4
    - rr + rr = rr4
    - Rr + Rr = RR1 Rr2 rr1
- 완두콩 n세대, p번째 개체 => 형질 출력

2. 입력 및 제한
- 1 <= queries 길이 <= 5
- queries 원소 [n, p]
    - 1 <= n <= 16
    - 1 <= p <= 4^n-1

3. 로직1 : 테스트케이스 2개 틀림
- 맨 처음과 맨 마지막 4^(n-1)개는 RR / rr이므로 자르기
- Rr = 중간 묶음 2, 3, 6, 7, ... 에서 두번째, 세번째 요소
"""


import math

def solution(queries):
    answer = []
    for n, p in queries:
        if n < 2:
            answer.append("Rr")
            continue
        if p <= 4 ** (n-2):
            answer.append("RR")
        elif p > 4 ** (n-1) - 4 ** (n-2):
            answer.append("rr")
        else:
            chunk = math.ceil(p/4) % 4 if p > 4 else p
            if chunk == 1:
                answer.append("RR")
            elif chunk == 0:
                answer.append("rr")
            else:
                answer.append("RR" if p%4 == 1 else "rr" if p%4 == 0 else "Rr")
    return answer


def check(func, inputs, outputs):
    print(f"Check {func.__name__}", end= ' : ')
    result = func(inputs)
    print(result, "->", "Right" if result == outputs else "Wrong")
        

if __name__ == '__main__':
    test_cases = [([[3, 5]], ["RR"]),
                  ([[3, 8], [2, 2]], ["rr", "Rr"]),
                  ([[3, 1], [2, 3], [3, 9]], ["RR", "Rr", "RR"]),
                  ([[4, 26]], ["Rr"])]
    for i, o in test_cases:
        check(solution, i, o)