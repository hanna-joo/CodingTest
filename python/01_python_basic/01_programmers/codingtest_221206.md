# LV1. 38-39

- 날짜 : 2022.12.06



### 1. k번째 수

```python
def solution(array, commands):
    return [sorted(array[x[0]-1:x[1]])[x[2]-1] for x in commands]
```



### 2. 숫자 문자열과 영단어

```python
def solution(s):
    nums = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 
            'four':'4', 'five':'5', 'six':'6', 'seven':'7', 
            'eight':'8', 'nine':'9', 'ten':'10'}
    for key in nums.keys():
        s = s.replace(key, nums.get(key))
    return int(s)
```

