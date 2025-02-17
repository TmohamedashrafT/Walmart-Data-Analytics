INSERT INTO walmart.fact_transaction (
    customer_id, promotion_sk, product_key, date_id, store_id, order_id, 
    quantity, unit_price, discount_price, total_amount
)
SELECT 
    o.customer_id AS customer_id,
    dp.promotion_sk AS promotion_sk,
    dpr.product_sk AS product_key,
    dd.date_sk AS date_id,
    o.store_id AS store_id,
    o.order_id AS order_id,
    oi.quantity AS quantity,
    p.product_price AS unit_price,
    p.product_price * (1 - pr.promotion_discount) AS discount_price,
    o.total_amount AS total_amount
FROM landing.order o
JOIN landing.order_items oi ON o.order_id = oi.order_id
JOIN landing.product p ON oi.product_id = p.product_id
LEFT JOIN landing.promotion pr ON oi.promotion_id = pr.promotion_pk
LEFT JOIN walmart.dim_promotion dp ON pr.promotion_pk = dp.promotion_pk
LEFT JOIN walmart.dim_product dpr ON p.product_id = dpr.product_id
LEFT JOIN walmart.dim_date dd ON DATE(o.order_date) = dd.full_date;
