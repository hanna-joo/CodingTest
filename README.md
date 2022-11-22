# Today I Learned (TIL)

221025 ~ 221114
- list
  - `list.count(문자열/숫자)` : 리스트 안의 해당 문자열/숫자의 개수 반환
  - `list.pop(인덱스)` : 인덱스에 해당하는 값 리스트에서 빼서 반환
- 문자열
  - string 은 수정이 불가능한 자료형
  - `문자열.join(리스트)`
  - `문자열.split(구분자)`
  - `문자열.replace(교체대상 문자열, 교체할 문자열)`
  - `문자열.lower()` / `문자열.upper()` / `문자열.islower()` / `문자열.isupper()`
  - `문자열.isdecimal()` : 문자열이 int 형으로 변환 가능한지 검사
  - `문자열.isdigit()` : 문자열이 숫자로 이루어져 있는지 검사(거듭제곱 특수문자도 인정)
  - `문자열.isnumeric()` : 문자열이 수로 볼 수 있는지 검사(제곱근, 분수, 거듭제곱 특수문자 인정)
- `eval(expression)`
  - 문자열로 이루어진 expression 을 python 코드로 인식하여 실행
- slicing, indexing
  - slicing 은 Index Out Of Range 에도 작동
  - indexing 은 Index Out Of Range 에 에러 발생
- `try~except`
  - try 구문에서 에러 발생 시 에러 발생 구문 아래의 구문은 스킵
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
- `list.sort(reverse=True))`
  - 리스트에만 사용 가능
  - 원본 리스트 정렬시키고 반환 값 없음
  - 내림차순 정렬 시 reverse=True 추가
- `sorted(list, key = lambda x:(-x[0], abs(x[1]-x[0])))`
  - 리스트 외에도 iterable 객체에 대해 사용 가능
  - 새로운 정렬 리스트 반환
  - x[0] 내림차순으로 1차 정렬, 값이 동일한 경우 abs(x[1]-x[0]) 값으로 2차 정렬
  
- lambda 함수
  - `(lambda x: True if x.count('p')==x.count('y') else False)(s.lower())`
- `float.is_integer()`
  - 실수가 정수인지 아닌지 판단해서 bool 값 리턴
 
