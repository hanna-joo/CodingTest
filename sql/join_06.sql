-- problem source : https://school.programmers.co.kr/learn/courses/30/lessons/59044
-- 입양을 못 간 동물 중에 가장 보호소에 오래 있었던 동물 3마리
-- 조회 : 이름, 보호 시작일
-- 정렬 : 보호 시작일 순

SELECT INS.NAME, INS.DATETIME
FROM ANIMAL_INS AS INS
    LEFT JOIN ANIMAL_OUTS AS OUTS
    ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE OUTS.ANIMAL_ID IS NULL
ORDER BY INS.DATETIME
LIMIT 3