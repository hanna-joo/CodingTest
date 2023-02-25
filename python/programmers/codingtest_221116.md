# DAY 24-1

- 날짜 : 2022.11.16



## 수학, 시뮬레이션, 문자열, 조건문 , 반복문

### 1. 치킨 쿠폰

```python
def solution(chicken):
    service = 0
    while chicken >= 10:
        new_service = chicken//10
        service += new_service
        chicken = chicken - new_service*10 + new_service
    return service
```



### 2. 이진수 더하기

```python
def solution(bin1, bin2):
    return bin(int(bin1, 2)+int(bin2, 2))[2:]
```

```python
def solution(bin1, bin2):
    return format(int(bin1, 2) + int(bin2, 2), 'b')
```





---

### 2진수, 8진수, 16진수

#### 각 진수의 접두어

- 파이썬에서는 기본적으로 10진수 형태로 숫자를 표현하기에 다른 진수인 경우 숫자 앞에 접두어를 붙임

  - 2진수 : `0b`

  - 8진수 : `0o`

  - 16진수 : `0x`

#### 숫자형 > 다른 진수의 문자열로 변환

- 10진수 > 2, 8, 16진수로 변환
  - `bin()`, `oct()`, `hex()`
  - `format(숫자, 'b')`, `format(숫자, 'o')`, `format(숫자, 'x')`, `format(숫자, 'X')`, `format(숫자, 'd')`

```python
>>> bin(42)
'0b101010'
>>> oct(42)
'0o52'
>>> hex(42)
'0x2a'
```

- 2진수 > 2, 8, 16진수로 변환

```python
>>> bin(0b101010)
'0b101010'
>>> oct(0b101010)
'0o52'
>>> hex(0b101010)
'0x2a'
>>> str(0b101010)
'42'
```

#### 다른 진수 문자열 > 숫자형으로 변환

- `int(문자열, 진수)`
  - 기본값 : 10

```python
>>> int('0b101010', 2)
42
>>> int('0o52', 8)
42
>>> int('0x2a', 16)
42
```

#### format()

- 숫자를 다른 진수의 문자열로 변경할 때 접두어 제외
  - `format(숫자, 'b')`, `format(숫자, 'o')`, `format(숫자, 'x')`, `format(숫자, 'X')`, `format(숫자, 'd')`

```python
>>> format(42, 'b')
'101010'
>>> format(42, 'o')
'52'
>>> format(42, 'x')
'2a'
>>> format(42, 'X')
'2A'
>>> format(42, 'd')
'42'
```

- 두번째 인자 문자열 맨 앞에 # 붙여주면 접두어 포함

```python
>>> format(42, '#b')
'0b101010'
>>> format(42, '#o')
'0o52'
>>> format(42, '#x')
'0x2a'
>>> format(42, '#X')
'0X2A'
```

```python
>>> "int: {0:d}, bin: {0:b}, oct: {0:o}, hex: {0:x}".format(42)
'int: 42, oct: 52, bin: 101010, hex: 2a'
```

