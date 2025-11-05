import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/ecommerce_sales.csv")

def get_df():
    return df

#Kod till 1. vad säljer vi?
unique_products = df["category"].unique()

category_revenue = df.groupby("category")["revenue"].sum().sort_values(ascending=False)


# Kod till 2. var säljer vi? vilka städer står för störst intäkt?
revenue_per_city = df.groupby('city')[['revenue']].sum()

top_cities = revenue_per_city.sort_values(by='revenue', ascending=False)

units_per_city = df.groupby(['city', 'category'])['units'].sum().unstack()

category_per_city = df.groupby(['city', 'category'])['revenue'].sum().unstack()


# Kod till 3. När säljer vi?

df_date = df.copy()

df_date["date"] = pd.to_datetime(df["date"])

df_date["month"] = df_date["date"].dt.month
df_date["day"] = df_date["date"].dt.day


revenue_by_day_of_month = df_date.groupby("day")["revenue"].sum().sort_values(ascending=False).round(2)
revenue_by_month = df_date.groupby("month")["revenue"].sum().sort_index(ascending=False)

# Kod till 4. Hur ser en typsik order ut?

def average_order(df):
  order_value = df["revenue"].agg(["mean", "std", "min", "max"])
  order_value.index = [
        "Genomsnittligt ordervärde:",
        "Standardavvikelse:",
        "Lägsta ordervärdet:",
        "Högsta ordervärdet:"
  ]
  for name, value in order_value.astype(int).items():
    print(f"{name} {value} kr")


# kod till 5. Top 3


# Summera intäkt per kategori
kategori_sum = df.groupby("category")["revenue"].sum()

# Plocka fram topp 3
top3 = kategori_sum.nlargest(3)

# Totala intäkten (avrundad uppåt till närmaste 500, med min 1000)
total = kategori_sum.sum()
total_rounded = max(1000, int(np.ceil(total / 500.0) * 500))

print("Top 3 kategorier baserat på omsättning:")
print(top3)
print(f"\nTotal omsättning: {total} (avrundad till {total_rounded})")

