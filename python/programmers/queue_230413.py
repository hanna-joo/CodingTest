# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42586

# 하루 1번 배포 가능하고 배포 순서 고정
# progresses : 배포 순서대로 작업 진도 현황
# speeds : 각 작업의 개발 속도
# return : 배포하는 날 배포 기능 개수

from collections import deque

def solution(progresses, speeds):
    progresses, speeds = deque(progresses), deque(speeds)
    answer = list()
    while progresses:
        # 하루 각 기능 진행률 업데이트
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        # 당일 배포 개수
        release_cnt = 0
        # progresses의 첫 번째 값이 100 이상이면 배포
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            release_cnt += 1
        if release_cnt > 0:
            answer.append(release_cnt)
    return answer

if __name__ == '__main__':
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    print(solution(progresses, speeds))