# 단어 필터
# keyword : 시뮬레이션, map(), 문자열 메소드
# return : 주어진 문자열에서 특정 단어 제거

"""
1. map() 
- map(Function, iterable Data)

2. s.replace(a, b)
- s안에 있는 문자열 a를 모두 b로 변환
- 단, 1번만 시행하기 때문에 시행 이후 결과에 또 a가 존재할 수 있음

3. s.find(a), s.index(a)
- s안에서 a가 가장 처음으로 등장하는 인덱스 추출
- find()는 a가 없는 경우 -1 반환
- index()는 a가 없는 경우 ValueError 발생
"""


def word_filter_1(word, msg):
    while word in msg:
        msg = msg.replace(word, '')

    if msg == '':
        return 'EMPTY'
    else:
        return msg


def word_filter_2(word, msg):
    while word in msg:
        idx = msg.find(word)
        msg = msg[:idx] + msg[idx+len(word):]

    if msg == '':
        return 'EMPTY'
    else:
        return msg


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [['goorm', 'goormabgoorm'], ['wow', 'wwowowikii'], ['A', 'AAAAAA']]
    test_cases.append([input().rstrip(), input().rstrip()])

    for case in test_cases:
        print(word_filter_1(case[0], case[1]))
        print(word_filter_2(case[0], case[1]))