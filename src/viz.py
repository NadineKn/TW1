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




#5. Top-3 kategorier

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

kategori_sum = df.groupby("category")["revenue"].sum()
top3 = kategori_sum.nlargest(3)
top3.plot(kind="bar", color="skyblue")

plt.title("Top 3 kategorier baserat på omsättning")
plt.ylabel("Total omsättning")

# Visa hela tal istället för 1e6
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

plt.show()
