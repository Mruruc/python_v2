stores_inventory = [
    ["The Great Gatsby", "To Kill a Mockingbird", "1984", "Harry Potter"],
    ["1984", "Harry Potter", "The Catcher in the Rye", "The Hobbit"],
    ["To Kill a Mockingbird", "The Hobbit", "The Great Gatsby", "1984"],
    ["The Lord of the Rings", "Harry Potter", "The Great Gatsby"]
]

# store_set = []
# for store in stores_inventory:
#     store_set.append(set(store))
stores_set = [set(store) for store in stores_inventory]

# Task 3: Find the book titles that are unique to each store
map_unique_book_per_store = dict(())

for i in range(len(stores_set)):
    unique_books = (stores_set[i]).copy()
    for j in range(len(stores_set)):
        if i != j:
            unique_books.difference_update(stores_set[j])
    map_unique_book_per_store[f"Store{i + 1}"] = unique_books


print(map_unique_book_per_store)


# Find the total number of unique book titles across all stores.
# unique_books = set(())
# for books in store_set:
#     unique_books.update(books)
#
# print(len(unique_books))
# print("Unique Books: ", unique_books)

# Identify the common book titles that are available in all stores.

# common_books = set.intersection(*stores_set)

# common_books = store_set[0]
#
# for books in store_set[1:]:
#     common_books = common_books.intersection(books)
# print(common_books)
