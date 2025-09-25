word = input()
vowels = ['a', 'o', 'u', 'e', 'i']

no_vowels_world = ''.join([char for char in word if char.lower() not in vowels])

print(no_vowels_world)