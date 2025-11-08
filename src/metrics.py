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

<<<<<<< HEAD
# Kod till 4. Hur ser en typsik order ut?
=======
# kod till 4. AOV

>>>>>>> dd8bdec0b1d43a5ef840e11cdeb331e80270a52b

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
    kategori_sum = np.ceil(kategori_sum)  # avrundar uppåt
    total = np.ceil(df["revenue"].sum())
 
    print("Intäkt per kategori (avrundat uppåt):")
    print(kategori_sum)
    print(f"\nTotal intäkt (avrundat uppåt): {int(total)}")
 
    return kategori_sum, int(total)

# Summera intäkt per kategori
kategori_sum = df.groupby("category")["revenue"].sum()

# Plocka fram topp 3
top3 = kategori_sum.nlargest(3)

# Totala intäkten (avrundad uppåt till närmaste 500, med min 1000)
total = kategori_sum.sum()
total_rounded = max(1000, int(np.ceil(total / 500.0) * 500))

# Kod till 6. Avvikelser (compute_z_scores, detect_anomalies)
def compute_z_scores(series):
    """
    Räknar ut z-värden, alltså hur långt varje värde är från medelvärdet.
    Om alla värden är lika blir resultatet nollor.
    """
    mean = series.mean()
    std = series.std(ddof=0)
    if std == 0:
        return series * 0
    return (series - mean) / std

def detect_anomalies(series, threshold=3.0):
    """
    Returnerar en serie värden där z-värdet är större än gränsen.
    """
    z = compute_z_scores(series)
    mask = z.abs() >= threshold
    return series[mask], z