import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/ecommerce_sales.csv")

def get_df():
    return df

#1. Vad säljer vi?

category_revenue = df.groupby("category")["revenue"].sum().sort_values(ascending=False)

plot_cat_rev = category_revenue.plot(kind="bar", title="Revenue per Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.grid(True, linestyle='-', linewidth=0.5)
plt.tight_layout()
plt.show()