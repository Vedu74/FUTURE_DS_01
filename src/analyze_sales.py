import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "sales_data_sample.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["month"] = df["order_date"].dt.to_period("M").astype(str)
    return df

def save_charts(df: pd.DataFrame) -> None:
    monthly = df.groupby(df["order_date"].dt.to_period("M")).agg(
        revenue=("sales", "sum"),
        profit=("profit", "sum"),
        orders=("order_id", "count"),
    ).reset_index()
    monthly["month"] = monthly["order_date"].astype(str)

    top_products = df.groupby("product_name").agg(
        revenue=("sales", "sum"),
        profit=("profit", "sum"),
        orders=("order_id", "count"),
    ).sort_values("revenue", ascending=False)

    top_categories = df.groupby("category").agg(
        revenue=("sales", "sum"),
        profit=("profit", "sum"),
        orders=("order_id", "count"),
    ).sort_values("revenue", ascending=False)

    top_regions = df.groupby("region").agg(
        revenue=("sales", "sum"),
        profit=("profit", "sum"),
        orders=("order_id", "count"),
    ).sort_values("revenue", ascending=False)

    plt.figure(figsize=(10, 5))
    plt.plot(monthly["month"], monthly["revenue"], marker="o")
    plt.xticks(rotation=45, ha="right")
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "revenue_trend.png", dpi=200)
    plt.close()

    plt.figure(figsize=(10, 5))
    top_products.head(7)["revenue"].sort_values().plot(kind="barh")
    plt.title("Top Products by Revenue")
    plt.xlabel("Revenue")
    plt.ylabel("Product")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "top_products.png", dpi=200)
    plt.close()

    plt.figure(figsize=(8, 5))
    top_categories["revenue"].sort_values().plot(kind="bar")
    plt.title("Revenue by Category")
    plt.xlabel("Category")
    plt.ylabel("Revenue")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "category_performance.png", dpi=200)
    plt.close()

    plt.figure(figsize=(8, 5))
    top_regions["revenue"].sort_values().plot(kind="bar")
    plt.title("Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Revenue")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "region_performance.png", dpi=200)
    plt.close()

def print_summary(df: pd.DataFrame) -> None:
    top_product = df.groupby("product_name")["sales"].sum().sort_values(ascending=False).index[0]
    top_category = df.groupby("category")["sales"].sum().sort_values(ascending=False).index[0]
    top_region = df.groupby("region")["sales"].sum().sort_values(ascending=False).index[0]

    print("=== Data Science & Analytics – Task 1 ===")
    print(f"Rows: {len(df):,}")
    print(f"Revenue: {df['sales'].sum():,.2f}")
    print(f"Profit: {df['profit'].sum():,.2f}")
    print(f"Average Order Value: {df['sales'].mean():,.2f}")
    print(f"Top Product: {top_product}")
    print(f"Top Category: {top_category}")
    print(f"Top Region: {top_region}")

def main() -> None:
    df = load_data(DATA_PATH)
    save_charts(df)
    print_summary(df)

if __name__ == "__main__":
    main()
