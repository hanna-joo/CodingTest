# DAY 25-1

- 날짜 : 2022.11.18



## 시뮬레이션, 조건문, 수학

### 1. 문자열 밀기

```python
def solution(A, B):
    cnt = 0
    while A != B:
        A = A[-1] + A[:-1]
        cnt += 1
        if cnt == len(A):
            return -1
    return cnt
```

```python
def solution(A, B):
    idx = (A+A).find(B)
    return len(A)-idx if idx > 0 else idx
```



### 2. 종이 자르기

```python
def solution(M, N):
    return M*N-1
```
