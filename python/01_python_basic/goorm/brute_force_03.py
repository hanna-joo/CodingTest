# 수 이어 붙이기
# keyword : 완전 탐색, 순열, permutations()
# return : 10-99의 수를 가진 N개의 카드 중 만들 수 있는 가장 작은 수 출력

"""
1. 제한 조건
- 카드 개수 1 <= N <= 8
- 카드에 적힌 수 10 <= A(i) <= 99

2. 문제 분석
- 두 카드에 적힌 숫자의 일부가 같다면 겹쳐서 이어붙일 수 있다
- 카드를 이어붙여서 만들 수 있는 수 중 가장 작은 수 구하기
- N의 제한이 8 > 가능한 모든 배치 방법을 시도하는 방법 O(N * N!) 가능

3. 순열과 조합
- N개의 원소 중 K개의 원소 고르는 경우의 수
- 순열 : 순서 고려함
- 조합 : 순서 고려하지 않음
- 문제에서 선택하는 순서가 중요한지 판단

4. 순열 구현 : permute_1
- 재귀 + swap 사용
- 현재 n번 원소까지 순열의 위치를 고정했을 때, 
- n+1번 원소가 가질 수 있는 값들은 현재 배열에서 n+1번째 원소부터 N번 원소 사이 값들
- n+1 ~ N번째 원소들을 하나하나 현재 위치에 swap 해보면서 모든 순열을 순회

5. 순열 구현 : permute_2
- 원래 배열의 원소는 그대로 두기
- 재귀 + used 배열 사용
- used 배열 : 원소를 사용했는지 여부를 나타내는 배열
- 사전 순으로 모든 순열을 순회할 때는 배열 정렬 후 permute_2 방식 사용해야 함

6. 순열 라이브러리
- permutations(iterable, r)
- iterable : 반복 가능한 객체, 순열 뽑을 배열
- r : 뽑고자 하는 순열의 길이
"""

def permute_1(arr, n):
    if len(arr) == n:
        print(arr)
        return
    for i in range(n, len(arr)):
        arr[n], arr[i] = arr[i], arr[n]
        permute_1(arr, n + 1)
        arr[n], arr[i] = arr[i], arr[n]

    # [1, 2, 3] ... [3, 2, 1], [3, 1, 2]


def permute_2(arr):
    new = [0 for _ in range(len(arr))]
    used = [0 for _ in range(len(arr) + 1)]

    def permute(old, new, n):
        if len(old) == n:
            print(new)
            return
        for i in range(0, len(old)):
            if used[i]: continue
            used[i] = 1
            new[n] = old[i]
            permute(old, new, n+1)
            used[i] = 0

    permute(arr, new, 0)

    # [1, 2, 3] ... [3, 1, 2], [3, 2, 1]


def nums_merge_1(cards):
    new = [0 for _ in range(8)]
    used = [0 for _ in range(8)]
    global ans 
    ans = 1e18

    # 숫자 합치기
    def calculate(new):
        ret = new[0]
        for i in range(1, len(cards)):
            if ret % 10 == new[i] // 10:
                ret = ret * 10 + new[i] % 10
            else:
                ret = ret * 100 + new[i]
        return ret

    def permute(old, new, n):
        global ans
        # n번째 요소까지 다 정했을 때 최솟값을 ans에 저장
        if len(old) == n:
            ans = min(ans, calculate(new))
            return
        for i in range(0, len(old)):
            if used[i]: continue
            used[i] = 1
            new[n] = old[i]
            permute(old, new, n+1)
            used[i] = 0
    
    permute(cards, new, 0)
    return ans


def nums_merge_2(cards):
    from itertools import permutations
    
    n = len(cards)
    cards.sort()

    answer = 1e18
    for order in permutations(cards, n):
        cur = order[0]
        for i in range(1, n):
            # 현재 값의 1의 자리와 10의 자리가 같은지 확인
            if cur % 10 == order[i] // 10:
                cur = cur * 10 + order[i] % 10
            else:
                cur = cur * 100 + order[i]
        answer = min(answer, cur)

    return answer


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [[42, 31, 16, 19],
                  [87, 88]] # 1631942, 887

    for case in test_cases:
        print(permute_1(case, 0))
        print(permute_2(case))
        print(nums_merge_1(case))
        print(nums_merge_2(case))