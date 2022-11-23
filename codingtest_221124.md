# LV1. 9-12

- 날짜 : 2022.11.24



### 1. 하샤드 수

```python
def solution(x):
    return True if x%sum(int(i) for i in str(x)) == 0 else False
```



### 2. x만큼 간격이 있는 n개의 숫자

- 0인 경우 고려해야 함

```python
def solution(x, n):
    return list(range(x, x*n+1, x)) if x>0 else list(range(x, x*n-1, x)) if x<0 else [0 for _ in range(n)]
```



### 3. 정수 내림차순으로 배치하기

```python
def solution(n):
    return int(''.join(sorted(str(n), reverse=True)))
```



### 4. 나머지가 1이 되는 수 찾기

```python
def solution(n):
    div = 2
    while n%div != 1:
        div += 1
    return div
```
