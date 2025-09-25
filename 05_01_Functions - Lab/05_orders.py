product = input()
quantity = int(input())

def sum_of_order(product_name, product_quantity):
    if product_name == "coffee":
        return f"{product_quantity * 1.50:.2f}"
    elif product_name == "coke":
        return  f"{(product_quantity * 1.40):.2f}"
    elif product_name == "snacks":
        return  f"{product_quantity * 2:.2f}"
    elif product_name == "water":
        return  f"{product_quantity * 1.00:.2f}"

# print(f"{sum_of_order(product, quantity):.2f}")
print(sum_of_order(product, quantity))