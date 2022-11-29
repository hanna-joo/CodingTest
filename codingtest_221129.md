# LV1. 21-24

- 날짜 : 2022.11.29



### 1. 가운데 글자 가져오기

```python
def solution(s):
    return (lambda x: s[x] if len(s)%2 == 1 else s[x-1:x+1])(len(s)//2)
```



### 2. 수박수박수박수박수박수?

```python
def solution(n):
    return ("수박"*5000)[:n]
```

```python
def solution(n):
    return ''.join(["수" if i%2==0 else "박" for i in range(n)])
```



### 3. 내적

```python
def solution(a, b):
    return sum(a[i] * b[i] for i in range(len(a)))
```

```python
def solution(a, b):
    total = 0
    for i in range(len(a)):
        total += a[i] * b[i]
    return total
```



### 4. 문자열 내림차순으로 배치하기

```python
def solution(s):
    return ''.join(sorted(s, reverse=True))
```
