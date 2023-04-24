# DAY 15

- 날짜 : 2022.11.01



## 문자열, 해시, 배열, 수학

### 1. 영어가 싫어요

- `문자열.join()` 과 `문자열.split()` 사용

```python
def solution(numbers):
    number_dict = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for key in number_dict.keys():
        if key in numbers:
            numbers = number_dict[key].join(numbers.split(key)) 
    return int(numbers)
```

- `문자열.replace()` 사용

```python
def solution(numbers):
    number_dict = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for num in number_dict.keys():
        numbers = numbers.replace(num, number_dict[num])
    return int(numbers)
```



### 2. 인덱스 바꾸기

- 만일 string 을 수정하려고 하는 경우 다음과 같은 에러 발생

  - `TypeError: 'str' object does not support item assignment`

  - string 은 수정이 불가능한 자료형으로 리스트로 변환하여 수정

```python
def solution(my_string, num1, num2):
    str_list = list(my_string)
    str_list[num1], str_list[num2] = str_list[num2], str_list[num1]
    return ''.join(str_list)
```



### 3. 한 번만 등장한 문자

```python
def solution(s):
    once_char = list()
    more_char = list()
    for char in s:
        if char not in once_char and char not in more_char:
            once_char.append(char)
        elif char in once_char:
            once_char.remove(char)
            more_char.append(char)
    return ''.join(sorted(once_char))
```

- `리스트.count()` 사용

```python
def solution(s):
    return ''.join(sorted(filter(lambda x: s.count(x) == 1, s)))
```



### 4. 약수 구하기


```python
def solution(n):
    divisor = []
    for num in range(1, int(n**0.5)+1):
        if n%num == 0:
            divisor.extend([num, n/num])
    return sorted(list(set(divisor)))
```

