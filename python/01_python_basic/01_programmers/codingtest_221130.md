# LV1. 25-28

- 날짜 : 2022.11.30



### 1. 문자열 다루기 기준

```python
def solution(s):
    return True if (len(s) == 4 or len(s) == 6) and s.isdigit() else False
```



### 2. 약수의 개수와 덧셈

```python
def solution(left, right):
    total = 0
    for i in range(left, right+1):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 0:
            total += i
        else:
            total -= i
    return total
```

```python
def solution(left, right):
    total = 0
    for i in range(left, right+1):
        if i**0.5 == int(i**0.5): total -= i
        else: total += i
    return total
```



### 3. 부족한 금액 계산하기

```python
def solution(price, money, count):
    return (lambda x: x - money if x > money else 0)(price*sum(range(count+1)))
```



### 4. 행렬의 덧셈

```python
def solution(arr1, arr2):
    rows, cols = len(arr1), len(arr1[0])
    for row in range(rows):
        for col in range(cols):
            arr1[row][col] += arr2[row][col]
    return arr1
```
