# 백준 온라인 저지 10986
# N개의 숫자가 주어졌을 때 연속된 부분의 합이 M으로 나누어떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.

# 필요 변수 선언
n, m = map(int, input().split())
arr = list(map(int, input().split()))
remainder_arr = [0] * n # 나머지 합 배열
remainder_cnt = [0] * m # 같은 나머지를 가진 인덱스 카운트
answer = 0

# 나머지 합 배열 저장 및 나머지 값별 개수 세기
for i in range(n):
    if i == 0:
        remainder_arr[i] = arr[0] % m
    else:
        remainder_arr[i] = (remainder_arr[i-1] + arr[i]) % m
    remainder_cnt[remainder_arr[i]] += 1

# 나머지가 없는 경우
answer += remainder_cnt[0]

# 나머지가 있는 경우 - 2개 뽑는 경우의 수
for i in range(m):
    if remainder_cnt[i] > 1:
        answer += (remainder_cnt[i] * (remainder_cnt[i] - 1) // 2)

print(answer)
print(remainder_arr, remainder_cnt)






