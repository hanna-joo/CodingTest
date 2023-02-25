# DAY 16

- 날짜 : 2022.11.02



## 문자열, 수학, 배열, 조건문

### 1. 편지

```python
def solution(message):
    return len(message)*2
```



### 2. 가장 큰 수 찾기

```python
def solution(array):
    largest = sorted(array, reverse=True)[0]
    return [largest, array.index(largest)]
```

- `max()` 사용

```python
def solution(array):
    return [max(array), array.index(max(array))]
```



### 3. 문자열 계산하기

- `eval(expression)` 사용
  - expression 이란 하나 이상의 값으로 표현될 수 있는 코드
  - 문자열로 이루어진 expression 을 python 코드로 인식하여 실행시켜주는 함수

```python
def solution(my_string):
    return eval(my_string)
```



### 4. 배열의 유사도


```python
def solution(s1, s2):
    similarity = 0
    for i in s1:
        for j in s2:
            if i == j:
                similarity += 1
    return similarity
```

```python
def solution(s1, s2):
    similarity = 0
    for i in s1:
        if i in s2:
            similarity += 1
    return similarity
```

- set 자료형 활용
  - 집합 자료형으로 교집합, 합집합, 차집합 구하기
    - 

```python
def solution(s1, s2):
    return len(set(s1) & set(s2))
```



---

### set 자료형 활용

- set 자료형의 특징
  - 중복 허용하지 않음
  - 순서가 없음 (인덱싱 미지원)

- set 자료형을 정말 유용하게 사용하는 경우는 교집합, 합집합, 차집합을 구할 때
- 교집합 구하기
  - `s1 & s2` 또는 `s1.intersection(s2)`

```python
>>> s1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
>>> s2 = set([6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
```

```python
>>> s1 & s2
{6, 7, 8, 9, 10}
```

- 합집합 구하기
  - `s1 | s2` 또는 `s1.union(s2)`

```python
>>> s1 | s2
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
```

- 차집합 구하기
  - `s1 - s2` 또는 `s1.difference(s2)`
  - `s2 - s1` 또는 `s2.difference(s1)`

```python
>>> s1 - s2
{1, 2, 3, 4, 5}
>>> s2 - s1
{11, 12, 13, 14, 15}
```

- 그 외 함수
  - 값 추가 : `s1.add(value)`
  - 값 여러 개 추가 : `s1.update([val1, val2, ...])`
  - 특정 값 제거 : `s1.remove(value)`
