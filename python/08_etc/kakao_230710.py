# 튜플
# problem source : https://school.programmers.co.kr/learn/courses/30/lessons/64065
# keyword : 튜플, 정렬
# return : 집합이 담긴 문자열 s를 보고, s가 표현하는 튜플을 배열에 담아 출력

"""
1. solution_1
- 문자열에서 가장 많이 등장한 숫자가 튜플 맨 앞 위치
- 많이 등장한 순서 = 튜플 순서
- 딕셔너리 value 기준으로 정렬

2. solution_2
- 위 등장 수 카운트를 Counter로 한 번에 해결
- solution_1을 두 줄 요약 코드

3. solution_3
- 정규식 사용하지 않고 해결
- 정렬 기준에 리스트 길이도 설정 가능
"""
def solution_1(s):
    import re
    from collections import defaultdict
    
    # 문자열에서 숫자만 추출해서 리스트로 생성
    s = list(map(int, re.findall(r'\d+', s)))
    
    # 원소별로 등장한 수 카운트
    cnt = defaultdict(int)
    for i in s:
        cnt[i] += 1
    
    # value 값이 가장 큰 순서대로 정렬
    cnt = sorted(cnt.items(), key=lambda x: -x[1])
    
    # key 값 차례로 넣기
    answer = []
    for i in cnt:
        answer.append(i[0])
    return answer


def solution_2(s):
    import re
    from collections import Counter

    # 많이 등장한 숫자 순서 = 튜플 순서
    s = Counter(re.findall(r'\d+', s))
    answer = list(map(int, [k for k, v in sorted(s.items(), key=lambda x: -x[1])]))
    
    return answer


def solution_3(s):
    s = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    for i in s:
        new_s.append(i.split(','))
    # 리스트 길이가 짧은 순으로 정렬
    new_s.sort(key = len)

    answer = []
    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = ["{{2},{2,1},{2,1,3},{2,1,3,4}}",
                  "{{1,2,3},{2,1},{1,2,4,3},{2}}",
                  "{{20,111},{111}}",
                  "{{123}}",
                  "{{4,2,3},{3},{2,3,4,1},{2,3}}"] # [2, 1, 3, 4], [111, 20], [123], [3, 2, 4, 1]

    for case in test_cases:
        print(solution_1(case))
        print(solution_2(case))
        print(solution_3(case))