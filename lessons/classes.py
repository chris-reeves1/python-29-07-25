# classes
# blueprint of methods (functions) + attributes(vars)
# instances can be built from a class -THIS IS STATEFUL!!!!

# Classes extend the language
# We want to describe an object that python doesnt currently describe.


# 4 oops - 
# - polymorphism: different ways of implementing the same methods. 
# - abstraction: I dont want to see the code
# - inheritance: Inherit from a parent class - coupled!!!! 
# - encapsulation: privacy. 

# example

# class Example:
#     # attributes
#     name = "chris"

#     # methods
#     def speak(self):
#         print("hello")

# person1 = Example()

# print(person1.name)
# person1.speak()
# person1.age = "10"
# person1.name = "chirs"
# print(person1.name)

# person2 = Example()

# person2.group = "a"
# person2.id = "dfvgndfbvn"

# class Students:
#     def __init__(self, first, last, age):
#         self.first = first 
#         self.last = last
#         self.age = age

# student1 = Students("j", "smith", 20)

# print(student1.age)

# class Students:
#     def __init__(self, first, last, age):
#         self.first = first 
#         self.last = last
#         self.age = age
#         self.full = first + " " + last 

# student1 = Students("j", "smith", 20)

# print(student1.full)

# with a method

# class Students:
#     def __init__(self, first, last, age):
#         self.first = first 
#         self.last = last
#         self.age = age


#     def fullName(self):
#         return self.first + " " + self.last
        

# student1 = Students("j", "smith", 20)

# print(student1.fullName())

# print(Students.fullName(student1))


# advanced methods example

# from types import MethodType
# import builtins

# class Students:
#     def __init__(self, first, last, age):
#         self.first = first 
#         self.last = last
#         self.age = age


#     def fullName(self):
#         return self.first + " " + self.last
        

# student1 = Students("j", "smith", 20)
# student2 = Students("a", "smith", 10)

# def outside_function(self):
#     print(f"{self.first} called me")

# student1.outside_function = MethodType(outside_function, student1)
# student1.outside_function()

# def outside_class_function(self):
#     print(f"{self.first} called me")

# Students.outside_class_function = outside_class_function

# student1.outside_class_function()
# student2.outside_class_function()

# self class variables

# class Students:

#     age_increase_amount = 10

#     def __init__(self, first, last, age):
#         self.first = first 
#         self.last = last
#         self.age = age


#     def fullName(self):
#         return self.first + " " + self.last

#     def changeAge(self):
#         self.age = self.age + self.age_increase_amount 


# student1 = Students("j", "smith", 20)
# student2 = Students("a", "smith", 10)

# print(student1.age)    
# student1.changeAge()
# print(student1.age, student2.age)

# print(student1.__dict__)
# print(student2.__dict__)
# #print(Students.__dict__)

# student1.age_increase_amount = 100

# # student1.changeAge()
# # print(student1.__dict__)
# # print(student2.__dict__)

# # non-self class variables

# class Students:
#     age_increase_amount = 10
#     __num_of_students = 0 # name mangling

#     def __init__(self, first, last, age):
#         self.first = first 
#         self.last = last
#         self.age = age

#         Students.__num_of_students += 1

#     def fullName(self):
#         return self.first + " " + self.last

#     def changeAge(self):
#         self.age = self.age + self.age_increase_amount 

#     @classmethod
#     def get_num_students(cls):
#         return cls.__num_of_students

# student1 = Students("j", "smith", 20)
# student2 = Students("a", "smith", 10)

# print(Students.get_num_students())
# print(Students._Students__num_of_students)
# print(student1)
# # inheritance


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f"{self.name} is eating")

    def __repr__(self):
        return f"{self.name!r} - {self.species!r} - {self.__class__.__name__!r}"

    # def __str__(self):
    #     return self.__repr__()

# class Cat(Animal):
#     def __init__(self, name, species, breed):
#         super().__init__(name, species)
#         self.breed = breed

#     def talk(self):
#         print(f"test")
    
#     def __repr__(self):
#         return super().__repr__() + f"- {self.breed}"

# c = Cat("n", "s", "b")
# c.talk()
# c.eat()
# print(c)


# x = "hello"

# print(f"{x}")
# print(f"{x!r}")

a = Animal("a", "b")
print(repr(a))
       

# todo:
# classes lab
# tasks:
#     #1. Create a Rectangle class with attributes length and width. 
#     #Add methods to calculate the area and perimeter of the rectangle. 

#     #2. Create a BankAccount class with attributes account_number and balance. 
#     #Add methods to deposit and withdraw money from the account.

#     #3. Create a Car class with attributes make, model, and year. 
#     #Add methods to get and set the values of the attributes. 

#     #4. Create a Product class with attributes name, price, and quantity. 
#     #Add methods to calculate the total value of the product (price * quantity) 
#     #and add or remove items from the product inventory.

# - Time on feedback task! 

def create_model(name, fields):
    def __init__(self, **kwargs):
        for field_name, default_value in fields.items():
            setattr(self, field_name, kwargs.get(field_name, default_value))

    def __repr__(self):
        field_strings = [f"{k}={getattr(self, k)!r}" for k in fields]
        return f"{name}({', '.join(field_strings)})"

    return type(name, (object,), {
        "__init__": __init__,
        "__repr__": __repr__,
    })


user_schema = {
    "name": "",
    "email": "",
    "is_admin": False,
}

User = create_model("User", user_schema)


user1 = User(name="chris", email="chris@chris.com", is_admin=True)
print(user1)