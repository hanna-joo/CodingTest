# 백준 온라인 저지 1874, 시간 제한 2초
# 1부터 n까지의 수를 스택에 저장하고 출력하는 방식으로 하나의 수열을 만든다.
# 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 가정한다.
# 수열이 주어졌을 때 이러한 방식으로 스택을 이용해 주어진 수열을 만들 수 있는지 확인하고 만들 수 있다면 어떤 순서로 push, pop을 수행해야 하는지 확인하는 프로그램을 작성하시오.
# n(1<=n<=100,000)

# 필요 변수 선언 및 초기화
seq_cnt = int(input())
seq = [int(input()) for _ in range(seq_cnt)]
print(seq)

num = 1
stack = list()
result = True
answer = ""

for i in range(seq_cnt):
    now = seq[i]
    if now >= num:
        while now >= num:
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else:
        temp = stack.pop()
        if temp == now:
            answer += "-\n"
        else:
            print("NO")
            result = False
            break

if result:
    print(answer)