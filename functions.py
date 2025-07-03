# repeatability
# abstraction 

# def greet(name):# parameters 
#     print(f"hello {name}")

# greet("chirs")

# def greet(name):# parameters 
#     return (f"hello {name}")

# x = greet(chirs"")
# print(x)

# def greet(first_name, last_name, age=30):# parameters - example with default.
#     print(f"hello {first_name} {last_name}, age {age}")

# greet(first_name="chirs", "a", 35)

# *args
#  we dont know how many args will be passed we use *args
# recieves a tuple

# def make_pizza(size, *toppings):
#     print(f"Order for {size}-inch pizza with toppings: ")
#     for topping in toppings:
#         print(topping)

# make_pizza(10, "peppers", "mushrooms")

# **kwargs

# def order(**items):
#     print("Order: ")
#     for x, y in items.items():
#         print(f"{x} - {y}")

# order(main="pasta", drink="cola", side_dish="garlic_bread")


# combined

# def combined(*args, **kwargs):
#     print("args: ", args)
#     print("kwargs: ", kwargs)

# combined(1, b=2, c=3, d=4)

# / and * 
# / enforce everything before it is a positiobnal arg
# after can be anything and not enforced.
# * enforces everything after is keyword.

# def example(a, b, /, *, c, d):
#     print(f"a is {a}, b is {b}, c is {c} and d is {d}")

# example(1, 2, c=3, d=4)

# def maths_function(a, b, /, operation="add", *, decimal_places=None):
#     if operation == "add":
#         result = a + b
#     elif operation == "subtract":
#         result = a - b
#     else:
#         raise TypeError("Operation not recognised")
#     return round(result, decimal_places)

# maths_function(10, 5, decimal_places=5)
# maths_function(10, 5, operation="subtract", decimal_places=2)
# maths_function(10, 4, "subtract", decimal_places=2)
# maths_function(10.2555, 1.36548, decimal_places=6)

# recurrsion

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
        

# print(factorial(5))
    
# import inspect

# def test_function():
#     print("im in", inspect.currentframe().f_code.co_name)
#     print("called from", inspect.stack()[1].function)
#     x = "hello"
#     print(locals())

# def call():
#     test_function()

# call()
# #print(locals())

# def recursive_func(n):
#     print(f"entering stack: adding({n})")

#     if n == 0:
#         print("base case reached will return 0")
#         return 0

#     partial = recursive_func(n - 1)
#     result = n + partial
#     print(f"returns as {n} + {partial} = {result}")
#     return result

# print(recursive_func(5))

# lamdas
# discrete functions, mostly unnamed. 
# lambda args : expression (iterable)
#add_function = lambda x, y : x + y 

#print(add_function(2, 3))

# numbers = [1, 2, 3, 4]

# squared = map(lambda x: x**2, numbers)

# print(list(squared))

# higher order functions:

# def square(x):
#     return x * x

# def apply_function(func, value):
#     return func(value)

# print(apply_function(square, 10))


    