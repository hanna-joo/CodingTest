-- problem : https://school.programmers.co.kr/learn/courses/30/lessons/131124
-- 리뷰를 가장 많이 작성한 회원(VIP)의 리뷰들
-- 조회 : 회원 이름, 리뷰 텍스트, 리뷰 작성일(2022-07-03)
-- 정렬 : 리뷰 작성일, 리뷰 텍스트
-- 주의 : VIP가 여러 명인 경우 고려! 

-- SOLUTION 1 : 가장 많이 리뷰한 회원과 동일한 리뷰 수를 가진 회원 찾기 
SELECT MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE AS M
    INNER JOIN (
        -- JOIN 전에 데이터 수 줄이기
        SELECT MEMBER_ID, REVIEW_TEXT, REVIEW_DATE
        FROM REST_REVIEW
        -- 가장 많이 리뷰한 회원들 선택
        WHERE MEMBER_ID IN (
            SELECT MEMBER_ID
            FROM REST_REVIEW
            GROUP BY MEMBER_ID
            HAVING COUNT(MEMBER_ID) = (
                SELECT COUNT(*)
                FROM REST_REVIEW
                GROUP BY MEMBER_ID
                ORDER BY COUNT(*) DESC
                LIMIT 1
            )
        )
    ) AS R
    ON R.MEMBER_ID = M.MEMBER_ID
ORDER BY REVIEW_DATE, REVIEW_TEXT


-- SOLUTION 2 : GROUP BY 중복 부분 > WITH 구문으로 테이블에 저장
WITH REVIEW_CNT AS (
    SELECT MEMBER_ID, COUNT(*) AS CNT
    FROM REST_REVIEW
    GROUP BY MEMBER_ID
)
SELECT MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE AS M
    INNER JOIN (
        -- JOIN 전에 데이터 수 줄이기
        SELECT MEMBER_ID, REVIEW_TEXT, REVIEW_DATE
        FROM REST_REVIEW
        -- 가장 많이 리뷰한 회원들 선택
        WHERE MEMBER_ID IN (
            SELECT MEMBER_ID
            FROM REVIEW_CNT
            WHERE CNT = (
                SELECT MAX(CNT)
                FROM REVIEW_CNT
            )
        )
    ) AS R
    ON R.MEMBER_ID = M.MEMBER_ID
ORDER BY REVIEW_DATE, REVIEW_TEXT


-- SOLUTION 3 : 리뷰 수 순으로 순위 매겨서 테이블로 저장
WITH REVIEW_RANK AS (
    SELECT MEMBER_ID, DENSE_RANK() OVER(ORDER BY CNT DESC) AS RANKS
    FROM (
        SELECT MEMBER_ID, COUNT(*) AS CNT
        FROM REST_REVIEW
        GROUP BY MEMBER_ID
    ) AS CNT
)
SELECT MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE AS M
    INNER JOIN (
        -- JOIN 전에 데이터 수 줄이기
        SELECT MEMBER_ID, REVIEW_TEXT, REVIEW_DATE
        FROM REST_REVIEW
        -- RANK 1위인 회원들 선택
        WHERE MEMBER_ID IN (
            SELECT MEMBER_ID
            FROM REVIEW_RANK
            WHERE RANKS = 1)
    ) AS R
    ON R.MEMBER_ID = M.MEMBER_ID
ORDER BY REVIEW_DATE, REVIEW_TEXT