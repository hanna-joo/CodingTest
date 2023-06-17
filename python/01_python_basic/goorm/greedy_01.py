# 거스름돈
# keyword : 그리디 알고리즘, 원인과 결과
# return : 1, 5, 10, 20, 40원 중 거슬러줘야 하는 동전의 최소 개수 출력

"""
1. 그리디 알고리즘
- 탐욕법, 탐욕 알고리즘
- 최적해를 구하는 데에 사용되는 근사적인 방법
- 문제를 해결할 때 있어서 현재 경우만 고려해서 최적의 상황을 선택하는 방법

2. 그리디 적용 필수 조건
- 현재의 최적의 선택이 다음 선택에 영향을 미치지 않아야 함
- 현재의 선택이 최종 선택의 최적 해결 방법에 포함되어야 함

3. 동전 교환 문제
- 모든 동전이 배수 관계에 있으면 그리디하게 문제 해결 가능
- 가장 큰 동전부터 금액을 넘기기 전까지 최대 개수로 채우면 됨

4. 그 외 그리디 문제
- 회의실 배정 문제
- Fractional Knapsack, 분할 가능한 배낭 채우기
- 다익스트라, 프림, 크루스칼 등의 비용 최적화하는 그래프 이론
"""

def change_1(change):
    coin_kind = [40, 20, 10, 5, 1]
    coin_cnt = 0

    for i in coin_kind:
        if change >= i:
            coin_cnt += change // i
            change %= i

    return coin_cnt


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = [55, 39] # 3, 7
    test_cases.append(int(input()))

    for case in test_cases:
        print(change_1(case))