CREATE TABLE walmart.fact_transaction (
    customer_id INT,
    promotion_sk INT,
    product_key INT,
    date_id INT,
    store_id INT,
    order_id INT,
    quantity INT,
    unit_price DECIMAL(18, 2),
    discount_price DECIMAL(18, 2),
    total_amount DECIMAL(18, 2)
);