
-- BRONZE LAYER
CREATE TABLE raw_sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sale_date DATE,
    store_id INT,
    product_id INT,
    units_sold INT,
    price DECIMAL(10,2),
    promotion_flag INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- SILVER LAYER
CREATE TABLE sales_clean (
    id INT AUTO_INCREMENT PRIMARY KEY,
    raw_sales_id INT NOT NULL,
    sale_date DATE,
    store_id INT,
    product_id INT,
    units_sold INT,
    price DECIMAL(10,2),
    revenue DECIMAL(12,2),

    CONSTRAINT fk_raw_sales
    FOREIGN KEY (raw_sales_id)
    REFERENCES raw_sales(id),

    CONSTRAINT unique_raw_record
    UNIQUE (raw_sales_id)
);


-- GOLD LAYER
CREATE TABLE sales_predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    store_id INT NOT NULL,
    product_id INT NOT NULL,
    prediction_date DATE NOT NULL,
    predicted_sales INT,
    model_type VARCHAR(50) DEFAULT 'rolling_avg_7d',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY unique_prediction (store_id, product_id, prediction_date)
);


-- CREATE METADATA TABLE

CREATE TABLE pipeline_metadata (

pipeline_name VARCHAR(50) PRIMARY KEY,
last_run_time DATETIME

);

-- Insert first record:

INSERT INTO pipeline_metadata
VALUES ('sales_pipeline', '2000-01-01');




-- Check counts:

SELECT COUNT(*) FROM raw_sales;
SELECT COUNT(*) FROM sales_clean;
SELECT COUNT(*) FROM sales_predictions;




-- Create Logging Table

CREATE TABLE pipeline_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pipeline_name VARCHAR(100),
    step_name VARCHAR(100),
    status VARCHAR(20),
    rows_processed INT,
    log_message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Update pipeline_logs Table
ALTER TABLE pipeline_logs
ADD COLUMN run_id INT;