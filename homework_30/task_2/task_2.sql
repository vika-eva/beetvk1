SELECT first_name as 'first', last_name as 'last' FROM employees

SELECT employee_id FROM employees

SELECT * FROM employees ORDER BY first_name DESC

SELECT first_name, last_name, salary * 12 / 100 as 'PF' FROM employees

--- SELECT first_name, last_name, MAX(cast(salary as DECIMAL(9,2))) as 'max_salary', MIN(cast(salary as DECIMAL(9,2))) as min_salary FROM employees

SELECT first_name, last_name, MAX(salary) as max_salary, MIN(salary) as 'min_salary' FROM employees


SELECT first_name, last_name, round(salary/12, 2) + commission_pct as 'month_sal' FROM employees


