# LV1. 50

- 날짜 : 2022.12.14



### 1. 로또의 최고 순위와 최저 순위

```python
def solution(lottos, win_nums):
    result = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    zeros, matched = lottos.count(0), 0
    for num in lottos:
        if num in win_nums:
            matched += 1
    return [result.get(zeros+matched), result.get(matched)]
```

```python
def solution(lottos, win_nums):
    zeros, matched = lottos.count(0), 0
    for num in lottos:
        if num in win_nums:
            matched += 1
    return [min(6, 7-(zeros+matched)), min(6, 7-matched)]
```

