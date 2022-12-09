# LV1. 44-45

- 날짜 : 2022.12.09



### 1. 소수 찾기

- continue 활용
  - 짝수 중에서는 2만 소수이므로 나머지는 소수 판별 대상에서 제외

```python
def divided(num):
    for divisor in range(3, int(num**0.5)+1, 2):
        if divisor != num and num % divisor == 0:
            return True
        
def solution(n):
    cnt = 1
    for num in range(3, n+1, 2):
        if divided(num):
            continue
        cnt += 1
    return cnt
```

- break 문 활용
  - break 문은 하나의 반복문(for, while) 에서 빠져나올 때 사용
  - for문의 range(a, b) 에서 b 가 a 보다 작은 경우 for문이 작동하지 않음


```python
def solution(n):
    cnt = 1
    for num in range(3, n+1, 2):
        cnt += 1
        for divisor in range(3, int(num**0.5)+1, 2):
            if divisor != num and num % divisor == 0:
                cnt -= 1
                break
    return cnt
```

```
테스트 1 〉	통과 (1948.02ms, 10.4MB)
테스트 2 〉	통과 (2047.90ms, 10.4MB)
테스트 3 〉	통과 (2123.39ms, 10.4MB)
테스트 4 〉	통과 (1898.84ms, 10.4MB)
```

- 에라토스테네스의 체 원리
  - 특정 수의 소수 여부 확인할 때에는 특정한 숫자의 제곱근까지만 약수 여부를 검증하면 O(N^1/2) 의 시간 복잡도로 빠르게 구할 수 있음
    - N이라는 숫자를 A로 나누면 B라는 몫이 생기는데 A, B 둘 중 하나는 무조건 N 제곱근 이하

  - 에라토스테네스의 체란 : 소수 판별 알고리즘으로 가장 먼저 소수를 판별할 범위만큼 배열을 할당하여 해당하는 값을 넣어주고, 이후에 하나씩 지워가는 방법
  - 에라토스테네스의 체 원리
    - 배열을 생성하여 초기화
    - 2부터 시작해서 특정 수의 배수에 해당하는 수를 모두 지움
      - 자기 자신은 지우지 않음
      - 이미 지워진 수는 건너뜀

    - 2부터 시작해서 남아있는 수를 모두 출력

  - **차집합이 가능한 set 자료형** 이용


```python
def solution(n):
    prime = set(range(2, n+1))
    for i in range(2, int(n**0.5)+1):
        if i in prime:
        	prime -= set(range(i+i, n+1, i))
    return len(prime)
```

```
테스트 1 〉	통과 (279.42ms, 116MB)
테스트 2 〉	통과 (247.41ms, 115MB)
테스트 3 〉	통과 (278.54ms, 116MB)
테스트 4 〉	통과 (251.21ms, 115MB)
```



### 2. 모의고사

- 수포자의 답지를 먼저 만들고 채점

```python
def supo(pattern, length):
    a, b = divmod(length, len(pattern))
    return pattern*a + pattern[:b]

def solution(answers):
    supo1 = supo([1, 2, 3, 4, 5], len(answers))
    supo2 = supo([2, 1, 2, 3, 2, 4, 2, 5], len(answers))
    supo3 = supo([3, 3, 1, 1, 2, 2, 4, 4, 5, 5], len(answers))
    scores = [0, 0, 0]
    for i in range(len(answers)):
        if supo1[i] == answers[i]: scores[0] += 1
        if supo2[i] == answers[i]: scores[1] += 1
        if supo3[i] == answers[i]: scores[2] += 1
    return [i+1 for i in range(len(scores)) if scores[i]==max(scores)]
```

- 수포자의 답지를 만들지 않고 인덱싱으로 채점

```python
def solution(answers):
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]
    for idx, answer in enumerate(answers):
        if supo1[idx%len(supo1)] == answer: scores[0] += 1
        if supo2[idx%len(supo2)] == answer: scores[1] += 1
        if supo3[idx%len(supo3)] == answer: scores[2] += 1
    return [i+1 for i in range(len(scores)) if scores[i]==max(scores)]
```

- 일반화

```python
def solution(answers):
    patterns = [[1, 2, 3, 4, 5], 
                [2, 1, 2, 3, 2, 4, 2, 5],
                [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    scores = [0] * len(patterns)
    for i, pattern in enumerate(patterns):
        for j, answer in enumerate(answers):
            if pattern[j%len(pattern)] == answer:
                scores[i] += 1
    return [i+1 for i in range(len(scores)) if scores[i]==max(scores)]
```
