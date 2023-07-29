# 정수 삼각형
# source : https://www.acmicpc.net/problem/1932
# keyword : 다이나믹 프로그래밍
# return : 정수 삼각형을 내려올 때 여러 경로 중에서 최댓값 출력

"""
1. 문제
- 정수로 이루어진 삼각형에서 아래로 내려올 때 합이 최대가 되는 경로
- 이동 방향 : (+1, 0), (+1, +1)

2. 입력
- 삼각형 크기 n (1<=n<=500)
- 정수로 이루어진 삼각형

3. 로직
- Bottom-Up
- dp[y][x]
    - (x,y) 지점까지 내려올 때 최댓값
    - (x,y-1) 또는 (x-1,y-1) 에서 (x,y)로 갈 수 있음
(1) 점화식
    - dp[y][x] = max(dp[y-1][x], dp[y-1][x-1]) + tri[y][x]
    - 범위 벗어나는지 확인 필수 (x-1)
(2) 초깃값
    - dp[0][0] = tri[0][0]
(3) 최종값
    - max(dp[n-1])

4. solution_2()
- between = 맨 끝과 맨 앞 제외하고 먼저 구하기 
- answer = [맨 끝, *between, 맨 앞]
- *리스트 : unpacking으로 리스트 안의 값들을 뺌
"""

def solution_1():
    N, *ls = map(int, open(0).read().rstrip().split())
    e=0
    tri = [ls[(e:=e+i):e+i+1] for i in range(0, N)]
    
    # (1) 점화식 구현 - 초깃값 별도 설정 필요X
    for y in range(1, N):
        for x in range(y+1):
            # 왼쪽 위에 값이 없을 때
            if x-1 < 0:
                tri[y][x] += tri[y-1][x]
                continue
            # 오른쪽 위에 값이 없을 때
            if x > y-1:
                tri[y][x] += tri[y-1][x-1]
                continue
            tri[y][x] += max(tri[y-1][x], tri[y-1][x-1])

    # (3) 최종값 출력
    print(max(tri[N-1]))


def solution_2():
    N = int(input())
    # 0번째 줄
    prev = [*map(int, input().split())]

    # 1번째 줄부터 계산 시작
    for i in range(1, N):
        # 새로운 값 가져오기
        new = [*map(int, input().split())]
        # 1 ~ (i-1)까지의 값
        between = [max(prev[j-1], prev[j])+new[j] for j in range(1, i)]
        # 맨 앞(0)과 맨 뒤(i) 값 추가
        prev = [prev[0]+new[0], *between, prev[-1]+new[-1]]

    # 최종값 출력
    print(max(prev))


solution_1()
solution_2()


"""
테스트 케이스 : 30

5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""