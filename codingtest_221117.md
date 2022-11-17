# DAY 24-2

- 날짜 : 2022.11.17



## 수학, 시뮬레이션, 문자열, 조건문 , 반복문

### 3. A로 B 만들기

```python
def solution(before, after):
    before, after, cnt = list(before), list(after), 0
    for char in before:
        if char in after:
            after.pop(after.index(char))
            cnt += 1
    return 1 if cnt == len(before) else 0
```

```python
def solution(before, after):
    return 1 if sorted(list(before)) == sorted(list(after)) else 0
```



### 4. k의 개수

```python
def solution(i, j, k):
    k, cnt = str(k), 0
    for num in range(i, j+1):
        if k in str(num):
            cnt += str(num).count(k)
    return cnt
```

```python
def solution(i, j, k):
    number = ''
    for num in range(i, j+1):
        number += str(num)
    return number.count(str(k))
```

