# problem : https://www.acmicpc.net/problem/1966
# keyword : 구현
# return : 각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력

"""
1. 문제
- 문서의 중요도 확인
- 중요도가 높은 문서가 하나라도 있다면 현재 문서 queue 맨 뒤에 배치

2. 입력 및 제한
- 테스트케이스 수
- 문서의 개수 N, 궁금한 문서의 위치 M
- N개의 문서 중요도
- 1<=중요도<=9, 중요도 중복 가능

3. 로직 1
- 중요도 정렬해서 별도로 저장한다
- 인쇄한 수(cnt), 궁금한 문서 위치(idx)
- 가장 높은 중요도를 발견할 때까지 뒤로 보낸다
    - 뒤로 보내는 게 idx이면 idx = len()-1
    - 뒤로 보내는 게 idx이 아니면 idx -= 1
- 가장 높은 중요도 발견하면 인쇄한다
    - cnt += 1
    - 인쇄한 수가 idx이면 종료
    - 인쇄한 수가 idx이 아니면 idx -= 1

4. 로직 2
- 일단 문서를 하나 빼고 idx -= 1
- 뺀 문서가 가장 높은 중요도를 가졌다면 idx 확인한다
    - cnt += 1
    - 0보다 작으면 종료
- 뺀 문서가 가장 높은 중요도가 아니라면 뒤로 보내고 idx 확인한다
    - 0보다 작으면 idx = len() - 1
"""

import sys
from collections import deque
input = sys.stdin.readline

def print_target_1(idx, docs):
    priority = deque(sorted(docs, reverse=True))

    cnt = 0
    while True:
        first = priority.popleft()
        while docs[0] != first:
            docs.append(docs.popleft())
            if idx == 0:
                idx = len(docs) - 1
            else:
                idx -= 1
        cnt += 1
        if idx == 0:
            break
        else:
            docs.popleft()
            idx -= 1

    return cnt

def print_target_2(idx, docs):
    cnt = 0
    while docs:
        first = max(docs)
        front = docs.popleft()
        idx -= 1

        if first == front:
            cnt += 1
            if idx < 0:
                break
        else:
            docs.append(front)
            if idx < 0:
                idx = len(docs) - 1
    return cnt


case_cnt = int(input())
for _ in range(case_cnt):
    doc_cnt, idx = map(int, input().split())
    docs = deque(map(int, input().split()))
    print(print_target_1(idx, docs)) # 64ms
    print(print_target_2(idx, docs)) # 70ms

"""
테스트 케이스 : 1 2 5

3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
"""