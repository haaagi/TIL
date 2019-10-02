-- SELECT DISTINCT age FROM users;

-- SELECT * FROM users WHERE age=30;
-- SELECT first_name FROM users WHERE age>=30 and last_name = '김';

-- SELECT last_name,age FROM users
-- WHERE age>=30 and last_name='김' LIMIT 10;  -- LIMIT 은 10개만 보겠다

-- <COUNT 소개>
-- SELECT COUNT(id) FROM users;

-- <AVG, SUM, MIN, MAX> -> 숫자 컬럼만 가능

-- 30살 이상인 사람들의 평균 나이
-- SELECT AVG(age) FROM users WHERE age>=30;

-- users에서 잔액이 가장 높은 사람과 잔액
-- SELECT MAX(balance), first_name FROM users;  --SELECT 에서 이미 MAX값을 찍어줘서 한 명밖에 안나와서 WHERE 문이 필요가 없다

-- 30살 이상인 사람들의 평균 잔액
-- SELECT AVG(balance) FROM users WHERE age>=30;

-- SELECT * FROM users WHERE age LIKE '2_';

-- SELECT * FROM users WHERE phone LIKE '02-%';

-- SELECT * FROM users WHERE first_name LIKE '%준';

-- SELECT * FROM users WHERE phone LIKE '%-5114-%';

-- <ORDER>

-- USERS 에서 나이순으로 오름차순 상위 10개
-- SELECT age, balance FROM users ORDER BY age,balance LIMIT 10;


SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;