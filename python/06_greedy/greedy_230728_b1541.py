# 잃어버린 괄호
# source : https://www.acmicpc.net/problem/1541
# keyword : 그리디
# return : 주어진 식에서 괄호를 적절히 쳐서 만들 수 있는 최솟값 출력

"""
1. 문제
- 연산 종류는 마이너스와 플러스 2가지

2. 로직
- 마이너스 기준으로 구분 -> 정수 / 정수+정수+정수 만 남음
- 플러스끼리 전부 괄호로 묶고, 나중에 빼면 최솟값
"""

import sys
input = sys.stdin.readline

expression = list(input().rstrip().split('-'))

# 첫 번째 값이 수식인지 판별
start = expression.pop(0)
if start.isdigit():
    start = int(start)
else:
    start = sum(map(int, start.split('+')))

# 두 번째 값부터 빼기 시작
answer = start
for e in expression:
    if e.isdigit():
        answer -= int(e)
    else:
        answer -= sum(map(int, e.split('+')))

print(answer)

"""
테스트 케이스 : -35 / 100 / 0

55-50+40

10+20+30+40

00009-00009

100-20+120-10-100+100 -> 100-140-10-200=-250

00009+00009+000010 -> -10
"""