materials = {"shards": 0,
             "fragments": 0,
             "motes": 0
             }
legendary_item = ""
legendary_item_obtain = False
while not legendary_item_obtain:
    text = input().split()

    for index in range(0, len(text), 2):
        key = text[index + 1].lower()
        value = int(text[index])
        if key not in materials.keys():
            materials[key] = 0
        materials[key] += value

        if materials["shards"] >= 250:
            materials["shards"] -= 250
            legendary_item = "Shadowmourne"
            legendary_item_obtain = True

        elif materials["fragments"] >= 250:
            materials["fragments"] -= 250
            legendary_item = "Valanyr"
            legendary_item_obtain = True

        elif materials["motes"] >= 250:
            materials["motes"] -= 250
            legendary_item = "Dragonwrath"
            legendary_item_obtain = True
        if legendary_item_obtain:
            break

print(f"{legendary_item} obtained!")
for key, value in materials.items():
    print(f"{key}: {value}")
