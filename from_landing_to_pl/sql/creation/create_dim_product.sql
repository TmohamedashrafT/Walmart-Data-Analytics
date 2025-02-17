CREATE TABLE walmart.dim_product (
    product_sk INT,
    product_id VARCHAR(50),
    product_name VARCHAR(255),
    product_brand VARCHAR(100),
    product_category VARCHAR(100),
    product_subcategory VARCHAR(100),
    product_weight DECIMAL(10, 2),
    product_price DECIMAL(18, 2),
    shelf_width DECIMAL(10, 2),
    shelf_height DECIMAL(10, 2),
    shelf_depth DECIMAL(10, 2),
    distance_from_cashier DECIMAL(10, 2),
    created_by VARCHAR(50),
    created_at TIMESTAMP,
    modified_by VARCHAR(50),
    modified_at TIMESTAMP
);