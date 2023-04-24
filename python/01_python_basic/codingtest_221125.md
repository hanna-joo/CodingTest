# LV1. 13-16

- 날짜 : 2022.11.25



### 1. 두 정수 사이의 합

```python
def solution(a, b):
    return sum(num for num in range(min(a, b), max(a, b)+1))
```

```python
def solution(a, b):
    summ = 0
    if a > b: a, b = b, a
    for i in range(a, b+1):
        summ += i
    return summ
```



### 2. 콜라츠 추측

```python
def solution(num):
    cnt = 0
    while num != 1:
        if num % 2 == 0: 
            num = num / 2
        else: 
            num = num * 3 + 1
        cnt += 1
        if cnt == 500: 
            return -1
    return cnt
```



### 3. 서울에서 김서방 찾기

```python
def solution(seoul):
    return f'김서방은 {seoul.index("Kim")}에 있다'
```



### 4. 핸드폰 번호 가리기

```python
def solution(phone_number):
    return "*"*(len(phone_number)-4) + phone_number[-4:]
```
