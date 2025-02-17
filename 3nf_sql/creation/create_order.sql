CREATE TABLE landing.order (
    order_id INT,
    customer_id INT,
    store_id INT,
    order_date TIMESTAMP,
    total_amount DECIMAL(10, 2),
    created_by VARCHAR(50),
    created_at TIMESTAMP,
    modified_by VARCHAR(50),
    modified_at TIMESTAMP
);