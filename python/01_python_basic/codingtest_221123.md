# LV1. 5-8

- 날짜 : 2022.11.23



### 1. 자연수 뒤집어 배열로 만들기

```python
def solution(n):
    return [int(i) for i in str(n)][::-1]
```



### 2. 정수 제곱근 판별

```python
def solution(n):
    return (n**0.5+1)**2 if (n**0.5).is_integer() else -1
```

```python
def solution(n):
    return (lambda x: (x+1)**2 if x.is_integer() else -1)(n**0.5)
```



### 3. 문자열 내 p와 y의 개수

```python
def solution(s):
    s = s.lower()
    return True if s.count('p') == s.count('y') else False
```

```python
def solution(s):
    return (lambda x: True if x.count('p') == x.count('y') else False)(s.lower())
```



### 4. 문자열을 정수로 바꾸기

- 내장함수 int() 사용하여 정수로 변환

```python
def solution(s):
    return int(s)
```

- 내장함수 사용하지 않고 정수로 변환

```python
def solution(s):
    num_dict = {'0':0, '1': 1, '2': 2, '3':3, '4':4, 
                '5':5, '6':6, '7':7, '8':8, '9':9}
    number, jari = 0, len(s)
    if s[0] == '-':
        for i in range(1, jari):
            number -= num_dict[s[i]] * (10 ** (jari-i-1))
    elif s[0] == '+':
        for i in range(1, jari):
            number += num_dict[s[i]] * (10 ** (jari-i-1))
    else:
        for i in range(jari):
            number += num_dict[s[i]] * (10 ** (jari-i-1))
    return number
```
