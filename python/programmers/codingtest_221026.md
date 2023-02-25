# DAY 11

- 날짜 : 2022.10.26



### 1. 주사위의 개수

```python
def solution(box, n):
    answer = 1
    for i in box: answer *= i//n
    return answer
```

```python
def solution(box, n):
    return (box[0]//n) * (box[1]//n) * (box[2]//n)
```



### 2. 합성수 찾기

```python
def solution(n):
    answer = 0
    for i in range(1, n+1):
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                answer += 1
                break
    return answer
```



### 3. 최댓값 만들기

```python
def solution(numbers):
    multi = list()
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if i != j: 
                multi.append(numbers[i]*numbers[j])
    multi.sort(reverse=True)
    return multi[0]
```

```python
def solution(numbers):
    numbers.sort(reverse=True)
    return numbers[0] * numbers[1]
```



### 4. 팩토리얼


```python
def solution(n):
    multi = 1
    for i in range(1, 12):
        multi *= i
        if multi > n:
            break
    return i-1
```

```python
def solution(n):
    multi = 1
    num = 1
    while multi <= n:
        num += 1
        multi *= num
    return num-1
```



