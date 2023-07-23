-- problem : https://school.programmers.co.kr/learn/courses/30/lessons/131534
-- 2021년 가입한 회원 중 상품 구매 회원 수와 비율을 연, 월 별 출력
-- 조회 : 회원 수, 회원 비율 (소수점 두번째 자리 반올림)
-- 정렬 : 연 ASC, 월 ASC

SELECT YEAR(A.SALES_DATE) AS YEAR, 
    MONTH(A.SALES_DATE) AS MONTH, 
    COUNT(DISTINCT A.USER_ID) AS PURCHASED_USERS,
    ROUND(COUNT(DISTINCT A.USER_ID)/B.TOTAL, 2) AS PURCHASED_RATIO
FROM ONLINE_SALE AS A
    JOIN (
        SELECT USER_ID, COUNT(*) AS TOTAL
        FROM USER_INFO
        WHERE YEAR(JOINED) = '2021'
    ) AS B
    ON A.USER_ID = B.USER_ID
GROUP BY YEAR(A.SALES_DATE), MONTH(A.SALES_DATE)