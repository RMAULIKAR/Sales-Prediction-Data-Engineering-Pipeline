from scripts.generate_sales_data import generate_sales
from scripts.load_to_mysql import insert_sales
from scripts.transform_sales import transform_sales
from scripts.predict_sales import predict_sales
from config.db_config import get_connection
from datetime import datetime


def run_pipeline():

    print("Generating data...")
    df = generate_sales()

    print("Loading data to MySQL...")
    insert_sales(df)

    print("Transforming data...")
    transform_sales()

    print("Generating predictions...")
    predict_sales()

    # update pipeline metadata
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


if __name__ == "__main__":
    run_pipeline()