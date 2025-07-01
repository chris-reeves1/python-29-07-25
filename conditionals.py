# if, else, elif

# on_holiday = False
# is_admin = True
# is_verified = False

# if (is_admin or is_verified) and not on_holiday:
#     print("access granted")

# import dis

# def example():
#     x = 0
#     while x < 3:
#         print("something")
#         x += 1 

# dis.dis(example)

# temp = 38

# if temp > 30:
#     print("very hot")
# elif temp > 25:
#     print("still pretty hot") 
# elif temp > 20:
#     print("something")
# else:

# multiple comparators

# deposit = 919
# password = "password"

# if (0 < deposit < 100) and password == "password":
#     print(f"Thank you for {deposit}-deposit")
# else:
#     print("failed")

# # example to avoid:
# if not 0 < deposit < 100 and password != "password":
#     print("failed")
# else:
#     print(f"Thank you for {deposit}-deposit")

# in and not in

# name = "root"

# # if name in ("root", "admin", "user"):
# #     print("invalid")
# # else:
# #     print("valid")


# if name not in ("root", "admin", "user"):
#     print("accepted/valid")
# else:
#     print("not -accepted")

# exercise
- weight converter app
- user to input a numeric weight
- user to input a unit (kg/lbs)
- logic: check unit
- logic: conversion
- print out converted result
- error handling: unit input (loops/upper/lower)
- optional: error handling for non-numeric input in weight. 
