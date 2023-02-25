# LV1. 33-36

- 날짜 : 2022.12.02



### 1. 3진법 뒤집기

```python
def solution(n):
    changed = ''
    while n > 0:
        changed += str(n % 3)
        n //= 3
    return int(changed, 3)
```



### 2. 예산

```python
def solution(d, budget):
    d, cnt = sorted(d), 0
    for i in range(len(d)):
        if (sum(d[:i+1]) <= budget): cnt += 1
        else: return cnt
    return cnt
```

```python
def solution(d, budget):
    cnt = 0
    for num in sorted(d):
        budget -= num
        if budget < 0: break
        else: cnt += 1
    return cnt
```



### 3. 시저 암호

```python
def solution(s, n):
    letters_up, letters_low = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'
    cipher = ''
    for char in s:
        if char == ' ':
            cipher += ' '
        elif char.isupper():
            cipher += letters_up[(letters_up.find(char)+n)%len(letters_up)]
        else:
            cipher += letters_low[(letters_low.find(char)+n)%len(letters_low)]
    return cipher
```

- 아스키코드 활용
  - 문자열도 비교 연산자 사용 가능 (아스키 코드 값 기준)

```python
def solution(s, n):
    cipher, ascii_A, ascii_a = '', ord('A'), ord('a')
    for char in s:
        if char == ' ':
            cipher += ' '
        elif char < 'a':
            cipher += chr((ord(char)+n - ascii_A)%26 + ascii_A)
        else:
            cipher += chr((ord(char)+n - ascii_a)%26 + ascii_a)
    return cipher
```



### 4. 최소 직사각형

```python
def solution(sizes):
    max1 = max([sorted(size)[0] for size in sizes])
    max2 = max([sorted(size)[1] for size in sizes])
    return max1*max2
```
