# 듣보잡 (s4, 40.828%)
# source : https://www.acmicpc.net/problem/1764
# keyword : 듣도 보도 못한 사람의 명단 출력

"""
1. 문제
- 듣도 못한 사람 명단과 보도 못한 사람 명단 주어짐
- 듣도 보도 못한 사람 명단 출력

2. 입력
- 듣도 못한 사람 수 N, 보도 못한 사람 수 M (0<=N,M<=500,000)
- 듣도 못한 사람 이름 N줄 (이름<=20)
- 보도 못한 사람 이름 M줄 (이름<=20)
- 중복 없음

3. 로직
- set 자료형 활용
"""


N, M, *names = open(0).read().split()
N, M = int(N), int(M)
both = set(names[:N]) & set(names[N:])
print(len(both))
for n in sorted(both):
    print(n)


"""
테스트케이스

3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton
---결과 출력
2
baesangwook
ohhenrie
"""


