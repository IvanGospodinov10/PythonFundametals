def check_employees_happiness(happiness_list,factor):
    improved_happiness = [current_happiness * factor for current_happiness in happiness_list]
    average_happiness = sum(improved_happiness) / len(improved_happiness)
    happiness_count = sum(num >= average_happiness for num in improved_happiness)
    total_count = len (improved_happiness)

    message = 'happy' if happiness_count >= total_count / 2 else 'not happy'

    return f'Score: {happiness_count}/{total_count}. Employees are {message}!'


happiness_lst = list(map(int, input().split()))
happiness_factor = int(input())
result = check_employees_happiness(happiness_lst, happiness_factor)
print(result)