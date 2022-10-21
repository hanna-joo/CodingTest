# DAY 7

- 날짜 : 2022.10. 20



### 1. 특정 문자 제거하기

```python
def solution(my_string, letter):
    return my_string.replace(letter, '')
```

```python
def solution(my_string, letter):
    str_list = list(my_string)
    return ''.join([char for char in str_list if char != letter])
```



### 2. 각도기

```python
def solution(angle):
    if angle < 90: answer = 1
    elif angle == 90: answer = 2
    elif 90 < angle < 180: answer = 3
    else: answer = 4
    return answer
```



### 3. 양꼬치

```python
def solution(n, k):
    lamb = 12000 * n
    drinks = 2000 * (k - (n//10))
    return lamb + drinks
```



### 4. 짝수의 합

```python
def solution(n):
    return sum([i for i in range(2, n+1, 2)])

def solution(n):
    even_sum = 0
    for i in range(2, n+1, 2): even_sum += i
    return even_sum
```
