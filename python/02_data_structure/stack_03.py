# 괄호 검사 1 : 효율성 10.72ms
def solution1(s):
    answer = True
    match_dict = {')':'('}
    match_stack = [s[0]]
    for char in s[1:]:
        if char == ')':
            if match_stack and match_stack[-1] == match_dict.get(char):            
                match_stack.pop()
            else:
                answer = False
                break
        elif char == '(':
            match_stack.append(char)
    if match_stack:  
        answer = False
    return answer

# 괄호 검사 2 : 효율성 10.97ms
def solution2(s):
    match_stack = []
    match_dict = {']':'[', '}':'{', ')':'('}
    answer = True
    for char in s:
        if char in ('[', '{', '('):
            match_stack.append(char)
        elif char in (']', '}', ')'):
            if match_stack and match_stack[-1] == match_dict.get(char):
                match_stack.pop()
            else:
                answer=False
                break
    if match_stack:
        answer = False
    return answer

# 괄호 검사 3 : 효율성 8.10ms
def solution3(s):
    is_pair = 0
    for char in s:
        if is_pair < 0: 
            break
        if char == "(":
            is_pair += 1
        else:
            if char == ")":
                is_pair -= 1
    return is_pair == 0

if __name__ == '__main__':
    test_cases = ["(())()", ")()(", "(()(", "((d))", "((()()(s)))"] # t f f t t
    for case in test_cases:
        print(solution1(case))
        print(solution2(case))
        print(solution3(case))
        print()