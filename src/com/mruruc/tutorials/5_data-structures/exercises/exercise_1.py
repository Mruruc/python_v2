import matplotlib.pyplot as plt


file_handler = open("store_data.txt", "rt")

map_of_books = dict()

for line in file_handler:
    line = line.strip()

    for book in line.split(","):
        book = book.strip()
        if book in map_of_books:
            map_of_books[book] += 1
        else:
            map_of_books[book] = 1

file_handler.close()

book_titles = list(map_of_books.keys())
book_counts = list(map_of_books.values())

plt.figure(figsize=(10, 6))
plt.bar(book_titles, book_counts, color='skyblue')

plt.xlabel('Book Titles')
plt.ylabel('Counts')
plt.title('Histogram of Book Counts')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()
