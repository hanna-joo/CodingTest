# 2022 테크 여름인턴십 코딩테스트 - 성격 유형 검사하기 (lv.1)
# source : https://school.programmers.co.kr/learn/courses/30/lessons/118666
# hint : https://tech.kakao.com/2022/07/13/2022-coding-test-summer-internship/
# keyword : 해시, 조건
# return : 지표 순서대로 유형 결과 출력

"""
1. 문제
- R-T / C-F / J-M / A-N
- 선택지에 따른 유형은 질문마다 다르지만 점수는 동일
- 더 높은 점수로 유형 판별, 동일하면 사전순 빠른 유형으로 판별
    - 1,7 -> 3 / 2,6 -> 2 / 3,5 -> 1 / 4 -> 0
    
2. 입력 및 제한
- choices 길이 = survey 길이
- 1 <= choices[i] <= 7

3. 로직
- 딕셔너리에 유형별 점수 저장
- 설문 종료 후 높은 점수를 유형으로 선택
"""


def solution(survey, choices):
    types = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for i in range(len(survey)):
        if choices[i] == 1:
            types[survey[i][0]] += 3
        elif choices[i] == 2:
            types[survey[i][0]] += 2
        elif choices[i] == 3:
            types[survey[i][0]] += 1
        elif choices[i] == 5:
            types[survey[i][1]] += 1
        elif choices[i] == 6:
            types[survey[i][1]] += 2
        elif choices[i] == 7:
            types[survey[i][1]] += 3
            
    answer = ''
    for t in ["RT", "CF", "JM", "AN"]:
        answer += t[0] if types[t[0]] >= types[t[1]] else t[1]
        
    return answer


if __name__ == "__main__":
    test_cases = [(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]), # TCMA
                  (["TR", "RT", "TR"], [7, 1, 3])] # RCJA
    for case in test_cases:
        print(solution(case[0], case[1]))