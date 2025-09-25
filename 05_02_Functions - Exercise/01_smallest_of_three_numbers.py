number_one = int(input())
number_two = int(input())
number_three = int(input())

def smallest_number(a:int,b:int,c:int):
    return min(a,b,c)
print(smallest_number(number_one, number_two, number_three))