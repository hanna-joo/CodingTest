# 소수 찾기
# keyowrd : 소수 판정, 에라토스테네스의 체
# return : 주어진 수열의 소수 번째 값들의 합 출력

"""
1. 소수 판정하기
- 소수 : 1과 자기 자신으로만 나누어 떨어지는 수
- 나누어 떨어질 때의 대칭적인 성질을 활용 (약수는 대칭적)
- 하나의 수 N에 대한 소수 판별 시 루트 N까지만 봐도 됨
- 시간복잡도 O(N**2) -> O(N**1.5)

2. 에라토스테네스의 체
- 여러 개의 수에 대한 소수 판별 시 사용
- 어떤 수의 약수를 세는 것보다 배수를 세는 것이 더 쉬움
- 어떤 수가 소수인지 판정 (X)
- 어떤 수가 소수가 아닌지 판정 (O)
- 전체 수를 소수 후보로 지정하고 소수의 배수들을 후보에서 제외
- 시간복잡도 O(NloglogN)
"""

def sum_prime_idx_1(nums):
    nums_cnt = len(nums)
    total = 0

    prime = set(range(2, nums_cnt+1))
    for i in range(2, int(nums_cnt**0.5)+1):
        prime -= set(range(i+i, nums_cnt+1, i))

    for i in prime:
        total += nums[i-1]

    return total

def sum_prime_idx_2(nums):
    nums_cnt = len(nums)
    nums = [0] + nums.copy()
    total = 0

    is_prime = [1 for _ in range(nums_cnt+1)]
    prime = []
    for i in range(2, nums_cnt+1):
        if not is_prime[i]:
            continue
        prime.append(i)
        for j in range(2 * i, nums_cnt+1, i):
            is_prime[j] = 0
    
    for i in prime:
        total += nums[i]

    return total

if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [[1, 2, 3, 4, 5, 6, 7], 
                  [-46, 65, 13, 24, -25, 60, -39, 31, -21, -10, 69, 9]] # 17, 83
    test_cases.append(list(map(int, input().split())))

    for case in test_cases:
        print(sum_prime_idx_1(case))
        print(sum_prime_idx_2(case))