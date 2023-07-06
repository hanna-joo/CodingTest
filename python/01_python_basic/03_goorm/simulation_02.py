# 규칙 숫자 야구
# keyword : 시뮬레이션
# return : 4자리 규칙 숫자 야구 게임에서 승리하기 위해 몇 번의 과정을 거쳐야 하는지 출력

"""
1. 시뮬레이션
- 특정 알고리즘 구현이 아니라 문제의 요구 사항에 맞게 코드 작성하는 유ㅇ

2. 구현 방안
- 입력과 정답 비교하여 Strike, Fail, Ball 판단
- Fail 값들 모두 처리 : 각각 유일값이 될 때까지 1씩 증가
- Ball 값이 있으면 처리 : Strike 값 제외하고 오른쪽으로 한 칸씩 이동
"""

def baseball_1(answer, player):
    answer = list(map(int, answer))
    player = list(map(int, player))
    n = len(player)

    # fail : 다른 자리에 없는 새로운 값 생성
    def fail():
        for i in range(n):
            if state[i] != 2:
                continue
            tmp = player[i]
            while tmp in player:
                tmp = (tmp + 1) % 10
            player[i] = tmp
        return
                
    # ball : ball 인 자리가 있다면 오른쪽으로 1칸씩 이동
    def ball():
        if 1 not in state:
            return
        pos, val = list(), list()
        for i in range(n):
            if state[i] != 0:
                pos.append(i)
                val.append(player[i])
        for i in range(len(pos)):
            if i == 0:
                player[pos[i]] = val[-1]
            else:
                player[pos[i]] = val[i-1]

    repeat = 0
    while True:
        repeat += 1
        state = [2] * n
        if player == answer:
            break
        for i in range(n):
            if player[i] == answer[i]:
                state[i] = 0
            elif player[i] in answer:
                state[i] = 1  
        fail()
        ball()
                
    return repeat


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [['1234', '0123'], ['1234', '1234']] # 4, 1
    test_cases.append([input().rstrip(), input().rstrip()])

    for case in test_cases:
        print(baseball_1(case[0], case[1]))