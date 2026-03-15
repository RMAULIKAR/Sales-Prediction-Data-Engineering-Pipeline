# Sales Prediction Data Engineering Pipeline

## Overview

This project demonstrates an **end-to-end data engineering pipeline** for generating, processing, and loading sales data to support a sales prediction workflow. The pipeline simulates a typical production-style data workflow including **data generation, transformation, storage, and preparation for analytics or machine learning models**.

The project focuses on **data pipeline design, modular code organization, and reproducible workflows** using Python and SQL.

---


## Purpose

This project was created to demonstrate **data engineering pipeline design and implementation

---

## Project Structure

```
Sales-Prediction-Data-Engineering-Pipeline
│
├── config
│   └── db_config.py              # Database configuration
│
├── pipeline                     # Core pipeline modules
│   └── __init__.py
│
├── scripts                      # Pipeline scripts
│   ├── generate_sales_data.py    # Generate synthetic sales data
│   ├── load_to_mysql.py          # Load raw data to MySQL
│   ├── transform_sales.py        # Data transformation logic
│   ├── predict_sales.py          # Prediction script
│   ├── reset_tables.py           # Reset database tables
│   └── logger.py                 # Logging utility
│
├── sql
│   └── queries.sql               # SQL queries for database operations
│
├── requirements.txt              # Project dependencies
└── .gitignore                    # Ignored files for Git
```

---

## Pipeline Workflow

The pipeline follows a typical **data engineering workflow**:

1. **Data Generation**

   * Synthetic sales data is generated using Python.

2. **Data Ingestion**

   * Raw data is inserted into a MySQL database.

3. **Data Transformation**

   * Cleaning and transformation steps are applied.

4. **Data Storage**

   * Processed data is stored in structured database tables.

5. **Prediction**

   * Prepared data can be used for sales prediction models.

---

## Pipeline Architecture

```
Raw Data Generation
        │
        ▼
generate_sales_data.py
        │
        ▼
Raw Sales Data (CSV / Dataset)
        │
        ▼
load_to_mysql.py
        │
        ▼
MySQL Database
        │
        ▼
transform_sales.py
        │
        ▼
Cleaned / Transformed Data
        │
        ▼
predict_sales.py
        │
        ▼
Sales Prediction Output

```
## Technologies Used

* **Python**
* **MySQL**
* **SQL**
* **Git & GitHub**
* **Logging for pipeline monitoring**

---

## How to Run the Project

### 1. Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/Sales-Prediction-Data-Engineering-Pipeline.git
```

### 2. Navigate to the Project

```
cd Sales-Prediction-Data-Engineering-Pipeline
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Run the Pipeline

Generate data:

```
python scripts/generate_sales_data.py
```

Load data to MySQL:

```
python scripts/load_to_mysql.py
```

Transform data:

```
python scripts/transform_sales.py
```

Run prediction:

```
python scripts/predict_sales.py
```

---

## Key Features

* Modular pipeline structure
* Synthetic data generation for testing pipelines
* Database ingestion and transformation
* Logging support for debugging and monitoring
* Clean repository structure following data engineering best practices

---
