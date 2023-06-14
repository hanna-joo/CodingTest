# Stack
# keyword : 스택
# return : Underflow, Overflow 출력 포함 스택 구현

"""
1. 스택
- 후입선출(LIFO)
"""

def block_boom_1(cnt, block):

    '''
    1. 첫 글자는 char에 지정하고 인덱스는 same에 넣는다
    2. 다음 글자는 char과 비교한다
    3. 같으면 인덱스를 same에 넣는다
    4. 다르면 same의 크기를 폭파 조건과 비교한다
    5. 폭파 조건이 된다면 폭파하고 1번으로 돌아간다
    6. 폭파 조건이 안된다면 same을 비우고 char에 새로운 글자를 지정한다
    7. 글자의 모든 탐색(for문)이 완료되었는데도 폭파가 되지 않았다면 same을 한번 더 확인한다
    8. 더 이상 폭파가 발생되지 않거나 맨 마지막 글자들이 폭파된다면 종료된다
    '''

    boom = True
    while boom:
        same, char = [0], block[0]
        boom = False
        for i in range(1, len(block)):
            if block[i] == char:
                same.append(i)
            else:
                if len(same) >= cnt:
                    block = block[:same[0]] + block[same[-1]+1:]
                    boom = True
                    break
                else:
                    stack = [i]
                    char = block[i]
            
        if not boom:
            if len(same) >= cnt:
                block = block[:same[0]] + block[same[-1]+1:]
                
    if block:
        return block
    else:
        return 'CLEAR!'


def block_boom_2(cnt, block):
    
    return


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [(2, 'ABCCBCCDA'), (3, 'ABCCCBBAAA')] # ADA, CLEAR!
    test_cases.append(int(input()), input().rstrip())

    for case in test_cases:
        block_boom_1(case[0], case[1])
        block_boom_2(case[0], case[1])