# ATM (s4, 68.120%)
# source : https://www.acmicpc.net/problem/11399
# keyword : 정렬
# return : 각 사람이 돈 인출하는데 필요한 시간의 합 최솟값 출력

"""
1. 문제
- 각 사람이 돈 인출하는데 걸리는 시간이 주어졌을 때, 
- 각 사람이 돈 인출하는데 필요한 시간의 합 최솟값

2. 입력 및 제한
- 사람의 수 N (1<=N<=1000)
- 각 사람이 돈 인출하는데 걸리는 시간 Pi (1<=Pi<=1000)

3. 로직
- 걸리는 시간이 짧은 사람 순서대로 인출하면 최솟값 
"""


def solution_1(num, arr):
    prev, total = 0, 0
    for tm in arr:
        prev += tm
        total += prev
    print(total)


def solution_2(num, arr):
    total = 0
    # 맨 마지막에 있는 시간은 1번 더함
    # 맨 앞에 있는 시간은 N번 더함
    for i in range(num):
        total += arr.pop() * (i+1)
    print(total)


if __name__ == "__main__":

    import sys
    input = sys.stdin.readline

    N = int(input())
    P = sorted(map(int, input().split()))

    solution_1(N, P)
    solution_2(N, P)


"""
테스트 케이스 : 32

5
3 1 4 3 2
"""