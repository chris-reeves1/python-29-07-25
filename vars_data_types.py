# vars + data types + misc

# string "words"
# int 10
# float .
# boolean: True/False, 1/0, something/nothing

# variable

#(a reference)  (= sets a value)     (data that is sotred in memory)
# x = False

#y = 256000
#print(hex(id(y)))
#x = 256000
#print(hex(id(x)))

#print(x is y) # is (object) and == different!

# interning + caching
# -256 - 256 stored in memory

#def test():
 #   c = int(str(257))
  #  return c

#def test1():
 #   d = int(str(257))
  #  return d

#print(test() is test1())

# Descriptive, consistancy, simple, comments
# case - snake_case(vars/funcs/methods), camelCase, PascalCase(class names)

# 1var = 
# Var = reserved for class names
# MON = const

# scope

# global_variable = "accessible everywhere"

# def my_function():
#     local_variable = "accessible only inside this function"
#     #global global_variable
#     global_variable = "changed the value but only inside this function!!"
#     print(local_variable)
#     print(global_variable)

# my_function()
# print(global_variable)


# inspect and traceback
# import traceback

# def function_a():
#     function_b()

# def function_b():
#     function_c()

# def function_c():
#     print("the call stack is...")
#     traceback.print_stack()

# # function_a()

# import inspect

# def example(num_1, num_2):
#    '''
#    description:

#    input:

#    ouptuts
#    '''
#    return num_1 + num_2


# print(inspect.getdoc(example))
# print(inspect.signature(example))
# print(inspect.getsource(example))

# in-builts

# print("send to standard-output")

# import sys

# with open("file.txt", "w") as file:
#     sys.stdout = file
#     print("GO to the file!!")

# sys.stdout = sys.__stdout__
# print("test")

# # input 
# name = input("Enter name: ") # defaults to a string "10"
# age = int(input("Enter age: ")) 

# # concatanation

# print("your age is", age, "and name is", name)
# print("your name is " + name)
# print(f"your name is {name} and age is {age}")

# escape chars
# \n - newline \t tab \u unicode \U extended unicode \\ backslash. 

# "\u63635 hello tyhis is red¬!\u33635 

#print("Person1: \tHello how are you?\nPerson2: \tGood thanks! \U0001f604")

# bodmas

# // - 10/3 = 3
# % - 1