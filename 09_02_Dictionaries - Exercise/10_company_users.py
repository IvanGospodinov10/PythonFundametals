company_users = {}

while True:
    user_data = input()
    if user_data == "End":
        break

    company, user_id = user_data.split(" -> ")

    if company not in company_users:
        company_users[company] = []

    if user_id not in company_users[company]:
        company_users[company].append(user_id)
# print(company_users)

for company, users in company_users.items():
    print(company)
    for user_id in users:
        print(f"-- {user_id}")
