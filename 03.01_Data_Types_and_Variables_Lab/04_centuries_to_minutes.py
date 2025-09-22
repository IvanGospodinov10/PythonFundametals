THE_TOPICAL_YEAR = 365.2422

centuries = int(input())
# Assume that one year has 365.2422 days on average

years = centuries * 100
days = int(years * THE_TOPICAL_YEAR)
hours = days * 24
minutes = hours * 60

print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")