# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42577

# 특정 번호가 다른 번호의 접두어인지 아닌지 판별
# return : 접두어면 false / 아니면 true

# 해시 미사용
def solution1(phone_book):
    answer = True
    for compare in phone_book:
        for num in phone_book:
            if compare != num and compare == num[:len(compare)]:
                answer = False
                break
    return answer

# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42577

# 특정 번호가 다른 번호의 접두어인지 아닌지 판별
# return : 접두어면 false / 아니면 true

def solution(phone_book):
    answer = True
    # 해시 테이블 생성
    phone_cnt = len(phone_book)
    hash_table = [0 for _ in range(phone_cnt)]
    # 해시 값 생성 및 테이블에 저장
    for val in phone_book:
        key = hash(num)
        addr = key % phone_cnt
        hash_table[addr] = val
    # 비교
    for compare in phone_book:
        for num in phone_book:
            key = hash(num[:len(compare)])
            addr = key % phone_cnt
            hash_table[addr] 
            if compare != num and compare == num[:len(compare)]:
                answer = False
                break
    return answer

if __name__ == '__main__':
    test_cases = ["(())()", ")()(", "(()(", "((d))", "((()()(s)))"] # t f f t t
    for case in test_cases:
        print(solution1(case))