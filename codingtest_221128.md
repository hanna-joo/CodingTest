# LV1. 13-16

- 날짜 : 2022.11.25



### 1. 나누어 떨어지는 숫자 배열

```python
def solution(arr, divisor):
    divided = list()
    for i in arr:
        if i % divisor == 0:
            divided.append(i)
    return sorted(divided) if divided else [-1]
```

```python
def solution(arr, divisor):
    divided = sorted(filter(lambda x: x % divisor == 0, arr))
    return if divided else [-1]
```



### 2. 제일 작은 수 제거하기

```python
def solution(arr):
    arr.pop(arr.index(min(arr)))
    return arr if arr else [-1]
```



### 3. 음양 더하기

```python
def solution(absolutes, signs):
    return sum(map(lambda x: absolutes[x] if signs[x] else -absolutes[x], range(len(absolutes))))
```

```python
def solution(absolutes, signs):
    return sum(map(lambda x: absolutes[x] if signs[x] else -absolutes[x], range(len(absolutes))))
```

```python
def solution(absolutes, signs):
    total = 0
    for i in range(len(absolutes)):
        if signs[i] == False:
            total -= absolutes[i]
        else:
            total += absolutes[i]
    return total
```



### 4. 없는 숫자 더하기

```python
def solution(numbers):
    return sum(filter(lambda x: x not in numbers,range(10)))
```
