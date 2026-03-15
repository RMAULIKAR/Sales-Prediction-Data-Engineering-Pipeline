from config.db_config import get_connection


def log_pipeline(run_id, pipeline, step, status, rows=0, message=""):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO pipeline_logs
    (run_id, pipeline_name, step_name, status, rows_processed, log_message)
    VALUES (%s,%s,%s,%s,%s,%s)
    """, (run_id, pipeline, step, status, rows, message))

    conn.commit()

    cursor.close()
    conn.close()