def add(current_book_shelf: list, current_book: str) -> list:
    if current_book not in current_book_shelf:
        current_book_shelf.insert(0, current_book)
    return current_book_shelf


def remove(current_book_shelf: list, current_books: str) -> list:
    if current_books in current_book_shelf:
        current_book_shelf.remove(current_books)
    return current_book_shelf


def swap(current_book_shelf: list, current_books: list) -> list:
    book_one = current_books[0]
    book_two = current_books[1]

    if book_one in current_book_shelf and book_two in current_book_shelf:
        index_one = current_book_shelf.index(book_one)
        index_two = current_book_shelf.index(book_two)

        current_book_shelf[index_one], current_book_shelf[index_two] = \
            current_book_shelf[index_two], current_book_shelf[index_one]
    return current_book_shelf


def insert_book(current_book_shelf: list, current_book: str) -> list:
    if current_book not in current_book_shelf:
        current_book_shelf.append(current_book)
    return current_book_shelf


def chek_book(current_book_shelf: list, current_index: int):
    if 0 <= current_index < len(current_book_shelf):
        print(current_book_shelf[index])


books_shelf = input().split("&")
command = input().split(" | ")

while command[0] != "Done":
    action = command[0]
    if command[0] == "Add Book":
        books = command[1]
        books_shelf = add(books_shelf, books)
    elif command[0] == "Take Book":
        books = command[1]
        books_shelf = remove(books_shelf, books)
    elif command[0] == "Swap Books":
        books = command[1:]
        books_shelf = swap(books_shelf, books)
    elif command[0] == "Insert Book":
        books = command[1]
        books_shelf = insert_book(books_shelf, books)
    elif command[0] == "Check Book":
        index = int(command[1])
        chek_book(books_shelf, index)

    command = input().split(" | ")

print(", ".join(books_shelf))
