# 백준 온라인 저지 1920, 시간 제한 2초
# N개의 정수 A[1], A[2], A[3], ... , A[N]이 주어졌을 때 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
# N(1<=N<=100,000) M(1<=M<=100,000) A[i](-2^31<=A[i]<2^31)

# 필요 변수 선언 및 초기화
nums_cnt = int(input())
nums = list(map(int, input().split()))
targets_cnt = int(input())
targets = list(map(int, input().split()))


# 이진 탐색
nums.sort()
for target in targets:
    find = False
    start = 0
    end = nums_cnt-1
    # 중앙값과 탐색값이 같을 때까지 반복
    while start <= end:
        mid = (start+end)//2
        if nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            find = True
            break
    if find:
        print(1)
    else:
        print(0)