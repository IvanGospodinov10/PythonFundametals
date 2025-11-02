bakery_inventor = {}

while True:
    stock = input()
    if stock == "statistics":
        break

    product, quantity = stock.split(": ")
    quantity = int(quantity)

    if product in bakery_inventor:
        bakery_inventor[product] += quantity
    else:
        bakery_inventor[product] = quantity

print("Products in stock:")
for key, value in bakery_inventor.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(bakery_inventor.keys())}")
print(f"Total Quantity: {sum(bakery_inventor.values())}")
