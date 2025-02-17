INSERT INTO walmart.dim_store (
    store_sk, store_id, Street_Adress, city, Postal_code
)
SELECT 
    ROW_NUMBER() OVER (ORDER BY s.store_id) + NVL((SELECT MAX(store_sk) FROM walmart.dim_store), 0) AS store_sk,
    s.store_id AS store_id,
    sa.street_address AS Street_Adress,
    ci.city_name AS city,
    ci.postal_code AS Postal_code
FROM landing.store s
JOIN landing.store_address sa ON s.store_id = sa.store_id
JOIN landing.city ci ON sa.city_id = ci.city_id;