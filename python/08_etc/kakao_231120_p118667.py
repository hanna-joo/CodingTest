# 2022 테크 여름인턴십 코딩테스트 - 두 큐 합 같게 만들기 (lv.2)
# source : https://school.programmers.co.kr/learn/courses/30/lessons/118667
# hint : https://tech.kakao.com/2022/07/13/2022-coding-test-summer-internship/
# keyword : 투 포인터, 그리디
# return : 각 큐의 원소 합 같게 만들기 위해 필요한 작업 횟수 최솟값

"""
1. 문제
- 각 큐의 원소 합 같게 만들기 위해 필요한 작업 횟수 최솟값
- 작업 1회 = pop + insert
    
2. 입력 및 제한
- 1 ≤ queue1의 길이 = queue2의 길이 ≤ 300,000
- 1 ≤ queue1의 원소, queue2의 원소 ≤ 109

3. 로직 1 : 투 포인터
- target = 두 큐 원소 합 // 2
- 투 포인터
    - n = 연산(pop, insert) 횟수
    - target 과 같은 경우 : answer = n, 종료
    - target 보다 큰 경우 : s+1 / (단, s==e 인 경우 s+1, e+1)
    - target 보다 작은 경우 : e+1
- 인덱스 에러 방지를 위해 (s+1) % base

4. 로직 2 : 탐욕법
- queue1의 합 > queue2의 합 : queue1 원소 -> queue2 원소
- queue1의 합 < queue2의 합 : queue1 원소 <- queue2 원소
- 작업 횟수 제한 필요 : len(queue) * 4
"""


def solution_1(queue1, queue2):
    # 두 개의 큐 합치기
    queue = queue1 + queue2
    if sum(queue) % 2 == 0:
        target = sum(queue) // 2
    else:
        return -1
    # 탐색 시작
    n = len(queue1)
    s, e, val = 0, n-1, sum(queue1)
    ans = 0
    while val != target:
        if val < target:
            e += 1
            if e == n * 2:
                return -1
            val += queue[e]
        else:
            val -= queue[s]
            s += 1
        ans += 1

    return ans


def solution_2(queue1, queue2):
    # 두 개의 큐를 합치기
    q = queue1 + queue2
    if sum(q) % 2:
        return -1
    target = sum(q) // 2

    # 탐색 시작
    s, e, val, cnt = 0, len(queue1)-1, sum(queue1), 0
    n = len(q)
    ans = -1
    
    while cnt < 3 * n:
        if val == target:
            ans = cnt
            break
        elif val < target:
            e = (e+1) % n
            val += q[e]
            cnt += 1
        else:
            val -= q[s]
            s = (s+1) % n
            cnt += 1

    return ans


def solution_3(queue1, queue2):
    
    left, right = sum(queue1), sum(queue2)
    if (left+right) % 2:
        return -1
    
    # 속도 개선을 위해 자료형 변환
    from collections import deque
    queue1, queue2 = deque(queue1), deque(queue2)
    # 탐색 시작
    for op in range(len(queue1) * 4):
        if left == right:
            ans = op
            return ans
        if left > right:
            elem = queue1.popleft()
            left -= elem
            queue2.append(elem)
            right += elem
        else:
            elem = queue2.popleft()
            right -= elem
            queue1.append(elem)
            left += elem
    return -1


if __name__ == "__main__":
    test_cases = [([3, 2, 7, 2], [4, 6, 5, 1]),
                  ([1, 2, 1, 2], [1, 10, 1, 2]),
                  ([1, 1], [1, 5]),
                  ([1, 1, 1, 1, 1], [1, 1, 1, 9, 1]),
                  ([1, 1, 1, 1, 1, 7], [1, 1, 1, 1, 1, 1]),
                  ([3, 3, 1], [1, 2, 2]),
                  ([3, 3, 3, 3, 1], [3, 3, 21, 1, 3])] # 2, 7, -1, 12
    
    for case in test_cases:
        print(solution_1(case[0], case[1]))
        print(solution_2(case[0], case[1]))
        print(solution_3(case[0], case[1]))