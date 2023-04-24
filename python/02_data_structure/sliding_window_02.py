# 백준 온라인 저지 11003, 시간 제한 2.4초
# N개의 수 A(1), A(2), ... , A(N) 과 L이 주어진다. A(i-L+1) ~ A(i) 중 최솟값을 D(i)라고 할 때, D에 저장된 수를 출력하는 프로그램을 작성하시오.
# 이 때 i <= 0 인 A(i)는 무시하고 D를 구해야 한다.
# N, L(1<=L<=N<=5,000,000), A(i)(-10**9<=A(i)<= 10**9)

# 필요 변수 선언 및 초기화
from collections import deque
nums_len, window_len = map(int, input().split())
nums = list(map(int, input().split()))
my_deque = deque()

for i in range(nums_len):
    # 1. 맨 뒤 값과 새로운 숫자 비교
    while my_deque and my_deque[-1][1] > nums[i]:
        my_deque.pop()              # 작으면 맨 뒤 삭제(더 이상 작지 않을 때까지 삭제)
    my_deque.append((i, nums[i]))   # 새로운 값 맨 뒤에 추가

    # 2. 윈도우 범위 계산
    min_idx = i - window_len + 1    # 범위 내 최소 인덱스
    if my_deque[0][0] < min_idx:    # 덱 첫번째 값 인덱스와 비교
        my_deque.popleft()          # 작으면 맨 앞 삭제

    # 3. 최솟값 출력
    print(my_deque[0][1], end=' ')