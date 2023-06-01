# problem source : https://codeup.kr/problem.php?id=6063
# keyword : 3항 연산
# return : 두 정수 중 큰 값을 10진수로 출력

# 비트단위 연산자
# not : ~ (tilde)
# and : & (ampersand)
# or  : | (vertical bar/pipe)
# xor : ^ (circumflex/caret)
# left shift : <<
# right shift : >>

"""
1. 3항 연산 : 3개의 요소로 이루어지는 연산
2. x if C else y
- C : True 혹은 False 여부를 평가할 조건식 또는 값
- x : C의 평가 결과가 True일 때 사용할 값
- y : C의 평가 결과가 False일 때 사용할 값
3. 복잡한 계산식이나 조건 처리, 비교 구조를 간단히 표현 가능
4. 이항 연산과 비교해서 성능 차이는 미비하고 자주 사용되진 않음
"""

import sys

input = sys.stdin.readline

num1, num2 = map(int, input().split())

# 두 수 중 더 큰 값 선별
bigger = num1 if num1 >= num2 else num2

print(bigger)
