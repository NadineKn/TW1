
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

# 3, när säljer vi?
from metrics import revenue_by_month, revenue_by_day_of_month

# Monthly
plt.plot(revenue_by_month.index, revenue_by_month.values)
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.title("Revenue by month")
plt.grid(True)
plt.tight_layout()
plt.show()

# What day of the month
plt.bar(revenue_by_day_of_month.index, revenue_by_day_of_month.values)
plt.xlabel("Day")
plt.ylabel("Revenue")
plt.title("Best selling days of the months")
plt.grid(True)
plt.tight_layout()
plt.show()

# 4, Hur ser en typisk order ut? AOV och spridning

# Average order value and distribution
fig, (ax_hist, ax_box) = plt.subplots(2, 1, figsize=(10, 6), gridspec_kw={"height_ratios":[4,1]})

ax_hist.hist(df["revenue"], bins=50)
ax_hist.set_title("Distribution of Order Values")

ax_hist.set_ylabel("Number of Orders")
ax_hist.grid(True, axis="y")

ax_box.boxplot(df["revenue"], vert=False)
ax_box.set_xlabel("Order Value (SEK)")
ax_box.set_yticklabels("")
ax_box.grid(True, axis="x")
plt.tight_layout()


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

plt.show()

