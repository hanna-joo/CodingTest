-- problem : https://school.programmers.co.kr/learn/courses/30/lessons/131528
-- 나이 정보가 없는 회원의 인원 수 출력
-- 조회 : 인원 수

SELECT COUNT(*) AS USERS
FROM USER_INFO
WHERE AGE IS NULL