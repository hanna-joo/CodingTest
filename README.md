# 1. 자료구조를 활용한 문제해결
## 1.1. 구간 합 : O(1)
## 1.2. 투 포인터 : O(nlogn)
## 1.3. 슬라이딩 윈도우 : O(n)
- 덱(deque) : 양방향 큐
  - `d.append(item)`, `d.appendleft(item)`, `d.pop()`, `d.popleft()`
## 1.4. 스택과 큐
- 스택(stack) : 후입선출
  - `s.append(data)`, `s.pop()`, `s[-1]`
- 큐(queue) : 선입선출
  - `q.append(data)`, `q.popleft()`, `q[0]`
- 우선순위 큐(priority queue) : 우선순위 정렬 및 선출
  - `q.put((우선순위, data))`, `q.get()`, `q.empty()`, `q.full()` `q.qsize()`
