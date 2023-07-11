-- problem source : https://school.programmers.co.kr/learn/courses/30/lessons/132202
-- 2022년 5월에 예약한 환자 수를 진료과 코드 별로 조회
-- 예약한 환자 수 기준 오름차순, 진료과 코드 기준 오름차순 정렬

SELECT MCDP_CD AS '진료과코드', COUNT(*) AS '5월예약건수' 
FROM APPOINTMENT
WHERE DATE_FORMAT(APNT_YMD, '%Y-%m') = '2022-05'
GROUP BY MCDP_CD
ORDER BY 2, 1