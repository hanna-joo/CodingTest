# 뿌요뿌요
# keyword : 스택, 예외처리 디테일 잡기
# return : 폭파 최소 조건과 문자열이 주어졌을 때 뿌요가 모두 터지고 난 후의 문자열 출력

"""
1. 폭파 최소 조건과 같을 때 무조건 터트리는 것이 아님
- 다른 문자열이 발견 되었을 때 폭파 여부 결정

2. 마지막 글자까지 탐색하거나 IndexError를 방지
- 겹치지 않는 더미 문자를 앞이나 뒤에 추가해서 간결화
- 마지막에 더미 문자 반드시 제거
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
    # 더미 변수 추가 (마지막 점검을 안해도 됨)
    block += 'z'

    boom = True
    while boom:
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
	# 더미 변수 제거			
    block = block[:-1]
    if block:
        return block
    else:
        return 'CLEAR!'

def block_boom_3(cnt, block):
    # 스택이 비었을 때 참조하게 되면 IndexError 발생하니 더미 문자 추가
    stack = list()
    stack.append(('', 0))
    
    # 마지막 뿌요가 터져야 할 수도 있으니 block 맨 뒤에 더미 문자 추가
    block += 'z'
    for char in block:
        if (stack[-1][0] != char) and (stack[-1][1] >= cnt):
                top = stack[-1][0]
                while top == stack[-1][0]:
                    stack.pop()
        if stack[-1][0] == char:
            stack.append((char, stack[-1][1] + 1))
        else:
            stack.append((char, 1))
    # block에 추가한 더미 문자 제거
    stack.pop()

    if len(stack) > 1:
        block = ''
        for char, num in stack:
            block += char
        return block
    else:
        return 'CLEAR!'


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [(2, 'ABCCBCCDA'), (3, 'ABCCCBBAAA')] # ADA, CLEAR!
    test_cases.append((int(input()), input().rstrip()))

    for case in test_cases:
        print(block_boom_1(case[0], case[1]))
        print(block_boom_2(case[0], case[1]))