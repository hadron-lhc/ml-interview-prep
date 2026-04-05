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
ON d.department_id = p.department_id;


/*
EXERCISE 4

Return:
employee name
department name
project name

Requirement:
Keep employees without department.
 */

SELECT e.name, d.department_name, p.project_name
FROM employees e

LEFT JOIN departments d
ON e.department_id = d.department_id

LEFT JOIN projects p
ON d.department_id = p.department_id;


/*
EXERCISE 5

Return:
department name
number_of_projects
number_of_employees

(Hint: cuidado con COUNT)

 */

SELECT
    d.department_name,
    count(DISTINCT p.project_id) as canti_project,
    count(DISTINCT e.employee_id) as cantidad_enployees
FROM departments d

LEFT JOIN employees e
ON d.department_id = e.department_id

JOIN projects p
ON d.department_id = p.department_id

GROUP BY d.department_name;


/*
EXERCISE 6

Return:
employee name
department name
salary

Condition:
Only employees from departments with more than 1 project.

(Hint mental):
JOIN
GROUP
FILTER GROUP
JOIN BACK

 */


SELECT
    e.name,
    d.department_name,
    e.salary
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.department_id
WHERE e.department_id IN (
    SELECT department_id
    FROM projects
    GROUP BY department_id
    HAVING COUNT(project_id) > 1
);
