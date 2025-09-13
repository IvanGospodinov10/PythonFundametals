budget = float(input())
flour_price = float(input())

eggs_price_per_loaf = flour_price * 0.75
milk_price_per_liter = flour_price * 1.25
milk_price_per_loaf = milk_price_per_liter * 0.25

loaf_cost = flour_price + eggs_price_per_loaf + milk_price_per_loaf
loaf_made = 0
color_eggs = 0

while budget >= loaf_cost:
    budget -= loaf_cost
    loaf_made += 1
    color_eggs += 3

    if loaf_made % 3 == 0:
        color_eggs -= loaf_made - 2

print(f"You made {loaf_made} loaves of Easter bread! Now you have {color_eggs} eggs and {budget:.2f}BGN left.")
