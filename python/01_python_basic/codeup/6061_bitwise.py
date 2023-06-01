# problem source : https://codeup.kr/problem.php?id=6061
# keyword : 비트단위(bitwise) 연산자
# return : 두 정수를 비트단위로 or 계산 수행 후 10진수 출력

# 비트단위 연산자
# not : ~ (tilde)
# and : & (ampersand)
# or  : | (vertical bar/pipe)
# xor : ^
# left shift : <<
# right shift : >>

"""
1. 두 비트열이 주어졌을 때 둘 중 하나라도 1인 자리를 1로 만들어줌
2. 비트단위 연산은 빠른 계산이 필요한 그래픽 처리에서 효과적

- 3       : 00000000 00000000 00000000 00000011
- 5       : 00000000 00000000 00000000 00000101
- 3 | 5   : 00000000 00000000 00000000 00000111

- 138     : 10001010
- 0       : 00000000
- 138 | 0 : 10001010
"""

import sys

input = sys.stdin.readline

num1, num2 = map(int, input().split())

# 0&0->0, 나머지->1 변환
pipe = num1 | num2

# 10진수로 출력
print(pipe)
