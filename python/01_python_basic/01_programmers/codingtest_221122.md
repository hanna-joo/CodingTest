# LV1. 1-4

- 날짜 : 2022.11.22



### 1. 짝수와 홀수

```python
def solution(num):
    return "Even" if num%2 == 0 else "Odd"
```



### 2. 약수의 합

```python
def solution(n):
    yaksu_sum = 0
    for i in range(1, n+1):
        if n % i == 0:
            yaksu_sum += i
    return yaksu_sum
```

```python
def solution(n):
    return sum(i for i in range(1, n+1) if n%i == 0)
```



### 3. 평균구하기

```python
def solution(arr):
    return sum(arr)/len(arr)
```



### 4. 자릿수 더하기

```python
def solution(n):
    return sum(int(num) for num in str(n))
```

