# 백준 온라인 저지 11286, 시간 제한 2초
# 절댓값 힙은 다음과 같은 연산을 지원하는 자료구조다. 절댓값 힙을 구현하시오.
# 1) 배열에 정수 x(x!=0)를 넣는다.
# 2) 0을 입력하면, 배열에서 절댓값이 가장 작은 값을 출력하고 배열에서 제거한다.
# 3) 절댓값이 가장 작은 값이 여러 개인 경우 그 중 가장 작은 수를 출력하고 제거한다.
# 4) 값이 없으면 0을 출력한다.
# 1<=연산의 개수<=100,000, -2^31 < 입력정수 < 2^31

# 필요 변수 선언 및 초기화
from queue import PriorityQueue # 내부적으로 heap 모듈 사용
calc_cnt = int(input())
priority = PriorityQueue()

# 연산 수만큼 반복
for i in range(calc_cnt):
    request = int(input())
    if request == 0:
        print(0) if priority.empty() else print(priority.get()[1])
    else:
        priority.put((abs(request), request))