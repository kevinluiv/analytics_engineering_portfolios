# Advanced Semi-Structured Data Pipelines with PySpark & Databricks

This repository contains a hands-on practical implementation of advanced data transformation techniques using **Apache Spark (PySpark)**. Inspired by the core architectural concepts of the *Databricks Academy: Developing Applications with Apache Spark* course, this project demonstrates how to ingest, flatten, serialize, and infer schemas from complex, nested BPO (Business Process Outsourcing) interaction datasets.

## 1. Project Overview & Business Context
In modern Operations and Business Intelligence, interaction logs (Chats, Voice calls) often arrive with multi-layered, semi-structured metadata—such as customer profile tiers and dynamic post-interaction surveys. 

This notebook processes simulated BPO interaction records containing both **Nested Structs** and **Arrays of Structs**, transforming raw hierarchical formats into clean, flat, analytics-ready structures.

## 2. Technical Features & Spark Mechanics Applied

* **Strict Schema Definition:** Enforced data integrity using `StructType` and `StructField` to establish safe data ingestion of plain and nested fields.
* **Granular Data Flattening:** Implemented `F.explode_outer()` to deconstruct array elements into individual rows. Using the `outer` variant ensures that interactions without surveys (nulls) are preserved, preventing data loss.
* **Dynamic Schema Inference (`schema_of_json`):** Demonstrated a highly dynamic pattern for schema management. Programmatically converted complex columns to stringified JSON text (`to_json`), captured a memory-efficient `first()` sample row, and used `schema_of_json()` alongside `from_json()` to dynamically parse and reconstruct schemas without hardcoding.
* **Advanced Extraction (Dot Notation):** Utilized the dot-method notation (`column.field`) to effortlessly unnest structure fields into native, flat DataFrame columns.
* **Aggregation Awareness:** Emphasizes the optimal balance between exploding arrays for analytics and reversing the process using `collect_list()` or `collect_set()` to optimize data payloads for downstream consumption without incurring memory bottlenecks.

## 3. Data Transformation Flow

### Source Schema (Nested & Arrays)
```text
 |-- interaction_id: string
 |-- customer_name: string
 |-- channel: string
 |-- customer_details: struct
 |    |-- customer_id: string
 |    |-- tier: string
 |-- survey: array
 |    |-- element: struct
 |    |    |-- question_id: string
 |    |    |-- score: integer
 ```

 ### Outcome Schema
```text
 |-- interaction_id: string
 |-- customer_name: string
 |-- channel: string
 |-- customer_id: string
 |-- tier: string
 |-- question: string
 |-- score: integer
 ```