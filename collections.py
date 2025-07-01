# collectrions

# lists [] - any values any data types. ordered (indexed)
# lowest performance.
# dictionaries - key:value pairs {} unique keys values totally open. 
# excellent scalable performance. -- unordered!

# () or nothing! - tuples read-only list (fast + mem efficiiant)
# {} sets - unique values.

# 
        # key
#x = hash("hello") (+ a value)
#print(x)

#y = x % 102
#print(y)


# fixed set of array() buckets

# 
# import time 

# large_dict = {num : True for num in range(10_000_000)}
# large_list = list(range(10_000_000))

# x = 99_000_00

# start_time = time.time()
# l_list = x in large_list
# stop_time = time.time()
# print(f"list time was {stop_time - start_time:.6f}")

# start_time = time.time()
# l_dict = x in large_dict
# stop_time = time.time()
# print(f"Dict time was {stop_time - start_time:.6f}")

# index position   0        1       2        3/-1
#colours =       ["red", "yellow", "blue", "green"]

# # direct access
# print(colours[2])
# print(colours[0:2])

# colours[0] = "orange"
# print(colours)
# # nested lists

# numbers = [1, 2, 3, 4,]
# letters = ["a", "b", "c", "d"]

# combined = [numbers, letters]

# print(combined[0][4][0],combined[1][1])

# methods

# colours.sort(key=len)
# print(colours)

# join 

# x = ", ".join(colours)

# print(x)

 #drinks = {"still": ["book", "Book2"], "hot": "coffee", "fizzy": "sprite"}

# direct access:

# print(drinks["fizzy"])

# print(drinks.get("fizzy1", "not a key!!"))

# print(drinks.items())
# print(drinks.values())
# print(drinks.keys())

# exercise:

# Make a dictionary with authors and books (multiple). 
# AN input to ask the user for an author name.
# Print a STRING of the books! (NOT A LIST OF THE BOOKS)
# Error handling for incorrect keys. 


# book_dictionary = {
# 	"N.T. Wright": ["The Bible for Everyone: A New Translation", "Surprised by Hope: Rethinking heaven, the resurrection and the mission of the Church"],
# 	"Martin Luther": ["95 Theses", "The Bondage of the Will", "Table Talk"],
# 	"Karl Barth": ["Church Dogmatics", "The Epistle to the Romans"]
# }

# author = input("Enter the name of the author: ")

# if author in book_dictionary:
# 	print("Books by " + author + ": ")
# 	books = ", ".join(book_dictionary[author])
# 	print(books)
# else:
# 	print("Cannot find any book by the author.")

# booklist = {

#     "J.K. Rowling": [
#         "Harry Potter and the Sorcerer's Stone",
#         "Harry Potter and the Chamber of Secrets",
#         "Harry Potter and the Prisoner of Azkaban"
#     ],
#     "Roald Dahl": [
#         "Charlie and the Chocolate Factory",
#         "Matilda",
#         "James and the Giant Peach"
#     ],
#     "Sheila McCullagh": [
#         "The Land of the Blue Flower",
#         "Tim and the Hidden People",
#         "The Village with Three Corners"
#     ]
# }

# print("Availible authors:")
# print(", ".join(booklist.keys()))

# author = input("please enter an authors name " )

# books = booklist.get(author, []) #or ["sorry no books found"] 

# print(", ".join(books) or "no books found")


# JacksBookshop = {
#   "author1": {
#   "name": "Rick Riordan",
#   "book1": "The Lightning Thief", 
#   "book2": "The Sea of Monsters", 
#   "book3": "The Last Olympian",
# },
#   "author2": {
#   "name": "Jonathan Haidt",
#   "book1": "The Happiness Hypothesis", 
#   "book2": "The Righteous Mind",
#   "book3": "The Anxious Generation",  
# },
#   "author3": {
#   "name": "Colleen Hoover", 
#   "book1": "It Ends With Us",
#   "book2": "Verity",
#   "book3": "Hopeless",    
# }
# }
# y = JacksBookshop.get("author2").get("name")
# print(y)

# record  = JacksBookshop.get("author2")

# list_to_print = []

# for a, b in record.items():
#     if "book" in a:
#         list_to_print.append(b)

# print(", ".join(list_to_print))








