# Executive Summary — Data Science & Analytics Task 1

## Dataset used
Synthetic retail sales data for 2025 with the following fields:
- order_id
- order_date
- customer_id
- region
- product_name
- category
- quantity
- unit_price
- discount_rate
- sales
- profit

## KPI summary
- **Total Revenue:** 328,581.51
- **Total Profit:** 125,879.19
- **Orders:** 3,527
- **Average Order Value:** 93.16
- **Unique Customers:** 299

## Insights
1. **Revenue peaks in Q4.** Revenue rises sharply in November and December, indicating seasonal demand and stronger purchasing activity near year-end.
2. **Office Chair is the top revenue product.** It contributes the highest revenue among all products and is a strong candidate for premium positioning.
3. **Furniture leads all categories.** This category generates the most revenue and profit, making it the highest-value product group.
4. **West is the strongest region.** It delivers the highest revenue and profit, followed by North.
5. **Accessories sell in high volume.** Even with lower unit prices, they contribute strongly due to order count.

## Recommendations
- Increase stock levels for top-selling products before the Q4 season.
- Run promotions and bundles for Accessories to increase basket value.
- Focus sales campaigns in the West and North regions.
- Improve performance in East and South with targeted offers.
- Use monthly trend monitoring to plan inventory and marketing budgets.

## Deliverables
- Analysis script: `src/analyze_sales.py`
- Dataset: `data/sales_data_sample.csv`
- Charts: `outputs/`
- README: project documentation and setup guide
