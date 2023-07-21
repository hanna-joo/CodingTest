-- 식품 분류별로 가장 비싼 식품 중 과자, 국, 김치, 식용유 분류만 조회
-- 조회 : 식품 분류, 가격, 이름
-- 정렬 : 식품 가격 DESC

SELECT A.CATEGORY, B.MAX_PRICE, A.PRODUCT_NAME
FROM FOOD_PRODUCT AS A
    JOIN (
        SELECT CATEGORY, MAX(PRICE) AS MAX_PRICE
        FROM FOOD_PRODUCT
        WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
        GROUP BY CATEGORY
    ) AS B
    ON A.CATEGORY = B.CATEGORY
    AND A.PRICE = B.MAX_PRICE
ORDER BY MAX_PRICE DESC;