# 대소문자 바꾸기
# return : 주어진 문자열의 대문자는 소문자로, 소문자는 대문자로 바꿔서 출력

"""
1. Python 입출력
(1) Python 기본 입출력 함수 input() 특징
- 입력 받은 문자열을 문자 단위로 읽음
- 개행 문자를 삭제함
- 문자를 문자열로 변환하여 반환함
(2) input()
- 입력 받은 문자열을 문자 단위로 하나씩 읽기 때문에 속도 느림
- 수십만 건의 입력을 받아야 하는 상황에 timeout 발생 가능성 높음
(3) sys.stdin.readline()
- 사용자 입력을 받는 버퍼를 만든 후 그 버퍼에서 입력을 다시 읽어들임
- 단, 개행 문자가 포함된 문자열로 저장되기 때문에 input().rstrip()과 같이 개행문자 바로 제거 필요

2. 대소문자 변경
- s.islower(), s.isupper() : 소문자 여부 확인, 대문자 여부 확인
- s.lower(), s.upper() : 소문자로 변경, 대문자로 변경
- s.swapcase() : 대소문자 변경
- Python String 메서드 : https://docs.python.org/3/library/string.html
"""


def upper_lower_1(s_len, s):
    answer = ''

    for c in s:
        if c.islower():
            answer += c.upper()
        else:
            answer += c.lower()
            
    return answer

def upper_lower_2(s_len, s):
    answer = s.swapcase()

    return answer

if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [(6, 'commit'), (10, 'goormLevel')]
    test_cases.append((int(input()), input().rstrip()))

    for case in test_cases:
        print(upper_lower_1(case[0], case[1]))
        print(upper_lower_2(case[0], case[1]))