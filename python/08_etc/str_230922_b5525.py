# IOIOI (s1, 30,133%)
# source : https://www.acmicpc.net/problem/5525
# keyword : 
# return : 

"""
1. 문제
- P(N) = I가 N+1개, O가 N개면서 교대로 나오는 문자열
    - P(1) = IOI
    - P(2) = IOIOI
- 문자열 S와 정수 N이 주어졌을 때 S안에 P(N)이 몇 군데 포함되어 있는지 구하는 프로그램

2. 입력 및 제한
- N (1<=N<=1,000,000)
- S의 길이 M (2N+1<=M<=1,000,000)
- 문자열 S (I와 O로만 이루어짐)

3. 수정 전 로직 -> O(N^2)
- 슬라이딩 윈도우로 앞에서부터 비교
    - 슬라이싱의 시간 복잡도 O(b-a) = O(N)
    - join() 시간 복잡도 = O(N)
    - 문자열끼리 비교 시간 복잡도 = O(N)

4. 수정 후 로직 -> O(N)
- 문자열이 I와 O로만 이루어진 규칙적인 문자열임을 이용
- IOI 일 때 count +1
    - cursor 2칸 이동
    - count = N일 때 answer +1, count -1
- IOI 아닐 때 cursor 1칸 이동, count 초기화
"""

import sys
input = sys.stdin.readline

N, M = int(input()), int(input())
S = input()
i, cnt, answer = 0, 0, 0

while i < M:
    if S[i:i+3] == 'IOI':
        i += 2
        cnt += 1
        if cnt == N:
            answer += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0

print(answer)


"""
테스트 케이스

1
13
OOIOIOIOIIOII
---
4

2
13
OOIOIOIOIIOII
---
2
"""