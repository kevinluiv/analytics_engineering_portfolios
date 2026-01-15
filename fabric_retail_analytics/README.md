Retail Data Engineering & Analytics in Microsoft Fabric

This project implements a complete End-to-End Medallion Architecture using Microsoft Fabric. It processes raw retail transaction data from an initial ingestion stage through transformation and final business insight layers, utilizing PySpark, T-SQL, and DirectLake connectivity for Power BI.
Project ArchitectureThe project follows the Medallion Architecture (Bronze, Silver, Gold) to ensure data quality and traceability:
Bronze Layer: Raw CSV data ingested into OneLake and stored as Delta tables.
Silver Layer: Data cleaning, schema enforcement, and normalization using PySpark.
Gold Layer: Analytical views and business logic implemented via SQL Analytics Endpoint.

Repository Structure

fabric-retail-analytics/
│
├── README.md             <-- Technical project log and documentation
├── notebooks/            <-- PySpark ETL processes
│   └── 01_retail_medallion_etl.ipynb
│
└── database/             <-- SQL Database Project (Exported from Fabric)
    ├── Tables/           <-- Table definitions
    └── Views/            <-- Business Logic (v_total_revenue, v_top_5_customers, etc.)
Key Technical Achievements

Data Engineering: Developed automated ETL pipelines in PySpark to handle null values, type conversions, and Delta Lake optimizations.
Analytics Engineering: Built a robust semantic layer using T-SQL to extract KPIs such as Total Revenue and Customer Concentration.
Version Control: Implemented a professional Git workflow to track SQL schemas and Notebook versions.
BI Integration: Established DirectLake connectivity for real-time reporting in Power BI Desktop.
Technical Challenges & Solutions
Tenant Restrictions: Navigated workspace capacity limitations by utilizing Power BI Desktop via SQL Connection Strings to maintain development momentum.
Schema Versioning: Leveraged the "SQL Database Project" export feature to treat database objects as code within this repository.

Tools Used
Microsoft Fabric: Data Factory (Pipelines), OneLake, Lakehouse, and SQL Analytics Endpoint.Languages: PySpark (Python) and T-SQL.Visualization: Power BI Desktop.Version Control: Git & GitHub.Developed as part of a professional Data Engineering portfolio.