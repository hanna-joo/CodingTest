# source : https://school.programmers.co.kr/learn/courses/15008/lessons/121683
# keyword : 해시
# return : 외톨이 알파벳들을 알파벳 순으로 이어 붙인 문자열 출력(없으면 'N')

"""
1. 문제
- 외톨이 알파벳
    - 문자열에서 2회 이상 나타났을 때
    - 2개 이상의 부분으로 나뉘어 있을 때

2. 입력 및 제한
- 1 <= input string 길이 <= 2,600

3. 로직
- 한 글자씩 외톨이 알파벳 찾기
    - 딕셔너리 : key=알파벳, value=(알파벳 수, 토큰 수)
    - 탐색할 때마다 개수+1
    - 현재값이 이전값과 다르면 이전값의 토큰+1
        - 방법1 : prev 변수 변경하는 방법
        - 방법2 : stack에 추가하고 stack[-1] 참조하는 방법
- 토큰 개수가 2개 이상인 알파벳 찾아서 붙이기
"""


from collections import defaultdict

def solution(input_string):
    info = defaultdict(int)
    prev = input_string[0]
    for cur in input_string+'-':
        if prev != cur:
            info[prev] += 1
        prev = cur
    answer = [k for k, v in info.items() if v >= 2]

    return ''.join(sorted(answer)) if answer else "N"


def check(func, inputs, outputs):
    print(f"Check {func.__name__}")
    result = func(inputs)
    print(result, True if result == outputs else False)
        

if __name__ == '__main__':
    test_cases = [("edeaaabbccd", "de"), ("eeddee", "e"),
                  ("string", "N"), ("zbzbz", "bz")]
    for i, o in test_cases:
        check(solution, i, o)