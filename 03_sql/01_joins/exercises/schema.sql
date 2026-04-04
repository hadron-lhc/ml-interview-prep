DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;


CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees VALUES
(1,'Ana','Engineering',90000),
(2,'Luis','Engineering',85000),
(3,'Carla','HR',70000),
(4,'Pedro','HR',72000),
(5,'Sofia','Sales',65000),
(6,'Tomas',NULL,60000);


CREATE TABLE departments (
    department TEXT,
    manager TEXT,
    budget INTEGER
);

INSERT INTO departments VALUES
('Engineering','Alice',500000),
('HR','Bob',200000),
('Sales','Charlie',300000);
