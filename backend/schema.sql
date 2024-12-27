CREATE TABLE orders (
    order_id VARCHAR(50) PRIMARY KEY,
    user_id VARCHAR(50),
    product_id VARCHAR(50),
    amount FLOAT
);

CREATE TABLE payments (
    payment_id VARCHAR(50) PRIMARY KEY,
    order_id VARCHAR(50),
    status VARCHAR(20)
);

CREATE TABLE inventory (
    product_id VARCHAR(50) PRIMARY KEY,
    stock INT
);
