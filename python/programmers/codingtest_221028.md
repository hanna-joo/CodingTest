# DAY 13

- 날짜 : 2022.10.28



### 1. 컨트롤 제트

```python
def solution(s):
    num_list = s.split(' ')
    sum_list = list()
    for i in num_list:
        if i != 'Z': sum_list.append(int(i))
        else : sum_list.pop()
    return sum(sum_list)
```



### 2. 배열 원소의 길이

```python
def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer
```

- 한 줄 코딩

```python
def solution(strlist):
    return [len(string) for string in strlist]
```



### 3. 중복된 문자 제거

```python
def solution(my_string):
    answer = ''
    for char in my_string:
        if char not in answer:
            answer += char
    return answer
```



### 4. 삼각형의 완성조건 (1)


```python
def solution(sides):
    sides.sort(reverse=True)
    if sides[0] < sides[1] + sides[2]: return 1
    else: return 2
```
