# 완전 수 구하기
# keyword : 완전 수
# return : 완전 수인지 아닌지 판별, 1부터 N까지 중 완전 수 개수 반환

"""
1. 완전수 : 자기 자신을 제외한 약수의 합이 자기 자신인 수
2. 약수 구하기
3. 약수의 모든 합
"""

def perfect_num(num):
    # 약수 구하기
    divisors = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            divisors.extend([i, num//i])
    # 약수 정렬
    divisors.sort()
    # 약수의 모든 합이 자기 자신과 같은지 확인
    for div in divisors[:-1]:
        num -= div
    if num == 0:
        return True
    else:
        return False
    

def perfect_num_cnt(s, e):
    cnt = 0
    for i in range(s, e+1):
        if perfect_num(i):
            cnt += 1
    return cnt


if __name__ == "__main__":
    test_cases = [1000, 6]
    for case in test_cases:
        print(perfect_num(case))

    test_cases = [[4, 1000], [6, 100]]
    for case in test_cases:
        print(perfect_num_cnt(case[0], case[1]))