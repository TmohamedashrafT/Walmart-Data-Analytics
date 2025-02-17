INSERT INTO walmart.dim_product (
    product_sk, product_id, product_name, product_brand, product_category, 
    product_subcategory, product_weight, product_price, shelf_width, shelf_height, 
    shelf_depth, distance_from_cashier, created_by, created_at, modified_by, modified_at
)
SELECT 
    ROW_NUMBER() OVER (ORDER BY p.product_id) + NVL((SELECT MAX(product_sk) FROM walmart.dim_product), 0) AS product_sk,
    p.product_id AS product_id,
    p.product_name AS product_name,
    b.brand_name AS product_brand,
    cat.category_name AS product_category,
    sc.subcategory_name AS product_subcategory,
    p.product_weight AS product_weight,
    p.product_price AS product_price,
    p.shelf_width AS shelf_width,
    p.shelf_height AS shelf_height,
    p.shelf_depth AS shelf_depth,
    p.distance_from_cashier AS distance_from_cashier,
    p.created_by AS created_by,
    p.created_at AS created_at,
    p.modified_by AS modified_by,
    p.modified_at AS modified_at
FROM landing.product p
LEFT JOIN landing.brand b ON p.brand_id = b.brand_id
LEFT JOIN landing.subcategory sc ON p.product_subcategory_id = sc.subcategory_id
LEFT JOIN landing.category cat ON sc.category_id = cat.category_id;