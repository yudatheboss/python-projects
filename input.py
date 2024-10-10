####input() = a function that prmpts the user to enter data and returns the data as a striung
from operator import length_hint

from variables import quantity

name = input("enter your name: ")
#when we receive the name, we convert it to an int (typecasting).
age = int(input("how old are you? "))
age = age + 1


print(f"hello {name}!")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old")


#area calc
print("area calculator (units)\n")

print("")
length = float(input("what is the length of your object? "))
width = float(input("what is the width of your object? "))
area = length*width
print("the area of your object is {area} units" )



#shopping cart program
item = input("what item would you like to buy? ")
price = float(input("what is the price of your item? "))
quantity = int(input("how many units of this item will you purchase? "))

total = price*quantity

print(f"you have bought {quantity} {item}/s each costing {price}.")
print(f" Your total is ${total}")




