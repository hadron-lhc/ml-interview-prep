DROP TABLE IF EXISTS logins;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS events;

CREATE TABLE logins (
    user_id INTEGER,
    login_date DATE
);

INSERT INTO logins VALUES
(1, '2024-01-01'),
(1, '2024-01-02'),
(1, '2024-01-03'),
(1, '2024-01-08'),
(1, '2024-01-09'),

(2, '2024-01-01'),
(2, '2024-01-03'),
(2, '2024-01-04'),
(2, '2024-01-05'),

(3, '2024-01-10');


CREATE TABLE orders (
    user_id INTEGER,
    order_date DATE,
    amount INTEGER
);

INSERT INTO orders VALUES
(1, '2024-01-01', 100),
(1, '2024-01-20', 50),
(1, '2024-03-01', 75),

(2, '2024-01-05', 30),
(2, '2024-01-06', 40),
(2, '2024-02-20', 90);


CREATE TABLE events (
    user_id INTEGER,
    event_time DATETIME
);

INSERT INTO events VALUES
(1, '2024-01-01 10:00:00'),
(1, '2024-01-01 10:05:00'),
(1, '2024-01-01 10:50:00'),
(1, '2024-01-01 11:00:00'),

(2, '2024-01-01 09:00:00'),
(2, '2024-01-01 09:10:00'),
(2, '2024-01-01 12:00:00');
