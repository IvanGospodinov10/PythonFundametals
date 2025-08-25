tasks_count = 0
task = input()

while task != 'END':

    first_char = task[0]


    if task == 'coding' or task == 'CODING':
        if first_char.isupper():
            tasks_count += 2
        else:
            tasks_count += 1

    if task == 'dog' or task == 'DOG' or task == 'cat' or task == 'CAT':
        if first_char.isupper():
            tasks_count += 2
        else:
            tasks_count += 1
    if task == 'movie' or task == 'MOVIE':
        if first_char.isupper():
            tasks_count += 2
        else:
            tasks_count += 1

    if tasks_count > 5:
        print(f"You need extra sleep")
        break
    task = input()

if tasks_count <= 5:
    print(tasks_count)


