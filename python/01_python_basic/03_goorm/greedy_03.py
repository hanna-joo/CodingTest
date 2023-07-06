# 직사각형 만들기
# keyword : 그리디 알고리즘
# return : 막대기의 길이들이 주어졌을 때 만들 수 있는 직사각형들의 넓이 합 최대 출력

"""
1. 간단한 경우
- 막대기 쌍의 길이 4개가 a <= b <= c <= d 만족
- 막대기 조합하는 방법 3가지와 그 때의 넓이
- (1) ab + cd
- (2) ac + bd
- (3) ad + bc
- 가정 : (1) >= (2) >= (3)
- ab+cd >= ac+bd ---> d(c-b) >= a(c-b) ---> d >= a
- ab+cd >= ad+bc ---> c(d-b) >= a(d-b) ---> c >= a
- ac+bd >= ad+bc ---> b(d-c) >= a(d-c) ---> b >= a
- 결과 : 가정 결과 모두 a<=b<=c<=d 만족
- 결론 : 큰 애들끼리 직사각형 만들고 작은 애들끼리 직사각형 만들자

2. 복잡한 경우
- 만든 직사각형들 중에 두 직사각형 A, B
- A의 짧은 변 >= B의 긴 변
"""

def rectangles_area_1(bars): # 시간 초과 알고리즘
    from collections import deque

    bars = deque(sorted(bars, reverse=True))
    usable = deque()
    while bars:
        now = bars.popleft()
        if bars and now == bars[0]:
            usable.append(now)
            bars.popleft()
            
    area = 0
    for i in range(1, len(usable), 2):
        area += usable[i-1] * usable[i]
    return area


def rectangles_area_2(bars):
    from collections import deque

    # 막대기 길이별 개수 세기
    dic = dict()
    for i in bars:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    # 막대기는 2개씩 사용 가능 > usable에 넣기
    usable = deque()
    for k, v in dic.items():
        usable.extend([k] * (v//2))
        
    # 가장 큰 수끼리 먼저 만들어야 최대 너비 합
    usable = deque(sorted(usable, reverse=True))
    area = 0
    while len(usable) >= 2:
        w, h = usable.popleft(), usable.popleft()
        area += w * h

    return area


def rectangles_area_3(bars):
    pair = []
    cnt = [0 for _ in range(1000001)]
    
    for bar in bars:
        cnt[bar] += 1

    for length in range(1, 1000001):
        while cnt[length] > 1:
            cnt[length] -= 2
            pair.append(length)

    pair.sort(reverse=True)
    area = 0
    for i in range(1, len(pair), 2):
        area += pair[i-1] * pair[i]

    return area

if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [[4, 8, 4, 8], 
                  [2, 4, 6, 8, 2, 4, 6, 8],
                  [1, 2, 3, 4, 5]] # 32, 56, 0
    test_cases.append(list(map(int, input().rstrip().split())))

    for case in test_cases:
        print(rectangles_area_1(case))
        print(rectangles_area_2(case))
        print(rectangles_area_3(case))