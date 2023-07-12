# SQL

## 기본 순서
```sql
SELECT 컬럼1, 컬럼2
FROM 테이블명
WHERE 조건1
AND 조건2
GROUP BY 컬럼
HAVING 조건절
ORDER BY 컬럼
LIMIT 숫자
```

## SELECT
- DISTINCT : 중복 제거
- CONCAT() : 문자열 합치기
```sql
SELECT DISTINCT 컬럼1, CONCAT(컬럼2, 컬럼3)
FROM 테이블명
WHERE 조건
```

## FROM
- 서브쿼리가 온다면 별칭(alias) 필수
- JOIN
    - INNER
    - LEFT / RIGHT / FULL OUTER
    - CROSS
        - 한 테이블의 모든 행(n)을 다른 테이블의 모든 행(m)과 조인해서 n*m행 생성
```sql
SELECT 컬럼1, 컬럼2
FROM 테이블1
    INNER JOIN 테이블2
    ON 테이블1.id = 테이블2.id
WHERE 조건1
```

## WHERE
```sql
SELECT *
FROM members
WHERE age >= 20
AND height BETWEEN 160 AND 170
AND addr IN ('경기', '인천', '세종')
AND name LIKE '김%'
AND drink LIKE '__콜라'
AND phone IS NOT NULL
ORDER BY height DESC, age
LIMIT 10
```

## GROUP BY
- 집계 함수와 함께 사용
    - COUNT(*) : 모든 행 개수
    - COUNT(DISTINCT) : 중복 제외 모든 행 개수
    - COUNT(컬럼) : 해당 컬럼에서 NULL값 제외한 행 개수
- 집계 함수는 
    - WHERE 절 (X)
    - HAVING 절 (O)
    - ORDER BY 절 (O)
```sql
SELECT SUM(salary-age), AVG(age), MIN(height), COUNT(*), COUNT(phone), COUNT(DISTINCT)
FROM members
GROUP BY id
HAVING SUM(salary) >= 1000
ORDER BY SUM(salary)
```

## OVER
- 행 별로 특정 기준에 따라 필요한 집합을 구해 함수 적용 시 사용하는 구문
- 행과 행 간의 관계를 정의하는 함수인 WINDOW FUNCTION
- 행의 범위를 지정해주는 느낌
### (1) ORDER BY
- 행 집합을 정의하는 기준
```sql
-- 날짜에 따른 누적합
-- 날짜로 정렬 -> 집합 = 상위 행 + 자기 자신 -> 집합 범위에서 SUM()

```

### (2) PARTITION BY


## 쿼리 성능 개선
- `*` 사용하지 말고 필요한 컬럼만 SELECT

## REFERENCES
- [SQL OVER 절](https://velog.io/@wltn716/SQL-Over-%EC%A0%88)