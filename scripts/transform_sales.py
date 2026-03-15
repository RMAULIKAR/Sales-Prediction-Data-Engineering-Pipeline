import pandas as pd
from config.db_config import get_connection


def transform_sales():

    conn = get_connection()

    query = """
    SELECT *
    FROM raw_sales
    WHERE id NOT IN (
        SELECT raw_sales_id FROM sales_clean
    )
    """

    df = pd.read_sql(query, conn)

    if df.empty:
        print("No new rows to clean")
        conn.close()
        return 0

    df["revenue"] = df["units_sold"] * df["price"]

    cursor = conn.cursor()

    for _, row in df.iterrows():

        cursor.execute("""
        INSERT INTO sales_clean
        (raw_sales_id, sale_date, store_id, product_id, units_sold, price, revenue)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """, (
            row["id"],
            row["sale_date"],
            row["store_id"],
            row["product_id"],
            row["units_sold"],
            row["price"],
            row["revenue"]
        ))

    conn.commit()

    rows_processed = len(df)

    cursor.close()
    conn.close()

    print(f"{rows_processed} new rows cleaned")

    return rows_processed