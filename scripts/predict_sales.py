import pandas as pd
from config.db_config import get_connection
from datetime import timedelta


def predict_sales():

    conn = get_connection()

    query = """
    SELECT store_id, product_id, sale_date, units_sold
    FROM sales_clean
    ORDER BY store_id, product_id, sale_date
    """

    df = pd.read_sql(query, conn)

    if df.empty:
        print("No sales data available")
        conn.close()
        return 0

    df["rolling_avg"] = (
        df.groupby(["store_id", "product_id"])["units_sold"]
        .transform(lambda x: x.rolling(7).mean())
    )

    df_pred = df.dropna()

    if df_pred.empty:
        print("Not enough data → no prediction")
        conn.close()
        return 0

    latest = (
        df_pred.sort_values("sale_date")
        .groupby(["store_id", "product_id"])
        .tail(1)
        .copy()
    )

    latest["prediction_date"] = latest["sale_date"] + timedelta(days=1)
    latest["predicted_sales"] = latest["rolling_avg"].round().astype(int)

    cursor = conn.cursor()

    for _, row in latest.iterrows():

        cursor.execute("""
        INSERT INTO sales_predictions
        (store_id, product_id, prediction_date, predicted_sales)
        VALUES (%s,%s,%s,%s)
        ON DUPLICATE KEY UPDATE
            predicted_sales = VALUES(predicted_sales),
            created_at = CURRENT_TIMESTAMP
        """, (
            row["store_id"],
            row["product_id"],
            row["prediction_date"],
            row["predicted_sales"]
        ))

    conn.commit()

    forecasts_created = len(latest)

    cursor.close()
    conn.close()

    print(f"{forecasts_created} forecasts created/updated")

    return forecasts_created