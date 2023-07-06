# problem source : https://codeup.kr/problem.php?id=6062
# keyword : 비트단위(bitwise) 연산자
# return : 두 정수를 비트단위로 xor 계산 수행 후 10진수 출력

# 비트단위 연산자
# not : ~ (tilde)
# and : & (ampersand)
# or  : | (vertical bar/pipe)
# xor : ^ (circumflex/caret)
# left shift : <<
# right shift : >>

"""
1. 두 비트열이 주어졌을 때 서로 값이 다를 때 1로 만들어줌
2. 전혀 다른 배타적 논리합이라고 함
3. 서로 다른 부분만 처리
4. 비트단위 연산은 빠른 계산이 필요한 그래픽 처리에서 효과적

- 3       : 00000000 00000000 00000000 00000011
- 5       : 00000000 00000000 00000000 00000101
- 3 ^ 5   : 00000000 00000000 00000000 00000110

- 138     : 10001010
- 0       : 00000000
- 138 ^ 0 : 10001010
"""

import sys

input = sys.stdin.readline

num1, num2 = map(int, input().split())

# 1&0->1, 나머지->0 변환
caret = num1 ^ num2

# 10진수로 출력
print(caret)
