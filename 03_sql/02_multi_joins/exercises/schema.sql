DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS projects;

CREATE TABLE employees (
    employee_id INTEGER,
    name TEXT,
    department_id INTEGER,
    salary INTEGER
);

INSERT INTO employees VALUES
(1,'Ana',1,90000),
(2,'Luis',1,85000),
(3,'Carla',2,70000),
(4,'Pedro',2,72000),
(5,'Sofia',3,65000),
(6,'Tomas',NULL,60000);

CREATE TABLE departments (
    department_id INTEGER,
    department_name TEXT,
    manager TEXT
);

INSERT INTO departments VALUES
(1,'Engineering','Alice'),
(2,'HR','Bob'),
(3,'Sales','Charlie');

CREATE TABLE locations (
    department_id INTEGER,
    city TEXT
);

INSERT INTO locations VALUES
(1,'New York'),
(2,'Chicago'),
(3,'San Francisco');

CREATE TABLE projects (
    project_id INTEGER,
    department_id INTEGER,
    project_name TEXT
);

INSERT INTO projects VALUES
(1,1,'ML Platform'),
(2,1,'Data Pipeline'),
(3,2,'Recruitment System'),
(4,3,'CRM Migration');
