
import numpy as np

sales = np.array([
    [120, 150, 135, 170],
    [80, 95, 110, 105],
    [200, 180, 220, 240]
])

product_totals = np.sum(sales, axis=1)
print("Total sales of each product:", product_totals)

month_totals = np.sum(sales, axis=0)
print("Total sales of each month:", month_totals)

highest_product = np.argmax(product_totals) + 1
print("Product with the highest total sales: Product", highest_product)

lowest_month = np.argmin(month_totals) + 1
print("Month with the lowest total sales: Month", lowest_month)

modified_sales = sales.copy()
modified_sales[modified_sales < 100] = 0

print("Original sales array:")
print(sales)

print("Modified sales array:")
print(modified_sales)
