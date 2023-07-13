-- problem : https://school.programmers.co.kr/learn/courses/30/lessons/157339
-- 테이블 : 자동차 정보, 대여 기록, 할인 정책

-- 차 종류  : '세단', 'SUV'
-- 대여 기간 : 2022-11-01 ~ 2022-11-30
-- 대여 금액 : 50만원 <= 30일 간 금액 < 200만원
-- 조회 : 자동차ID, 자동차 종류, 대여 금액
-- 정렬 : 대여 금액 DESC, 자동차 종류 ASC, 자동차ID DESC

SELECT A.CAR_ID, A.CAR_TYPE, 
    ROUND((A.DAILY_FEE*30*(1-B.DISCOUNT_RATE/100))) AS FEE
FROM CAR_RENTAL_COMPANY_CAR AS A
    INNER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS B
    ON A.CAR_TYPE = B.CAR_TYPE
WHERE A.CAR_ID NOT IN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    -- 2022-10-31 ~ 2022-12-31 대여 자동차도 대여 불가
    -- 11월 이력이 걸쳐있으면 무조건 제외 (이전 이력과 상관 없이)
    WHERE START_DATE <= '2022-11-30'
    AND END_DATE >= '2022-11-01'
)
    AND B.DURATION_TYPE = '30일 이상'
    AND A.CAR_TYPE IN ('SUV', '세단')
HAVING FEE >= 500000 
    AND FEE < 2000000
ORDER BY FEE DESC, A.CAR_TYPE, A.CAR_ID DESC;