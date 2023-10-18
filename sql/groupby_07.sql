-- problem : https://school.programmers.co.kr/learn/courses/30/lessons/59413
-- 시간대별로 입양 발생 건수 조회
-- 조회 : 시간대, 건수
-- 정렬 : 시간대 ASC

WITH RECURSIVE CTE (H) AS (
    SELECT 0
    UNION ALL
    SELECT H+1 FROM CTE WHERE H < 23
)

SELECT CTE.H, IFNULL(A.COUNT, 0)
FROM CTE
LEFT JOIN (
    SELECT HOUR(DATETIME) AS HOUR, COUNT(*) AS COUNT
    FROM ANIMAL_OUTS
    GROUP BY HOUR(DATETIME)
) AS A
ON CTE.H = A.HOUR
ORDER BY CTE.H;