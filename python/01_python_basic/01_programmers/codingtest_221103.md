# DAY 17

- 날짜 : 2022.11.03



## 문자열, 수학, 조건문, 배열, 사칙연산

### 1. 숫자 찾기

```python
def solution(num, k):
    return str(num).index(str(k))+1 if str(k) in str(num) else -1
```



### 2. n의 배수 고르기

```python
def solution(num, k):
    return str(num).index(str(k))+1 if str(k) in str(num) else -1
```



### 3. 자릿수 더하기

```python
def solution(n):
    answer = 0
    for num in str(n): 
        answer += int(num)
    return answer
```

```python
def solution(n):
		return sum([int(num) for num in str(n)])
```



### 4. OX 퀴즈


```python
def solution(quiz):
    quiz = list(map(lambda x: x.split(" = "), quiz))
    return list(map(lambda x: "O" if eval(x[0])==int(x[1]) else "X", quiz))
```

