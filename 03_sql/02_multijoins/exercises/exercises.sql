/*
EXERCISE 1

Return:

employee name
department name
manager
city
*/

SELECT e.name, d.department_name, d.manager, l.city
FROM employees e

LEFT JOIN departments d
ON e.department_id = d.department_id

LEFT JOIN locations l
ON d.department_id = l.department_id;



/*
EXERCISE 2

Return:

department name
number of employees
avg salary
*/

SELECT d.department_name, COUNT(*) as count_employees, AVG(e.salary) as avg_salary
FROM employees e
JOIN departments d
ON e.department_id = d.department_id
GROUP BY d.department_id
ORDER BY avg_salary DESC;



/*
EXERCISE 3

Return:

employee name
project name
department name

(Hint: chain joins)
*/

SELECT e.name, p.project_name, d.department_name
FROM employees e

LEFT JOIN departments d
ON e.department_id = d.department_id

LEFT JOIN projects p
ON d.department_id = p.department_id

