import re

total_price = 0
bought_furniture = []
pattern = r">>([A-Za-z]+)<<(\d+\.?\d+)[!](\d+)"

while True:
    line = input()

    if line == "Purchase":
        break
    match = re.search(pattern, line)
    if match:
        furniture_name, price, quantity = match.groups()
        bought_furniture.append(furniture_name)
        total_price += float(price) * int(quantity)

print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_price:.2f}")
