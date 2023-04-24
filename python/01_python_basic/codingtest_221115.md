# DAY 22-1, 23-2

- 날짜 : 2022.11.15



## dp, 수학, 조건문, 배열

### 1. 저주의 숫자 3

```python
def solution(n):
    num_3x = 0
    for _ in range(n):
        num_3x += 1
        while '3' in str(num_3x) or num_3x % 3 == 0:
            num_3x += 1
    return num_3x
```



### 2. 평행

- 기울기 구해서 비교
  - 삼각형의 변 길이로 하면 기울기가 -2, 2 인 경우에도 slope1 == slope2 라고 인식하기 때문에 기울기로 해야 함

```python
def solution(dots):
    for i in range(1, 4):
        idx = [1, 2, 3]
        idx.pop(idx.index(i))
        slope1 = (dots[0][0]-dots[i][0])/(dots[0][1]-dots[i][1])
        slope2 = (dots[idx[0]][0]-dots[idx[1]][0])/(dots[idx[0]][1]-dots[idx[1]][1])
        if slope1 == slope2:
            return 1
    return 0
```



## 배열, 정렬, 문자열

### 3. 옹알이 (1)

```python
def solution(babbling):
    answer = 0
    announce = ["aya", "ye", "woo", "ma"]
    for word in babbling:
        for ann in announce:
            if ann in word:
                word = word.replace(ann, ' ')
        if word.replace(' ', '') == '':
            answer += 1
    return answer
```



### 4. 로그인 성공?

```python
def solution(id_pw, db):
    for data in db:
        if id_pw[0] == data[0]:
            if id_pw[1] == data[1]: 
                return "login"
            else:
                return "wrong pw"
    return "fail"
```

