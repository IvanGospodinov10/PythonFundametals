stock = input().split()

stock_inventor = {}

for i in range(0,len(stock), 2):
    key = stock[i]
    value = int(stock[i + 1])

    stock_inventor[key] = value

print(stock_inventor)

