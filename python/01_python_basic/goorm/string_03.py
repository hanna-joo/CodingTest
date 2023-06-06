# 큰 수식 찾기
# return : 주어진 두 식의 결과 중 큰 값 출력

"""
1. eval()
- 주어진 문자열을 연산자 우선순위에 따라 계산
"""

def max_value(expressions):
    maximum = max(map(eval, input().split()))

    return maximum

if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = ['10+5 10+6', '10*3-10 10*4-50', '10*10-99 99-10*10']
    test_cases.append(input().rstrip())

    for case in test_cases:
        print(max_value(case))