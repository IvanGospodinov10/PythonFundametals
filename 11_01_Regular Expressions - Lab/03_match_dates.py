import re
date_list = input()

pattern = r'(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})'

match_valid_data = re.findall(pattern, date_list)

for match in match_valid_data:

    day = match[0]
    month = match[2]
    year = match[3]
    print(f'Day: {day}, Month: {month}, Year: {year}')
