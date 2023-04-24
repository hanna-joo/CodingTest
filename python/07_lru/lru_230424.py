# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/17680
# 캐시 크기에 따른 실행시간 측정 프로그램
# 캐시 교체 알고리즘 : LRU
# cache hit : 조회한 값이 cache 안에 있으면 빼서 다시 추가
# cache miss : 조회한 값이 cache 안에 없으면 오래된 값을 빼고 리스트에 추가

def solution(cacheSize, cities):
    cache = list()
    answer = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            city_idx = cache.index(city)
            cache.append(cache.pop(city_idx))
            answer += 1
        else:
            if len(cache) < cacheSize:
                cache.append(city)
            elif cache:
                cache.pop(0)
                cache.append(city)
            answer += 5
    return answer