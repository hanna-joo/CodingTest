# 소수 찾기
# return : 주어진 수열의 소수 번째 값들의 합 출력
"""
1. n진수로 변환
- 10진수의 수를 n으로 나누어서 몫이 더 이상 n으로 나눌 수 없을 때까지 나누어 나온 남은 몫과 나머지

"""

def sum_prime_idx_1(nums):
    nums_cnt = len(nums)
    total = 0

    idx = set(range(2, nums_cnt+1))
    for i in range(2, int(nums_cnt**0.5)+1):
        idx -= set(range(i+i, nums_cnt+1, i))

    for i in idx:
        total += nums[i-1]

    return total

def sum_prime_idx_2(nums):
    nums_cnt = len(nums)
    total = 0

    return total

if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [[1, 2, 3, 4, 5, 6, 7], [-46, 65, 13, 24, -25, 60, -39, 31, -21, -10, 69, 9]]
    test_cases.append(list(map(int, input().rstrip().split())))

    for case in test_cases:
        print(sum_prime_idx_1(case))
        print(sum_prime_idx_2(case))