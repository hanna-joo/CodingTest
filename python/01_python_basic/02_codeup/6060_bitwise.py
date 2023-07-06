# problem source : https://codeup.kr/problem.php?id=6059
# keyword : 비트단위(bitwise) 연산자
# return : 두 정수를 비트단위로 and 계산 수행 후 10진수 출력

# 비트단위 연산자
# not : ~ (tilde)
# and : & (ampersand)
# or  : |
# xor : ^
# left shift : <<
# right shift : >>

"""
1. 두 비트열이 주어졌을 때 둘 다 1인 부분의 자리만 1로 만들어줌
2. 특정 부분만 모두 0으로 만들 수 있음
3. 네트워크에 연결되어 있는 두 개의 컴퓨터가 데이터 주고 받기 위해
   같은 네트워크에 있는지 아닌지 판단 시 사용
4. 비트단위 연산은 빠른 계산이 필요한 그래픽 처리에서 
   마스크 연산(특정 부분을 가리고 출력) 수행에 효과적

- 3       : 00000000 00000000 00000000 00000011
- 5       : 00000000 00000000 00000000 00000101
- 3 & 5   : 00000000 00000000 00000000 00000001

- 138     : 10001010
- 0       : 00000000
- 138 & 0 : 00000000
"""

import sys

input = sys.stdin.readline

num1, num2 = map(int, input().split())

# 1&1->1, 나머지->0 변환
ampersand = num1 & num2

# 10진수로 출력
print(ampersand)
