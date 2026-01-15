-- Auto Generated (Do not modify) 9E26A807617976AB01A177073A7471B875824B72E7CB1656C38E89855C4323F3
CREATE VIEW top_5_customers_per_spent AS
SELECT TOP 5 CustomerID, ROUND(SUM(Quantity * UnitPrice), 2) AS total_spent
FROM silver_retail_dataset
GROUP BY CustomerID
ORDER BY 2 DESC;