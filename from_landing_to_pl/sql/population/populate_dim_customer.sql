INSERT INTO walmart.dim_customer (
    customer_sk, customer_id, customer_first_name, customer_last_name, customer_age, 
    customer_city, customer_phone, customer_email, created_by, modified_by, created_at, modified_at
)
SELECT 
    ROW_NUMBER() OVER (ORDER BY c.customer_id) + NVL((SELECT MAX(customer_sk) FROM walmart.dim_customer), 0) AS customer_sk,
    c.customer_id AS customer_id,
    c.customer_first_name AS customer_first_name,
    c.customer_last_name AS customer_last_name,
    c.customer_age AS customer_age,
    ci.city_name AS customer_city,
    c.phone AS customer_phone,
    c.customer_email AS customer_email,
    c.created_by AS created_by,
    c.modified_by AS modified_by,
    c.created_at AS created_at,
    c.modified_at AS modified_at
FROM landing.customer c
LEFT JOIN landing.city ci ON c.city_id = ci.city_id;