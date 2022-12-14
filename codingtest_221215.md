# LV1. 51

- 날짜 : 2022.12.15



### 1. 푸드 파이트 대회

```python
def solution(food):
    array = ''
    for calorie, quantity in enumerate(food):
        if quantity > 1:
            array += f'{calorie}'*(quantity//2)
    return array+'0'+array[::-1]
```

- 두 줄 코딩

```python
def solution(food):
    array = ''.join(str(i)*(j//2) for i, j in enumerate(food) if j>1)
    return array+'0'+array[::-1]
```

