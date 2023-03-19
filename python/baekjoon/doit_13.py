# 백준 온라인 저지 2164, 시간 제한 2초
# 1번부터 N번까지의 번호가 있는 카드가 있고, 1번 카드가 가장 위, N번 카드가 가장 아래에 놓여 있다.
# 다음과 같은 동작을 카드가 1장 남을 때까지 반복할 때, 가장 마지막에 남는 카드를 구하는 프로그램을 작성하시오.
# 1) 가장 위에 있는 카드를 버린다.
# 2) 그 다음 가장 위에 있는 카드를 가장 아래에 있는 카드 밑으로 옮긴다.
# N(1<=N<=500,000)

# 필요 변수 선언 및 초기화
from collections import deque
card_cnt = int(input())
queue = deque(range(1, card_cnt+1))

# 카드 1장 남을 때까지 반복
while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

# 정답 출력 (마지막 1장 남은 카드 번호)
print(queue[0])