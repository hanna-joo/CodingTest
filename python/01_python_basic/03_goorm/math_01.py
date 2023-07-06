# 최장 맨해튼 거리
# keyword : 맨해튼 거리, 완전 탐색, 정렬
# return : 주어진 숫자 4개를 활용하여 최장 맨해튼 거리 출력

"""
1. 최장 맨해튼 거리
- 가장 큰 값과 가장 작은 값 차이 + 나머지 두 값의 차이

2. 완전 탐색
- 모든 경우의 수 탐색
- 4개이기 때문에 24개의 경우의 수 존재

3. 정렬
- |x2 - x1| + |y2 - y1|
- 절댓값 기호 제거 -> x2 + y2 - x1 - y1
- x2, y2 는 클수록 이득
- x1, y1 는 작을수록 이득
"""

def manhattan_dist_1(nums):
    nums = nums.copy()
    x1, x2 = nums.pop(nums.index(max(nums))), nums.pop(nums.index(min(nums)))
    y1, y2 = nums[0], nums[1]
    dist = abs(x1-x2) + abs(y1-y2)

    return dist

def manhattan_dist_2(nums):
    dist = 0
    for x1 in nums:
        for y1 in nums:
            if x1 == y1:
                continue
            for x2 in nums:
                if x2 == x1 or x2 == y1:
                    continue
                for y2 in nums:
                    if y2 == x1 or y2 == y1 or y2 == x2:
                        continue
                    temp = abs(x1-x2) + abs(y1-y2)
                    dist = max(temp, dist)

    return dist

def manhattan_dist_3(nums):
    nums.sort()
    dist = nums[3] + nums[2] - nums[1] - nums[0]

    return dist

if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [[1, 3, 5, 10], [-1, -3, 5, -10]] # 11, 17
    test_cases.append(list(map(int, input().rstrip().split())))

    for case in test_cases:
        print(manhattan_dist_1(case))
        print(manhattan_dist_2(case))
        print(manhattan_dist_3(case))