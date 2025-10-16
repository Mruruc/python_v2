book_store1 = {"The Great Gatsby", "To Kill a Mockingbird", "1984", "Harry Potter"}

book_store2 = book_store1

book_store2.add("Great Wafle")
print("Book Store :",
      book_store1)  # Book Store : {'1984', 'To Kill a Mockingbird', 'Harry Potter', 'The Great Gatsby', 'Great Wafle'}
print("Reference : ",
      book_store2)  # Reference :  {'1984', 'To Kill a Mockingbird', 'Harry Potter', 'The Great Gatsby', 'Great Wafle'}

book_store3 = book_store1.copy()
book_store3.add("Book 6")
print("Copy of the Book1: ", book_store3)
print("Book Store: ", book_store1)

print("Book Store :           ", id(book_store1))
print("Book Store Reference : ", id(book_store2))
print("Book Store Copy :      ", id(book_store3))
