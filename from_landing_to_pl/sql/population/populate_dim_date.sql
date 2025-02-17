INSERT INTO walmart.dim_date (
    date_sk, full_date, day_of_week, day_of_month, day_of_year, week_of_year, 
    month, month_name, quarter, year
)
SELECT 
    ROW_NUMBER() OVER (ORDER BY full_date) + NVL((SELECT MAX(date_sk) FROM walmart.dim_date), 0) AS date_sk,
    full_date AS full_date,
    TO_CHAR(full_date, 'Day') AS day_of_week,
    EXTRACT(DAY FROM full_date) AS day_of_month,
    EXTRACT(DOY FROM full_date) AS day_of_year,
    EXTRACT(WEEK FROM full_date) AS week_of_year,
    EXTRACT(MONTH FROM full_date) AS month,
    TO_CHAR(full_date, 'Month') AS month_name,
    EXTRACT(QUARTER FROM full_date) AS quarter,
    EXTRACT(YEAR FROM full_date) AS year
FROM (
    SELECT DISTINCT DATE(order_date) AS full_date
    FROM landing.order
) AS dates;