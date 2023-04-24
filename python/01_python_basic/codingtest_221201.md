# LV1. 29-32

- 날짜 : 2022.12.01



### 1. 직사각형 별찍기

```python
n, m = map(int, input().strip().split(' '))
for _ in range(m):
    print("*" * n)
```

```python
n, m = map(int, input().strip().split(' '))
print(("*" * n + "\n") * m)
```



### 2. 최대공약수와 최대공배수

```python
def solution(n, m):
    final = [1, n*m]
    small, big = min(n, m), max(n, m)
    for i in range(small, 1, -1):
        if big % i == 0 and small % i == 0:
            final[0] = i
            break
    if final[0] == 1:
        return final
    else:
        final[1] = (lambda x: (big//x)*(small//x)*x)(final[0])
        return final
```



### 3. 같은 숫자는 싫어

```python
def solution(arr):
    unique = [arr[0]]
    for num in arr:
        if num != unique[-1]:
            unique.append(num)
    return unique
```



### 4. 이상한 문자 만들기

```python
def solution(s):
    words = s.split(' ')
    transfered = list()
    for word in words:
        new_word = ''.join([char.upper() if i%2==0 else char.lower() for i, char in enumerate(word)])
        transfered.append(new_word)
    return ' '.join(transfered)
```
