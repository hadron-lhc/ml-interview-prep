DROP TABLE IF EXISTS employees;

CREATE TABLE employees (

employee_id INTEGER,
name TEXT,
manager_id INTEGER,
department TEXT,
salary INTEGER

);

INSERT INTO employees VALUES
(1,'Alice',NULL,'Engineering',120000),
(2,'Bob',1,'Engineering',90000),
(3,'Charlie',1,'Engineering',85000),
(4,'David',2,'Engineering',70000),
(5,'Eva',2,'Engineering',72000),
(6,'Frank',NULL,'HR',70000),
(7,'Grace',6,'HR',80000),
(8,'Helen',6,'HR',78000),
(9,'Ian',7,'HR',60000);
