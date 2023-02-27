# 백준 온라인 저지 1940
# 두 개의 재료가 M(1<=M<=10,000,000)이면 갑옷을 만들 수 있다.
# N(1<=N<=15,000)개의 재료와 M이 주어졌을 때 몇 개의 갑옷을 만들 수 있는지를 구하는 프로그램을 작성하시오.

# 필요 변수 선언 및 초기화
n = int(input())
m = int(input())
material = sorted(list(map(int, input().split()))) # 정렬 알고리즘의 시간 복잡도는 O(nlogn)
start_idx, end_idx = 0, n - 1
answer = 0

# 투 포인터 활용
while start_idx < end_idx:
    material_sum = material[start_idx] + material[end_idx]
    if material_sum < m:
        start_idx += 1
    elif material_sum > m:
        end_idx -= 1
    else:
        answer += 1
        start_idx += 1
        end_idx -= 1

# 정답 출력
print(answer)
