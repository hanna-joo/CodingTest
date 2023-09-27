# 나무 자르기 (s2, 25.906%)
# source : https://www.acmicpc.net/problem/2805
# keyword : 이진탐색
# return : 적어도 M미터의 나무를 가져가기 위해 절단기 설정 높이 최댓값 출력

"""
1. 문제
- 1줄의 나무를 자를 때 절단기 높이를 H로 지정
    - 20, 15, 10, 17 -> H = 15 -> 15, 15, 10, 15
    - 상근이는 총길이가 7미터(5+2)인 나무를 들고 집에 감
- 적어도 M미터의 나무를 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값 출력

2. 입력 및 제한
- 나무의 수 N, 필요한 나무 길이 M (1<=N<=1,000,000, 1<=M<=2,000,000,000)
- 나무의 높이 (M<=높이의 합)

3. 로직
- 이진탐색 -> O(logN)
"""


N, M = map(int, input().split())
trees = [*map(int, input().split())]
s, e = 1, max(trees)

while s <= e:
    cut = (s + e) // 2
    total = 0
    for tree in trees:
        if tree > cut:
            total += (tree - cut)
    if total >= M:
        s = cut+1
    else:
        e = cut-1

print(e)


"""
테스트케이스

4 7
20 15 10 17
---
15

5 20
4 42 40 26 46
---
36

2 10
5 5
---
0

2 3
5 5
---
3

3 11
5 5 5
---
1
"""