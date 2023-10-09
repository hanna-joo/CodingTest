-- problem : https://school.programmers.co.kr/learn/courses/30/lessons/131118
-- 서울에 위치한 식당들과 평균점수 출력
-- 조회 : 식당 ID, 식당 이름, 음식 종류, 즐겨찾기수, 주소, 리뷰 평균 점수(소수3째반올림)
-- 정렬 : 평균점수 DESC, 즐겨찾기수 DESC

SELECT A.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, SCORE
FROM REST_INFO AS A
    JOIN (
        SELECT REST_ID, ROUND(AVG(REVIEW_SCORE), 2) AS SCORE
        FROM REST_REVIEW
        GROUP BY REST_ID
    ) AS B
    ON A.REST_ID = B.REST_ID
WHERE ADDRESS LIKE '서울%'
ORDER BY SCORE DESC, FAVORITES DESC