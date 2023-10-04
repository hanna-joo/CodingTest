-- problem : https://school.programmers.co.kr/learn/courses/30/lessons/59410
-- 이름이 없는 동물은 No name으로 출력
-- 조회 : 생물 종, 이름, 성별 및 중성화 여부
-- 정렬 : 아이디

SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name'), SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID