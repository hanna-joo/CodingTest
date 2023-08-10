# AC (g5, 19.965%)
# source : https://www.acmicpc.net/problem/5430
# keyword : 구현
# return : 배열 초기값과 함수 주어졌을 때 최종 결과 구하는 프로그램

"""
1. 문제
- AC : 정수 배열에 연산하기 위한 언어
    - R : 배열에 있는 수의 순서 뒤집기
    - D : 첫 번째의 수를 버리기
- 배열이 비었는데 D 사용 시 에러 발생

2. 입력
- 테스트 개수 T (T<=100)
    - 수행할 함수 p (1<=p길이<-100,000)
    - 배열에 들어있는 수의 개수 n (0<=n<=100,000)
    - 배열에 들어있는 정수 (1<=xi<=100)
- p 길이의 합 + n 합 <= 700,000

3. 로직
- 배열에 수가 안들어 있을 수도 있음
"""

import sys
input = sys.stdin.readline

def solution_1(commands, array):
    array = array.copy()
    reverse = False
    for c in commands:
        if c == 'R':
            reverse = False if reverse else True
        else:
            if not array:
                print('error')
                return
            if reverse:
                array.pop()
            else:
                array.pop(0)
    if len(array) == 0:
        print('[]')
        return
    
    if reverse:
        print(f'[{",".join(array[::-1])}]')
    else:
        print(f'[{",".join(array)}]')


def solution_2(commands, array):
    commands = [*map(len, commands.replace("RR", "").split("R"))]
    # R이 홀수 개수 -> commands 짝수 개수
    reverse = (len(commands) + 1) % 2
    front = sum(commands[0::2])
    back = sum(commands[1::2])

    if front + back > len(array):
        print('error')
        return
    else:
        array = array[front:(len(array)-back)]
    
    if reverse:
        array.reverse()
    print(f'[{",".join(array)}]')



if __name__ == "__main__":

    T = int(input().rstrip())
    for _ in range(T):
        p = input().rstrip()
        n = int(input().rstrip())

        if n == 0:
            input()
            arr = []
        else:
            #arr = input().rstrip()[1:-1].split(',')
            arr = input().strip("[]\n").split(",")

        solution_1(p, arr)
        solution_2(p, arr)

    

"""
---테스트케이스
5
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
R
0
[]

---결과
[2,1]
error
[1,2,3,5,8]
error
[]
"""
