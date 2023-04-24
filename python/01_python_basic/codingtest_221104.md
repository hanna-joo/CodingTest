# DAY 18

- 날짜 : 2022.11.04



## 문자열, 수학, 조건문, 정렬

### 1. 문자열 안에 문자열

```python
def solution(str1, str2):
    return 1 if str2 in str1 else 2
```



### 2. 제곱수 판별하기

```python
def solution(n):
    return 1 if n**0.5 == int(n**0.5) else 2
```

```python
def solution(n):
    return 1 if (n**0.5).is_integer() else 2
```



### 3. 세균 증식

```python
def solution(n, t):
    return n*2**t
```

```python
def solution(n, t):
    answer = n
    for i in range(t):
        answer *= 2
    return answer
```



### 4. 문자열 정렬하기 (2)

- `sorted(iterable)`
  - 리스트 외에도 iterable 객체에 대해 사용 가능
  - 새로운 정렬 리스트반환
- `list.sort()` 
  - 리스트에만 사용 가능
  - 원본 리스트를 정렬시키고 아무것도 반환하지 않음
    - 원본 리스트가 필요없을 경우 효율적


```python
def solution(my_string):
    return ''.join(sorted(my_string.lower()))
```

```python
def solution(my_string):
    answer = ''
    for char in sorted(my_string.lower()):
        answer += char
    return answer
```

