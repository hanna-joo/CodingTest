# problem source : https://codeup.kr/problem.php?id=6064
# keyword : 연산자 우선순위
# return : 입력 받은 3개의 수 중 가장 작은 수 출력

"""
Java의 연산자
1. 단항 연산자
- 피연산자가 단 하나뿐인 연산자
- 부호 연산자 : +, -
- 증감 연산자 : ++, --
- 논리 부정 연산자 : !
2. 이항 연산자
- 피연산자가 2개인 연산자
- 산술 연산자 : +, -, *, /, %
- 문자열 결합 연산자 : +
- 비교 연산자 : <, <=, >, >=, ==, !=
- 논리 연산자 : &&, ||, &, |, ^, !
- 대입 연산자 : =, +=, -=, *=, /=, %=
3. 삼항 연산자
- 3개의 피연산자를 필요로 하는 연산자
- C ? x : y
4. 연산자 우선순위
- 단항 > 이항(산술>비교>논리>대입) > 삼항
"""


import sys

input = sys.stdin.readline

n1, n2, n3 = map(int, input().split())

print(n1 if (n1 < n2 and n1 < n3) else (n2 if n2 < n3 else n3))
print(n1 if (n1 > (n2 if n2 > n3 else n3)) else (n2 if n2 > n3 else n3))
