a , b = int(input()), int(input())

temporary_value = a
print(f"Before:\na = {a}\nb = {b}")
a = b
b= temporary_value
print(f"After:\na = {a}\nb = {b}")