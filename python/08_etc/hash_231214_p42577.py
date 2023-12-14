# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42577
# keyword : 해시, 정렬
# return : 특정 번호가 다른 번호의 접두어면 false / 아니면 true

'''
1. 문제
- phone_book의 번호가 다른 번호의 접두어에 속하면 false

2. 입력 및 제한
- 1 <= phone_book 길이 <= 1,000,000
- 1 <= 각 전화번호의 길이 <= 20
- 중복 전화번호 없음

3. 로직1 : 완전 탐색, 효율성 fail
- O(N) * O(N) = 100만 * 100만
- 모든 번호를 서로 1:1 매칭하는 방법

4. 로직2 : 정렬, 해시 자료형
- O(NlogN) + O(N) = 100만log100만 + 100만 * 20
- 딕셔너리에 번호를 저장하고 있는지 없는지 확인하는 방법

5. 로직3 : 정렬 미사용, 해시 자료형
- O(N) + O(N) = 100만 + 100만 = 200만
- 딕셔너리에 한 번에 폰 번호 저장하고 확인하는 방법
'''


def solution_1(phone_book):
    answer = True
    for compare in phone_book:
        for num in phone_book:
            if compare != num and compare == num[:len(compare)]:
                answer = False
                break
    return answer


from collections import defaultdict

def solution_2(phone_book):
    answer = True
    phone_dict = defaultdict(int)
    phone_book.sort()
    for nums in phone_book:
        char = ''
        for num in nums:
            char += num
            if phone_dict.get(char, 0) != 0:
                answer = False
                break
        phone_dict[nums] += 1
    return answer  


def solution_3(phone_book):
    answer = True
    phone_dict = dict()
    for nums in phone_book:
        phone_dict[nums] = 1
    for nums in phone_book:
        char = ''
        for num in nums:
            char += num
            if phone_dict.get(char) and nums != char:
                answer = False
                break
    return answer


if __name__ == '__main__':
    test_cases = [["119", "97674223", "1195524421"],
                  ["123","456","789"],
                  ["12","123","1235","567","88"],
                  ["119", "11819", "119112", "119211"]] # f t f f
    for case in test_cases:
        print(solution_1(case))
        print(solution_2(case))
        print(solution_3(case))