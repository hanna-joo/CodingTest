# DAY 12

- 날짜 : 2022.10.27



### 1. 모음 제거

```python
def solution(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in vowels:
        my_string = my_string.replace(i, '')
    return my_string
```

```python
def solution(my_string):
    return ''.join(map(lambda x: x if x not in 'aeiou' else '', my_string))
```



### 2. 문자열 정렬하기 (1)

```python
def solution(my_string):
    return sorted(list(map(int, filter(lambda x: x in '0123456789', my_string))))
```

- `isdecimal()`
  - 주어진 문자열이 0-9까지의 수로 이루어진 것인지 검사하는 함수
  - 주어진 문자열이 int 형으로 변환 가능한지 검사
- `isdigit()`
  - 해당 문자열이 '숫자' 로 이루어져 있는지 검사 
    - 예) "3²" : True
- `isnumeric()`
  - '수로 볼 수 있는 것' 인 경우 모두 True 로 반환, 
  - 제곱근 및 분수, 거듭제곱 특수문자도 True 로 반환
    - 예) “½”, "3²" : True

```python
def solution(my_string):
    return sorted([int(x) for x in my_string if x.isdecimal()])
```



### 3. 숨어있는 숫자의 덧셈

```python
def solution(my_string):
    return sum(map(int, filter(lambda x: x in '0123456789', my_string)))
```



### 4. 소인수분해


```python
def solution(n):
    answer = []
    for i in range(2, n+1):
        if n % i == 0: 
            answer.append(i)
            while n % i == 0:
                n /= i
    return answer
```



