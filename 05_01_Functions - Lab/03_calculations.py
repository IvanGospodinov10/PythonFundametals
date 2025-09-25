def calculation(operator_, num1_ , num2_):
    if operator_ == "multiply":
        return num1_ * num2_
    elif operator_ == "divide":
        return int(num1_ / num2_)
    elif operator_ == "add":
        return num1_ + num2_
    elif operator_ == "subtract":
        return num1_ - num2_
    return None
operator = input()
num1 = int(input())
num2 = int(input())

print(calculation(operator, num1, num2))