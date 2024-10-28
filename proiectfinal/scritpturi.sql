CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    country TEXT,
    registration_date DATE
);

-- Exemplu pentru primele 10 înregistrări
INSERT INTO customers (customer_id, name, email, country, registration_date) VALUES
(1, 'Alice Popescu', 'alice.popescu@example.com', 'Romania', '2022-01-15'),
(2, 'Bogdan Ionescu', 'bogdan.ionescu@example.com', 'Romania', '2022-02-18'),
(3, 'Carla Dinu', 'carla.dinu@example.com', 'Bulgaria', '2021-11-20'),
(4, 'Daniel Raducanu', 'daniel.raducanu@example.com', 'Hungary', '2021-12-05'),
(5, 'Elena Marinescu', 'elena.marinescu@example.com', 'Germany', '2022-03-11'),
(6, 'Fabian Moldovan', 'fabian.moldovan@example.com', 'Poland', '2022-04-10'),
(7, 'Georgiana Nastase', 'georgiana.nastase@example.com', 'Romania', '2021-10-30'),
(8, 'Horia Georgescu', 'horia.georgescu@example.com', 'France', '2021-09-12'),
(9, 'Irina Constantin', 'irina.constantin@example.com', 'Spain', '2022-02-25'),
(10, 'Janos Horvath', 'janos.horvath@example.com', 'Hungary', '2022-03-02');
-- Continuă inserarea până la 3.000 de înregistrări


CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    stock INTEGER
);

-- Exemplu pentru primele 10 înregistrări
INSERT INTO products (product_id, product_name, category, stock) VALUES
(1, 'Laptop', 'Electronics', 50),
(2, 'Smartphone', 'Electronics', 150),
(3, 'Office Chair', 'Furniture', 30),
(4, 'Desk Lamp', 'Furniture', 60),
(5, 'Backpack', 'Accessories', 200),
(6, 'Wireless Mouse', 'Electronics', 120),
(7, 'Keyboard', 'Electronics', 100),
(8, 'Monitor', 'Electronics', 80),
(9, 'Coffee Table', 'Furniture', 40),
(10, 'Desk Organizer', 'Accessories', 300);
-- Continuă inserarea până la 500 de înregistrări

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    order_date DATE,
    quantity INTEGER,
    price REAL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Exemplu pentru primele 10 înregistrări
INSERT INTO orders (order_id, customer_id, product_id, order_date, quantity, price) VALUES
(1, 1, 1, '2022-01-20', 1, 1200.00),
(2, 2, 2, '2022-02-25', 2, 700.00),
(3, 3, 3, '2021-11-22', 1, 150.00),
(4, 1, 4, '2022-02-28', 3, 50.00),
(5, 4, 5, '2021-12-10', 4, 25.00),
(6, 5, 2, '2022-03-15', 1, 700.00),
(7, 2, 7, '2022-02-18', 2, 45.00),
(8, 1, 8, '2022-04-05', 1, 300.00),
(9, 3, 9, '2021-11-30', 1, 80.00),
(10, 6, 10, '2022-03-10', 5, 20.00);
-- Continuă inserarea până la 10.000 de înregistrări


CREATE TABLE reviews (
    review_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    rating INTEGER,
    review_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Exemplu pentru primele 10 înregistrări
INSERT INTO reviews (review_id, customer_id, product_id, rating, review_date) VALUES
(1, 1, 1, 5, '2022-01-22'),
(2, 2, 2, 4, '2022-02-27'),
(3, 3, 3, 3, '2021-11-23'),
(4, 1, 4, 4, '2022-03-01'),
(5, 4, 5, 5, '2021-12-15'),
(6, 5, 2, 2, '2022-03-16'),
(7, 2, 7, 5, '2022-04-07'),
(8, 3, 8, 3, '2021-12-12'),
(9, 1, 9, 4, '2022-03-10'),
(10, 6, 10, 1, '2022-03-11');
-- Continuă inserarea până la 5.000 de înregistrări
