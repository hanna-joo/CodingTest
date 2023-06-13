# Stack
# keyword : 스택
# return : Underflow, Overflow 출력 포함 스택 구현

"""
1. 스택
- 후입선출(LIFO)
"""

def block_boom_1(cnt, block):

    '''
    1. 첫 글자는 stack에 넣는다
    2. 다음 글자는 stack 마지막 문자와 비교한다
    3. 같으면 stack에 넣는다
    4. 다르면 stack의 크기를 폭파 조건과 비교한다
    5. 폭파 조건이 된다면 폭파하고 1번으로 돌아간다
    6. 폭파 조건이 안된다면 stack을 비우고 글자를 넣는다
    7. stack에 넣을 글자가 없다면 종료한다
    '''

    boom = True
    while boom and block:
        stack, char = [0], block[0]
        boom = False
        for i in range(1, len(block)):
            if block[i] == char:
                stack.append(i)
            else:
                if len(stack) >= cnt:
                    block = block[:stack[0]] + block[stack[-1]+1:]
                    boom = True
                    break
                else:
                    stack = [i]
                    char = block[i]
            
        if not boom:
            if len(stack) >= m:
                block = block[:stack[0]] + block[stack[-1]+1:]
                boom = True
            else:
                break
                
    if block:
        return block
    else:
        return 'CLEAR!'


def block_boom_2(cnt, block):
    
    return


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [(2, 'ABCCBCCDA'), (3, 'ABCCCBBAAA')]
    test_cases.append(int(input()), input().rstrip())

    for case in test_cases:
        block_boom_1(case[0], case[1])
        block_boom_2(case[0], case[1])