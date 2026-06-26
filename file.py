class book:
    def __init__(self,book_id,title,author):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.available=True
class library:
    def __init__(self):
        self.books={}

    def add_book(self):
        book_id=int(input("enter Book ID:"))
        if book_id in self.books:
            print("Error: Book ID already exists!")
        else:
            title=input("enter title:")
            author=input("enter author:")
            new_book=book(book_id,title,author)
            self.books[book_id]=new_book
            print("book added successfully")
            print("current books:",self.books)

    def view_book(self):
        if not self.books:
            print("no book in library")
        else:
            for book_id,book in self.books.items():
                print(f"Book ID:{book.book_id}")
                print(f"title:{book.title}")
                print(f"author:{book.author}")
                print(f"available:{'yes'if book. available else'no'}")

    def issue_book(self):
        book_id=int(input("enter book id:"))
        if book_id not in self.books:
            print("book not found")
        elif not self.books[book_id].available:
             print("already issued")
        else:
            self.books[book_id].available=False
            print("book issued succesfully")

    def return_book(self):
        book_id=int(input("enter book id to return:"))
        if book_id not in self.books:
            print("Error:book id not found!")
        else:
            book=self.books[book_id]
            if book.available:
                print("Error:this book was not issued!")
            else:
                book.available=True
                print(f"book '{book.title}'returned successfully!")

    def search_book(self):
        book_id=int(input("enter book id to search: "))
        if book_id in self. books:
            print("book found: ")
            book=self.books[book_id]
            print(f"book id: {book.book_id}")
            print(f"title: {book.title}")
            print(f"author: {book.author}")
            print(f"status: {'available' if book.available else 'issued'}")
        else:
            print("book not found in library")

lib=library()

while True:
    print("LMS")
    print("1.add book")
    print("2.view book")
    print("3.issue book")
    print("4.return book")
    print("5.search book")
    print("6.exit")

    choice=input("enter choice:")
    if choice =='1':
      lib.add_book()
    elif choice =='2':
      lib.view_book()
    elif choice =='3':
      lib.issue_book()
    elif choice =='4':
      lib.return_book()
    elif choice =='5':
      lib.search_book()
    elif choice =='6':
        print("thank you for using LMS")
        break
    else:
         print("invalid choice!try again")

print("program execution completed succesfully")





lib=library()
lib.add_book()
lib.view_book()
lib.issue_book()
lib.return_book()
lib.search_book()