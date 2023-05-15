# problem source : https://www.acmicpc.net/problem/11659

# input() 보다 빠른 입력 방법 : https://www.acmicpc.net/blog/view/56
import sys
input = sys.stdin.readline

nums_cnt, quiz_cnt = map(int, input().split())
nums = list(map(int, input().split()))

# 합 배열 구하기
sum_arr = [0]
temp = 0
for num in nums:
    temp += num
    sum_arr.append(temp)

# i부터 j까지의 구간 합 = sum_arr[j] - sum_arr[i-1]
for _ in range(quiz_cnt):
    i, j = map(int, input().split())
    prefix_sum = sum_arr[j] - sum_arr[i-1]
    print(prefix_sum)