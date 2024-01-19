-- 자동차 평균 대여기간 구하기 : 
-- 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/157342
-- 조건 : 평균 대여 기간이 7일 이상인 자동차들
-- 조회 : 자동차 ID, 평균 대여 기간(소수점 첫번째자리까지)
-- 정렬 : 평균 대여 기간 DESC, 자동차ID DESC
-- 풀이 : 자동차별로 그룹바이 -> 평균 대여 기간 -> 필터링

SELECT CAR_ID, ROUND(AVG(DATEDIFF(END_DATE, START_DATE)+1), 1) AS AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
HAVING AVERAGE_DURATION >= 7
ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC;