# 1. 자료구조를 활용한 문제해결
## 1.1. 구간 합 : O(1)
- 문제 : doit_05
## 1.2. 투 포인터 : O(nlogn)
- 문제 : doit_06 ~ doit_08
## 1.3. 슬라이딩 윈도우 : O(n)
- 윈도우를 한 칸씩 이동하며 현재 상태 리스트 업데이트
  - 제거된 칸과 새로 추가된 칸만 반영해서 확인하고 업데이트
  - 윈도우 전체를 스캔할 필요 없이 앞 뒤만 확인하면 되기 때문에 효율적
- 슬라이딩 윈도우를 덱으로 구현하면 정렬 효과
  - 덱(deque) : 양방향 큐로 양쪽 방향에서 엘리먼트를 append 하거나 pop 가능
  - 일반적인 리스트는 양끝 엘리먼트에 접근하여 append, pop하는 경우 O(n) 소요
  - 데크의 경우 양끝 엘리먼트에 접근하여 append, pop하는 경우 O(1) 소요
  - `deque.append(item)`, `deque.appendleft(item)`, `deque.pop()`, `deque.popleft()`
- 문제 : doit_09 ~ doit_10
## 1.4. 스택과 큐
- 스택(stack) : 삽입과 삭제 연산이 후입선출로 이루어지는 자료구조
  - 삽입과 삭제가 한 쪽(top)에서만 일어남
  - 파이썬에서는 list로 구현
  - `s.append(data)`, `s.pop()`, `s[-1]`
  - 깊이 우선 탐색(Depth First Search), 백트래킹 종류의 코딩에 효과적
- 큐(queue) : 삽입과 삭제 연산이 선입선출로 이루어지는 자료구조
  - 삽입(rear)과 삭제(front)가 양방향으로 일어남
  - 파이썬에서는 deque로 구현
  - `s.append(data)`, `s.popleft()`, `s[0]`
  - 너비 우선 탐색(Breadth First Search)에서 자주 사용
  - 문제 : doit_11 ~ doit_14
