INSERT INTO walmart.dim_promotion (
    promotion_sk, promotion_pk, promotion_name, promotion_discount, promotion_category, 
    start_date, end_date, last_updated
)
SELECT 
    ROW_NUMBER() OVER (ORDER BY promotion_pk) + NVL((SELECT MAX(promotion_sk) FROM walmart.dim_promotion), 0) AS promotion_sk,
    promotion_pk AS promotion_pk,
    promotion_name AS promotion_name,
    promotion_discount AS promotion_discount,
    promotion_category AS promotion_category,
    start_date AS start_date,
    end_date AS end_date,
    last_updated AS last_updated
FROM landing.promotion;
