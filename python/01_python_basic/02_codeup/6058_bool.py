# problem source : https://codeup.kr/problem.php?id=6058
# keyword : 논리연산
# return : 둘 다 거짓인 경우에만 참 출력

import sys

input = sys.stdin.readline

n1, n2 = map(int, input().split())

# not A and not B = not(A or B)
print(not (bool(n1) or bool(n2)))
print(not (bool(n1)) and not (bool(n2)))
