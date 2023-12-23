-- problem : https://school.programmers.co.kr/learn/courses/30/lessons/131532
-- 년, 월, 성별 별로 상품 구매한 회원수 집계
-- 조회 : 년, 월, 성별, 회원수
-- 정렬 : 년, 월, 성별 ASC
-- 주의 : 성별 정보가 없는 경우 결과에서 제외, 

SELECT YEAR(SALES_DATE) AS YEAR,
    MONTH(SALES_DATE) AS MONTH,
    GENDER, 
    COUNT(DISTINCT A.USER_ID) AS USERS
FROM ONLINE_SALE AS A
    JOIN USER_INFO AS B
    ON A.USER_ID = B.USER_ID
WHERE GENDER IS NOT NULL
GROUP BY YEAR(SALES_DATE), MONTH(SALES_DATE), GENDER
ORDER BY YEAR, MONTH, GENDER;