num = int(input())

# num_list = [int(digit) for digit in str(num)]

num_list = []
for digits in str(num):
    num_list.append(int(digits))

num_list.sort(reverse=True)
num = int(''.join(map(str,num_list)))

print(num)