CREATE TABLE landing.order_items (
    order_item_id INT,
    order_id INT,
    product_id VARCHAR(50),
    quantity INT,
    promotion_id INT,
    created_by VARCHAR(50),
    created_at TIMESTAMP,
    modified_by VARCHAR(50),
    modified_at TIMESTAMP
);