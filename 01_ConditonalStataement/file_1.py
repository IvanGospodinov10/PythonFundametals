rows = int(input("Enter your number:"))

# "this is first pattern test in python

for i in range(0, rows - 1):
    for j in range(0, rows -i - 1):
        print(" ",end='')
    for j in range(0, i + 1):
        print("* ", end='')
    print()
