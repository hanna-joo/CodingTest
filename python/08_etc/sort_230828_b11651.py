# 좌표 정렬하기 2 (s5, 66.755%)
# source : https://www.acmicpc.net/problem/11651
# keyword : 정렬
# return : N개의 줄에 y, x 오름차순으로 점을 정렬한 결과 출력


nums = [[*map(int, input().split())] for _ in range(int(input()))]
nums.sort(key=lambda x: (x[1], x[0]))
for r in nums:
    print(*r, end=' ')
    print()


"""
테스트케이스

5
0 4
1 2
1 -1
2 2
3 3
---결과 출력
1 -1
1 2
2 2
3 3
0 4
"""