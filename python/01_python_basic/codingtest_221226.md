# LV1. 59

- 날짜 : 2022.12.26



### 1. 숫자 짝꿍

**문제 설명**

```
두 정수 `X`, `Y`의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다(단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용합니다). `X`, `Y`의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다. `X`, `Y`의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.

예를 들어, `X` = 3403이고 `Y` = 13203이라면, `X`와 `Y`의 짝꿍은 `X`와 `Y`에서 공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330입니다. 다른 예시로 `X` = 5525이고 `Y` = 1255이면 `X`와 `Y`의 짝꿍은 `X`와 `Y`에서 공통으로 나타나는 2, 5, 5로 만들 수 있는 가장 큰 정수인 552입니다(`X`에는 5가 3개, `Y`에는 5가 2개 나타나므로 남는 5 한 개는 짝 지을 수 없습니다.)두 정수 `X`, `Y`가 주어졌을 때, `X`, `Y`의 짝꿍을 return하는 solution 함수를 완성해주세요.
```

**제한 사항**

```
- 3 ≤ `X`, `Y`의 길이(자릿수) ≤ 3,000,000입니다.
- `X`, `Y`는 0으로 시작하지 않습니다.
- `X`, `Y`의 짝꿍은 상당히 큰 정수일 수 있으므로, 문자열로 반환합니다.
```

**입출력 예**

| X       | Y        | result |
| ------- | -------- | ------ |
| "100"   | "2345"   | "-1"   |
| "100"   | "203045" | "0"    |
| "100"   | "123450" | "10"   |
| "12321" | "42531"  | "321"  |
| "5525"  | "1255"   | "552"  |

**문제 풀이**

- 아래 코드의 성공 이유
  - 기존에 "000" 을 "0" 으로 만들기 위해 사용한 str(int()) 가 생각보다 많은 시간 소요
  - 해당 부분을 다른 코드로 변경했더니 시간 초과 에러 통과

```python
from collections import Counter
def solution(X, Y):
    X, Y = Counter(X), Counter(Y)
    common = ''
    for num in X.keys():
        if num in Y.keys():
            common += num * min(X[num], Y[num])
    if common:
        if common.count("0") == len(common):
            return "0"
        else:
            return ''.join(sorted(common, reverse=True))
    else:
        return "-1"
```

```
테스트 11 〉	통과 (395.00ms, 53.5MB)
테스트 12 〉	통과 (427.35ms, 51.1MB)
테스트 13 〉	통과 (364.66ms, 53.5MB)
테스트 14 〉	통과 (428.54ms, 51.1MB)
테스트 15 〉	통과 (409.27ms, 46.5MB)
테스트 16 〉	통과 (0.03ms, 10.3MB)
테스트 17 〉	통과 (0.02ms, 10.3MB)
테스트 18 〉	통과 (0.02ms, 9.96MB)
테스트 19 〉	통과 (0.02ms, 10MB)
```

```python
def solution(X, Y):
    Y, common = list(Y), ''
    for num in set(X):
        if num in Y:
            common += str(num) * min(X.count(num), Y.count(num))
    if common:
        if common.count("0") == len(common):
            return "0"
        else:
            return ''.join(sorted(common, reverse=True))
    else:
        return "-1"
```

```
테스트 11 〉	통과 (583.96ms, 76.4MB)
테스트 12 〉	통과 (572.64ms, 78.3MB)
테스트 13 〉	통과 (558.30ms, 74MB)
테스트 14 〉	통과 (561.22ms, 76.2MB)
테스트 15 〉	통과 (558.55ms, 78.4MB)
테스트 16 〉	통과 (0.01ms, 10MB)
테스트 17 〉	통과 (0.01ms, 10.2MB)
테스트 18 〉	통과 (0.01ms, 10.3MB)
테스트 19 〉	통과 (0.01ms, 10MB)
```

```python
def solution(X, Y):
    common = ''
    for i in range(9,-1,-1) :
        str_num = str(i)
        common += (str_num * min(X.count(str_num), Y.count(str_num)))
    if common == '':
        return "-1"
    elif common.count("0") == len(common):
        return "0"
    else:
        return common
```

```
테스트 11 〉	통과 (82.21ms, 27.5MB)
테스트 12 〉	통과 (81.78ms, 27.8MB)
테스트 13 〉	통과 (81.06ms, 27.6MB)
테스트 14 〉	통과 (82.29ms, 27.8MB)
테스트 15 〉	통과 (83.54ms, 27.6MB)
```

- 실행시간 초과

```python
# str(int()) 수정해도 remove() 때문에 불가
def solution(X, Y):
    Y, common = list(Y), list()
    for num in X:
        if num in Y:
            common.append(num)
            Y.remove(num)
    if common:
        return str(int(''.join(sorted(common, reverse=True))))
    else:
        return "-1"
```

```python
def solution(X, Y):
    Y, common = list(Y), ''
    for num in set(X):
        if num in Y:
            common += str(num) * min(X.count(num), Y.count(num))
    if common:
        return str(int(''.join(sorted(common, reverse=True))))
    else:
        return "-1"
```

```python
from collections import Counter
def solution(X, Y):
    X, Y = Counter(X), Counter(Y)
    common = ''
    for num in X.keys():
        if num in Y.keys():
            common += num * min(X[num], Y[num])
    if common:
        return str(int(''.join(sorted(common, reverse=True))))
    else:
        return "-1"
```

