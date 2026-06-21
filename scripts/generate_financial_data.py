import pandas as pd
import numpy as np

np.random.seed(42)

months = pd.date_range(
    start="2022-01-01",
    periods=36,
    freq="ME"
)

departments = [
    "Sales",
    "Marketing",
    "Operations",
    "Finance",
    "IT"
]

rows = []

for month in months:

    for dept in departments:

        revenue = np.random.randint(
            50000,
            200000
        )

        expenses = np.random.randint(
            25000,
            120000
        )

        profit = revenue - expenses

        investment = np.random.randint(
            10000,
            50000
        )

        roi = (
            profit /
            investment
        ) * 100

        rows.append({

            "Month": month,

            "Department": dept,

            "Revenue": revenue,

            "Expenses": expenses,

            "Profit": profit,

            "Investment": investment,

            "ROI": round(roi, 2)

        })

df = pd.DataFrame(rows)

df.to_csv(
    "../data/financial_data.csv",
    index=False
)

print("financial_data.csv created")