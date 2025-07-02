# Sam has gone into the local milk bar to drown his sorrows. 
# He has a budget, and there's a choice of three (or more) 
# milkshakes, differently priced. 
# The barman says, "What can I fix you?" and Sam can reply 
# with a number corresponding to the relevant flavour:
# this list is displayed every iteration. 
# If he enters Q, he quits and leaves; the barman wishes him well. 
# If he orders but can't pay he's thrown out.

budget = int(input("Enter a budget: "))

milkshakes = {
    "1": (3, "Whole"),
    "2": (4, "choc"),
    "3": (5, "vanilla")
}

while True:
    print("drinks menu:")
    for option, (price, flavour) in milkshakes.items():
        print(f"{option} - {flavour} - ${price}")

    
    choice = input("enter you choice of drink? ")

    if choice not in milkshakes:
        print("invalid choice")
        continue

    if choice.upper() == "Q":
        print("bye")
        break

    price, flavour = milkshakes[choice]
    if price > budget:
        print("kicked out!")
        break
    
    print(f"enjoy {flavour} drink")
    budget -= price
    print(f"budget is now {budget}")



