/*
EXERCISE 1

Return:

department
number_of_employees
avg_salary
*/

SELECT department, COUNT(*), AVG(salary)
FROM employees
GROUP BY department;


/*
EXERCISE 2

Return:

department
avg_salary

Condition:

Only departments with avg salary > 75000

(Hint: HAVING)
*/

SELECT department, AVG(salary)
FROM employees
GROUP BY department
HAVING AVG(salary) > 75000;



/*
EXERCISE 3

Return:

department
max salary

(Hint: aggregation pattern)
*/


SELECT department, MAX(salary)
FROM employees
GROUP BY department;


/*
EXERCISE 4

Return:

department
total payroll

(sum of salaries)

(Hint: SUM)
*/

SELECT department, SUM(salary)
FROM employees
GROUP BY department;


/*
EXERCISE 5

Return:

department
number_of_senior_employees

Definition:

experience >= 5

(Hint: conditional count)
*/


SELECT department, COUNT(CASE WHEN experience >= 5 THEN 1 END)
FROM employees
GROUP BY department;


/*
EXERCISE 6

Return:

department
avg salary

Order by highest avg salary
Return only top department

(Hint:

GROUP
ORDER
LIMIT

Classic interview question)
*/

SELECT department, AVG(salary)
FROM employees
GROUP BY department
ORDER BY AVG(salary) DESC
LIMIT 1;


