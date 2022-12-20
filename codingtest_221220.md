# LV1. 54

- 날짜 : 2022.12.20



### 1. 가장 가까운 같은 글자

**문제 설명**

```
문자열 `s`가 주어졌을 때, `s`의 각 위치마다 자신보다 앞에 나왔으면서, 자신과 가장 가까운 곳에 있는 같은 글자가 어디 있는지 알고 싶습니다.예를 들어, `s`="banana"라고 할 때,  각 글자들을 왼쪽부터 오른쪽으로 읽어 나가면서 다음과 같이 진행할 수 있습니다.

- b는 처음 나왔기 때문에 자신의 앞에 같은 글자가 없습니다. 이는 -1로 표현합니다.
- a는 처음 나왔기 때문에 자신의 앞에 같은 글자가 없습니다. 이는 -1로 표현합니다.
- n은 처음 나왔기 때문에 자신의 앞에 같은 글자가 없습니다. 이는 -1로 표현합니다.
- a는 자신보다 두 칸 앞에 a가 있습니다. 이는 2로 표현합니다.
- n도 자신보다 두 칸 앞에 n이 있습니다. 이는 2로 표현합니다.
- a는 자신보다 두 칸, 네 칸 앞에 a가 있습니다. 이 중 가까운 것은 두 칸 앞이고, 이는 2로 표현합니다.

따라서 최종 결과물은 [-1, -1, -1, 2, 2, 2]가 됩니다.

문자열 `s`이 주어질 때, 위와 같이 정의된 연산을 수행하는 함수 solution을 완성해주세요.
```

**제한 사항**

```
- 1 ≤ `s`의 길이 ≤ 10,000
    - `s`은 영어 소문자로만 이루어져 있습니다.
```

**문제 풀이**

- 문자열의 위치를 dict 자료형에 담기

```python
def solution(s):
    chars, result = dict(), list()
    for idx, char in enumerate(s):
        if chars.get(char) == None:
            result.append(-1)
            chars[char] = [idx]
        else:
            result.append(idx - chars[char][-1])
            chars[char].append(idx)
    return result
```

- find() 함수 활용하기

```python
def solution(s):
    result = list()
    for now_idx in range(len(s)):
        recent_idx = s.find(s[now_idx])
        if now_idx == recent_idx:
            result.append(-1)
        else:
            result.append(now_idx - recent_idx)
            s = s.replace(s[recent_idx], ' ', 1)
    return result
```
