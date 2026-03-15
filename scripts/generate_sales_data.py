import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def generate_sales():

    records = []
    today = datetime.today().date()

    stores = range(1, 4)
    products = range(1, 6)

    min_days = 7
    min_rows = len(stores) * len(products) * min_days

    total_rows = np.random.randint(min_rows, 500)

    for _ in range(total_rows):

        store = np.random.choice(list(stores))
        product = np.random.choice(list(products))
        sale_day = today - timedelta(days=np.random.randint(0, min_days))

        units = np.random.randint(5, 50)
        price = np.random.randint(10, 100)

        records.append({
            "sale_date": sale_day,
            "store_id": store,
            "product_id": product,
            "units_sold": units,
            "price": price,
            "promotion_flag": np.random.randint(0, 2)
        })

    df = pd.DataFrame(records)

    return df