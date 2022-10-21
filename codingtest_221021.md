# DAY 8

- 날짜 : 2022.10. 21



### 1. 배열 자르기

```python
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]
```



### 2. 외계행성의 나이

```python
def solution(age):
    planet_num = 'abcdefghij'
    num_str = list(str(age))
    planet_age = ''.join([planet_num[int(i)] for i in num_str])
    return planet_age
```

- 아스키 코드 활용

```python
def solution(age):
	# a의 아스키코드 97
	return ''.join([chr(97+int(s)) for i in str(age)])
```



### 3. 진료순서 정하기

```python
def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)
    for i, val in enumerate(emergency):
        # 정렬된 응급도 리스트의 인덱스 찾아서 넣기
        emergency[i] = sorted_emergency.index(val) + 1
    return emergency
```



### 4. 순서쌍의 개수

- 1부터 n 까지 세기

```python
def solution(n):
    cnt = 0 # 약수 개수
    for num in range(1, n+1):
        if n % num == 0: 
            cnt += 1
    return cnt
```

- 1부터 n 의 제곱근까지만 세기
  - 앞 뒤 순서쌍이 존재하기 때문에 절반까지만 돌리기 위해 제곱근 활용
  - n 의 제곱근이 정수인 경우 순서쌍은 1개만 존재
    - 예) 100 의 제곱근은 10 으로 순서쌍이 (10, 10) 1개

```python
def solution(n):
    cnt = -1 if n**0.5 == int(n**0.5) else 0
    for num in range(1, int(n**0.5)+1):
        if n % num == 0:
            cnt += 2
    return cnt
```

