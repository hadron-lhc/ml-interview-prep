-- Drop tables if exist
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS events;

-- USERS
CREATE TABLE users (
    user_id INT,
    signup_date DATE
);

INSERT INTO users VALUES
(1, '2022-12-25'),
(2, '2023-01-01'),
(3, '2023-01-01'),
(4, '2023-01-01');

-- ORDERS
CREATE TABLE orders (
    user_id INT,
    order_date DATE,
    amount INT
);

INSERT INTO orders VALUES
-- user 1
(1, '2023-01-01', 100),
(1, '2023-01-10', 150),
(1, '2023-02-20', 80),
(1, '2023-02-25', 120),

-- user 2 (gap grande)
(2, '2023-01-01', 50),
(2, '2023-03-10', 300),

-- user 3
(3, '2023-01-01', 200),
(3, '2023-01-20', 220),
(3, '2023-01-25', 210),

-- user 4 (streaks)
(4, '2023-01-01', 100),
(4, '2023-01-02', 120),
(4, '2023-01-03', 140),
(4, '2023-01-04', 130),
(4, '2023-01-05', 150);

-- EVENTS (para sessionization)
CREATE TABLE events (
    user_id INT,
    ts TIMESTAMP
);

INSERT INTO events VALUES
-- user 1
(1, '2023-01-01 10:00'),
(1, '2023-01-01 10:20'),
(1, '2023-01-01 11:00'),
(1, '2023-02-15 09:00'),

-- user 2
(2, '2023-01-05 14:00'),
(2, '2023-01-05 14:50'),
(2, '2023-03-10 16:00'),

-- user 3 (cambio de día)
(3, '2023-01-01 23:50'),
(3, '2023-01-02 00:10'),
(3, '2023-01-02 00:20');
