-- problem : https://school.programmers.co.kr/learn/courses/30/lessons/144855
-- 2022년 1월 카테고리 별 도서 판매량 합산
-- 조회 : 카테고리, 총 판매량
-- 정렬 : 카테고리 ASC

SELECT B.CATEGORY, SUM(SALES) AS TOTAL_SALES
FROM BOOK_SALES AS A
    INNER JOIN BOOK AS B
    ON A.BOOK_ID = B.BOOK_ID
WHERE A.SALES_DATE LIKE '2022-01%'
GROUP BY B.CATEGORY
ORDER BY B.CATEGORY;