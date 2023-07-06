# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12939
# 문자열의 값에서 최솟값과 최댓값 추출
# return : "최솟값 최댓값"

def solution(s):
    s_list = list(map(int, s.split()))
    return ' '.join([str(min(s_list)), str(max(s_list))])