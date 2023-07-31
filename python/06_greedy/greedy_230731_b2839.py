# 설탕 배달
# source : https://www.acmicpc.net/problem/2839
# keyword : 그리디
# return : 설탕 N킬로그램 배달할 때 사용하는 봉지의 최소 개수 출력 (-1)


"""
1. 문제
- 봉지 용량은 3, 5킬로그램 2가지
- 정확히 N킬로그램 만들 수 없으면 -1 출력

2. 입력
- 배달 용량 N킬로그램(3<=N<=5,000)

3. 로직 1 : 5를 먼저 뺀다
- 5보다 크면 계속 실행
    - 5의 배수인지 확인 -> 후보군에 추가
    - 3의 배수인지 확인 -> 후보군에 추가
    - N에서 5 빼고 cnt ++1

4. 로직 2 : 3을 먼저 뺀다
- 0보다 크거나 같으면 계속 실행
    - 5의 배수인지 확인 -> 맞으면 멈춤
    - N에서 3 빼고 cnt++1
- while~else
    - break -> else문 실행되지 않음
    - 반복문 종료 -> else문 실행
"""
import sys
input = sys.stdin.readline

def solution_1(num):
    cnts = []
    temp = 0
    while num >= 5:
        if num % 5 == 0:
            cnts.append(N//5)
            break
        if num % 3 == 0:
            cnts.append(temp + num//3)
        num -= 5
        temp += 1
    if num >= 3:
        temp += num//3
        num %= 3
    if num == 0:
        cnts.append(temp)

    if len(cnts) > 0:
        print(min(cnts))
    else:
        print(-1)

def solution_2(num):
    cnt = 0
    while num >= 0:
        if num % 5 == 0:
            cnt += num // 5
            print(cnt)
            break
        num -= 3
        cnt += 1
    else:
        print(-1)


N = int(input())
solution_1(N)
solution_2(N)

"""
테스트 케이스 : 4 / -1 / 2 / 3 / 3

18
4
6
9
11
"""