# 양 (s1, 63.234%)
# source : https://www.acmicpc.net/problem/3184
# keyword : dfs/bfs
# return : 살아남은 양과 늑대의 수 출력

"""
1. 문제
- 마당에 #는 울타리, o는 양, v는 늑대
- 상하좌우로 울타리 없으면 같은 영역
- 영역 안에 양의 수 > 늑대 수 -> 늑대 쫓아냄
- 영역 안에 양의 수 <= 늑대 수 -> 양 잡아먹힘

2. 입력 및 제한
- R, C (3<=R,C<=250)
- 마당의 구조 (#, o, v)

3. 로직
- 모든 구역 탐색 (bfs)
- 같은 영역에 늑대와 양 탐색 및 쫓아내기/잡아먹히기
- 예외 처리 : 범위 초과, 울타리/방문
"""


def bfs(cy, cx):
    global graph, wolf, sheep
    q, v, o = [(cy, cx)], 0, 0
    while q:
        cy, cx = q.pop(0)
        for dy, dx in [(0, 0), (0, 1), (1, 0), (-1, 0), (0, -1)]:
            ny, nx = cy+dy, cx+dx
            if ny<0 or ny>=R or nx<0 or nx>=C:
                continue
            if graph[ny][nx] == '#':
                continue
            if graph[ny][nx] == 'v':
                v += 1
            if graph[ny][nx] == 'o':
                o += 1
            q.append((ny, nx))
            graph[ny][nx] = '#'
    if v >= o:
        wolf += v
    else:
        sheep += o

    
R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
sheep, wolf = 0, 0
for i in range(R):
    for j in range(C):
        if graph[i][j] == '#':
            continue
        bfs(i, j)
print(sheep, wolf)


"""
테스트케이스

6 6
...#..
.##v#.
#v.#.#
#.o#.#
.###.#
...###
---
0 2

8 8
.######.
#..o...#
#.####.#
#.#v.#.#
#.#.o#o#
#o.##..#
#.v..v.#
.######.
---
3 1

9 12
.###.#####..
#.oo#...#v#.
#..o#.#.#.#.
#..##o#...#.
#.#v#o###.#.
#..#v#....#.
#...v#v####.
.####.#vv.o#
.......####.
---
3 5
"""