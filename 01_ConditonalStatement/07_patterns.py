number = int(input())

for i in range(1, number + 1):
    for j in range(1, i+1):
        print("*", end="")
    print()

for n in range(number - 1, -1, -1):
    for f in range(n-1, -1, -1):
        print("*", end="")
    print()