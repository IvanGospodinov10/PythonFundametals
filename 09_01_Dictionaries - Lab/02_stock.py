stok = input().split()
search_list = input().split()

bakery = {}

for i in range(0, len(stok), 2):
    key = stok[i]
    value = stok[i + 1]
    bakery[key] = value

for product in search_list:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
