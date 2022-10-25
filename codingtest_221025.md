# DAY 10

- 날짜 : 2022.10.25



### 1. 점의 위치 구하기

```python
def solution(dot):
    if dot[0] > 0 and dot[1] > 0: return 1
    elif dot[0] < 0 and dot[1] > 0: return 2
    elif dot[0] < 0 and dot[1] < 0: return 3
    elif dot[0] > 0 and dot[1] < 0: return 4
```



### 2. 2차원으로 만들기

```python
def solution(num_list, n):
    answer = []
    before = 0
    for i in range(n, len(num_list)+1, n):
        answer.append(num_list[before:i])
        before = i
    return answer
```



### 3. 공 던지기

```python
def solution(numbers, k):
    cnt = 0
    while k > 0:    
        index = cnt % len(numbers)
        k -= 1
        cnt += 2
    return numbers[index]
```



### 4. 배열 회전시키기


```python
def solution(numbers, direction):
    if direction == "right":
        last = numbers.pop(len(numbers)-1)
        answer = [last]
        answer.extend(numbers)
    else:
        first = numbers.pop(0)
        answer = numbers
        answer.append(first)
    return answer
```



