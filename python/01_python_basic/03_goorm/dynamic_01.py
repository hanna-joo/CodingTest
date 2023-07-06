# 피보나치 수
# keyword : 다이나믹 프로그래밍
# return : 정수 K가 주어졌을 때 피보나치 수열 K번째 값 출력

"""
1. 재귀적으로 구하기
- 재귀의 깊이가 깊어질 때마다 호출되는 함수가 거의 2배 증가
- 시간 복잡도만 보면 거의 O(2^N)에 가까워서 큰 N에 대해 작동이 잘 되지 않음
- 또한 같은 부분 문제를 여러 번 구하고 있기 때문에 별도로 저장 필요

2. 다이나믹 프로그래밍
- 같은 부분 문제가 여러 번 반복해서 등장할 때 해당 값을 저장해서 효율적으로 처리하는 기법
- 같은 연산이 여러 번 반복되지 않도록 값 저장하는 것이 핵심!!!

3. 나눈 나머지 출력
- 문제의 값이 매우 커질 경우를 대비해 계산을 용이하게 하기 위해서 나눔
- 덧셈, 뺄셈, 곱셈 연산 시마다 잘 나눠주면 됨

4. 점화식과 초기값
- 점화식 : f[i] = f[i-1] + f[i-2]
- 초기값 : f[1] = f[2] = 1
"""

# Bottom-Up
def fibonacci_1(num):
    fibo = [1, 1]
    mod = 1000000007

    for i in range(2, num):
        fibo.append((fibo[-2]+fibo[-1]) % mod)

    return fibo[-1] % mod

# Top-Down
def fibonacci_2(num):
    import sys
    sys.setrecursionlimit(150000)
    
    def fibo(n):
        if (n <= 2):
            return 1
        return (fibo(n-2) + fibo(n-1)) % 1000000007

    return fibo(num)

# Top-Down
def fibonacci_3(num):
    import sys
    sys.setrecursionlimit(150000)

    # import resource
    # resource.setrlimit(resource.RLIMIT_STACK, (64 * 1024 * 1024, -1))
    
    # 재귀함수 실행 시 같은 문제가 여러 번 생기지 않도록 저장
    f = [-1 for _ in range(100008)]

    def fibo(n):
        if f[n] != -1:
            return f[n]
        if n <= 2:
            return 1
        f[n] = (fibo(n-2) + fibo(n-1)) % 1000000007
        return f[n]
    
    return fibo(num)


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [6, 10] # 8, 55
    test_cases.append(int(input().rstrip()))

    for case in test_cases:
        print(fibonacci_1(case))
        print(fibonacci_2(case))
        print(fibonacci_3(case))