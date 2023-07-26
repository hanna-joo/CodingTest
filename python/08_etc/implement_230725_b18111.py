# problem : https://www.acmicpc.net/problem/18111
# keyword : dfs/bfs
# return : 땅 고르기 작업에 걸리는 최소 시간과 땅의 높이 출력

"""
1. 문제
- 땅 고르기 작업 = 땅 높이 일정하게 만들기
- 블록 제거 : (i, j) 맨 위 블록 빼서 인벤토리에 저장 -> 2초 소요
- 블록 추가 : 인벤토리에서 블록 꺼내서 (i, j) 위치에 추가 -> 1초 소요

2. 입력 및 제한
- 세로 n, 가로 m, 저장된 블럭 b개
- 0 <= 땅의 높이 <= 256

3. 경우의 수
- 추가하는 경우
- 인벤토리에 부족한 경우
- 제거하는 경우

4. 수정 전 로직
(1) 가장 높은 높이(max)와 가장 낮은 높이(min) 파악
(2) base = range(min, max+1)
(3) base에 높이 맞추기
(4) 땅 하나하나 탐색하기
(4-1) base랑 같으면, 넘어가기
(4-2) base보다 작으면, 블럭 추가(1초) -> 부족하면 아예 넘어가기
(4-3) base보다 크면, 블럭 제거(2초)
(5) 최솟값 업데이트

5. 로직 약점
- (1)번 : 시간이 꽤 소요되므로 생략 -> base = range(257)
- (4-1)번 : 없어도 됨 -> 생략
- (4-2)번 : 인벤토리에 블럭이 없어도 다른 칸에서 블럭을 가져다 쓸 수 있음 -> 탐색 끝까지 한 후에 인벤토리 체크

6. 수정 후 로직
(1) base = range(257)
(2) base에 높이 맞추기
(3) 땅 하나하나 탐색하기
(3-1) base보다 작으면, 블럭 추가(1초)
(3-2) base보다 크면, 블럭 제거(2초)
(4) 탐색 후 (필요한 블럭 수 >= 가용 가능한 블럭 수) 인 경우만 시간 계산
(5) 최솟값 업데이트
"""

# 수정 전 로직
def match_base_wrong(base):
    # 인벤토리 초기화
    global b
    inventory = b
    put_b, remove_b = 0, 0
    for i in range(n):
        for j in range(m):
            cur = ground[i][j]
            # (4-1)
            if (cur == base):
                continue
            # (4-2)
            if (cur < base):
                # 인벤토리 없는 경우 작업 중지
                if inventory < (base-cur):
                    return -1
                inventory -= (base-cur)
                put_b += (base-cur)
            # (4-3)
            else:
                inventory += (cur-base)
                remove_b += (cur-base)
            
    return put_b + (2 * remove_b)

# 수정 후 로직
def match_base(base):
    global b
    put_b, remove_b = 0, 0
    # (3) 땅 하나하나 탐색하기
    for i in range(n):
        for j in range(m):
            cur = ground[i][j]
            # (3-1) base보다 작으면, 블럭 추가
            if cur < base:
                put_b += (base-cur)
            # (3-2) base보다 크면, 블럭 제거
            else:
                remove_b += (cur-base)
    # (4) 탐색 후 블럭 비교
    if put_b > remove_b + b:
        return -1
    return put_b + (2 * remove_b)


import sys
input = sys.stdin.readline
# 입력 값 받기
global b
n, m, b = map(int, input().rstrip().split())
ground = []
for _ in range(n):
    ground.append(list(map(int, input().split())))

min_tm = sys.maxsize
min_tm_h = sys.maxsize
# (1) base = range(257)
for base in range(257):
    # (2) base에 높이 맞추기
    base_tm = match_base(base)
    # (5) 최솟값 업데이트
    if 0 <= base_tm <= min_tm:
        min_tm = base_tm
        min_tm_h = base

print(min_tm, min_tm_h)