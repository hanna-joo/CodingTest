-- problem : https://school.programmers.co.kr/learn/courses/30/lessons/131534
-- 2021년 가입한 회원 중 상품 구매 회원 수와 비율을 연, 월 별 출력
-- 조회 : 회원 수, 회원 비율 (소수점 두번째 자리 반올림)
-- 정렬 : 연 ASC, 월 ASC

WITH B AS (
    SELECT USER_ID, COUNT(*) OVER() AS TOTAL
    FROM USER_INFO
    WHERE YEAR(JOINED) = '2021'
)
SELECT YEAR(A.SALES_DATE) AS YEAR, 
    MONTH(A.SALES_DATE) AS MONTH, 
    COUNT(DISTINCT A.USER_ID) AS PURCHASED_USERS,
    ROUND(COUNT(DISTINCT A.USER_ID)/B.TOTAL, 1) AS PURCHASED_RATIO
FROM ONLINE_SALE AS A
    JOIN B
    ON A.USER_ID = B.USER_ID
GROUP BY YEAR(A.SALES_DATE), MONTH(A.SALES_DATE)
ORDER BY YEAR, MONTH;


SELECT YEAR(SALES_DATE) AS YEAR, 
    MONTH(SALES_DATE) AS MONTH,
    COUNT(DISTINCT A.USER_ID) AS PURCHASED_USERS,
    ROUND(
        COUNT(DISTINCT A.USER_ID)/(
            SELECT COUNT(*) 
            FROM USER_INFO
            WHERE YEAR(JOINED) = '2021'
        ), 1
    ) AS PURCHASED_RATIO
FROM ONLINE_SALE AS A, USER_INFO AS B
WHERE A.USER_ID = B.USER_ID
AND YEAR(JOINED) = '2021'
GROUP BY YEAR(SALES_DATE), MONTH(SALES_DATE)
ORDER BY YEAR, MONTH;