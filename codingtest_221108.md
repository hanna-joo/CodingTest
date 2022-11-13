# DAY 20

- 날짜 : 2022.11.08, 2022.11.13



## 수학, 시뮬레이션, 문자열, 사칙연산

### 1. 직사각형 넓이 구하기

```python
def solution(dots):
    length1 = abs(dots[1][0] - dots[0][0]) if dots[1][1] == dots[0][0] else abs(dots[1][1] - dots[0][1])
    length2 = abs(dots[2][1] - dots[0][1]) if dots[1][1] == dots[0][0] else abs(dots[2][0] - dots[0][0])
    return length1 * length2
```

```python
def solution(dots):
    return abs(dots[1][0] - dots[0][0]) * abs(dots[2][1] - dots[0][1]) if dots[1][1] == dots[0][0] else abs(dots[1][1] - dots[0][1]) * abs(dots[2][0] - dots[0][0])
```



### 2. 캐릭터의 좌표

#### 문제

```
머쓱이는 RPG게임을 하고 있습니다. 게임에는 up, down, left, right 방향키가 있으며 각 키를 누르면 위, 아래, 왼쪽, 오른쪽으로 한 칸씩 이동합니다. 예를 들어 [0,0]에서 up을 누른다면 캐릭터의 좌표는 [0, 1], down을 누른다면 [0, -1], left를 누른다면 [-1, 0], right를 누른다면 [1, 0]입니다. 머쓱이가 입력한 방향키의 배열 keyinput와 맵의 크기 board이 매개변수로 주어집니다. 캐릭터는 항상 [0,0]에서 시작할 때 키 입력이 모두 끝난 뒤에 캐릭터의 좌표 [x, y]를 return하도록 solution 함수를 완성해주세요.
```

#### 테스트 케이스

```
keyinput = ["left", "left", "left", "right"]
board = [3, 3]
---
[0, 0]

keyinput = ["down", "up"]
board = [3, 3]
---
[0, 0]
```

#### 풀이

```python
def solution(keyinput, board):
    point = [0, 0]
    move = {"up": [0, 1], "down": [0, -1], "left": [-1, 0], "right": [1, 0]}
    board = [board[0]//2, board[1]//2]
    for key in keyinput:
        for i in range(2):
            if move[key][i] == 0:
                pass
            elif move[key][i] > 0 and point[i] > 0:
                if point[i] < board[i]:
                    point[i] += move[key][i]
            elif move[key][i] < 0 and point[i] < 0:
                if point[i] > -(board[i]):
                    point[i] += move[key][i]
            else:
                point[i] += move[key][i]
    return point
```

```python
def solution(keyinput, board):
    point = [0, 0]
    x_limit, y_limit = board[0]//2, board[1]//2
    for key in keyinput:
        if key == 'left' and point[0] > x_limit*(-1):
            point[0] -= 1
        if key == 'right' and point[0] < x_limit:
            point[0] += 1
        if key == 'down' and point[1] > y_limit*(-1):
            point[1] -= 1
        if key == 'up' and point[1] < y_limit:
            point[1] += 1
    return point
```



### 3. 최댓값 만들기 (2)

```python
def solution(numbers):
    numbers.sort(reverse=True)
    return numbers[0]*numbers[1] if numbers[0]*numbers[1] > numbers[-1]*numbers[-2] else numbers[-1]*numbers[-2]
```



### 4. 다항식 더하기

#### 문제

```
한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다. 다항식을 계산할 때는 동류항끼리 계산해 정리합니다. 덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때, 동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요. 같은 식이라면 가장 짧은 수식을 return 합니다.
```

#### 테스트케이스

```
polynomial = "1 + 1"
---
"2"
```

```
polynomial = "x + 7 + 15"
---
"x + 22"
```

```
polynomial = "x"
---
"x"
```

#### 풀이


```python
def solution(polynomial):
    add_list = polynomial.split(' + ')
    coef, const = 0, 0
    for add in add_list:
        if "x" in add:
            if len(add) == 1: 
                coef += 1
            else: 
                coef += int(add[:-1])
        else:
            const += int(add)
    if const == 0:
        if coef == 1: 
            answer = 'x'
        else: 
            answer = f'{coef}x'
    elif coef == 0:
        answer = f'{const}'
    else:
        if coef == 1: 
            answer = f'x + {const}'
        else: 
            answer = f'{coef}x + {const}'
    return answer
```

