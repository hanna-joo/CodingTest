# 8진수 계산기
# keyword : 진법, 진법 변환 함수
# return : 주어진 숫자들의 총합을 8진수로 출력

"""
1. n진법
- n개의 숫자로 수를 표현하는 방법
- 16진수의 경우 0~9 와 A~F 알파벳을 이용해 숫자 표현

2. n진수 변환
- 10진수의 수를 n으로 나누어서 몫이 더 이상 n으로 나눌 수 없을 때까지 나누어 나온 남은 몫과 나머지

3. Python 내장 함수
- bin() -> 0b
- oct() -> 0o
- hex() -> 0x
"""

def sum_octal_1(nums):
    total = sum(nums)
    octal = oct(total) # Oo12 형식으로 출력됨
    octal = octal[2:]

    return octal

def sum_octal_2(nums):
    total = sum(nums)
    octal = ''
    while total:
        octal += str(total % 8)
        total //= 8
    octal = octal[::-1]

    return octal

if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [[1, 2, 3, 4], [8, 8, 8]] # 12, 30
    test_cases.append(list(map(int, input().rstrip().split())))

    for case in test_cases:
        print(sum_octal_1(case))
        print(sum_octal_2(case))