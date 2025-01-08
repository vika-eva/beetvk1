---1
SELECT employees.first_name, employees.last_name, employees.department_id, department.department_name
FROM employees
CROSS JOIN department
WHERE employees.department_id = department.department_id;

---2
SELECT employees.first_name, employees.last_name, department.department_name, locations.city, locations.state_province
FROM employees, department
CROSS JOIN locations
WHERE employees.department_id = department.departament_id AND department.location_id = locations.location_id

---3
SELECT employees.first_name, employees.last_name, employees.department_id, department.department_name
FROM employees
JOIN department ON employees.department_id = department.department_id
WHERE employees.department_id = 80 OR employees.department_id = 40

---4
SELECT depart_name FROM departments
--- or
SELECT departaments.department_id, departaments.depart_name, employees.first_name
FROM departaments
FULL JOIN employees
ON departaments.department_id = employees.department_id

---5
SELECT Emp.first_name AS 'employee', Man.first_name AS 'manager'
FROM employees Emp
JOIN employees Man ON Emp.manager_id = Man.manager_id

---6
SELECT jobs.job_title, (first_name, last_name) AS 'full_name', jobs.max_salary - employees.salary AS 'difference'
FROM employees
JOIN jobs ON employees.job_id = jobs.job_id

---7
SELECT job_title, (max_salary - min_salary)/2 AS avarage
FROM jobs
---or
SELECT jobs.job_title, AVG(employees.salary) AS avarage
FROM employees
JOIN jobs ON employees.job_id = jobs.job_id
GROUP BY DESC

---8
SELECT (first_name, last_name) AS 'full_name', salary
FROM employees
JOIN department USING (department_id)
JOIN locations USING (location_id)
WHERE city = 'London'

---9
SELECT department_name AS 'dep_name', COUNT(*) AS 'empl'
FROM department
INNER JOIN employees
ON employees.department_id = department.department_id










