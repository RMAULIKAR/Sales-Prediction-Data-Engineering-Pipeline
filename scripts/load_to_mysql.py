from config.db_config import get_connection


def insert_sales(df):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO raw_sales
    (sale_date, store_id, product_id, units_sold, price, promotion_flag)
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    rows_inserted = 0

    for _, row in df.iterrows():

        cursor.execute(query, (
            row["sale_date"],
            row["store_id"],
            row["product_id"],
            row["units_sold"],
            row["price"],
            row["promotion_flag"]
        ))

        rows_inserted += 1

    conn.commit()

    cursor.close()
    conn.close()

    print(f"{rows_inserted} rows inserted into raw_sales")

    return rows_inserted