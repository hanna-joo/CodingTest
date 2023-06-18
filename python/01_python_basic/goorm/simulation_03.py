# 폭탄 구현하기
# keyword : Hash Table, 창의적 해결
# return : 두 명의 점수 합이 0인 경우 커플 매칭 성공, 커플 매칭이 안 된 사람들의 점수 합 출력

"""
1. sum() 이용
- 매칭된 커플의 합은 0
- 매칭 안 된 커플의 합 = 모든 사람의 합

2. Hash Table
- Key 값 --(Hash Function)--> 정수 -> 고유 메모리 주소 할당
- O(1) 의 시간 복잡도로 저장된 값들에 접근 가능
- Key 값으로 메모리에 접근하는 것이 아니라 정수 값으로 접근
- 현재 내 점수와 같으면서 부호가 반대인 점수 존재하는지 O(1) 시간에 판별 가능
- dictionary로 구현, dictionary의 in은 key에 한해서 동작

3. 절댓값의 개수
- 모든 사람은 중복되는 점수가 존재하지 않음
- 소개팅 진행 가능하다면 abs(n)를 절댓값으로 가지는 점수는 배열에서 2개
- 점수의 절댓값들이 몇 번 등장하는지 세고, 한 번만 등장하는 경우 배열에서 해당 숫자 탐색
"""

def no_couple_score_1(scores):
    answer = sum(scores)

    return answer


def no_couple_score_2(scores):
    occur = dict()

    # 모든 참가자의 점수 기록
    for i in range(len(scores)):
        occur[scores[i]] = 1

    answer = 0
    for i in range(len(scores)):
        # 현재 사람의 짝(부호가 반대인 사람)이 있는지 확인
        # 리스트보다 dict가 탐색 속도가 빨라서 사용
        if -scores[i] not in occur:
            answer += scores[i]

    return answer


def no_couple_score_3(scores):
    occur = [0 for _ in range(200001)]
    for i in range(len(scores)):
        occur[abs(scores[i])] += 1
    
    answer = 0
    for i in range(1, 200001):
        if occur[i] != 1:
            continue
        for j in range(len(scores)):
            if abs(scores[j]) == i:
                answer += scores[j]
    return answer

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