# Supply Chain Order Analysis

A beginner-friendly data analysis project using Python to analyze sales and delivery performance in a supply chain order dataset.

## Project Overview

This project analyzes a sample dataset containing 40 customer orders.

The goal is to explore order data and evaluate sales performance, product demand, revenue, and delivery efficiency using Python.

## Tools Used

- Python
- Pandas
- Matplotlib

## Analysis

The project includes:

- Total products sold
- Total revenue
- Best-selling product
- Average delivery time
- Delayed order rate
- Revenue analysis by product category
- Monthly revenue trend

## Key Findings

- **Total Products Sold:** 623 units
- **Total Revenue:** €13,102
- **Best-Selling Product:** Notebook Pack (152 units)
- **Average Delivery Time:** 4.8 days
- **Delayed Order Rate:** 32.5%
- **Highest Revenue Month:** April (€2,121)

> Note: August contains only partial-month data, so its revenue should not be directly compared with complete months.

## Revenue by Product Category

![Revenue by Product Category](category_revenue.png)

## Monthly Revenue Trend

![Monthly Revenue Trend](monthly_revenue.png)

## Dataset

The dataset contains 40 sample orders with information about:

- Order date
- Product
- Product category
- Quantity
- Unit price
- Delivery time
- Delivery status

Revenue is calculated as:

`Revenue = Quantity × Unit Price`

## How to Run

Install the required libraries:

```bash
pip install pandas matplotlib

## Then run 
python analysis.py

## Author
Cansu Bora
