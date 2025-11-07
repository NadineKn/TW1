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










# kod till 5. Top 3


import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd

def plot_top3_categories(df):
   
   
    kategori_sum = df.groupby("category")["revenue"].sum()
    top3 = kategori_sum.nlargest(3)

    ax = top3.plot(kind="bar", color="skyblue")
    plt.title("Top 3 kategorier baserat på omsättning")
    plt.ylabel("Total omsättning")
    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    plt.show()


def revenue_summary(df):
  
    kategori_sum = df.groupby("category")["revenue"].sum()
    kategori_sum = np.ceil(kategori_sum)  # avrunda uppåt
    total = np.ceil(df["revenue"].sum())

    print("Intäkt per kategori (avrundat uppåt):")
    print(kategori_sum)
    print(f"\nTotal intäkt (avrundat uppåt): {int(total)}")

    return kategori_sum, int(total)


def detect_anomalies(df, column="revenue", Z=3):
  
    mean = df[column].mean()
    std = df[column].std()
    condition = np.abs(df[column] - mean) > Z * std
    anomalies = df[condition]

    print(f"Antal dagar som avviker mer än {Z} standardavvikelser: {len(anomalies)}")
    return anomalies


