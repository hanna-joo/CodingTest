# Stack
# keyword : 스택
# return : Underflow, Overflow 출력 포함 스택 구현

"""
1. 스택
- 후입선출(LIFO)
"""

def stack_1(cnt, size):
    stack = list()
    for _ in range(cnt):
        command = input().split()
        if command[0] == 'push':
            if len(stack) < size:
                stack.append(command[1])
            else:
                print("Overflow")
        elif command[0] == 'pop':
            if stack:
                print(stack.pop())
            else:
                print("Underflow")

    return


def stack_2(cnt, size):
    from collections import deque
    
    stack = deque()
    for _ in range(cnt):
        op = input().rstrip().split()
        if op[0] == 'push':
            if len(stack) < size:
                stack.append(int(op[1]))
            else:
                print("Overflow")
        else:
            if stack:
                print(stack.pop())
            else:
                print("Underflow")
    
    return


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [(10, 3), (5, 3)]

    for case in test_cases:
        stack_1(case[0], case[1])
        stack_2(case[0], case[1])