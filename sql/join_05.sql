-- problem source : https://school.programmers.co.kr/learn/courses/30/lessons/59045
-- 보호소 들어올 당시에는 중성화 되지 않았지만, 나갈 당시에는 중성화된 동물
-- 아이디, 생물 종, 이름을 아이디 순으로 조회

SELECT OUTS.ANIMAL_ID, OUTS.ANIMAL_TYPE, OUTS.NAME
FROM ANIMAL_INS AS INS
    INNER JOIN ANIMAL_OUTS AS OUTS
    ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.SEX_UPON_INTAKE LIKE 'Intact%'
AND OUTS.SEX_UPON_OUTCOME NOT LIKE 'Intact%'
ORDER BY OUTS.ANIMAL_ID