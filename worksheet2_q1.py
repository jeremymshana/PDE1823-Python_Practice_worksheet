class Book:

    def __init__(self, title, author, total_copies):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.borrowed_copies = 0


    def available_copies(self):
        return self.total_copies - self.borrowed_copies


    def borrow_book(self):

        if self.available_copies() > 0:
            self.borrowed_copies += 1
            return True

        else:
            return False


    def return_book(self):

        if self.borrowed_copies > 0:
            self.borrowed_copies -= 1
            return True

        else:
            return False


    def display_info(self):

        print(
            f"{self.title} by {self.author} | Available copies: {self.available_copies()}"
        )



# Main Program

books = []


number_of_books = int(input("How many books do you want to enter? "))


for i in range(number_of_books):

    print("\nEnter details for book", i + 1)

    title = input("Enter title: ")
    author = input("Enter author: ")
    copies = int(input("Enter number of copies: "))

    book = Book(title, author, copies)

    books.append(book)



while True:

    print("\nLibrary Menu")
    print("1. Display books")
    print("2. Borrow book")
    print("3. Return book")
    print("4. Exit")


    choice = int(input("Menu choice: "))


    if choice == 1:

        print("\nLibrary Book List:")

        for i, book in enumerate(books):
            print(i + 1, end=". ")
            book.display_info()



    elif choice == 2:

        number = int(input("Enter book number to borrow: "))

        selected_book = books[number - 1]


        if selected_book.borrow_book():

            print(
                "Book borrowed successfully:",
                selected_book.title
            )

            print(
                "Available copies now:",
                selected_book.available_copies()
            )

        else:

            print("Sorry, this book is not available.")



    elif choice == 3:

        number = int(input("Enter book number to return: "))

        selected_book = books[number - 1]


        if selected_book.return_book():

            print(
                "Book returned successfully:",
                selected_book.title
            )

            print(
                "Available copies now:",
                selected_book.available_copies()
            )

        else:

            print("No borrowed copies to return.")



    elif choice == 4:

        print("Thank you for using the library system.")
        break


    else:

        print("Invalid option.")