first_line = input().split(" | ")
second_line = input().split(" | ")
command = input()

notebook = {}

for text in first_line:
    word, definition = text.split(": ")
    if word not in notebook:
        notebook[word] = []
    notebook[word].append(definition)

if command == "Test":
    for test_word in second_line:
        if test_word in notebook:
            print(f"{test_word}:")
            for definitions in notebook[test_word]:
                print(f" -{definitions}")
elif command == "Hand Over":
    print(" ".join(notebook.keys()))
