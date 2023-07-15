-- problem : https://school.programmers.co.kr/learn/courses/30/lessons/157341
-- '세단' 자동차들 중 10월에 대여 시작한 기록이 있는 자동차
-- 조회 : 자동차 ID (중복 없이)
-- 정렬 : 자동차 ID DESC

SELECT DISTINCT A.CAR_ID
FROM CAR_RENTAL_COMPANY_CAR AS A
    JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS B
    ON A.CAR_ID = B.CAR_ID
WHERE A.CAR_TYPE = '세단'
    AND DATE_FORMAT(B.START_DATE, '%m') = '10'
ORDER BY A.CAR_ID DESC