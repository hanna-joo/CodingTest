# DAY 19

- 날짜 : 2022.11.07



## 문자열, 배열, 조건문

### 1. 7의 개수

```python
def solution(array):
    count_7 = 0
    for num in array:
        count_7 += str(num).count('7')
    return count_7
```

```python
def solution(array):
    return ''.join(map(lambda x: str(x), array)).count('7')
```



### 2. 잘라서 배열로 저장하기

```python
def solution(my_str, n):
    sliced = []
    for i in range(0, len(my_str), n):
        if i+n <= len(my_str):
            sliced.append(my_str[i:i+n])
        else:
            sliced.append(my_str[i:])
    return sliced
```

- [Python Slicing 은 Index Out Of Range 에도 작동](https://blog.finxter.com/daily-python-puzzle-overshoot-index-slicing/)
  - Slicing : `[start:end]` 표기법을 사용하여 시퀀스 유형의 하위 시퀀스에 엑세스하는 것
    - `end` 인덱스가 최대 시퀀스 인덱스보다 큰 경우에도 에러를 발생시키지 않고 최대 시퀀스 인덱스까지만 슬라이싱하여 가져옴
    - `start` 인덱스가 범위를 벗어나도 빈 리스트 반환함
  - 단일 값을 가져오는 Indexing 은 `index out of range`  에러 발생시킴

```python
def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0, len(my_str), n)]
```



### 3. 중복된 숫자 개수

```python
def solution(array, n):
    return array.count(n)
```

```python
def solution(array, n):
    return sum(map(lambda x: 1 if x == n else 0, array))
```

```python
def solution(array, n):
    return sum(1 if i == n else 0 for i in array)
```

```python
def solution(array, n):
    return sum(1 for i in array if i == n)
```



### 4. 머쓱이보다 키 큰 사람


```python
def solution(array, height):
    return sum(1 for i in array if i > height)
```

```python
def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)
```

