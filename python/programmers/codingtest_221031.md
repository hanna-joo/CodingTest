# DAY 14

- 날짜 : 2022.10.31



### 1. 가까운 수

```python
def solution(array, n):
    nearest = [array[0], abs(array[0] - n)]
    for i in array[1:]:
        distance = abs(i-n)
        if distance < nearest[1] or (distance == nearest[1] and i < nearest[0]): 
            nearest[0], nearest[1] = i, distance
    return nearest[0]
```



### 2. 369 게임

```python
def solution(order):
    clap = 0
    for num in str(order):
        if num in '369': 
            clap += 1
    return clap
```



### 3. 암호 해독

```python
def solution(cipher, code):      
    return ''.join([cipher[i] for i in range(code-1, len(cipher), code)])
```



### 4. 대문자와 소문자

- 참고 함수
  - `문자열.lower()`
  - `문자열.upper()`
  - `문자열.islower()`
  - `문자열.isupper()`


```python
def solution(my_string):
    return ''.join([char.lower() if char.isupper() else char.upper() for char in my_string])
```
