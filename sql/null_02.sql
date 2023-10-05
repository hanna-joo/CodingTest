-- problem : https://school.programmers.co.kr/learn/courses/30/lessons/131114
-- 경기도 창고 중에 냉동시설 여부 값이 없으면 N로 출력
-- 조회 : 창고ID, 이름, 주소, 냉동시설 여부
-- 정렬 : 창고ID ASC

SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, IFNULL(FREEZER_YN, 'N') AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE WAREHOUSE_NAME LIKE '%_경기%'
ORDER BY WAREHOUSE_ID ASC