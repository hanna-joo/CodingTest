-- problem : https://school.programmers.co.kr/learn/courses/30/lessons/164668
-- 완료된 중고거래 총금액이 70만원 이상인 사람
-- 조회 : 회원ID, 닉네임, 총거래금액
-- 정렬 : 총거래금액 ASC

SELECT B.USER_ID, B.NICKNAME, SUM(PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD AS A
    JOIN USED_GOODS_USER AS B
    ON A.WRITER_ID = B.USER_ID
WHERE A.STATUS = 'DONE'
GROUP BY WRITER_ID
HAVING SUM(PRICE) >= 700000
ORDER BY TOTAL_SALES ASC;