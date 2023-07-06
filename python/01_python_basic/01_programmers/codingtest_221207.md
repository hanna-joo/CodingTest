# LV1. 40-41

- 날짜 : 2022.12.07



### 1. 삼총사

```python
def solution(nums):
    cnt = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if sum([nums[i], nums[j], nums[k]]) == 0 :
                    cnt += 1
    return cnt
```

- itertools 함수 사용

  - `product('ABCD', repeat=2)` : 데카르트 곱, 중첩된 for 문과 동일

    - ```
      AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
      ```

  - `permutations('ABCD', 2)` : r- 길이 튜플들, 모든 가능한 순서, 반복되는 요소 없음

    - ```python
      AB AC AD BA BC BD CA CB CD DA DB DC
      ```

  - `combinations('ABCD', 2)` : r-길이 튜플들, 정렬된 순서, 반복되는 요소 없음

    - ```python
      AB AC AD BC BD CD
      ```

  - `combinations_with_replacement('ABCD', 2)` : r- 길이 튜플들, 모든 가능한 순서, 반복되는 요소 있음

    - ```python
      AA AB AC AD BB BC BD CC CD DD
      ```

```python
from itertools import combinations
def solution(nums):
    return sum(1 for combi in combinations(nums, 3) if sum(combi) == 0)
```

- 아래 풀이는 [0, 0, 0, 0] 케이스일 때 안 됨
  - 같은 값을 가진 경우 겹치기 때문에 잡지 못 함

```python
def solution(nums):
    sets = list()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            key = -(nums[i] + nums[j])
            if key in nums:
                key_idx = nums.index(key)
                if key_idx!=i and key_idx!=j:
                    new = sorted([i, j, key_idx])
                    if new not in sets:
                        sets.append(new)
    return len(sets)
```



### 2. 두 개 뽑아서 더하기

- set 자료형 활용

```python
def solution(numbers):
    sets = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            sets.add(numbers[i] + numbers[j])
    return sorted(list(sets))
```

- 한 줄 코딩

```python
def solution(nums):
    return sorted(list(set([nums[i]+nums[j] for i in range(len(nums)) for j in range(i+1, len(nums))])))
```

- itertools 함수 사용

```python
from itertools import combinations
def solution(nums):
    return sorted(list(set([sum(combi) for combi in combinations(nums, 2)])))
```

