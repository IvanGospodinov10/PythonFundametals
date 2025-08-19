number = float(input())

if number == 0:
    print("zero")
else:
    if number > 0:
        print("positive")
        if number < 1:
            print("small positive")
        if number > 1000000:
            print("big positive")
    else:
        print("negative")
        if number > -1:
            print("small negative")
        if abs(number) > 1000000:
            print("big negative")
