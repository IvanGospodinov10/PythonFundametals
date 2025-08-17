budget = int(input())
total_spend = 0
is_enough = False

while True:
    product_price = input()
    if product_price == "End":
        break
    elif total_spend + int(product_price) > budget:
        is_enough = True
        break
    else:
        total_spend += int(product_price)

if is_enough:
    print(f"You went in overdraft!")
else:
    print(f"You bought everything needed.")

