-- problem : https://school.programmers.co.kr/learn/courses/30/lessons/131117
-- 생산일자가 2022년 05월인 식품들
-- 조회 : 식품 ID, 식품 이름, 총매출
-- 정렬 : 총매출 DESC, 식품 ID ASC

SELECT P.PRODUCT_ID, P.PRODUCT_NAME, (O.AMOUNT * P.PRICE) AS TOTAL_SALES
FROM FOOD_PRODUCT AS P
    INNER JOIN (
        SELECT PRODUCT_ID, SUM(AMOUNT) AS AMOUNT
        FROM FOOD_ORDER
        -- WHERE DATE_FORMAT(PRODUCE_DATE, '%Y-%m') = '2022-05'
        WHERE PRODUCE_DATE LIKE '2022-05%'
        GROUP BY PRODUCT_ID
    ) AS O
    ON P.PRODUCT_ID = O.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, PRODUCT_ID