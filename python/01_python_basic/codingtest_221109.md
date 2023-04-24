# DAY 21

- 날짜 : 2022.11.09 ~ 2022.11.12



## 문자열, 사칙연산, 시뮬레이션, 2차원배열, 수학 배열

### 1. 숨어있는 숫자의 덧셈(2)

```python
def solution(my_string):
    before = ''
    numbers = list()
    for char in my_string:
        if char.isdecimal():
            if before.isdecimal():
                numbers.append(numbers.pop()+char)
            else:
                numbers.append(char)
        before = char
    return sum(map(lambda x: int(x), numbers))
```

```python
def solution(my_string):
    numbers = ''.join([s if s.isdecimal() else ' ' for s in my_string])
    return sum(int(i) for i in numbers.split())
```



### 2. 안전지대

#### 문제

```
지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.
지뢰는 2차원 배열 `board`에 1로 표시되어 있고 `board`에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
지뢰가 매설된 지역의 지도 `board`가 매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.
```

#### 테스트 케이스

```
board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
---
13

board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
---
19
```

#### 풀이

- 가능한 인덱스 범위를 먼저 구해놓고 값 변경

```python
def idx_range(m, n, length):
    idx_m = list(filter(lambda x: 0<=x<length,[m-1, m, m+1]))
    idx_n = list(filter(lambda x: 0<=x<length, [n-1, n, n+1]))
    cross = [(m, n) for m in idx_m for n in idx_n]
    return cross

def solution(board):
    narray = len(board)
    for m in range(narray):
        if 1 in board[m]:
            for n in filter(lambda x: board[m][x] == 1, range(narray)):
                idxs = idx_range(m, n, narray)
                for idx in idxs:
                    if board[idx[0]][idx[1]] == 0: board[idx[0]][idx[1]] = 2
    return sum(map(lambda x: x.count(0), board)) 
```

- 오답
  - `try~except` 구문 쓰면 에러 발생 시 try 문에 남은 명령어들을 실행 안 해서 에러 발생
  - 또한 아래처럼 진행할 경우 `m-1`/`n-1` 이 -1 인 경우 인덱싱을 안하는 게 아니라 배열의 끝 값을 변경하게 됨

```python
def solution(board):
    narray = len(board)
    for m in range(narray):
        if 1 in board[m]:
            for n in filter(lambda x: board[m][x] == 1, range(narray)):
                try:
                    if board[m-1][n] == 0: board[m-1][n] = 2
                    if board[m+1][n] == 0: board[m+1][n] = 2
                    if board[m][n-1] == 0: board[m][n-1] = 2
                    if board[m][n+1] == 0: board[m][n+1] = 2
                    if board[m-1][n-1] == 0: board[m-1][n-1] = 2
                    if board[m-1][n+1] == 0: board[m-1][n+1] = 2
                    if board[m+1][n-1] == 0: board[m+1][n-1] = 2
                    if board[m+1][n+1] == 0: board[m+1][n+1] = 2
                except:
                    pass
    return sum(map(lambda x: x.count(0), board))
```



### 3. 삼각형의 완성조건 (2)

```python
def solution(sides):
    cnt = 0
    # 주어진 경우
    for side in range(1, max(sides)+1):
        if side + min(sides) > max(sides):
            cnt += 1
    # 안 주어진 경우
    while side+1 < sides[0] + sides[1]:
        cnt += 1
        side += 1
    return cnt
```

- 다른 풀이

```python
def solution(sides):
    # 주어진 경우: max(sides)-min(sides) < x <= max(sides)
    inside = max(sides) - (max(sides) - min(sides))
    # 안 주어진 경우: max(sides) < x < sum(sides)
    outside = sum(sides) - max(sides) - 1
    return inside + outside
```

```python
def solution(sides):
    return 2 * min(sides) - 1
```



### 4. 외계어 사전

#### 문제

```
PROGRAMMERS-962 행성에 불시착한 우주비행사 머쓱이는 외계행성의 언어를 공부하려고 합니다. 알파벳이 담긴 배열 spell과 외계어 사전 dic이 매개변수로 주어집니다. spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재한다면 1, 존재하지 않는다면 2를 return하도록 solution 함수를 완성해주세요.
```

#### 테스트케이스

```
spell = ["p", "o", "s"]
dic = ["sod", "eocd", "qixm", "adio", "soo"]
---
2
```

```
spell = ["z", "d", "x"]
dic = ["def", "dww", "dzx", "loveaw"]
---
1
```

#### 풀이


```python
def solution(spell, dic):
    for word in dic:
        exist = len(spell)
        for char in spell:
            if char in word:
                exist -= 1
        if exist == 0:
            return 1
    return 2
```

- `set()` 함수 사용

```python
def solution(spell, dic):
    for word in dic:
        if set(list(word)) == set(spell):
            return 1
    return 2
```

