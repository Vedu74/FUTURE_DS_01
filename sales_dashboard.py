import pandas as pd
import numpy as np
import plotly.express as px
from dash import Dash, dcc, html

# Sample dataset
data = {
    "Date": pd.date_range(start="2024-01-01", periods=100),
    "Revenue": np.random.randint(1000, 5000, 100),
    "Product": np.random.choice(["Product A", "Product B", "Product C"], 100),
    "Category": np.random.choice(["Category 1", "Category 2"], 100),
    "Region": np.random.choice(["North", "South", "East", "West"], 100)
}

df = pd.DataFrame(data)

# Revenue Trend
fig_revenue = px.line(df, x="Date", y="Revenue", title="Revenue Trend")

# Top Products
top_products = df.groupby("Product")["Revenue"].sum().reset_index()
fig_products = px.bar(top_products, x="Product", y="Revenue", title="Top Selling Products")

# Category Performance
category_perf = df.groupby("Category")["Revenue"].sum().reset_index()
fig_category = px.pie(category_perf, names="Category", values="Revenue", title="Category Performance")

# Regional Sales
region_sales = df.groupby("Region")["Revenue"].sum().reset_index()
fig_region = px.bar(region_sales, x="Region", y="Revenue", title="Regional Sales")

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Sales Dashboard"),
    dcc.Graph(figure=fig_revenue),
    dcc.Graph(figure=fig_products),
    dcc.Graph(figure=fig_category),
    dcc.Graph(figure=fig_region),
])

if __name__ == "__main__":
    app.run(debug=True) 