-- problem source : https://school.programmers.co.kr/learn/courses/30/lessons/59042
-- 입양 간 기록은 있으나 보호소에 들어온 기록이 없는 동물 ID, 이름 조회
-- ID 순으로 정렬

SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_OUTS AS OUTS
    LEFT JOIN ANIMAL_INS AS INS
    ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
WHERE INS.ANIMAL_ID IS NULL
ORDER BY OUTS.ANIMAL_ID