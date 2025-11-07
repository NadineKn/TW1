import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/ecommerce_sales.csv")

def get_df():
    return df

#1. Vad säljer vi?

#category_revenue = df.groupby("category")["revenue"].sum().sort_values(ascending=False)

#plot_cat_rev = category_revenue.plot(kind="bar", title="Revenue per Category")
#plt.xlabel("Category")
#plt.ylabel("Revenue")
#plt.grid(True, linestyle='-', linewidth=0.5)
#plt.tight_layout()
#plt.show()

# 2, var säljer vi?

# category_per_city = df.groupby(['city', 'category'])['revenue'].sum().unstack()

# fig, ax = plt.subplots()
# category_per_city.plot(kind='bar', ax=ax)
# ax.set_title("Intäkter per stad och kategori")
# ax.set_xlabel("Stad")
# ax.set_ylabel("Intäkt")
# ax.grid(True, axis='y')
# plt.tight_layout()
# plt.show()

# # 3, när säljer vi?
# from metrics import revenue_by_month, revenue_by_day_of_month

# # Monthly
# plt.plot(revenue_by_month.index, revenue_by_month.values)
# plt.xlabel("Månad")
# plt.ylabel("Intäkt")
# plt.title("Intäkt per månad")
# plt.grid(True)
# plt.tight_layout()
# plt.show()

# # What day of the month
# plt.bar(revenue_by_day_of_month.index, revenue_by_day_of_month.values)
# plt.xlabel("Dag")
# plt.ylabel("Intäkt")
# plt.title("Månadens bäst säljande dagar")
# plt.grid(True)
# plt.tight_layout()
# plt.show()

#4. AOV


#5. Top-3 kategorier

# import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker

# kategori_sum = df.groupby("category")["revenue"].sum()
# top3 = kategori_sum.nlargest(3)
# top3.plot(kind="bar", color="skyblue")

# plt.title("Top 3 kategorier baserat på omsättning")
# plt.ylabel("Total omsättning")

# # Visa hela tal istället för 1e6
# plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

#plt.show()

# Kod till 6. Avvikelser (Henrik)
def plot_anomalies(daily_revenue, anomalies, z, Z=3.0):
    """
    Ritar grafer över daglig intäkt och z-poäng med avvikelser markerade.
    """
    print(f"Antal dagar som avviker mer än {Z} standardavvikelser: {len(anomalies)}")

    fig1 = plt.figure(figsize=(9, 4))
    plt.plot(daily_revenue.index, daily_revenue.values, label="Daglig intäkt")
    if len(anomalies) > 0:
        plt.scatter(
            anomalies.index, anomalies.values,
            s=50, color="red",
            label=f"Avvikande dagar över {Z} std",
        )
    plt.title("Daglig intäkt")
    plt.xlabel("Datum")
    plt.ylabel("Intäkt i kr")
    plt.legend(loc="upper right")
    plt.grid(True, axis="y", linestyle=":", alpha=0.8)
    plt.tight_layout()
    #plt.show()

  
    fig2 = plt.figure(figsize=(9, 2.8))
    plt.scatter(z, np.zeros_like(z), s=20)
    plt.axvline(0,  color="black", linestyle="-",  linewidth=1, label="Medel")
    plt.axvline(-Z, color="red",   linestyle="--", linewidth=1, label=f"-{Z} std")
    plt.axvline( Z, color="red",   linestyle="--", linewidth=1, label=f"+{Z} std")
    plt.yticks([])
    plt.xlabel("Z-poäng")
    plt.title("Fördelning av Z-poäng")
    plt.legend(loc="upper right")
    plt.tight_layout()
    #plt.show()
    return fig1, fig2
