-- problem : https://school.programmers.co.kr/learn/courses/30/lessons/59039
-- 이름이 없는 채로 들어온 동물의 ID
-- 조회 : ID
-- 정렬 : ID ASC

SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL
ORDER BY ANIMAL_ID ASC