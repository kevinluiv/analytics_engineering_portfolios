-- Auto Generated (Do not modify) 7B7E2CDE9F29DA398D8640C4650BE3599D3CFB43AEE000348012ED09C2E16D3D
CREATE VIEW top_3_contries_per_spent AS
SELECT TOP 3 Country, ROUND(SUM(Quantity * UnitPrice), 2) AS total_spent
FROM silver_retail_dataset
GROUP BY Country
ORDER BY 2 DESC;