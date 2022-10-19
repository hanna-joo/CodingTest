# DAY 6

- 날짜 : 2022.10.19



### 1. 문자열 뒤집기

```python
def solution(my_string):
    return my_string[::-1]
```

### 2. 직각삼각형 출력하기

```python
def solution(my_string):
    return my_string[::-1]
```

### 3. 짝수 홀수 개수

```python
def solution(num_list):
    even, odd = 0, 0
    for i in num_list:
        if i % 2 == 0: even += 1
        else: odd += 1
    return [even, odd]
```

### 4. 문자 반복 출력하기

```python
def solution(my_string, n):
    answer = ''
    for s in my_string:
        answer += s * n
    return answer
```
