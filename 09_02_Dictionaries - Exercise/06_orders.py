products_dict = {}

while True:
    products = input()
    if products == "buy":
        break
    name, price, quantity = products.split()
    price = float(price)
    quantity = int(quantity)
    if name not in products_dict.keys():
        products_dict[name] = {"price": price, "quantity": quantity}
    else:
        products_dict[name]["quantity"] += quantity
        products_dict[name]["price"] = price

for product, data in products_dict.items():
    total = data["price"] * data["quantity"]
    print(f"{product} -> {total:.2f}")
