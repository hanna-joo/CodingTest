# 가장 가까운 세 사람의 심리적 거리 (s1, 36.426%)
# source : https://www.acmicpc.net/problem/20529
# keyword : 구현
# return : N명의 학생 중에 심리적 거리가 가장 가까운 세 학생 사이의 거리 출력
"""
1. 문제
- 세 사람의 심리적 거리 = (A,B)+(B,C)+(A,C)

2. 입력
- 테스트 케이스 개수 T (1<=T<=50)
    - 학생의 수 N (3<=N<=100,000)
    - 각 학생의 MBTI 유형

3. 로직 -> 시간 초과
- 2명 간의 거리를 나타내는 2차원 배열을 구한다
- 3개의 조합을 구한다
- 최솟값을 구한다

4. 로직 추가
- 귀류법
    - 비둘기 집 n개에서 n+1마리의 비둘기가 살고 있다면,
    - 최소 한 개의 비둘기 집에는 2마리 이상 살고 있을 것이다
- 사람이 33명이 16개의 mbti를 가진다면, 최소 3명은 같은 mbti이다
"""

import sys
from itertools import combinations


def solution_1(num, lst): # 52ms
    mbti = [*map(set, lst)]
    if num > 32:
        print(0)
        return

    dist = [[0 for _ in range(num)] for _ in range(N)]
    for i in range(num):
        for j in range(i, num):
            if i == j:
                continue
            dist[i][j] = len(mbti[i]-mbti[j])

    triple_dist = 8
    for x, y, z in combinations(range(num), 3):
        tmp = dist[x][y] + dist[y][z] + dist[x][z]
        if triple_dist > tmp:
            triple_dist = tmp
    print(triple_dist)


def solution_2(num, lst): # 364ms
    if num > 32:
        print(0)
        return

    dist = 8
    for combi in combinations(lst, 3):
        dist = min(dist, sum((c1!=c2) + (c2!=c3) + (c1!=c3) for c1, c2, c3 in zip(*combi)))
        if dist == 0:
            break
    print(dist)


if __name__ == "__main__":

    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        mbti = input().split()
        solution_1(N, mbti)
        solution_2(N, mbti)


"""
테스트케이스

5
3
ENTJ INTP ESFJ
4
ESFP ESFP ESFP ESFP
5
INFP INFP ESTP ESTJ ISTJ
5
ISTP ESTP ESTJ ISTP ISTP
4
INFP INFP INTP INFP

---결과 출력
8
0
4
0
0
"""
