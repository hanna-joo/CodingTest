# 단어 정렬 (s5, 40.361%)
# source : https://www.acmicpc.net/problem/1181
# keyword : 정렬
# return : 단어 길이, 사전 순으로 중복 없이 단어 출력


print('\n'.join(sorted({input().rstrip() for _ in range(int(input()))}, key=lambda x: (len(x), x))))


"""
테스트케이스

13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
---결과 출력
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
"""