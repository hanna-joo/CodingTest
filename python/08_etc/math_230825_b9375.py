# 패션왕 신해빈 (s3, 55.096%)
# source : https://www.acmicpc.net/problem/9375
# keyword : 수학, 자료 구조, 해시
# return : 해빈이가 며칠을 패션왕으로 살 수 있는지 계산 및 출력

"""
1. 문제
- 같은 조합의 옷은 절대 입지 않는 해빈이
- 옷을 추가하거나 바꾸거나 해서 새로운 조합을 입어야 한다
- 의상이 주어졌을 때 해빈이가 알몸이 아닌 상태로 며칠을 버틸 수 있을까?

2. 입력 및 제한
- 테스트 케이스 (T<=100)
    - 해빈이가 가진 의상 수 n (0<=n<=30)
    - 해빈이가 가진 의상 이름과 종류
    - 같은 종류는 하나만 착용 가능

3. 로직
- 카테고리별 옷 갯수 세기
- 카테고리별 착용하는 경우의 수 = 카테고리별 옷 갯수 + 착용 안한 경우
- 총 경우의 수 = 카테고리1 * 카테고리2 * 카테고리3 * ...
- 마지막에 모두 착용 안한 경우(1) 빼기
"""

import sys
from collections import defaultdict
input = sys.stdin.readline

def fashion_king():
    closet = defaultdict(int)
    for _ in range(int(input())):
        closet[input().rstrip().split()[1]] += 1

    days = 1
    for val in closet.values():
        days *= val + 1

    print(days-1)


for _ in range(int(input())):
    fashion_king()

"""
테스트케이스

3
3
hat headgear
sunglasses eyewear
turban headgear
3
mask face
sunglasses face
makeup face
6
hat headgear
sunglasses eyewear
turban headgear
mask face
sunglasses face
makeup face

---결과 출력
5
3
23
"""