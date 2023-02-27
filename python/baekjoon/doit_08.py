# 백준 온라인 저지 1253
# 주어진 N개의 수에서 (서로)다른 두 수의 합으로 표현되는 수가 있다면, 그 수를 '좋은 수'라고 한다.
# N개의 수 중 좋은 수가 총 몇 개인지 출력하시오.
# 시간 제한 2초
# N(1<=N<=2,000), Ai(|Ai| <= 1,000,000,000, Ai는 정수)

# 필요 변수 선언 및 초기화
n = int(input())
nums = list(map(int, input().split()))
answer = 0

# 투 포인터 활용 : 두 포인터 인덱스가 k가 아니면서 포인터들 합이 find와 동일
nums.sort()
for k in range(n):
    start, end, find = 0, n-1, nums[k]
    while start < end:
        nums_sum = nums[start] + nums[end]
        if nums_sum < find:
            start += 1
        elif nums_sum > find:
            end -= 1
        else:
            if start != k and end != k: # 포인터 값이 0인 경우 예외 처리
                answer += 1
                break
            elif start == k:
                start += 1
            else:
                end -= 1      

# 정답 출력
print(answer)