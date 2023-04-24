# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42842

# 노란색 격자를 갈색 격자가 둘러싸고 있는 카펫 크기 구하기
# return : [가로, 세로] (단, 가로 >= 세로)

def solution(brown, yellow):
    for i in range(1, int(yellow**0.5)+1):
        # 노란색 격자 개수 약수로 노란색 가로, 세로 찾기
        if yellow % i == 0:
            # 가로 = 노란색 가로 + 2 / 세로 = 노란색 세로 + 2
            height, width = i + 2, yellow//i + 2
            # 너비 = 노란색 격자 + 갈색 격자 = 가로 * 세로
            if (brown + yellow) == (height * width):
                answer = [width, height]
    return answer

if __name__ == '__main__':
    brown = [24, 10, 8]
    yellow = [24, 2, 1]
    for i in range(len(brown)):
        print(solution(brown[i], yellow[i]))