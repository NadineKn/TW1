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

# Kod till 3. När säljer vi? Tidsmönster/Säsong

df_date = df.copy()

df_date["date"] = pd.to_datetime(df["date"])

df_date["month"] = df_date["date"].dt.month
df_date["day"] = df_date["date"].dt.day


revenue_by_day_of_month = df_date.groupby("day")["revenue"].sum().sort_values(ascending=False).head(10)
revenue_by_month = df_date.groupby("month")["revenue"].sum().sort_index(ascending=False)




