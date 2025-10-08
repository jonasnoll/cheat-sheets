
# 1.629.034

-- Select all
SELECT * FROM your_table_name
LIMIT 3


-- Select Where
SELECT * FROM your_table_name
WHERE column_name=15
LIMIT 3

-- Get distinct values in column
SELECT DISTINCT column_name
FROM your_table_name;


-- Get count of distinct values in column
SELECT COUNT(DISTINCT column_name) AS unique_count
FROM your_table_name;


-- Get count of occourances of each distinct value in column
SELECT column_name, COUNT(*) AS occurrence_count
FROM your_table_name
GROUP BY column_name
ORDER BY occurrence_count DESC;


-- Get all entries where a column matches the first three distinct values that appear in the column
SELECT *
FROM my_table
WHERE column_name IN (
    SELECT DISTINCT column_name
    FROM my_table
    ORDER BY column_name
    LIMIT 3
);

-- Get how many unique days are available in date column
SELECT COUNT(DISTINCT DATE_TRUNC('day', date_column::timestamp)) AS unique_days_count
FROM my_table;