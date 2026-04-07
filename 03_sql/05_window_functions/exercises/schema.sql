CREATE TABLE departments(
    id INTEGER PRIMARY KEY,
    name TEXT
);

INSERT INTO departments VALUES
(1,'Engineering'),
(2,'HR'),
(3,'Sales');

CREATE TABLE employees(
    id INTEGER PRIMARY KEY,
    name TEXT,
    department_id INTEGER,
    salary INTEGER,
    hire_date DATE,

    FOREIGN KEY(department_id)
    REFERENCES departments(id)
);

INSERT INTO employees VALUES
(1,'Ana',1,95000,'2020-01-10'),
(2,'Luis',1,87000,'2021-03-15'),
(3,'Carla',1,91000,'2019-07-23'),
(4,'Pedro',2,72000,'2018-02-11'),
(5,'Sofia',2,68000,'2022-06-01'),
(6,'Martin',3,78000,'2020-09-05'),
(7,'Julia',3,82000,'2017-11-19');


CREATE TABLE customers(
    id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
);

INSERT INTO customers VALUES
(1,'Alice','NY'),
(2,'Bob','LA'),
(3,'Charlie','Chicago'),
(4,'Diana','Miami'),
(5,'Eve','Boston');


CREATE TABLE orders(
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    employee_id INTEGER,
    order_date DATE,
    amount INTEGER,

    FOREIGN KEY(customer_id)
    REFERENCES customers(id),

    FOREIGN KEY(employee_id)
    REFERENCES employees(id)
);

INSERT INTO orders VALUES
(1,1,1,'2023-01-10',500),
(2,2,2,'2023-01-12',700),
(3,3,7,'2023-01-15',400),
(4,1,3,'2023-02-01',900),
(5,4,4,'2023-02-03',650),
(6,5,7,'2023-02-10',300),
(7,2,6,'2023-02-14',750),
(8,3,1,'2023-03-01',820),
(9,4,2,'2023-03-03',610),
(10,1,5,'2023-03-05',990),
(11,1,7,'2023-03-09',990)
