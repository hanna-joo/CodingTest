# 괄호짝 검사
def solution(S):
    stack = []
    matching = {']':'[', '}':'{', ')':'('}
    answer = 'TRUE'
    for s in S:
        if s in ('[', '{', '('):
            stack.append(s)
        elif s in (']', '}', ')'):
            if stack and stack[-1] == matching.get(s):
                stack.pop()
            else:
                answer='FALSE'
                break
    if stack:
        answer = 'FALSE'
    return answer
