# Sample dataset representing the customer orders
orders = [
    {"customer_name": "Alice", "product": "Laptop", "quantity": 1, "price": 1200.00},
    {"customer_name": "Bob", "product": "Smartphone", "quantity": 2, "price": 500.00},
    {"customer_name": "Charlie", "product": "Headphones", "quantity": 3, "price": 150.00},
    {"customer_name": "Alice", "product": "Mouse", "quantity": 2, "price": 25.00},
    {"customer_name": "David", "product": "Monitor", "quantity": 1, "price": 300.00},
    {"customer_name": "Eva", "product": "Smartphone", "quantity": 1, "price": 500.00}
]

# 1. Calculate total revenue
total_revenue = sum(order["quantity"] * order["price"] for order in orders)
print(f"Total Revenue: ${total_revenue:,.2f}")

# 2. Find the most expensive order
# An order's cost is determined by quantity * price
most_expensive_order = max(orders, key=lambda x: x["quantity"] * x["price"])
exp_cost = most_expensive_order["quantity"] * most_expensive_order["price"]
print(f"Most Expensive Order: {most_expensive_order['customer_name']} bought "
      f"{most_expensive_order['quantity']}x {most_expensive_order['product']} for ${exp_cost:,.2f}")

# 3. Display customers spending more than $1,000 in total
customer_spending = {}
for order in orders:
    cost = order["quantity"] * order["price"]
    customer_spending[order["customer_name"]] = customer_spending.get(order["customer_name"], 0) + cost

high_spenders = [name for name, total in customer_spending.items() if total > 1000]
print(f"Customers spending more than $1,000: {', '.join(high_spenders)}")

# 4. Calculate total quantity sold for each product
product_sales = {}
for order in orders:
    product_sales[order["product"]] = product_sales.get(order["product"], 0) + order["quantity"]

print("Total quantity sold per product:")
for product, qty in product_sales.items():
    print(f" - {product}: {qty}")

# 5. Display the best-selling product (by quantity)
best_selling_product = max(product_sales, key=product_sales.get)
print(f"Best-selling Product: {best_selling_product} ({product_sales[best_selling_product]} units sold)")
