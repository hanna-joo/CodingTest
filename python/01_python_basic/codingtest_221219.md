# LV1. 53

- 날짜 : 2022.12.19



### 1. 완주하지 못한 선수

**문제 설명**

```
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
```

**제한 사항**

```
- 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
- completion의 길이는 participant의 길이보다 1 작습니다.
- 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
- 참가자 중에는 동명이인이 있을 수 있습니다.
```

**문제 풀이**

- 해시 사용

```python
def solution(participant, completion):
    hash_dict, hash_sum = dict(), 0
    
    for part in participant:
        hash_dict[hash(person)] = person
        hash_sum += hash(person)
        
    for comp in completion:
        hash_sum -= hash(person)
        
    return hash_dict[hash_sum]
```

- 해시 미사용 (효율성 통과)

```python
def solution(participant, completion):
    participant, completion = sorted(participant), sorted(completion)
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]
```

- 해시 미사용 (효율성 탈락)

```python
def solution(participant, completion):
    for person in completion:
        participant.remove(person)
    return participant[0]
```

- collections Counter 사용

```python
from collections import Counter
def solution(participant, completion):
    uncomplete = Counter(participant) - Counter(completion)
    return list(uncomplete.keys())[0]
```



---

### collections.Counter(iterable)

- `Counter(iterable)` : key 가 iterable 의 요소, value 가 iterable 의 count 인 딕셔너리 반환

```python
from collections import Counter

participant = ["mislav", "stanko", "mislav", "ana", "stanko"]
completion = ["stanko", "ana", "mislav", "mislav"]

print(Counter(participant))
print(Counter(completion))
---
Counter({'mislav': 2, 'stanko': 2, 'ana': 1})
Counter({'mislav': 2, 'stanko': 1, 'ana': 1})
```

- 배열 간의 차 구할 수 있음

```python
uncomplete = Counter(participant) - Counter(completion)

print(uncomplete)
---
Counter({'stanko': 1})
```

- 배열의 키 값 가져오기

```python
print(Counter(participant).keys())
---
dict_keys(['mislav', 'stanko', 'ana'])
```

```python
print(list(Counter(participant).keys()))
---
['mislav', 'stanko', 'ana']
```

