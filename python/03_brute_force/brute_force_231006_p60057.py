# 문자열 압축하기 (lv2)
# source : https://school.programmers.co.kr/learn/courses/30/lessons/60057
# keyword : 완전 탐색
# return : 제일 짧게 문자열 압축 후 길이 출력

"""
1. 문제
- 비손실 압축 방법 : 같은 값이 연속해서 나타나면 개수+값으로 표현해서 압축
- 1개 이상 단위로 문자열을 잘라 압축할 때 가장 짧게 압축한 문자열의 길이 출력
    - abcabcdede -(2)-> abcabc2de -> 9
    - abcabcdede -(3)-> 2abcdede -> 8
- 문자열은 제일 앞부터 정해진 길이만큼 잘라야 함
    - xababcdcdababcdcd -> 압축 불가

2. 입력 및 제한
- 1 <= s의 길이 <= 1,000

3. 풀이
- 완전 탐색
"""


def compress(num, s):
    res, cnt = '', 1
    for i in range(0, len(s), num):
        cur, nxt = s[i:i+num], s[i+num:i+2*num]
        if cur == nxt:
            cnt += 1
        else:
            if cnt > 1:
                res += str(cnt)
                cnt = 1
            res += cur
    return len(res)
        
    
def solution(s):
    ans = 1001
    for i in list(range(1, int(len(s)/2)+1)) + [len(s)]:
        ans = min(ans, compress(i, s))
    return ans


if __name__ == "__main__":

    import sys
    s = sys.stdin.readline()

    print(solution(s))


"""
테스트케이스

"aabbaccc"
---
7

"ababcdcdababcdcd"
---
9

"abcabcdede"
---
8

"abcabcabcabcdededededede"
---
14

"xababcdcdababcdcd"
---
17
"""