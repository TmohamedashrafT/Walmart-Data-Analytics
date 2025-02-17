CREATE TABLE walmart.dim_customer (
    customer_sk INT,
    customer_id INT,
    customer_first_name VARCHAR(25),
    customer_last_name VARCHAR(25),
    customer_age INT,
    customer_city VARCHAR(25),
    customer_phone VARCHAR(25),
    customer_email VARCHAR(100),
    created_by VARCHAR(25),
    modified_by VARCHAR(25),
    created_at TIMESTAMP,
    modified_at TIMESTAMP
);