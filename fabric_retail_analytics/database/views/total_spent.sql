-- Auto Generated (Do not modify) 212A15442B6AE55374F7F846259980EE74C9F34EDA7FB4EF86179DE5181EBCDA
CREATE VIEW total_spent AS
SELECT ROUND(SUM(Quantity * UnitPrice), 2) AS total_spent
FROM silver_retail_dataset;