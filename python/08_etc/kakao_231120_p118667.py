# 2022 테크 여름인턴십 코딩테스트 - 두 큐 합 같게 만들기 (lv.2)
# source : https://school.programmers.co.kr/learn/courses/30/lessons/118667
# hint : https://tech.kakao.com/2022/07/13/2022-coding-test-summer-internship/
# keyword : 
# return : 각 큐의 원소 합 같게 만들기 위해 필요한 작업 횟수 최솟값

"""
1. 문제
- 각 큐의 원소 합 같게 만들기 위해 필요한 작업 횟수 최솟값
- 작업 1회 = pop + insert
    
2. 입력 및 제한
- 1 ≤ queue1의 길이 = queue2의 길이 ≤ 300,000
- 1 ≤ queue1의 원소, queue2의 원소 ≤ 109

3. 로직
- target = 두 큐 원소 합 // 2

"""


def solution(survey, choices):
    answer = -2
        
    return answer


if __name__ == "__main__":
    test_cases = [([3, 2, 7, 2], [4, 6, 5, 1]),
                  ([1, 2, 1, 2], [1, 10, 1, 2]),
                  ([1, 1], [1, 5])] # 2, 7, -1
    for case in test_cases:
        print(solution(case[0], case[1]))