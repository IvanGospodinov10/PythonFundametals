import re

pattern = r"%([A-Z][a-z]+)%[^|$%.]*<(\w+)>[^|$%.]*\|(\d+)\|[^|$%.]*?(\d+(\.\d+)?)\$"

total_money = 0

while True:
    line = input()
    if line == "end of shift":
        break
    match = re.search(pattern, line)
    if match:
        customer =  match.group(1)
        product =match.group(2)
        count = int(match.group(3))
        price = float(match.group(4))
        total_product_price = int(count) * float(price)
        total_money += int(count) * float(price)
        print(f"{customer}: {product} - {total_product_price:.2f}")
print(f"Total income: {total_money:.2f}")

