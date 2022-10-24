# DAY 9

- 날짜 : 2022.10.24



### 1. 개미군단

```python
def solution(hp):
    return hp//5 + (hp%5)//3 + (hp%5)%3
```



### 2. 모스부호 (1)

```python
def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    char_list = letter.split(' ')
    return ''.join([morse[i] for i in char_list])
```



### 3. 가위바위보

```python
def solution(rsp):
    answer = ''
    for given in rsp:
        if given == "2": answer += "0"
        elif given == "0": answer += "5"
        else: answer += "2"
    return answer
```

- 사전 활용

```python
def solution(rsp):
    answer = ''
    win_dict = {'2': '0', '0': '5', '5': '2'}
    for given in rsp: answer += win_dict[given]
    return answer
```

- map 함수 활용

```python
def solution(rsp):
    return ''.join(map(lambda x : '5' if x=='0' else '0' if x=='2' else '2', rsp))
```



### 4. 구슬을 나누는 경우의 수

- 서로 다른 n개 중 m개를 뽑는 경우의 수
  - `n! / (n-m)! * m!`


```python
def solution(balls, share):
    top = 1
    bottom = 1
    for i in range(1, balls+1): top*=i
    for i in range(1, share+1): bottom*=i
    for i in range(1, balls-share+1): bottom*=i
    
    return top_multi / bottom_multi
```



---

### iterable 과 iterator?

- **iterator**
  - 순서대로 다음 값을 리턴할 수 있는 객체
  - 자체적으로 내장하고 있는 `__next__` 메소드를 통해 다음 값 가져올 수 있음
- **iterable**
  - 내부 요소를 하나씩 리턴할 수 있는 객체
  - 대표적으로 collection 타입과 sequence 타입의 객체
    - collection 타입 : list, tuple, set, dictionary 여러 개의 요소를 갖는 데이터 타입
    - sequence 타입 : list, tuple, range, str 과 같이 순서가 존재하는 데이터 타입 
  - `__next__` 메소드가 존재하지 않음
  - `iter(변수)` 함수 또는 `변수.__iter__()`를 활용해 iterator 로 변경 가능

```python
iterator1 = iter([1, 2, 3])
print(type(iterator1))

iterator2 = [a, b, c].__iter__()
print(type(iterator2)) 		# list_iterator
print(iterator2.__next__()) # a 출력
print(iterator2.__next__()) # b 출력
print(iterator2.__next__()) # c 출력
print(iterator2.__next__()) # StopIteration Exception 발생
```

- **sequence**

  - `__len()__`, `__getitem()` 메소드를 가지고 있는 객체

  - list, tuple 등 python 기본 iterable 타입들은 sequence 이자 iterable

- for 문은 내부적으로 iterator 을 생성하여 동작
  - for 문을 돌리는 객체가 iterable
    -  `__iter__` 메소드로 iterator 생성
    - `__next__` 메소드를 이용해 순회를 돔
    - `StopIteration` 예외가 발생하면 순회를 마침

- `map(function, iterable, ...)`
  - iterator 반환
  - iterable 객체의 모든 요소에 function 을 적용한 iterator
- `range(start, stop)`
  - 함수라기보다는 range() 는 사실상 변경 불가능한 sequence 타입
- `str.join(iterable)`
  - 공식문서에는 iterable 을 넣으라고 했지만 iterator 을 반환하는 map() 함수도 적용이 되었음
