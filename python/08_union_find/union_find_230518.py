# problem source : https://www.acmicpc.net/problem/1717
# return : union 연산 후 a와 b가 같은 집합에 포함되어 있는지 출력

import sys
from collections import deque
sys.setrecursionlimit(100000)
input = sys.stdin.readline

# 원소 개수, 연산 개수
elem_cnt, cal_cnt = map(int, input().split())
elems = list(range(elem_cnt+1))

# find() : 대표 노드 찾기 + 경로 압축
def find(a):
    # a가 대표 노드인지 확인
    # yes : 재귀함수 종료
    if a == elems[a]:
        return a
    # no : a값의 index로 이동
    else:
        # 거치는 노드 값 대표 노드로 변경
        elems[a] = find(elems[a])
        return elems[a]

# union() : 두 노드의 대표 노드 연결
def union(a, b):
    # a와 b의 대표 노드 찾기
    root_a, root_b = find(a), find(b)
    # 대표 노드끼리 연결
    if root_a != root_b:
        root = min(root_a, root_b)
        elems[root_a], elems[root_b] = root, root
        #elems[root_b] = root_a

# same_group() : a와 b가 같은 그룹에 속해있는지 확인
def same_group(a, b):
    # a와 b의 대표 노드 찾기
    root_a, root_b = find(a), find(b)
    if root_a == root_b:
        return True
    return False

for _ in range(cal_cnt):
    cal, a, b = map(int, input().split())
    if cal == 0:
        union(a, b)
    else:
        if same_group(a, b):
            print('YES')
        else:
            print('NO')
