DROP TABLE IF EXISTS employees;

CREATE TABLE employees (

employee_id INTEGER,
name TEXT,
department TEXT,
salary INTEGER,
experience INTEGER

);

INSERT INTO employees VALUES
(1,'Ana','Engineering',95000,5),
(2,'Luis','Engineering',87000,4),
(3,'Carla','Engineering',91000,6),
(4,'Pedro','HR',72000,3),
(5,'Sofia','HR',68000,2),
(6,'Tomas','HR',70000,4),
(7,'Julia','Sales',65000,3),
(8,'Martin','Sales',62000,2),
(9,'Laura','Sales',64000,4),
(10,'Diego','Sales',66000,5);
