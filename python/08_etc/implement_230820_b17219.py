# 비밀번호 찾기 (s4, 70.040%)
# source : https://www.acmicpc.net/problem/17219
# keyword : 구현, 해시
# return : 사이트 주소의 비밀번호를 차례대로 출력

"""
1. 문제
- 비밀번호를 찾으려는 사이트 주소의 비밀번호를 차례대로 출력

2. 입력
- 저장된 사이트 주소의 수 N와 비밀번호 필요한 사이트 주소의 수 (1<=N,M<=100,000)
- N줄은 사이트 주소와 비밀번호 (길이<=20)
- M줄은 비밀번호 찾으려는 사이트 주소

3. 로직 
- Hash 자료형 활용
"""


import sys
input = sys.stdin.readline
N, M = map(int, input().split())

password = dict()
for _ in range(N):
    tmp = input().rstrip().split()
    password[tmp[0]] = tmp[1]

for _ in range(M):
    print(password[input().rstrip()])


"""
테스트케이스 : 3 / 171 / 2731

2
8
12
"""