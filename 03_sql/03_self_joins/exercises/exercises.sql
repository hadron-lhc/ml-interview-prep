/*
EXERCISE 1

Return:

employee name
manager name

Requirement:

Keep employees without manager
*/

SELECT e.name AS employee_name, m.name AS manager_name
FROM employees e

LEFT JOIN employees m
ON e.manager_id = m.employee_id;


/*
EXERCISE 2

Return:

employee name
manager name
employee salary
manager salary
*/

SELECT e.name, m.name, e.salary, m.salary
FROM employees e
LEFT JOIN employees m
ON e.manager_id = m.employee_id;


/*
EXERCISE 3

Return:

employee name
manager name

Condition:

employee salary > manager salary

(Hint: comparison self join)
*/

SELECT e.name, m.name
FROM employees e
JOIN employees m
ON e.manager_id = m.employee_id
WHERE e.salary > m.salary;


/*
EXERCISE 4

Return:

manager name
number_of_reports

(Hint: GROUP BY manager)
*/

SELECT m.name, COUNT(e.employee_id)
FROM employees m
LEFT JOIN employees e
ON m.employee_id = e.manager_id
GROUP BY m.employee_id
HAVING COUNT(e.employee_id) > 0;


/*
EXERCISE 5

Return:

employee name
grandmanager name

(Hint: triple self join)
*/

SELECT e.name, p.name
FROM employees e

JOIN employees m
ON e.manager_id = m.employee_id

JOIN employees p
ON m.manager_id = p.employee_id

GROUP BY e.employee_id;


/*
EXERCISE 6

Return:

manager name
avg team salary

(Hint: aggregation self join)
*/


SELECT m.name, AVG(e.salary)
FROM employees m
JOIN employees e
ON m.employee_id = e.manager_id
GROUP BY m.employee_id


