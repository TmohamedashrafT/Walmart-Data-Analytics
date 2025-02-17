CREATE TABLE walmart.dim_promotion (
    promotion_sk INT,
    promotion_pk INT,
    promotion_name VARCHAR(100),
    promotion_discount DECIMAL(5, 2),
    promotion_category VARCHAR(50),
    start_date DATE,
    end_date DATE,
    last_updated TIMESTAMP
);