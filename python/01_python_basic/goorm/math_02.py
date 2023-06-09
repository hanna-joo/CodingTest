# 8진수 계산기
# return : 주어진 숫자들의 총합을 8진수로 출력

"""
1. n진수로 변환
- 10진수의 수를 n으로 나누어서 몫이 더 이상 n으로 나눌 수 없을 때까지 나누어 나온 남은 몫과 나머지
"""

def sum_octal_1(nums):
    total = sum(nums)
    octal = oct(total) # Oo12 형식으로 출력됨
    octal = octal[2:]

    return octal

def sum_octal_2(nums):
    total = sum(nums)
    octal = ''
    while total > 8:
        octal += str(total % 8)
        total //= 8
        if total < 8:
            octal += str(total)
    octal = octal[::-1]

    return octal

if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [[1, 2, 3, 4], [8, 8, 8]]
    test_cases.append(list(map(int, input().rstrip().split())))

    for case in test_cases:
        print(sum_octal_1(case))
        print(sum_octal_2(case))