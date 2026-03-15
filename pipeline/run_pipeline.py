from scripts.generate_sales_data import generate_sales
from scripts.load_to_mysql import insert_sales
from scripts.transform_sales import transform_sales
from scripts.predict_sales import predict_sales
from scripts.logger import log_pipeline
from config.db_config import get_connection
from datetime import datetime


def run_pipeline():

    pipeline_name = "sales_pipeline"
    run_id = int(datetime.now().timestamp())

    try:

        print("Generating data...")
        df = generate_sales()

        log_pipeline(run_id, pipeline_name, "generate_sales", "SUCCESS", len(df), "Sales data generated")

        print("Loading data to MySQL...")
        rows_loaded = insert_sales(df)

        log_pipeline(run_id, pipeline_name, "load_sales", "SUCCESS", rows_loaded, "Data inserted into raw_sales")

        print("Transforming data...")
        rows_transformed = transform_sales()

        log_pipeline(run_id, pipeline_name, "transform_sales", "SUCCESS", rows_transformed, "Data transformed")

        print("Generating predictions...")
        forecasts = predict_sales()

        log_pipeline(run_id, pipeline_name, "predict_sales", "SUCCESS", forecasts, "Forecasts generated")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE pipeline_metadata
        SET last_run_time = %s
        WHERE pipeline_name = 'sales_pipeline'
        """, (datetime.now(),))

        conn.commit()

        cursor.close()
        conn.close()

        print("Pipeline completed successfully")

    except Exception as e:

        log_pipeline(run_id, pipeline_name, "pipeline_failure", "FAILED", 0, str(e))

        print("Pipeline failed:", e)


if __name__ == "__main__":
    run_pipeline()