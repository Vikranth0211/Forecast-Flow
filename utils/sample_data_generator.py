import pandas as pd
import numpy as np

def generate_sample_dataset(filepath="sample_sales_data.csv", products=None, n_per_product=30):
    if products is None:
        products = ['Product A', 'Product B', 'Product C', 'Product D']

    np.random.seed(42)
    records = []
    for product in products:
        for i in range(n_per_product):
            month1 = np.random.randint(1000, 5000)
            month2 = np.random.randint(1000, 5000)
            noise = np.random.normal(0, 200)
            month3 = int(0.5 * month1 + 0.5 * month2 + noise)
            promo = np.random.choice([0, 1])
            holiday = np.random.choice([0, 1])
            date = pd.Timestamp('2023-01-01') + pd.DateOffset(months=i)
            records.append([product, month1, month2, month3, promo, holiday, date])

    df = pd.DataFrame(records, columns=[
        'Product', 'Month1', 'Month2', 'Month3', 'Promo', 'Holiday', 'Date'
    ])
    df.to_csv(filepath, index=False)
    return df
