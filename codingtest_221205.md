# LV1. 36-37

- 날짜 : 2022.12.05



### 1. 1차[비밀지도]

```python
def solution(n, arr1, arr2):
    arr1 = list(map(lambda x: bin(x)[2:] if len(bin(x)[2:])==n else (n-len(bin(x)[2:]))*'0'+bin(x)[2:], arr1))
    arr2 = list(map(lambda x: bin(x)[2:] if len(bin(x)[2:])==n else (n-len(bin(x)[2:]))*'0'+bin(x)[2:], arr2))
    final = list()
    for i in range(n):
        row = ''
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                row += '#'
            else:
                row += ' '
        final.append(row)
    return final
```

- `str.zfill(width)`
  - width(숫자)보다 문자열 자릿수가 적으면 그 앞부분을 0으로 채워줌
  - `str.rjust(width, [, fillchar])`
    - 문자열을 오른쪽으로 정렬하고 왼쪽의 남은 공백(`width-문자열 자릿수`)을 특정 문자열로 채워줌, 기본값은 space
  - `str.ljust(width, [, fillchar])`
    - 문자열을 오른쪽으로 정렬하고 오른쪽의 남은 공백(`width-문자열 자릿수`)을 특정 문자열로 채워줌, 기본값은 space

```python
def solution(n, arr1, arr2):
    arr1 = [bin(x)[2:].zfill(n) for x in arr1]
    arr2 = [bin(x)[2:].zfill(n) for x in arr2]
    return [''.join('#' if arr1[i][j]=='1' or arr2[i][j]=='1' else ' ' for j in range(n)) for i in range(n)]
```



### 2. 문자열 내 마음대로 정하기

```python
def solution(strings, n):
    strings.sort(key = lambda x: (x[n], x))
    return strings
```

```python
def solution(strings, n):
    return sorted(strings, key = lambda x: (x[n], x))
```

