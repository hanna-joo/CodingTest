-- problem : https://school.programmers.co.kr/learn/courses/30/lessons/132204
-- 2022년 4월 13일 취소되지 않은 흉부외과(CS) 진료 예약 내역 조회
-- 조회 : 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시
-- 정렬 : 진료예약일시 ASC
-- 구현 : 4월 13일 취소되지 않은 흉부외과 예약 내역 -> 조인

SELECT A.APNT_NO, P.PT_NAME, P.PT_NO, A.MCDP_CD, D.DR_NAME, A.APNT_YMD
FROM (
    SELECT *
    FROM APPOINTMENT
    WHERE APNT_YMD LIKE '2022-04-13%'
        AND MCDP_CD = 'CS'
        AND APNT_CNCL_YN = 'N'
) AS A, PATIENT AS P, DOCTOR AS D
WHERE A.PT_NO = P.PT_NO
    AND A.MDDR_ID = D.DR_ID
ORDER BY APNT_YMD ASC;


SELECT A.APNT_NO, P.PT_NAME, P.PT_NO, A.MCDP_CD, D.DR_NAME, A.APNT_YMD
FROM APPOINTMENT AS A, PATIENT AS P, DOCTOR AS D
WHERE A.APNT_YMD LIKE '2022-04-13%'
    AND A.MCDP_CD = 'CS'
    AND A.APNT_CNCL_YN = 'N'
    AND A.PT_NO = P.PT_NO
    AND A.MDDR_ID = D.DR_ID
ORDER BY APNT_YMD ASC;