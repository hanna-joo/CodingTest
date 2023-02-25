# LV1. 42-43

- 날짜 : 2022.12.08



### 1. 2016년

- datetime 함수 사용
  - `datetime(2022,12,08).strftime()` : 문자열로 반환
    - `%Y` : 앞의 빈자리를 0으로 채우는 4자리 연도
    - `%m` : 앞의 빈자리를 0으로 채우는 2자리 월
    - `%d` : 앞의 빈자리를 0으로 채우는 2자리 일
    - `%H` : 앞의 빈자리를 0으로 채우는 24시간 형식 2자리 시간
    - `%M` : 앞의 빈자리를 0으로 채우는 2자리 분
    - `%S` : 앞의 빈자리를 0으로 채우는 2자리 초
    - `%A` : 영어로 된 요일 문자열
    - `%a` : 영어로 된 요일(요약어) 문자열
    - `%B` : 영어로 된 월 문자열

```python
from datetime import datetime
def solution(a, b):
    return datetime(2016, a, b).strftime('%a').upper()
```

- datetime 함수 미사용

```python
def solution(a, b):
    # 2016년 2월은 29일까지
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 2016-01-01 은 금요일
    week_days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return week_days[sum(month_days[:a-1], b)%7 - 1]
```



### 2. 폰켓몬

```python
def solution(nums):
    return (lambda x, y: x if x<=y else y)(len(nums)//2, len(set(nums)))
```

```python
def solution(nums):
    return min(len(nums)//2, len(set(nums)))
```
