-- problem source : https://school.programmers.co.kr/learn/courses/30/lessons/59043
-- 보호 시작일 > 입양일인 동물 아이디와 이름 조회
-- 보호 시작일이 빠른 순으로 조회

SELECT ins.ANIMAL_ID, ins.NAME
FROM ANIMAL_INS AS ins
    INNER JOIN ANIMAL_OUTS AS outs
    ON ins.ANIMAL_ID = outs.ANIMAL_ID
WHERE ins.DATETIME > outs.DATETIME
ORDER BY ins.DATETIME ASC