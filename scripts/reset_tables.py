from config.db_config import get_connection


def reset_tables():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM sales_predictions")
    cursor.execute("DELETE FROM sales_clean")
    cursor.execute("DELETE FROM raw_sales")

    conn.commit()

    cursor.close()
    conn.close()

    print("All tables reset")


if __name__ == "__main__":
    reset_tables()