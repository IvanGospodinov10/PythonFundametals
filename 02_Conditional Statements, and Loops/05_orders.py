orders_number = int(input())

total_price = 0
order_price = 0
# is_order_wrong = False

for i in range(1, orders_number + 1):
    order_price = 0
    prise_per_capsula = float(input())
    days = int(input())
    capsula_per_day = int(input())

    if prise_per_capsula < 0.01 or prise_per_capsula > 100.00:
        # is_order_wrong = True
        continue
    elif days < 1 or days > 31:
        # is_order_wrong = True
        continue
    elif capsula_per_day < 1 or capsula_per_day > 2000:
        # is_order_wrong = True
        continue

    order_price = prise_per_capsula * capsula_per_day * days
    total_price += order_price

    print(f"The price for the coffee is: ${order_price:.2f}")

print(f"Total: ${total_price:.2f}")
