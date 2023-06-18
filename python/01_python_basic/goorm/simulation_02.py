# 규칙 숫자 야구
# keyword : 시뮬레이션
# return : 두 명의 점수 합이 0인 경우 커플 매칭 성공, 커플 매칭이 안 된 사람들의 점수 합 출력

"""
1. 시뮬레이션
- 특정 알고리즘 구현이 아니라 문제의 요구 사항에 맞게 코드 작성하는 유ㅇ

2. 구현 방안
- 입력과 정답 비교하여 Strike, Fail, Ball 판단
- Fail 처리
- Ball 처리
"""

def baseball_1(answer, player):
    answer = list(map(int, answer))
    player = list(map(int, player))

    return answer


def baseball_2(answer, player):
    answer = list(map(int, answer))
    player = list(map(int, player))
    # 사용자 입력 만든 횟수
    make_input_cnt = 0
    # 각 자리의 상태 관리 (Strike:0, Ball:1, Fail:2)
    result = [2] * len(player)
    for i in range(len(player)):
        if player[i] in answer:
            if player[i] == answer[i]:
                result[i] = 0
            else:
                result[i] = 1

    return answer


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [['1234', '0123'], ['1234', '1234']] # 4, 1
    test_cases.append(list(input(), input()))

    for case in test_cases:
        print(baseball_1(case[0], case[1]))
        print(baseball_2(case[0], case[1]))