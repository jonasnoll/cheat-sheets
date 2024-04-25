

-- Select all
SELECT * FROM your_table_name;


-- Get detinct values in column
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