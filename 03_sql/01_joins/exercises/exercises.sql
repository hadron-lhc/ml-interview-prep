/* 
EXERCISE 1

Return:

name
department
manager
salary
*/

SELECT e.name, e.department, d.manager, e.salary
FROM employees e
JOIN departments d
ON d.department = e.department;


/*
EXERCISE 2

Return all employees even if department missing.
*/


SELECT e.name, e.department, d.manager, e.salary
FROM employees e
LEFT JOIN departments d
ON d.department = e.department;



/*
EXERCISE 3

Find employees without manager.
*/


SELECT e.name, e.department, d.manager, e.salary
FROM employees e
LEFT JOIN departments d
ON d.department = e.department
WHERE d.department is NULL;

/*
EXERCISE 4

Return:
employee name
salary
manager

Condition:
salary > 75000

Requirement:
Keep employees even if department missing.
 */

SELECT e.name, e.salary, d.manager
FROM employees e
LEFT JOIN departments d
ON e.department = d.department
WHERE e.salary > 75000;


/*
EXERCISE 5

Return:
manager
number_of_employees
avg_salary
 */


SELECT d.manager, COUNT(*) as number_of_employees, AVG(e.salary) as avg_salary
FROM employees e
JOIN departments d
ON d.department = e.department
GROUP BY d.manager;


/*
EXERCISE 6

Return:
department
avg_salary

Hint (interview thinking):
JOIN
GROUP BY
ORDER BY
LIMIT
 */

SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department
ORDER BY AVG(salary) DESC
LIMIT 1;
