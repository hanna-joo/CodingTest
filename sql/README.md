# SQL
- 관계형 데이터베이스 관리 시스템의 데이터 관리하기 위해 설계된 프로그래밍 언어
- DDL (Data Definition L) : 정의
    - `CREATE`, `ALTER`, `DROP`
    - `RENAME`, `COMMENT`, `TRUNCATE`
- DML (Data Manipulation L) : 조작
    - `SELECT`
    - `INSERT`, `UPDATE`, `DELETE`
    - `MERGE`, `CALL`, `EXPLAIN PLAN`, `LOCK TABLE`
- DCL (Data Control L) : 제어
    - `GRANT`, `REVOKE`
- TCL (Transaction Control L)
    - `COMMIT`, `ROLLBACK`, `SAVEPOINT`, `TRANSACTION`

# DML
## 1. 기본 순서
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

## 2. SELECT
- DISTINCT : 중복 제거
- CONCAT() : 문자열 합치기
```sql
SELECT DISTINCT 컬럼1, CONCAT(컬럼2, 컬럼3)
FROM 테이블명
WHERE 조건
```

## 3. FROM
- 서브쿼리가 온다면 별칭(alias) 필수
- JOIN : 열 합치기
    - 종류
        - INNER 
        - LEFT / RIGHT / FULL OUTER
        - CROSS : 한 테이블의 모든 행(n)을 다른 테이블의 모든 행(m)과 조인해서 n*m행 생성
    - cf. UNION : 쿼리 사이에 넣기, 행 합치기(중복 값 삭제)
    - cf. UNION ALL : 행 합치기(중복 값 모두 포함)
```sql
SELECT 컬럼1, 컬럼2
FROM 테이블1
    INNER JOIN 테이블2
    ON 테이블1.id = 테이블2.id
WHERE 조건1
```

## 4. WHERE
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

## 5. GROUP BY
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

## 6. OVER
- 행 별로 특정 기준에 따라 필요한 집합을 구해 함수 적용 시 사용하는 구문
- Window Function 적용 전에 행 집합의 분할, 순서 결정
    - 행의 범위를 지정해주는 느낌
    - GROUP BY와 달리 행 개수에 영향을 미치지 않음(열 추가)
- 이동 평균, 누적 집계, 상위 N개의 값 등을 구하기 위해 함수 적용
    - 순위 : ROW_NUMBER(), RANK(), DENSE_RANK()
    - 집계 : SUM(), AVG(), COUNT(), MIN(), MAX()
- 인수
    - PARTITION BY : 쿼리 결과 집합을 파티션으로 분할
    - ORDER BY : 쿼리 결과 집합의 각 파티션 내에서 행의 순서 지정
    - ROWS/RANGE : 파티션 내의 시작점 및 끝점 지정(ORDER BY 필요)
    - 인수를 지정하지 않는 경우 전체에 Window Function 적용

### (1) PARTITION BY
- 쿼리 결과 집합을 파티션으로 분할
- Window Function은 각 파티션에 별도 적용
- 별도로 지정하지 않으면 단일 파티션으로 간주
- `PARTITION BY <value_expression>`
    - SELECT 절의 식, 별칭 참조 불가
    - 열, 식, 사용자 정의 변수 가능
```sql
-- 각 행에 min, max 열 추가 -> type별 가장 작은 값과 큰 값
SELECT object_id, type
    , [min] = min(object_id) OVER(partition by type)
    , [max] = max(object_id) OVER(partition by type)
from sys.objects
```

### (2) ORDER BY
- 쿼리 결과 집합의 각 파티션 내에서 행의 논리적 순서 정의
    - **파티션 내에서 행의 집합 정의**하는 기준
    - Window function이 수행되는 순서
- `ORDER BY <order_by_expression> [ASC | DESC]`
    - order_by_expression의 값이 같은 경우 Window Function을 같이 계산
```sql
-- 날짜에 따른 누적합
-- 날짜로 정렬 -> 집합 = 상위 행 + 자기 자신 -> 집합 범위에서 SUM()
SELECT 번호
  , 날짜
  , 수량
  , SUM(수량) OVER(ORDER BY 날짜) AS 재고
FROM 창고
```
- 이동평균과 누적합 구하기
```sql
-- 지역 별 연간 매출의 이동 평균과 누적 합계
SELECT BusinessEntityID, TerritoryID   
   , DATEPART(yy,ModifiedDate) AS SalesYear  
   , CONVERT(VARCHAR(20),SalesYTD,1) AS  SalesYTD  
   , CONVERT(VARCHAR(20),AVG(SalesYTD) OVER (
        -- 지역 별로 함수 적용
        PARTITION BY TerritoryID 
        -- 같은 연도의 데이터들은 한 번에 같이 평균 값 계산 > 누적
        ORDER BY DATEPART(yy,ModifiedDate)   
    ),1) AS MovingAvg  
   , CONVERT(VARCHAR(20),SUM(SalesYTD) OVER (
        PARTITION BY TerritoryID   
        ORDER BY DATEPART(yy,ModifiedDate)   
    ),1) AS CumulativeTotal  
FROM Sales.SalesPerson  
WHERE TerritoryID IS NULL OR TerritoryID < 5  
ORDER BY TerritoryID,SalesYear;
```

## 7. 쿼리 성능 개선
- SELECT
    - `*` 는 사용하지 말고 필요한 컬럼만 SELECT
    - DISTINCT
        - 중복 제거는 연산 시간 많이 소요
        - 가능하면 EXISTS + 서브쿼리 활용해서 대체 
        - GROUP BY 시 사용 금지 : 이미 그룹화하기 때문에 필요 없음
        - UNION 시 사용 금지 : UNION 에 중복 제거 기능 있음
- WHERE
    - LIKE : `%` 는 끝에 작성, 앞에 작성하면 Full Table Scan
    - EXISTS : 서브 쿼리의 결과가 많으면 IN 보다 나은 성능 (일치 항목이 발견되는 즉시 검색 프로세스 종료)
    - IN : 서브 쿼리의 결과가 적으면 사용 (모든 항목 비교)
    - 인덱스로 잡혀있는 컬럼은 WHERE, JOIN에서 함수화 함께 사용 금지
- GROUP BY
    - 가급적이면 WHERE 활용 : 쿼리 실행 시 WHERE 먼저 실행하기 때문에 미리 데이터 크기 작게 만들 수 있음
- ORDER BY
    - 서브 쿼리에서 사용 금지 : 비용 많이 발생
- 암시적 변환 금지
    - 암시적 변환 : 데이터 타입이 다른 경우 DB가 자동으로 타입 변환 및 값 비교
    - 불필요한 리소스 소모되므로 동일한 타입의 값만 비교

## REFERENCES
- [microsoft OVER 절](https://learn.microsoft.com/ko-kr/sql/t-sql/queries/select-over-clause-transact-sql?view=sql-server-ver15)
- [SQL OVER 절](https://velog.io/@wltn716/SQL-Over-%EC%A0%88)
- [간단하면서 쉬운 쿼리 최적화 방법](https://developer-talk.tistory.com/420)
- [쿼리 최적화: 빠른 쿼리를 위한 7가지 체크리스트](https://medium.com/watcha/%EC%BF%BC%EB%A6%AC-%EC%B5%9C%EC%A0%81%ED%99%94-%EC%B2%AB%EA%B1%B8%EC%9D%8C-%EB%B3%B4%EB%8B%A4-%EB%B9%A0%EB%A5%B8-%EC%BF%BC%EB%A6%AC%EB%A5%BC-%EC%9C%84%ED%95%9C-7%EA%B0%80%EC%A7%80-%EC%B2%B4%ED%81%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8-bafec9d2c073)
- [DB 개요](https://velog.io/@alicesykim95/DB-DDL-DML-DCL-TCL%EC%9D%B4%EB%9E%80)