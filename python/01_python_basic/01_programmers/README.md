# Today I Learned (TIL)
---
1. [String](#String)
2. [Float](#Float)
3. [List](#List)
4. [Set](#Set)
5. [함수](#함수)
6. [기타](#기타)
7. [날짜](#날짜)
---
221025 ~ 221114
## 논리 연산자
- A and B : A가 False면 A 반환, True면 B 반환
- A or B : A가 True면 A 반환, False면 B 반환
```python
print((2==1) and 'B') # False
print((1==1) and 'B') # B
print((1==1) or 'B') # True
print((2==1) or 'B') # B
```
## String
- string 은 수정이 불가능한 자료형
- `문자열.join(리스트)`
- `문자열.split(구분자)`
- `문자열.replace(교체대상 문자열, 교체할 문자열)`
- `문자열.lower()` / `문자열.upper()` / `문자열.islower()` / `문자열.isupper()`
- `문자열.isdecimal()` : 문자열이 int 형으로 변환 가능한지 검사
- `문자열.isdigit()` : 문자열이 숫자로 이루어져 있는지 검사(거듭제곱 특수문자도 인정)
- `문자열.isnumeric()` : 문자열이 수로 볼 수 있는지 검사(제곱근, 분수, 거듭제곱 특수문자 인정)
- `str.zfill(width)`
  - width(숫자)보다 문자열 자릿수가 적으면 그 앞부분을 0으로 채워줌
- `str.rjust(width, [, fillchar])`
  - 문자열을 오른쪽으로 정렬하고 왼쪽의 남은 공백(`width-문자열 자릿수`)을 특정 문자열로 채워줌, 기본값은 space
- `str.ljust(width, [, fillchar])`
  - 문자열을 왼쪽으로 정렬하고 오른쪽의 남은 공백(`width-문자열 자릿수`)을 특정 문자열로 채워줌, 기본값은 space
## Float
- `float.is_integer()`
  - 실수가 정수인지 아닌지 판단해서 bool 값 리턴
## List
- `list.count(문자열/숫자)` : 리스트 안의 해당 문자열/숫자의 개수 반환
- `list.pop(인덱스)` : 인덱스에 해당하는 값 리스트에서 빼서 반환
- slicing, indexing
  - slicing 은 Index Out Of Range 에도 작동
  - indexing 은 Index Out Of Range 에 에러 발생
## Set
- `set(iterable)`
  - iterable 객체의 unique 값을 얻을 때도 사용
  - 교집합, 합집합, 차집합 구할 때 유용
  - 교집합 : `s1&s2`, `s1.intersection(s2)`
  - 합집합 : `s1|s2`, `s1.union(s2)`
  - 차집합
    - `s1-s2`, `s1.difference(s2)`
    - `s2-s1`, `s2.difference(s1)`
  - 값 변경
    - `s1.add(value)`
    - `s1.update([val1, val2, ... ])`
    - `s1.remove(value)`
## 정렬
- `list.sort(reverse=True))`
  - 리스트에만 사용 가능
  - 원본 리스트 정렬시키고 반환 값 없음
  - 내림차순 정렬 시 reverse=True 추가
- `sorted(list, key = lambda x:(-x[0], abs(x[1]-x[0])))`
  - 리스트 외에도 iterable 객체에 대해 사용 가능
  - 새로운 정렬 리스트 반환
  - x[0] 내림차순으로 1차 정렬, 값이 동일한 경우 abs(x[1]-x[0]) 값으로 2차 정렬
## 함수
- itertools 함수 사용
  - `product('ABCD', repeat=2)` : 데카르트 곱, 중첩된 for 문과 동일
    - `AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD`
  - `permutations('ABCD', 2)` : r- 길이 튜플들, 모든 가능한 순서, 반복되는 요소 없음
    - `AB AC AD BA BC BD CA CB CD DA DB DC`
  - `combinations('ABCD', 2)` : r-길이 튜플들, 정렬된 순서, 반복되는 요소 없음
    - `AB AC AD BC BD CD`
  - `combinations_with_replacement('ABCD', 2)` : r- 길이 튜플들, 모든 가능한 순서, 반복되는 요소 있음
    - `AA AB AC AD BB BC BD CC CD DD`
```python
from itertools import combinations
def solution(nums):
    return sum(1 for combi in combinations(nums, 3) if sum(combi) == 0)
```
## 기타
- `eval(expression)`
  - 문자열로 이루어진 expression 을 python 코드로 인식하여 실행
- `try~except`
  - try 구문에서 에러 발생 시 에러 발생 구문 아래의 구문은 스킵
- lambda 함수
  - `(lambda x: True if x.count('p')==x.count('y') else False)(s.lower())`
- 소수 판별 알고리즘
  - [에라스토스테네스의 체](https://github.com/hanna-joo/CodingTest/blob/master/codingtest_221209.md)  
- `break`
  - 하나의 반복문(for/while) 에서 빠져나오기 위한 명령문
- `for i in range(a, b)`
  - a 가 b 보다 크면 for 문 미작동
## 날짜
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
