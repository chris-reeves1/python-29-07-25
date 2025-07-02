# while loops and for loops
# saves time + code duplication

# while

# we need a condition to start a while loop. 
# Need a condition for a while loop to end. 
# otherwise they go on forever. 

# x = 0 

# while x < 101:
#     print(x)
#     x += 1

# break and continue

# i = 0

# while i < 6:
#     if i == 3:
#         break
#     print(i)
#     i += 1

# i = 0

# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# for loops
# for iterating through an iterable

my_fruits = ["kiwi", "apple", "pear", "orange"]

# for item in iterable:
#     code.....

# for fruit in my_fruits:
#     print(fruit)

# # while loop version
# l = 0
# while l < len(my_fruits):
#     print(my_fruits[l])
#     l += 1

# using range()

# for a in range(0, 10, 2):
#     print(a)

# strings

# for letter in "hello world".split():
#     print(letter)

# dictionaries

# for i in {"drink": "cola"}:
#     print(i)

# for i, y in {"drink": "cola"}.items():
#     print(i, y)

# nested for loops

# for i in range(1,3):
#     for j in range(1,4):
#         print(i, "x", j, "=", i*j)

# list comprehension
# making and changing lists

          # expressions     item      iterable
#result = [   x**2    for x in   range(5)]
#print(result)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_squared_numbers = [number**2 for number in numbers if number % 2 == 0]
# print(even_squared_numbers)

# inner list
#[input("enter something: ") for a in range(5)]

# outer list
#[print(f"{y}") for y in iterable]


# x = [print(f"{y} is in the list") for y in [input("enter something: ") for a in range(5)]]

# print(x)

y = print("hello")
print(y)

