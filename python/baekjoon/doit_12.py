# 백준 온라인 저지 17298, 시간 제한 1초
# 크기가 N인 수열 A = A(1), A(2), ... , A(N) 이 있다. 수열의 각 원소 A(i)에 관련된 오큰수 NGE(i)를 구하려고 한다.
# A(i)의 오큰수는 오른쪽에 있으면서 A(i)보다 큰 수 중 가장 왼쪽에 있는 수를 의미한다.
# 이러한 수가 없을 때 오큰수는 -1이다. 오큰수 수열을 구하는 프로그램을 작성하시오.
# N(1<=N<=1,000,000), A(i)(1<=A(i)<=1,000,000)

# 필요 변수 선언 및 초기화
seq_cnt = int(input())
seq = list(map(int, input().split()))
stack = list()
answer = [0] * seq_cnt

# seq(수열) 개수만큼 반복문
for i in range(seq_cnt):
    # 스택이 비어있지 않고, 현재 인덱스 값(i)과 stack top 인덱스 값과 비교 
    while stack and seq[i] > seq[stack[-1]]:
        answer[stack.pop()] = seq[i]
    # 현재 인덱스 값(i) stack 에 추가
    stack.append(i)

# stack에 남은 인덱스 -1 채우기
while stack:
    answer[stack.pop()] = -1

# 정답 출력
print(" ".join(map(str, answer)))