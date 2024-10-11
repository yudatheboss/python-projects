# Do some code only IF some condition is True

age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up.")
elif age >= 18:
    print("you are now signed up.! ")
elif age <= 0:
    print("You are non-existent.")
elif age >= 100:
    print("You are too old to sign up.")
else:
    print("You must be 18 or older to sign up.")

response = input("would you like food? (Y/N) " )
if response == ("Y", "y"):
    print("Here you go my young padawan")
else:
    print("No food for you...")

name = input("Input your name: ")

if name == "":
    print("You did not enter your name!")
else:
    print(f"Hello {name}")

#if statements with booleans
for_sale = True

if for_sale:
    print("This item is for sale")
else:
    print("This item is out of stock. try again another time.")

