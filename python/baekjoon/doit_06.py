# 백준 온라인 저지 2018
# 어떠한 자연수 N은 몇 개의 연속된 자연수의 합으로 나타낼 수 있다.
# 어떤 자연수 N(1<=N<=10,000,000)을 몇 개의 연속된 자연수의 합으로 나타내는 가짓수를 구하는 프로그램을 작성하시오.

# 필요 변수 선언 및 초기화
n = int(input())
start_idx, end_idx, num_sum, answer = 1, 1, 1, 1

# 투 포인터 활용 : sum 과 n 비교해서 처리
while end_idx < n:
    if num_sum == n:
        answer += 1
        end_idx += 1
        num_sum += end_idx
    elif num_sum > n:
        num_sum -= start_idx
        start_idx += 1
    else:
        end_idx += 1
        num_sum += end_idx

# 정답 출력
print(answer)
