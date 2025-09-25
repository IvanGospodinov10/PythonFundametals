words = input().split()
palindrome = input()

palindrome_found = [word for word in words if word == word[::-1]]

print(palindrome_found)
print(f"Found palindrome {palindrome_found.count(palindrome)} times")