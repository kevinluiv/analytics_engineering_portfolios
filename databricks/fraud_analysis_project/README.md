# Financial Fraud Detection: Databricks ETL & Analysis

## Purpose
This project was developed as a hands-on laboratory to master the **Databricks** environment, Spark Notebooks, and the **Medallion Architecture**. The goal was to build a complete pipeline—from raw data ingestion to business insights—using a large-scale financial dataset.

## Architecture: The Medallion Approach
- **Bronze Layer:** Ingested the raw Credit Card Fraud dataset (284k+ records) from Databricks sample datasets.
- **Silver Layer:** Performed data cleaning and enrichment by mapping anonymized `amountRange` into human-readable brackets and reformatting PII-protected vectors.
- **Gold Layer:** Conducted high-level analysis using **Spark SQL** to identify fraud rates per bracket and statistical correlations.

## Key Technical Skills
- **PySpark & Spark SQL:** Hybrid development for data manipulation.
- **Statistical Analysis:** Calculated Pearson Correlation to identify fraud patterns.
- **AI-Augmented Engineering:** Leveraged Databricks Assistant for code optimization and logic generation.