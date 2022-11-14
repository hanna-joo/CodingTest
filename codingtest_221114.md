# DAY 23-1

- 날짜 : 2022.11.14



## 배열, 정렬, 문자열

### 1. 특이한 정렬

```python
def solution(numlist, n):
    dist = [[num, abs(num-n)] for num in numlist]
    dist.sort(key = lambda x: (x[1], -x[0]))
    return [i[0] for i in dist]
```

```python
def solution(numlist, n):
    return sorted(numlist, key = lambda x: (abs(x-n), -x))
```



### 2. 등수 매기기

```python
def solution(score):
    avg = [(s[0]+s[1])/2 for s in score]
    avg.sort(reverse=True)
    rank = []
    for i in range(len(score)):
        rank.append(avg.index((score[i][0]+score[i][1])/2) + 1)
    return rank
```

