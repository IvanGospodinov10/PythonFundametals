# shopping_list = {
#     "foods": {"nuts": "almonds"},
#     "drinks": {"soft": "lemonade", "wine": "merlot"}
# }
# for key, value in shopping_list.items():
#     for nested_key, nested_value in value.items():
#         print(f'{nested_value} bought')
#         shopping_list[key][nested_key] = 'bought'

txt = "I like bananas bananas bananas"
x = txt.replace("bananas", "apples", 4)
y = x.replace("apples","orange", 2)
print(y)
