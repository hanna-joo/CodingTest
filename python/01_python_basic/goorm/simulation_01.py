# 0커플
# keyword : Hash Table, 창의적 해결
# return : 두 명의 점수 합이 0인 경우 커플 매칭 성공, 커플 매칭이 안 된 사람들의 점수 합 출력

"""
1. Hash Table
- Hash Function 이용해 Key 값들 정수로 변환
- 변환된 각 정수에 고유 메모리 주소 할당
- O(1) 의 시간 복잡도로 저장 값들에 접근 가능
- 현재 내 점수와 같으면서 부호가 반대인 수 존재하는지 O(1) 시간에 판별 가능

2. 완전 탐색
- 모든 경우의 수 탐색
- 4개이기 때문에 24개의 경우의 수 존재

3. 
"""

def no_couple_score_1(scores):
    answer = sum(scores)

    return answer

def no_couple_score_2(scores):
    occur = dict()
    for i in range(len(scores)):
        occur[scores[i]] = 1

    return

def no_couple_score_3(nums):

    return

if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [[1, 2, 3, 4, -1, -2, -3, -5], 
                  [-1, 1, 2, -2, 3, -3, 4, 5]] # -1, 9
    test_cases.append(list(map(int, input().rstrip().split())))

    for case in test_cases:
        print(no_couple_score_1(case))
        print(no_couple_score_2(case))
        print(no_couple_score_3(case))