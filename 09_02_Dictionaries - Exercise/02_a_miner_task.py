miner_items = {}

while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())

    if resource not in miner_items:
        miner_items[resource] = quantity
    else:
        miner_items[resource] += quantity

# print(miner_items)
for key, value in miner_items.items():
    print(f"{key} -> {value}")